# lib/helpers.py
from models.homeroom import Homeroom
from models.student import Student



def seed_data():
    Homeroom.drop_table()
    Homeroom.create_table()
    Student.drop_table()
    Student.create_table()
    homeroom_101 = Homeroom.create(101,"Mr. Taylor",1)
    homeroom_103 = Homeroom.create(103,"Mr Jackson",1)
    homeroom_201 = Homeroom.create(201,"Ms. Martha",2)
    homeroom_301 = Homeroom.create(301,"Mrs. Casca",3)
    
    Student.create("Jojo Joestar",10,2.7,0,homeroom_301)
    Student.create("Josuke Joestar",9,3.7,2,homeroom_301)
    Student.create("Alexander Jono",9,4.0,2,homeroom_103)
    Student.create("Cynthia Unos",10,3.8,2,homeroom_201)
    Student.create("Mark Unos",12,4.0,2,homeroom_201)
    Student.create("Todd Jason",11,3.2,1,homeroom_101)
    Student.create("Mary Jason",11,3.9,2,homeroom_101)
    Student.create("Larry Nona",10,3.3,1,homeroom_101)
    
def delete_Homeroom():
    hr_room = input("Enter the room number of homeroom you want to remove: ")
    if homeroom := Homeroom.find_by_room(hr_room):
        #DELETES HOMEROOM
        homeroom.delete()
        print(f"Homeroom {hr_room} deleted")
    else:
        print(f"Homeroom {hr_room} not found")
    
def delete_student():
    student_name = input("Enter the name of the student you want to remove: ")
    if student := Student.find_by_name(student_name):
        student.delete()
        print(f"Student {student_name} deleted")
    else:
        print(f"Student {student_name} not found")

def list_by_floor(hr_floor):
    
    homerooms = Homeroom.get_all()
    count = 0
    for homeroom in homerooms:
        if homeroom.floor == int(hr_floor):
            print(homeroom)
            count += 1
    if count ==0:
        print("No homerooms found on this floor")
        return None
    else:
        return 1
def student_check(grade):
    students = Student.get_all()
    try:
        int(grade)
    except ValueError:
        print("Value not an integer")
        return False
    for student in students:
        if student.grade == int(grade):
            return True
    print("Grade not found")
    

def list_by_grade(grade):
    students = Student.get_all()
    sorted_students = sorted(students, key=lambda student: student.name)
    max_name_length = max(len(student.name) for student in sorted_students) + 2
    for student in sorted_students:
        if student.grade == grade:
            homeroom = Homeroom.find_by_id(student.homeroom_id)
            print(f'{student.name:{max_name_length}},Grade: {student.grade},GPA: {student.gpa},Homeroom: Room {homeroom.room}')
def homeroom_check(floor):
    homerooms = Homeroom.get_all()
    try:
        int(floor)
    except ValueError:
        print("Value not an integer")
        return False
    for homeroom in homerooms:
        if homeroom.floor == int(floor):
            return True
    print("Floor not found")
def homeroom_list(floor):
    homerooms = Homeroom.get_all()
    for homeroom in homerooms:
        if homeroom.floor == floor:
            print(f'Homeroom {homeroom.room},Floor: {homeroom.floor},Teacher: {homeroom.teacher}')
    


def detailed_student(name):
    students = Student.get_all()
    for student in students:
        if student.name == name:
            
            return student
    return None
def detailed_homeroom(room):
    homerooms = Homeroom.get_all()
    try:
        int(room)
    except ValueError:
        return None
    for homeroom in homerooms:
        if homeroom.room == int(room):
            return homeroom
    return None


        



def list_homerooms():
    homerooms = Homeroom.get_all()
    sorted_homeroom = sorted(homerooms, key= lambda homeroom: homeroom.room)
    for homeroom in sorted_homeroom:
        print(f"*.Homeroom {homeroom.room}, Teacher: {homeroom.teacher}")
def list_students():
    students = Student.get_all()
    sorted_students = sorted(students, key=lambda student: student.grade)
    max_name_length = max(len(student.name) for student in sorted_students) + 2
    for student in sorted_students:
        print(f'*. {student.name:{max_name_length}},Grade Level: {student.grade}')
#VALIDATES USER INPUT
def valid_choice(prompt):
    user_input = input(prompt)
    if user_input.lower() in ['q','a','b','f','g','e','r','s','z1','m','h','b','c']:
        return user_input.lower()
    try:
        int(user_input)
        return int(user_input)                                                                                                                                                                                                                                                                                                                                                                                                                                
    except ValueError:
        print("invalid input #4")
        return user_input.lower()
    
def int_check(prompt):
    user_input = input(prompt)
    try:
        int(user_input)
        return int(user_input)
    except ValueError:
        print("invalid input #5")
        return user_input
    
def convert_room_to_id(num):
    homerooms = Homeroom.get_all()
    for homeroom in homerooms:
        if num == homeroom.room:
            return homeroom
    return 1

def create_homeroom():
    room = input("Enter the homeroom room number: ")
    existing_homeroom = Homeroom.find_by_room(room)
    
    teacher = input("Enter name of the teacher: ")
    floor = input("Enter the level of the floor: ")
    if existing_homeroom:
        print(f'Homeroom {room} already exists')
        return
    try:
        homeroom = Homeroom.create(int(room),teacher,int(floor))
        print(f'Success: Homeroom {homeroom.room} created!')
    except Exception:
        print("Error: ",Exception)

def create_student():
    name = input("Enter the name of the student: ")
    grade = input("Enter the grade the student is in: ")
    gpa = input("Enter the students GPA: ")
    honors_classes = input("Enter the number of honors classes the student is in: ")
    homeroom_id = input("Enter the the room number of Homeroom: ")
    homeroom_id_verif =convert_room_to_id(int(homeroom_id))
    if homeroom_id_verif == 1:
        print("Not a valid homeroom")
        return
    try:
        student = Student.create(name,int(grade),float(gpa),int(honors_classes),homeroom_id_verif)
        print(f'Success Student: {student.name} added!')
    except Exception as exec:
        print("Error: ",exec)

def list_students_in_hr(num):
    
    students = Student.get_all()
    for student in students:
        if(student.homeroom_id == num):
            print(student)
        
    

def exit_program():
    print("Goodbye!")
    exit()

