# lib/cli.py

#IMPORT HELP FUNCTIONS HERE
from helpers import (
    exit_program,
    check_homerooms,
    convert_room_to_id,
    list_homerooms,
    list_students_in_hr,
    seed_data,
    valid_choice,
    delete_Homeroom,
    create_homeroom,
    list_by_floor,
    int_check
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
                
                list_homerooms()
                inner_menu()
                #IF STRING, TURNS TO LOWERCASE
                inner_choice = valid_choice("> ")
                menu_top()
                
                if inner_choice == 'q':
                    exit_program()
                elif inner_choice =='a':
                    create_homeroom()
                elif inner_choice =='r':
                    delete_Homeroom()
                elif inner_choice =='t':
                    t_option = int_check("Enter floor level: ")
                    list_by_floor(t_option)

                #checks if room # is found in Homeroom table
                elif check_homerooms((inner_choice)):
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
    
    print("b. Go back")
    print("q. Exit the program")
    print("a. Add a homeroom")
    print("t. List by floor")
    print("r. Remove a homeroom")

def super_inner_menu():
    pass


if __name__ == "__main__":
    main()
