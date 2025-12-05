import os
import sys
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
user_input = input("Do you want to restart the program? (yes/no): ").lower()

def main_program_logic():
    """Contains the main logic of your program."""
    print("Program started.")
    # Your program's code goes here
    print("Program finished its current execution.")

if __name__ == "__main__":
    main_program_logic()

if user_input == "yes":
        print("Restarting program...")
        restart_program()
else:
        print("Exiting program.")