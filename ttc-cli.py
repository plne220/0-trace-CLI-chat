import socket, ssl, threading, struct, hashlib, os, sys, subprocess, pathlib, urllib.request

PORT = 4444
CERT = "server.crt"
KEY = "server.key"

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "unknown"

def get_public_ip():
    try:
        return urllib.request.urlopen("https://api.ipify.org", timeout=5).read().decode()
    except:
        return "unavailable"

def get_tailscale_ip():
    try:
        out = subprocess.check_output(["tailscale","ip","-4"], stderr=subprocess.DEVNULL)
        return out.decode().strip().split("\n")[0]
    except:
        return None

def gen_cert():
    if os.path.exists(CERT) and os.path.exists(KEY):
        return
    subprocess.run([
        "openssl","req","-x509","-newkey","rsa:4096",
        "-keyout",KEY,"-out",CERT,"-days","365","-nodes",
        "-subj","/CN=secure_cli"
    ], check=True)

def recv_all(s, n):
    d=b""
    while len(d)<n:
        c=s.recv(n-len(d))
        if not c:
            return None
        d+=c
    return d

def handle_client(conn, addr, pw_hash):
    auth=recv_all(conn,32)
    if auth!=pw_hash:
        conn.close()
        return
    print("Connected:",addr)
    while True:
        h=recv_all(conn,5)
        if not h:
            break
        t=h[:1]
        size=struct.unpack(">I",h[1:])[0]
        data=recv_all(conn,size)
        if data is None:
            break
        if t==b"M":
            print(f"[{addr}] {data.decode(errors='ignore')}")
        elif t==b"F":
            nlen=struct.unpack(">H",data[:2])[0]
            name=data[2:2+nlen].decode(errors='ignore')
            content=data[2+nlen:]
            pathlib.Path("received").mkdir(exist_ok=True)
            with open(os.path.join("received",name),"wb") as f:
                f.write(content)
            print(f"[{addr}] file saved: received/{name}")
    conn.close()

def run_server(password):
    gen_cert()
    pw_hash=hashlib.sha256(password.encode()).digest()
    ctx=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain(CERT,KEY)

    print("\n=== SERVER INFO ===")
    print("Hostname:", socket.gethostname())
    print("Local IP:", get_local_ip())
    print("Public IP:", get_public_ip())
    ts_ip = get_tailscale_ip()
    if ts_ip:
        print("Tailscale IP:", ts_ip)
    print("Port:", PORT)
    print("===================\n")

    s=socket.socket()
    s.bind(("0.0.0.0",PORT))
    s.listen()
    print("Server running...")

    while True:
        c,a=s.accept()
        sc=ctx.wrap_socket(c,server_side=True)
        threading.Thread(target=handle_client,args=(sc,a,pw_hash),daemon=True).start()

def socks_connect(dest_host,dest_port,proxy=("127.0.0.1",9050)):
    s=socket.socket()
    s.connect(proxy)
    s.sendall(b"\x05\x01\x00")
    s.recv(2)
    h=dest_host.encode()
    req=b"\x05\x01\x00\x03"+bytes([len(h)])+h+struct.pack(">H",dest_port)
    s.sendall(req)
    r=s.recv(10)
    if r[1]!=0:
        raise RuntimeError("SOCKS fail")
    return s

def run_client(host,password,use_tor):
    if use_tor:
        sock=socks_connect(host,PORT)
    else:
        sock=socket.create_connection((host,PORT))

    ctx=ssl.create_default_context()
    ctx.check_hostname=False
    ctx.verify_mode=ssl.CERT_NONE

    s=ctx.wrap_socket(sock)

    auth=hashlib.sha256(password.encode()).digest()
    s.sendall(auth)

    while True:
        cmd=input("m=msg f=file q=quit > ").strip().lower()
        if cmd=="q":
            break
        if cmd=="m":
            msg=input("Message: ").encode()
            p=b"M"+struct.pack(">I",len(msg))+msg
            s.sendall(p)
        elif cmd=="f":
            path=input("File path: ").strip()
            if not os.path.isfile(path):
                print("Not found")
                continue
            name=os.path.basename(path).encode()
            content=open(path,"rb").read()
            payload=struct.pack(">H",len(name))+name+content
            p=b"F"+struct.pack(">I",len(payload))+payload
            s.sendall(p)

def main():
    if len(sys.argv)<2:
        print("Usage:")
        print("  Server: python secure_cli.py server")
        print("  Client: python secure_cli.py client <host> [--tor]")
        return

    mode=sys.argv[1]
    pw=input("Password: ")

    if mode=="server":
        run_server(pw)

    elif mode=="client":
        if len(sys.argv)<3:
            print("Host required")
            return
        host=sys.argv[2]
        tor="--tor" in sys.argv
        run_client(host,pw,tor)

if __name__=="__main__":
    main()

