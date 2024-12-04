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
    

def helper_prime():
    Homeroom.drop_table()
    Homeroom.create_table()

def check_homerooms(target_room):
    if (isinstance(target_room,str)):
        return None
    target = (target_room)
    homerooms = Homeroom.get_all()
    for homeroom in homerooms:
        if homeroom.room == target:
            #print(f"Found homeroom: {homeroom}")
            return homeroom
    print(f"No homeroom found with room number {target}")
    return None




def list_homerooms():
    homerooms = Homeroom.get_all()
    for homeroom in homerooms:
        print(homeroom)

def valid_choice(prompt):
    user_input = input(prompt)
    if user_input.lower() in ['q','a','b']:
        return user_input.lower()
    try:
        int(user_input)
        return int(user_input)
    except ValueError:
        print("Invalid input")
        return None
        



def convert_room_to_id(num):
    
    
    homerooms = Homeroom.get_all()
    for homeroom in homerooms:
        if num == homeroom.room:
            print(f"TEST: HOMEROOM ID: {homeroom.id}")
            return homeroom.id
    return None
    
def list_students_in_hr(num):
    
    students = Student.get_all()
    for student in students:
        if(student.homeroom_id == num):
            print(student)
        
    

def exit_program():
    print("Goodbye!")
    exit()

