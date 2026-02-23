rt"
KEY = "server.key"

SALT = "6d477e7f16fc7141bbcda0c2950da171"
PASSWORD_HASH = "daae92a9a7001e3bb73a8a56c9f868837f9e6f0631cb3a645dea85d494740063" #dont bother cracking ts 

TAILSCALE_ONLY = True

SERVER_LOGO = r"""
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

"""

CLIENT_LOGO = r"""
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

"""

NEON = "\033[92m"
RESET = "\033[0m"

clients = []
lock = threading.Lock()

def gen_cert():
    if os.path.exists(CERT) and os.path.exists(KEY):
        return
    subprocess.run([
        "openssl","req","-x509","-newkey","rsa:2048",
        "-keyout",KEY,"-out",CERT,
        "-days","3650","-nodes",
        "-subj","/CN=ttc"
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_tailscale_ip():
    try:
        return subprocess.check_output(
            ["tailscale","ip","-4"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
    except:
        return None

def broadcast(msg, sender=None):
    with lock:
        dead=[]
        for c in clients:
            if c!=sender:
                try: c.sendall(msg)
                except: dead.append(c)
        for d in dead:
            clients.remove(d)

def handle_client(conn, addr):

    if TAILSCALE_ONLY and not addr[0].startswith("100."):
        conn.close()
        return

    try:
        conn.send(b"Username: ")
        user = conn.recv(1024).strip().decode()

        conn.send(b"Password: ")
        pw = conn.recv(1024).strip().decode()

        test = hashlib.sha256((SALT + pw).encode()).hexdigest()

        pw = None

        if test != PASSWORD_HASH:
            conn.close()
            return

        conn.send(b"OK\n")

        with lock:
            clients.append(conn)

        broadcast(f"[+] {user} joined\n".encode(), conn)

        while True:
            data = conn.recv(4096)
            if not data:
                break

            if data.startswith(b"/f "):
                _, name, size = data.split(b" ", 2)
                size = int(size.decode())

                conn.send(b"READY")

                remaining = size
                fdata = b""
                while remaining > 0:
                    chunk = conn.recv(min(4096, remaining))
                    if not chunk: break
                    fdata += chunk
                    remaining -= len(chunk)

                broadcast(f"[FILE] {user}: {name.decode()} ({size} bytes)\n".encode())
                broadcast(fdata)

            else:
                broadcast(f"[{user}] ".encode()+data, conn)

    finally:
        with lock:
            if conn in clients:
                clients.remove(conn)
        conn.close()

def run_server():
    print(SERVER_LOGO)
    gen_cert()

    ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ctx.load_cert_chain(CERT, KEY)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.set_ciphers("ECDHE+AESGCM")

    ip = get_tailscale_ip() or "No Tailscale IP found"

    print("Tailscale IP:", ip)
    print("Port:", PORT)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", PORT))
    s.listen(50)

    print("Server running (Tailscale only)...\n")

    while True:
        c, a = s.accept()
        c.settimeout(30)
        sc = ctx.wrap_socket(c, server_side=True)
        threading.Thread(target=handle_client, args=(sc,a), daemon=True).start()

def recv_loop(sock):
    while True:
        data = sock.recv(4096)
        if not data:
            break
        print(NEON + data.decode(errors="ignore") + RESET, end="")

def run_client(host):
    print(CLIENT_LOGO)

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    s = socket.create_connection((host, PORT), timeout=20)
    ss = ctx.wrap_socket(s)

    print(NEON + ss.recv(1024).decode() + RESET, end="")
    ss.send(input().encode()+b"\n")

    print(NEON + ss.recv(1024).decode() + RESET, end="")
    ss.send(input().encode()+b"\n")

    if not ss.recv(1024).startswith(b"OK"):
        print("Auth failed")
        return

    print(NEON + "Connected\n" + RESET)

    threading.Thread(target=recv_loop, args=(ss,), daemon=True).start()

    while True:
        msg = input(NEON + "> " + RESET)

        if msg.startswith("/s "):
            path = msg[6:]
            if os.path.exists(path):
                size = os.path.getsize(path)
                name = os.path.basename(path)

                ss.send(f"/f {name} {size}".encode())

                if ss.recv(5) == b"READY":
                    with open(path,"rb") as f:
                        ss.sendall(f.read())
        else:
            ss.send((msg+"\n").encode())

if __name__ == "__main__":
    if "server" in sys.argv:
        run_server()
    elif "client" in sys.argv:
        run_client(sys.argv[-1])
    else:
        print("Use server or client <Tailscale-IP>")
