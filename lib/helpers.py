# lib/helpers.py
from models.homeroom import Homeroom
from models.student import Student



def seed_data():
    Homeroom.drop_table()
    Homeroom.create_table()
    Student.drop_table()
    Student.create_table()
    homeroom_101 = Homeroom.create(101,"Mr. Taylor",1)
    homeroom_201 = Homeroom.create(201,"Ms. Martha",2)
    homeroom_103 = Homeroom.create(103,"Mr Jackson",1)
    Student.create("Alexander Jono",9,4.0,2,homeroom_103)
    Student.create("Cynthia Unos",10,3.8,2,homeroom_201)
    Student.create("Mark Unos",12,4.0,2,homeroom_201)
    Student.create("Todd Jason",11,3.2,1,homeroom_101)
    Student.create("Mary Jason",11,3.9,2,homeroom_101)
    Student.create("Larry Nona",10,3.3,1,homeroom_101)
    
def delete_Homeroom():
    hr_room = input("Enter the room number of homeroom you want to remove: ")
    if homeroom := Homeroom.find_by_room(hr_room):
        homeroom.delete()
        print(f"Homeroom {hr_room} deleted")
    else:
        print(f"Homeroom {hr_room} not found")

def list_by_floor(hr_floor):
    
    homerooms = Homeroom.get_all()
    count = 0
    for homeroom in homerooms:
        if homeroom.floor == int(hr_floor):
            print(homeroom)
            count += 1
    if count ==0:
        print("Floor does not exist")
        

def check_homerooms(target_room):
    if (isinstance(target_room,str)):
        return None
    homerooms = Homeroom.get_all()
    for homeroom in homerooms:
        if homeroom.room == target_room:
            #print(f"Found homeroom: {homeroom}")
            return homeroom
    
    print(f"No homeroom found with room number {target_room}")
        
    return None

def list_homerooms():
    homerooms = Homeroom.get_all()
    for homeroom in homerooms:
        print(homeroom)

def valid_choice(prompt):
    user_input = input(prompt)
    if user_input.lower() in ['q','a','b','e','r','t']:
        return user_input.lower()
    try:
        int(user_input)
        return int(user_input)
    except ValueError:
        print("invalid input #4")
        return user_input
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
            print(f"TEST: HOMEROOM ID: {homeroom.id}")
            return homeroom.id
    return None
def create_homeroom():
    room = input("Enter the homeroom room number: ")
    teacher = input("Enter name of the teacher: ")
    floor = input("Enter the level of the floor: ")
    try:
        homeroom = Homeroom.create(int(room),teacher,int(floor))
        print(f'Success: {homeroom}')
    except Exception:
        print("Error: ",Exception)

    
def list_students_in_hr(num):
    
    students = Student.get_all()
    for student in students:
        if(student.homeroom_id == num):
            print(student)
        
    

def exit_program():
    print("Goodbye!")
    exit()

