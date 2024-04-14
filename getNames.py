import requests
import time

def getName(username):
    response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    return response.status_code != 200

count = 0
        
with open("nameList.txt") as fp:
    print("Finding available names...")
    for line in fp:
        name = line.strip()
        if name.isalpha():
            if len(set(name)) <= 25 and len(set(name)) >= 3: 
                if getName(name):
                    nameFile = open('nameFound.txt', 'a')
                    nameFile.write(f"{name}\n")
                    nameFile.close()
                    
                    print("Available name found:", name)
                    count += 1   
        
        time.sleep(1.7)
        
    print("We found", count, "Names")

input("Press enter to close")
