from cryptography.fernet import Fernet

# Generate and save a key (only run once)
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the previously generated key
def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Only generate a key if it doesn't already exist
import os
if not os.path.exists("key.key"):
    write_key()

# Prompt for master password (used for access control, not encryption here)
master_pwd = input("What is the master password? ")

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            if "|" in data:
                user, encrypted_pwd = data.split("|")
                try:
                    decrypted_pwd = fer.decrypt(encrypted_pwd.encode()).decode()
                    print(f"User: {user} | Password: {decrypted_pwd}")
                except Exception as e:
                    print(f"Error decrypting password for {user}: {e}")

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    encrypted_pwd = fer.encrypt(pwd.encode()).decode()

    with open('passwords.txt', 'a') as f:
        f.write(f"{name}|{encrypted_pwd}\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")