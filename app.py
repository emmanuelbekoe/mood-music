import os
from dotenv import load_dotenv

# 1. Load the secrets
load_dotenv()
my_id = os.getenv('SPOTIPY_CLIENT_ID')

# 2. Say Hello
print("--------------------------")
print("WELCOME TO MOOD MUSIC!")
print(f"I found your Secret ID: {my_id[:5]}...") 
print("--------------------------")

mood = input("How do you feel? (happy/sad): ")

if mood == "happy":
    print("Finding a SUNNY song! ☀️")
else:
    print("Finding a COZY song! ☁️")
