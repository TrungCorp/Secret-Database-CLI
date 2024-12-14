# lib/cli.py

#IMPORT HELP FUNCTIONS HERE
from helpers import (
    exit_program,
    convert_room_to_id,
    list_homerooms,
    list_students_in_hr,
    seed_data,
    list_by_grade,
    valid_choice,
    delete_Homeroom,
    create_homeroom,
    list_by_floor,
    int_check,
    list_students,
    create_student,
    delete_student
)


def main():
    #LVL 1
    choice = ""
    #LVL 2
    inner_choice = ""
    #LVL 3
    super_inner_choice = ""
    sort_search = ""
    sort_choice = ""
    s_inner_choice = ""
    m_inner_choice = ""
    f_inner_choice = ""
    print("Welcome Counselor")
    menu_top()
    
    seed_data()
    while choice !="q":
        #RESETS INNER_CHOICE AND SUPER_INNER
        inner_choice = ""
        
        

        
        menu()
        choice = valid_choice("> ")
        
        if choice == "q":
            exit_program()
        elif choice == "e":
            while inner_choice !="b":
                #CHOICE LEVEL 2
                menu_top()
                
                displayed_list(sort_choice,sort_search)
                inner_menu()
                #IF STRING, TURNS TO LOWERCASE
                inner_choice = valid_choice("> ")
                menu_top()
                
                if inner_choice == 'q':
                    exit_program()
                elif inner_choice == 'z1':
                    print(f'inner choice: {inner_choice},search: {sort_search}, s inner choice: {s_inner_choice}')
                elif inner_choice =='s':
                    while s_inner_choice != 'b':
                        sort_menu()
                        s_inner_choice = valid_choice("> ")
                        if s_inner_choice =='h':
                            if s_inner_choice == sort_choice:
                                print("Sort option already selected!")
                                

                            sort_choice = 'h'
                            s_inner_choice = ""
                            inner_choice = ""
                            break
                        elif s_inner_choice == "m":
                            if s_inner_choice == sort_choice:
                                print("Sort option already selected!")
                                
                            sort_choice = 'm'
                            s_inner_choice=""
                            inner_choice =""
                            break
                        elif s_inner_choice =='g':
                            sort_choice = 'g'
                            g_query = input("Enter the floor level you want to sort the list by: ")
                            if sort_check(g_query):
                                sort_search = int(g_query)
                            else:
                                print("Invalid input!")
                            s_inner_choice = ""
                            inner_choice=""
                            break
                            

                        else:
                            print("Invalid choice")
                    inner_choice= ""
                    s_inner_choice= ""
                            

                    
                elif inner_choice =='f':
                    while f_inner_choice!='b':
                        print("MANAGE BY HR")
                        print("q. Quit")
                        print("b. Back")
                        print("a. Add Homeroom")
                        print("r. Remove Homeroom")
                        f_inner_choice = valid_choice("> ")
                        if f_inner_choice =='a':
                            create_homeroom()
                            f_inner_choice = ""
                            inner_choice = ""
                        elif f_inner_choice =='r':
                            delete_Homeroom()
                            f_inner_choice = ""
                            inner_choice= ""
                        elif f_inner_choice =='q':
                            exit_program()
                    inner_choice =""
                    f_inner_choice = ""



                elif inner_choice =='m':
                    
                    while m_inner_choice != 'b':
                        manage_by_student_menu()
                        m_inner_choice = valid_choice("> ")
                        if m_inner_choice == 'a':
                            create_student()
                            m_inner_choice = ""
                        elif m_inner_choice == 'r':
                            delete_student()
                            m_inner_choice = ""
                        elif m_inner_choice == 'q':
                            exit_program()
                        
                    inner_choice = ""
                    m_inner_choice= ""
                    
                
       
                
                    
                
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
    print("s. Sort displayed list")
    print("f. Manage by Homeroom")
    print("m. Manage by Student")
    print("g. Get Detailed Info")
    
    
def sort_menu():
    print("SORT LIST")
    print("b. Go back")
    print("q. Exit the program")
    print("h. List all Homerooms")
    print("m. List all Students")

    
def sort_check(search):
    try:
       int(search)
       return True
    except ValueError:
        return False


def displayed_list(choice,search = None):
    if choice == "":
        list_homerooms()
        menu_top()
    elif choice == 'h':
        list_homerooms()
        menu_top()
    elif choice == 'm':
        list_students()
        menu_top()
    elif choice == 'g':
        list_by_floor(search)

def manage_by_student_menu():
    menu_top()
    print("b. Go back")
    print("q. Exit the program")
    print("a. Add a student")
    print("r. Remove a student")
    


if __name__ == "__main__":
    main()
