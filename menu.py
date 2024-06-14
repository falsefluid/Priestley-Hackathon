# menu.py
import login
from leaderboard import leaderboard, friend_leaderboard
from room import room
import time
import sys

def menu():
    user_info = login.login_system()
    while True:
        try:
            menu_choice = int(input("""\nChoose your choice from the menu:
1. Leaderboard
2. Friend Leaderboard
3. Your Stats
4. Reward System
5. Rooms in use
6. Sign Out
7. Exit\n"""))
            if (menu_choice >= 1) and (menu_choice <= 7):
                if menu_choice == 1:
                    leaderboard(user_info)
                elif menu_choice == 2:
                    friend_leaderboard(user_info)
                elif menu_choice == 3:
                    pass
                elif menu_choice == 4:
                    pass
                elif menu_choice == 5:
                    room()
                elif menu_choice == 6:
                    print("Sign out complete.")
                    menu()
                else:
                    break
            else:
                print(f"{menu_choice} is not a valid choice, please pick from 1 - 6.")
        except ValueError:
            print("That is not a valid choice, please pick from 1 - 6.")
            time.sleep(1)
            