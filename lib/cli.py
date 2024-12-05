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
    menu_top()
    
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
                menu_top()
                inner_menu()
                #IF STRING, TURNS TO LOWERCASE
                inner_choice = valid_choice("> ")
                menu_top()
                if inner_choice == 'q':
                    exit_program()
                elif inner_choice =='a':
                    pass
                elif inner_choice =='r':
                    pass
                elif inner_choice =='g':
                    list_homerooms()

                #checks if room # is found in Homeroom table
                if check_homerooms((inner_choice)):
                    list_students_in_hr(convert_room_to_id(inner_choice))
                
                    
                
        else:
            print("Invalid choice")


def menu():
    
    print("Please select an option:")
    print("q. Exit the program")
    print("e. Enter the program")
def menu_top():
    print("****************************")
def inner_menu():
    
    print("b. To go back")
    print("q. Exit the program")
    print("a. add a homeroom")
    print("t. List by floor")

def super_inner_menu():
    pass


if __name__ == "__main__":
    main()
