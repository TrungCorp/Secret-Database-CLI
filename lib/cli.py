# lib/cli.py

#IMPORT HELP FUNCTIONS HERE
from helpers import (
    exit_program,
    convert_room_to_id,
    list_homerooms,
    list_students_in_hr,
    seed_data,
    valid_choice,
    delete_Homeroom,
    create_homeroom,
    list_by_floor,
    int_check,
    create_student
)


def main():
    #LVL 1
    choice = ""
    #LVL 2
    inner_choice = ""
    #LVL 3
    super_inner_choice = ""
    print("Welcome Counselor")
    menu_top()
    
    seed_data()
    while choice !="q":
        #RESETS INNER_CHOICE AND SUPER_INNER
        inner_choice = ""
        super_inner_choice = ""
        
        menu()
        choice = valid_choice("> ")
        
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
                elif inner_choice == 'e':
                    print("e choice selected")
                #checks if room # is found in Homeroom table
                elif (inner_choice) =='e':
                    e_option = int_check("Enter the room number of homeroom: ")
                    list_students_in_hr(convert_room_to_id(e_option))
                    super_inner_choice = input("> ")
                    while super_inner_choice !='b':
                        super_inner_menu()
                
                    
                
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
    print("g. View all Homerooms")
    print("f. View Homeroom by floor level")
    print("a. Add a homeroom")
    
    print("r. Remove a homeroom")

def super_inner_menu():
    menu_top()
    print("b. Go back")
    print("q. Exit the program")
    print("a. Add a student")
    print("r. Remove a student")
    


if __name__ == "__main__":
    main()
