# lib/cli.py

#IMPORT HELP FUNCTIONS HERE
from helpers import (
    exit_program,
    check_homerooms,
    convert_room_to_id,
    list_homerooms,
    list_students_in_hr,
    seed_data,
    valid_choice
)


def main():
    choice = ""
    inner_choice = ""
    print("Welcome Counselor")
    
    
    seed_data()
    while choice !="q":
        #CHOICE LEVEL 1
        inner_choice = ""
        menu()

        choice = input("> ")

        if choice == "q":
            exit_program()
        elif choice == "e":
            while inner_choice !="b":
                #CHOICE LEVEL 2
                inner_menu()

                inner_choice = valid_choice("> ")
                
                if check_homerooms((inner_choice)):
                    list_students_in_hr(convert_room_to_id(int(inner_choice)))
                
                    
                
        else:
            print("Invalid choice")


def menu():
    print("*************************")
    print("Please select an option:")
    print("q. Exit the program")
    print("e. Enter the program")

def inner_menu():
    list_homerooms()
    print("b. To go back")
    print("q. Exit the program")
    print("a. add a homeroom")
    print("t. List by floor")

def super_inner_menu():
    pass


if __name__ == "__main__":
    main()
