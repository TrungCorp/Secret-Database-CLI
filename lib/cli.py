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
    delete_student,
    detailed_student
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
                    print(f's inner choice: {s_inner_choice},search: {sort_search}, s inner choice: {s_inner_choice}')
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
                        elif s_inner_choice == 'g':
                            g_option = ""
                            
                            
                            while g_option !="b":
                                print("b. Back")
                                print("q. Quit program")
                                print("h. Detailed Info on Homerooms")
                                print("m. Detailed Info on Students")
                                g_option = input("> ")
                                if g_option =='h':
                                    print("HOMEROOM OPTION CHOSEN!")
                                    s_inner_choice = "b"
                                    inner_choice=""
                                    g_option = 'b'
                                    break
                                elif g_option =='m':
                                    inner_g_option = ""
                                    while inner_g_option != 'b':
                                        name = input("enter students name")

                                        student_name =detailed_student(name)
                                        if student_name == 1:
                                            inner_g_option = 'b'
                                        else:
                                            print("Student does not exist")
                                    s_inner_choice="b"
                                    inner_choice =""
                                    g_option = 'b'
                                    break

                        else:
                            print("Invalid choice")
                    inner_choice= ""
                    s_inner_choice= ""
                            

                    
                elif inner_choice =='f':
                    
                    while f_inner_choice!='b':
                        sort_choice = 'h'
                        displayed_list(sort_choice)
                        manage_by_hr_menu()
                        
                        f_inner_choice = valid_choice("> ")
                        if f_inner_choice =='a':
                            create_homeroom()
                            f_inner_choice = "b"
                            inner_choice = ""
                        elif f_inner_choice =='r':
                            delete_Homeroom()
                            f_inner_choice = "b"
                            inner_choice= ""
                        elif f_inner_choice =='q':
                            exit_program()
                    inner_choice =""
                    f_inner_choice = ""
                    sort_choice = ""



                elif inner_choice =='m':
                    
                    while m_inner_choice != 'b':
                        sort_choice = 'm'
                        displayed_list(sort_choice)
                        manage_by_student_menu()
                        m_inner_choice = valid_choice("> ")
                        if m_inner_choice == 'a':
                            create_student()
                            m_inner_choice = ""
                        elif m_inner_choice == 'r':
                            delete_student()
                            m_inner_choice = ""
                        elif m_inner_choice == 'f':
                           
                            grade = ""

                            while grade != "b":
                                print("Enter the grade level: ")
                                grade = input("> ")
                                try:
                                    num = int(grade)
                                    print(num)
                                    list_by_grade(num)
                                    if num<9 or num >12:
                                        print("Please enter a grade between 9 and 12")
                                    grade = 'b'
                                except ValueError:
                                    print("Invalid Input")
                                
                            grade =""
                            m_inner_choice = ""



                            
                            
                        elif m_inner_choice == 'q':
                            exit_program()
                        
                    inner_choice = ""
                    m_inner_choice= ""
                    sort_choice = ""
                
       
                
                    
                
        else:
            print("Invalid choice")


def menu():
    print("WELCOME TO THE CONSULOR APP")
    print("Please select an option:")
    print("q. Exit the program")
    print("e. Enter the program")
def menu_top():
    print("****************************")
def inner_menu():
    print("MAIN MENU")
    print("b. Go back")
    print("q. Exit the program")
    print("s. Sort displayed list")
    print("f. Manage by Homeroom")
    print("m. Manage by Student")
    
def manage_by_hr_menu():
    print("MANAGE BY HR")
    print("q. Quit")
    print("b. Back")
    print("a. Add Homeroom")
    print("r. Remove Homeroom")  
    print("f. List Homeroom by Floor")
    print("h. List All Homerooms")
    print("g. Detailed Info on Homeroom")   

def manage_by_student_menu():
    print("MANAGE BY STUDENTS")
    print("b. Go back")
    print("q. Exit the program")
    print("a. Add a student")
    print("r. Remove a student") 
    print("m. List all Students")
    print("f. List Student by Grade")
    print("g. Detailed Info on Student")
def sort_menu():
    print("SORT LIST")
    print("b. Go back")
    print("q. Exit the program")
    print("h. List all Homerooms")
    print("m. List all Students")
    print("g. Detailed Info")
    print("f. List Homeroom by Floor")
    print("c. List Student by Grade")
    
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


    


if __name__ == "__main__":
    main()
