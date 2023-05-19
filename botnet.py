import socket
import threading
#import virus

text = r"""

                           .xm*f""??T?@hc.
                          z@"` '~((!!!!!!!?*m.
                        z$$$K   ~~(/!!!!!!!!!Mh
                      .f` "#$k'`~~\!!!!!!!!!!!MMc
                     :"     f*! ~:~(!!!!!!!!!!XHMk
                     f      " %n:~(!!!!!!!!!!!HMMM.
                    d          X~!~(!!!!!!!X!X!SMMR
                    M :   x::  :~~!>!!!!!!MNWXMMM@R
 n                  E ' *  ueeeeiu(!!XUWWWWWXMRHMMM>                :.
 E%                 E  8 .$$$$$$$$K!!$$$$$$$$&M$RMM>               :"5
z  %                3  $ 4$$$$$$$$!~!*$$$$$$$$!$MM$               :" `
K   ":              ?> # '#$$$$$#~!!!!TR$$$$$R?@MME              z   R
?     %.             5     ^""^~~~:XW!!!!T?T!XSMMM~            :^    J
 ".    ^s             ?.       ~~d$X$NX!!!!!!M!MM             f     :~
  '+.    #L            *c:.    .~"?!??!!!!!XX@M@~           z"    .*
    '+     %L           #c`"!+~~~!/!!!!!!@*TM8M           z"    .~
      ":    '%.         'C*X  .!~!~!!!!!X!!!@RF         .#     +
        ":    ^%.        9-MX!X!!X~H!!M!N!X$MM        .#`    +"
          #:    "n       'L'!~M~)H!M!XX!$!XMXF      .+`   .z"
            #:    ":      R *H$@@$H$*@$@$@$%M~     z`    +"
              %:   `*L    'k' M!~M~X!!$!@H!tF    z"    z"
                *:   ^*L   "k ~~~!~!!!!!M!X*   z*   .+"
                  "s   ^*L  '%:.~~~:!!!!XH"  z#   .*"
                    #s   ^%L  ^"#4@UU@##"  z#   .*"
                      #s   ^%L           z#   .r"
                        #s   ^%.       u#   .r"
                          #i   '%.   u#   .@"
                            #s   ^%u#   .@"
                              #s x#   .*"
                               x#`  .@%.
                             x#`  .d"  "%.
                           xf~  .r" #s   "%.
                     u   x*`  .r"     #s   "%.  x.
                     %Mu*`  x*"         #m.  "%zX"
                     :R(h x*              "h..*dN.
                   u@NM5e#>                 7?dMRMh.
                 z$@M@$#"#"                 *""*@MM$hL
               u@@MM8*                          "*$M@Mh.
             z$RRM8F"                             "N8@M$bL
            5`RM$#                                  'R88f)R
            'h.$"                                     #$x*


        ▄▄▄▄    ▒█████  ▄▄▄█████▓ ███▄    █ ▓█████▄▄▄█████▓
        ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
        ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
        ▒██░█▀  ▒██   ██░░ ▓██▓ ░ ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ 
        ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ ▒██░   ▓██░░▒████▒ ▒██▒ ░ 
        ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   
        ▒░▒   ░   ░ ▒ ▒░     ░    ░ ░░   ░ ▒░ ░ ░  ░   ░    
        ░    ░ ░ ░ ░ ▒    ░         ░   ░ ░    ░    ░      by Th3L1ghtn1ng
        ░          ░ ░                    ░    ░  ░        
            ░                                             
"""
print("\033[31m" + text + "\033[0m")

HOST = "192.168.1.112"  # Indirizzo IP del server
PORT = 2222  # Porta del server

def bind():
    # Creazione del socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Associazione del socket all'host e alla porta specificati
    s.bind((HOST, PORT))

    # Inizio dell'ascolto delle connessioni
    s.listen()

    print(f"In attesa di connessioni su {HOST}:{PORT}...")

    # Ciclo principale del server
    while True:
        # Accettazione di una connessione in entrata
        conn, addr = s.accept()
        print(f"Connessione accettata da {addr}")

        # Gestione della connessione
        with conn:
            while True:
                # Ricezione dei dati dal client
                data = conn.recv(1024)
                if not data:
                    break

                # Elaborazione dei dati
                # ...

                # Invio di una risposta al client
                response = "Messaggio ricevuto"
                conn.sendall(response.encode())

# Creazione del thread per la funzione bind()
t = threading.Thread(target=bind)
# Avvio del thread
t.start()

# Lettura degli indirizzi IP delle macchine dal file "machines"
with open("machines", "r") as machines_file:
    machines = machines_file.read().split(", ")

# Stampa degli indirizzi IP delle macchine disponibili
print("Macchine disponibili:")
for addr in machines:
    print(addr)

# Richiesta di login all'utente
login = input("In quale macchina vuoi loggarti? ")

# Controllo se l'indirizzo IP scelto dall'utente è disponibile
if login in machines:
    print(f"Accesso alla macchina {login} riuscito!")
else:
    print("Accesso negato: la macchina specificata non è disponibile.")
