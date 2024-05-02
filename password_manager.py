from cryptography.fernet import Fernet #module to encrypt

#declare functions####################
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() + master_pwd.encode()
fern = Fernet(key)

'''#function to generate cryptography key to decrypt text, key already generated therefor function not needed anymore
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def view():
    with open('passwords.txt', 'r') as f:#with opens and closes file as needed, 'a' mode appends to the text file 
        for line in f.readlines():
            data = line.rstrip()#rstrip will strip off carriage return
            user, passw = data.split("-")#splits data into user and passw after each - symbol
            print("User:", user, ", Password:", 
                  fern.decrypt(passw.encode()).decode())
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:#with opens and closes file as needed, 'a' mode appends to the text file 
        f.write(name + "-"  + fern.encrypt(pwd.encode()).decode() + "\n")
######################################3

while True:
    mode = input("View or Add new password?(q to Quit)").lower()
    if mode == "q":
        break
    elif mode == "view": 
        view()
    elif mode == "add":
        add()
    else:
        print("invalid selection")
        continue
