#Script created by: Benjamin Ortiz

import os

def show_menu():
    print("Select an option:")
    print("1. Convert YouTube to MP3")
    print("2. Background remover")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Loading...")
        os.system("python youtubeToMp3.py")
        
    elif choice == '2':
        print("Loading...")
        os.system("python backgroundRemover.py")
        
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid option. Please try again.")