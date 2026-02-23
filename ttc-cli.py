import socket, ssl, threading, struct, hashlib, os, sys, subprocess, pathlib, urllib.request, time

PORT = 4444
CERT = "server.crt"
KEY = "server.key"
SALT = b"simple_static_salt"

clients = []

LOGO = r"""
      
                                                                                            +
                                  -                 +           .:                          +
                              -=:%@@@@-         +=:%@@@@-    *:=@@@@%                       +
                              *%%@@@@#.         *%%@@@@#.    %%@@@@%+      =                +
                   .  :@#+=.            :  -@*+=      .         .      *==@@@@@.            +
                   :@@@@@@#-            .@@@@@@#-     -  #@++-         #*#@@@@*             +
                   .  :***:        .-   :  -***.      *@@@@@%* .  .@+-:                     +
                                %-=@@@@%              .  **+-  :@@@@@@%+                    +
                    :%:        .%#%@@@@*    ..  %%+=.          :. =##%-                     +
                   *@@@.                     @@@@@@#=     .=             :                  +
         :@-     .@@@@@@@@@@@@#                 **#:   #:-@@@@@:     .*.#@@@@*              +
          *@@= .*@@@@@@@@@@@@@@@+       *              %%@@@@@%      -@%@@@@@-              +
          =@@@@@@@@@@@@@@@@@@*=.    ++-@@@@@-                                               +
          %@@@@@@@@@@@@@@@@@@@%*    *#%@@@@#. .. .%%++.      :  #@*+:                       +
         +@%=--+%@@@@@@@@@@@@@+                @@@@@@#=      *@@@@@#+.  =  %@%#+            +
                   %#+++==%.                  .. :*+*-       : .++*=.   #@@@@@%*.           +
                          .   -  +@**=       -.     .  =@#*=.              ----             +
                              -@@@@@@*.  ==:*@@@@=   @@@@@@#:     .: .@@#*:                 +
                              :  -+++.   =%%@@@@%:  :  :*++.       @@@@@@#=                 +
                           ..                  .            **..      =-=.                  +
                        *.-@@@@*      .                  @%@@@@@%.                          +
                        @@@@@@@*  =  @@@@#   .= -@@@@-  :=:+@@@#:       .%+::               +
                                  +@@@@@%*    @@@@@@*-                @@@@@@%=              +
                                     :...        :.:                 :..-%%%-               +
                                                                                            +
                                                                                            +
                                                                                            +
          ##**+.  .**#*.    ++   *: .+***: *#%#*+   #***.  **   -#   =- *:  =#*#:           +
         .%.  .%:-%    @-   #*@. #- %    **  %=     @.  % =#*+  ++%. +- %: %.               +
         .%.   +=*=    *+   #-.%.#--*    -%  %=     @*+#: %::%  +=.%:+- %:-*                +
         .%.  -%.:@.  .@:   #- .%%- %:   #-  %=     @.   #=  -% ==  #*- %: %-               +
          +++-.    -*+:     -.   =.  :++-    -:     =.  .=    =.::   =. =.  .+*+.           +
                                                                                            +
                                                                                            +
                                 +.      :*                                                 +
                         .    *@@@@#% .#@@@@%*                                              +
                      +@@@%-*. =##+... .*+*:.::=*%. :                      :*#@= ..         +
                      .#@@%++=#%@@: - +#%@. - +%@@@@*                      =%@@@@%.         +
                 *%@@-.+      #@@@@#+ *@@@@%*  :.: .=+%. .                .+-...            +
                 +@@@%##:#%@@:.-  -*#@- =  *%@@-.= *@@@@@#              =%@@@%%             +
                        .*@@@%#=  -%@@@@@  +@@@@#*  ---   -             .=++=...            +
                             :##@* -: -##@# :. -#%@+ -.#@@@%+*       .%@@@=-=               +
                   -%:       -#@@@%@. -#@@@%%. -%@@@%% -#%%=:=        *@@@#*+ .             +
                  :@@@+           :#%@: - :=*%. . -##@= :  +#%@. . =*%@. : *@@@=.+          +
          .#@@@@@@@@@@@@      =@  =%@@@@% +@@@@@= +%@@@@# .*@@@@@-.*@@@@@+ *@@@@##.         +
         +@@@@@@@@@@@@@@@+. =@@+      .:@. : ..-+%. .  :-@: .  .=##  .  .:@-                +
          :+#@@@@@@@@@@@@@@@@@@:     -#@@@@#  =%@@@@+ -#@@@@%  +@@@@@- :*@@@@@.             +
         .#@@@@@@@@@@@@@@@@@@@@*    .#::::  .# :..  .+:....  -- :..  -= .-::  -             +
          .*@@@@@@@@@@@@@%+-:+@@+ *@@@@%# *@@@@%# =%@@@%% :%@@@@%:.#@@@@@= %@@@%+#          +
              -@=+*++#%         +..=++:.:+.=++-.::=-+++....:++*... :+++:=- :#%%+-=          +
               .             =%@@@#@. *@@@@## :%@@@%#=.%@@@--=       -@@@@**-               +
                           .- -**=.:-+.=+*-.:.-:*+#:.: *@@@#++        =%%#---               +
                   .=   :%@@@#*=  #@@@%## .%@@@*+* .=+%. :              :+*@* ..            +
                 #@@@%+# -###-.-.-.+**-.+: =#%%+-= +%@@@@#              :#@@@@@.            +
                 :#%%+:=...  :%@@@#+=:%@@@*#- .:**  -..                   . ..+             +
                      -@@@@=*--#%%=.= =%%#-:-.*@@@@@-                      #@@@@%%          +
                       +@@%=---%%@+ -  =%@@- = =.:                          =**: .          +
                              *%@@@@%  *@@@@@%                                              +
                                                                                            +
                                                                                            +
                                                                                            +
                                                                                            +
            -***#+.   *#***-    :+****:    .#*     *#.    #  .#.  -****. .##***=            +
          :@-    .@+  @-   %+ :@-          %=#*    %=%=   @  :@: +@.     :@:                +
          #%      +@  @#*#@=  @+   =***   %+  %*   %= +%. @  :@:  .+##=  :@#***:            +
          :@=    :@=  @:  :@. :@-    -@  *%...:@=  %=  .%+@  :@:      ## :@:                +
            :*##*-    *:   =+   .+###*= -*      #. +-    =#  .#. -*##*:  .#####*            +
                                                                                            +
                                                                                            +
                                                                                            +
"""

def hash_pw(user, pw):
    return hashlib.sha256(SALT + user.encode() + pw.encode()).digest()

def gen_cert():
    if os.path.exists(CERT) and os.path.exists(KEY):
        return
    subprocess.run([
        "openssl","req","-x509","-newkey","rsa:4096",
        "-keyout",KEY,"-out",CERT,"-days","365","-nodes",
        "-subj","/CN=secure_cli"
    ], check=True)

def get_public_ip():
    try:
        return urllib.request.urlopen("https://api.ipify.org", timeout=5).read().decode()
    except:
        return "unavailable"

def recv_all(s, n):
    d=b""
    while len(d)<n:
        c=s.recv(n-len(d))
        if not c:
            return None
        d+=c
    return d

def broadcast(msg, sender=None):
    for c in clients:
        if c != sender:
            try:
                c.sendall(msg)
            except:
                pass

def handle_client(conn, addr):
    conn.settimeout(60)

    ulen = struct.unpack(">H", recv_all(conn,2))[0]
    user = recv_all(conn, ulen).decode(errors="ignore")

    plen = struct.unpack(">H", recv_all(conn,2))[0]
    pw = recv_all(conn, plen).decode(errors="ignore")

    if hash_pw(user, pw) != hash_pw(user, pw):
        conn.close()
        return

    clients.append(conn)
    join = f"[+] {user} joined".encode()
    broadcast(b"M"+struct.pack(">I",len(join))+join)
    print(join.decode())

    while True:
        h = recv_all(conn,5)
        if not h:
            break
        t = h[:1]
        size = struct.unpack(">I",h[1:])[0]
        data = recv_all(conn,size)
        if data is None:
            break

        if t == b"M":
            msg = f"[{user}] {data.decode(errors='ignore')}".encode()
            broadcast(b"M"+struct.pack(">I",len(msg))+msg, conn)
            print(msg.decode())

        elif t == b"F":
            nlen = struct.unpack(">H",data[:2])[0]
            name = os.path.basename(data[2:2+nlen].decode(errors="ignore"))
            content = data[2+nlen:]
            pathlib.Path("received").mkdir(exist_ok=True)
            path = f"received/{user}_{name}"
            with open(path,"wb") as f:
                f.write(content)
            notice = f"[{user}] sent file: {name}".encode()
            broadcast(b"M"+struct.pack(">I",len(notice))+notice, conn)
            print(notice.decode())

    clients.remove(conn)
    leave = f"[-] {user} left".encode()
    broadcast(b"M"+struct.pack(">I",len(leave))+leave)
    print(leave.decode())
    conn.close()

def run_server():
    print(LOGO)
    gen_cert()

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain(CERT, KEY)

    print("Public IP:", get_public_ip())
    print("Port:", PORT)

    s = socket.socket()
    s.bind(("0.0.0.0", PORT))
    s.listen()

    print("Server running...\n")

    while True:
        c, a = s.accept()
        sc = ctx.wrap_socket(c, server_side=True)
        threading.Thread(target=handle_client, args=(sc,a), daemon=True).start()

def run_client(host, use_tor):
    print(LOGO)

    username = input("Username: ")
    password = input("Password: ")

    if use_tor:
        s = socket.socket()
        s.connect(("127.0.0.1",9050))
        s.sendall(b"\x05\x01\x00")
        s.recv(2)
        h = host.encode()
        req = b"\x05\x01\x00\x03"+bytes([len(h)])+h+struct.pack(">H",PORT)
        s.sendall(req)
        s.recv(10)
        sock = s
    else:
        sock = socket.create_connection((host,PORT))

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    s = ctx.wrap_socket(sock)

    u = username.encode()
    p = password.encode()

    s.sendall(struct.pack(">H",len(u)) + u)
    s.sendall(struct.pack(">H",len(p)) + p)

    def listen():
        while True:
            h = recv_all(s,5)
            if not h:
                break
            size = struct.unpack(">I",h[1:])[0]
            data = recv_all(s,size)
            if data:
                print("\n"+data.decode(errors="ignore"))

    threading.Thread(target=listen, daemon=True).start()

    while True:
        cmd = input("m=msg f=file q=quit > ").lower()
        if cmd == "q":
            break
        if cmd == "m":
            msg = input("Message: ").encode()
            s.sendall(b"M"+struct.pack(">I",len(msg))+msg)
        elif cmd == "f":
            path = input("File path: ").strip()
            if not os.path.isfile(path):
                print("Not found")
                continue
            name = os.path.basename(path).encode()
            content = open(path,"rb").read()
            payload = struct.pack(">H",len(name))+name+content
            s.sendall(b"F"+struct.pack(">I",len(payload))+payload)

def main():
    if len(sys.argv) < 2:
        print("Server: python secure_cli.py server")
        print("Client: python secure_cli.py client <host> [--tor]")
        return

    if sys.argv[1] == "server":
        run_server()
    else:
        host = sys.argv[2]
        tor = "--tor" in sys.argv
        run_client(host, tor)

if __name__ == "__main__":
    main()
