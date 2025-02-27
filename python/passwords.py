import hashlib
import os
#file to store the passwords and site names
FILENAME = "Passwords.txt"
# Function to hash the password
def hash_password(password):
    """hash a pasword for storing"""

    return(hashlib.sha256(password.encode()).hexdigest())

#Function to save the password
def save_password(site, password):
    """"save the site name and the password"""
    hashed_password = hash_password(password)
    with open(FILENAME, "a") as file:
        file.write(f"{site} {hash_password}\n")
        print(f"Password for the site {site} is saved successfully")

    # Function to get the password
    def get_password (site):
        """"Retrive the password for the site"""
        if not os.path.exists(FILENAME):
            print("No passwords saved yet")
            return
        with open(FILENAME, "r") as f:
            for line in f:
                stored_site, store_password =line.strip().split(" ")
                if stored_site == site:
                    return store_password
        print(f" No password saved for the site {site}")
        return None

def main():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            pass #create the file if it does not exist

    action = input("Enter 'save' to save a password or 'get' to get a password: ")

    if action == "save":
        site = input("Enter the site : ")
        import string
        import random
        # Generate a random password
        characters= string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choices(characters, k=10))
        print(f"Generated password: {password}")
        save_password(site, password)
    elif action == "get":
        site = input("Enter the site name : ")
        password,_ = hash_password (site)
        if password:
            print(f" Password for the site {site} is {password}")
        else:
            print("invalid action")
if __name__=="__main__":
    main()
