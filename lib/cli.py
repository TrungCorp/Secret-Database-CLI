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
    detailed_homeroom,
    detailed_student,
    homeroom_check,
    homeroom_list,
    student_check
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
        
        

        #MAIN MENU
        menu()
        choice = valid_choice("> ")
        
        if choice == "q":
            exit_program()
        elif choice == "e":
            while inner_choice !="b":
               
                menu_top()
                
                displayed_list(sort_choice,sort_search)
                inner_menu()
                #IF STRING, TURNS TO LOWERCASE
                #ASKS FOR INNER CHOICE
                inner_choice = valid_choice("> ")
                menu_top()
                
                if inner_choice == 'q':
                    exit_program()
                #SORT OPTION
                elif inner_choice =='s':
                    while s_inner_choice != 'b':
                        displayed_list(sort_choice,sort_search)
                        sort_menu()
                        s_inner_choice = valid_choice("> ")
                        #H CHOICE WITHIN SORT 
                        if s_inner_choice =='h':
                            if s_inner_choice == sort_choice or sort_choice == "" :
                                print("Homerooms already displayed!")
                            
                            #SET SORT CHOICE TO H AND RESETS INNER AND S_INNER CHOICE
                            sort_choice = 'h'
                            s_inner_choice = ""
                            #inner_choice = ""
                            
                        #M CHOICE WITHIN SORT
                        elif s_inner_choice == "m":
                            if s_inner_choice == sort_choice:
                                print("Sort option already selected!")
                               
                            sort_choice = 'm'
                            s_inner_choice=""
                            #inner_choice =""
                            
                        #G CHOICE WITHIN SORT
                        elif s_inner_choice == 'g':
                            g_h_option = ""
                            g_m_option = ""
                            g_option = ""
                            
                            while g_option !="b":
                                print("b. Back")
                                print("q. Quit program")
                                print("h. Detailed Info on Homerooms")
                                print("m. Detailed Info on Students")
                                g_option = input("> ")
                                if g_option =='h':
                                    while g_h_option != 'b':
                                        room = input("Enter room number of Homeroom: ")
                                        homeroom_obj = detailed_homeroom(room)

                                        if homeroom_obj :
                                            print(f"Success! {homeroom_obj.room} found!")
                                            sort_search = room
                                            sort_choice = 'j'
                                            g_h_option= "b"
                                        elif room =='b':
                                            g_h_option = 'b'
                                        else:
                                            print("Homeroom does not exist")
                                    s_inner_choice = ""
                                    #inner_choice=""
                                    g_option = 'b'
                                    
                                elif g_option =='m':
                                    
                                    while g_m_option != 'b':
                                        name = input("Enter student's name: ")

                                        student_obj = detailed_student(name)
                                        if student_obj:
                                            print(f"Success! {student_obj.name} found!")
                                            sort_search = name
                                            sort_choice = 'k'
                                            
                                            g_m_option = 'b'
                                        elif name =="b":
                                            g_m_option = 'b'
                                        else:
                                            print("Student does not exist")
                                    s_inner_choice=""
                                    #inner_choice =""
                                    g_option = 'b'
                                    break
                        #F CHOICE WITHIN SORT
                        elif s_inner_choice == 'f':
                            if sort_choice !='v':

                                sort_choice ="h"
                                sort_search = ""
                            f_choice_op = ""
                            while f_choice_op !="b":
                                displayed_list(sort_choice,sort_search)
                                f_choice_op = input("Enter floor")
                                
                                hr_room = homeroom_check(f_choice_op)
                                if hr_room  :
                                    print(f"Success! Floor  found!")
                                    sort_choice = 'v'
                                    sort_search = int(f_choice_op)
                                    f_choice_op = 'b'
                            s_inner_choice = ''
                            #inner_choice = ""
                            

                        elif s_inner_choice == 'c':
                            
                            c_inner_choice = ""
                            while c_inner_choice !="b":
                                print("Enter grade of students: ")
                                c_inner_choice = input("> ")
                                floor = student_check(c_inner_choice)
                                if floor:
                                    sort_choice = "c"
                                    sort_search = int(c_inner_choice)
                                    c_inner_choice ="b"
                                    #inner_choice=""
                                    


                        

                        else:
                            print("Invalid choice")
                    inner_choice= ""
                    s_inner_choice= ""
                            
 
                #MANAGE BY HR CHOICE
                elif inner_choice =='f':
                    
                    while f_inner_choice!='b':
                        if sort_choice !='j' and sort_choice !="v":
                            sort_choice = 'h'
                        displayed_list(sort_choice,sort_search)
                        manage_by_hr_menu()
                        
                        f_inner_choice = input("> ")
                        if f_inner_choice =='a':
                            create_homeroom()
                            
                        elif f_inner_choice =='r':
                            delete_Homeroom()
                        
                            
                        elif f_inner_choice =='q':
                            exit_program()
                        elif f_inner_choice == 'f':
                            hr_op = ""
                            while hr_op !="b":
                                print("Enter Floor: ")
                                hr_op = input("> ")
                                if hr_op == "b":
                                    break
                                floor = homeroom_check(hr_op)
                                if floor:
                                    sort_choice = "v"
                                    sort_search = int(hr_op)
                                    hr_op = "b"

                        elif f_inner_choice == "h":
                            if sort_choice == "h":
                                print("Homerooms already displayed!")
                            sort_choice = "h"
                            sort_search = ""
                        elif f_inner_choice == "b":
                            break
                        else:
                            print("Invalid choice")
                    inner_choice =""
                    f_inner_choice = ""
                    


                #MANAGE BY STUDENT CHOICE
                elif inner_choice =='m':
                    
                    while m_inner_choice != 'b':
                        if sort_choice !="k" and sort_choice !="c":
                            sort_choice = 'm'
                        displayed_list(sort_choice,sort_search)
                        manage_by_student_menu()
                        m_inner_choice = valid_choice("> ")
                        if m_inner_choice == 'a':
                            create_student()
                            m_inner_choice = ""
                        elif m_inner_choice == 'r':
                            delete_student()
                            m_inner_choice = ""
                        elif m_inner_choice == 'm':
                            
                            sort_choice = 'm'
                            sort_search = ""
                        elif m_inner_choice == 'f':
                           
                            grade = ""

                            while grade != "b":
                                print("Enter the grade level: ")
                                grade = input("> ")
                                student_grade = student_check(grade)
                                if student_grade:
                                    sort_choice = "c"
                                    sort_search =int(grade)
                                    break
                                
                            grade =""
                            m_inner_choice = ""



                            
                        #QUIT PROGRAM  
                        elif m_inner_choice == 'q':
                            exit_program()
                    #RESETS INNER CHOICE AND M INNER CHOICE
                    inner_choice = ""
                    m_inner_choice= ""
                



        #PRINTS INVALID CHOICE FOR MAIN MENU
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
    elif choice == 'k':
        var_k = detailed_student(search)
        print(f'{var_k.name},Grade: {var_k.grade},GPA: {var_k.gpa},Honors Classes: {var_k.honors_classes}')
    elif choice == 'j':
        var_j = detailed_homeroom(search)
        print(f"Homeroom {var_j.room}, Floor: {var_j.floor}, Teacher: {var_j.teacher}")
    elif choice == "v":
        homeroom_list(search)
    elif choice == "c":
        list_by_grade(search)


    


if __name__ == "__main__":
    main()
