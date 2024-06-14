# login.py
import pandas as pd
import time

# Load the data
df = pd.read_csv('MainSheet.csv', converters={'ID': str,
                 'Password':str}) # makes ID and password string just in case they start with 0

# Identification and validation of the user
def login_system():
    while True:
        try:
            username = input("What is your username? ")
            if username not in df["Uname"].values: # sees if username is in the column 'Uname'
                print("This username does not exist, try again.")
            else:
                user_info = df[df["Uname"] == username]
                print(f"{username} found!")
                for attempt in range(3):
                    password = input(f"Enter your password (Attempt {attempt + 1}/3): ") # password input
                    if password != user_info["Password"].values[0]:
                        print("Password is wrong. Retry.")
                    else:
                        print("Password is correct!\n")
                        time.sleep(1)
                        print(f"Welcome, {user_info['Uname'].values[0]}!")
                        return user_info 
                print("Number of attempts reached. Restarting.")
                time.sleep(1) # simulation of locking out
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Restarting...")
            time.sleep(1) # simulation of locking out

def view_score(user_info):
    pass
    points = user_info["TotalPoints"].values[0]
    u_name = user_info["Uname"].values[0]
    ID = user_info["ID"].values[0]
    print(f"Hello {u_name} {ID}, you currently have {points} points. Would you like to spend it?")

