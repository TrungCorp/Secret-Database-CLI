from models.__init__  import CURSOR , CONN
from models.homeroom import Homeroom
class Student:
    all = {}

    def __init__(self,name,grade,gpa,honors_classes,homeroom, id= None):
        self.id = id
        self.name = name
        self.grade = grade
        self.gpa = gpa
        self.honors_classes = honors_classes
        self.homeroom_id = homeroom.id


    def __repr__(self):
        return(
            f"<Student: Name:{self.name},GPA: {self.gpa},honors classes: {self.honors_classes}>"
        )
    @property
    def homeroom(self):
        return self._homeroom
    
    @homeroom.setter
    def homeroom(self,homeroom):
        if isinstance(homeroom,Homeroom) and homeroom.id is not None:
            self.homeroom_id = homeroom.id
        else:
            raise ValueError("Invalid homeroom provided")
    #GPA PROPERTY
    @property
    def gpa(self):
        return self._gpa
    @gpa.setter
    def gpa(self,gpa):
        if isinstance(gpa,float) and (gpa>= 0.0 and gpa<= 4.0):
            self._gpa = gpa
        else:
            raise ValueError(
                "gpa must be a float between 0 and 4"
            )
    #NAME PROPERTY
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) :
            self._name = name
        else:
            raise ValueError(
                "name must be of type string and non-empty"
            )
    #GRADE PROPERTY
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self,grade):
        if isinstance(grade,int) and (grade>=9 and grade<=12):
            self._grade = grade
        else:
            raise ValueError(
                "grade must be of type integer and be between 9 and 12"
            )
 
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Employee instances """
        sql = """
            CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            grade INTEGER,
            gpa FLOAT,
            honors_classes INTEGER,
            homeroom_id INTEGER,
            FOREIGN KEY (homeroom_id) REFERENCES homerooms(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Employee instances """
        sql = """
            DROP TABLE IF EXISTS students;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, job title, and department id values of the current Student object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO students (name, grade,gpa,honors_classes, homeroom_id)
                VALUES (?, ?, ? , ? , ?)
        """

        CURSOR.execute(sql, (self.name, self.grade,self.gpa,self.honors_classes ,self.homeroom_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    
    def update(self):
        """Update the table row corresponding to the current Student instance."""
        sql = """
            UPDATE employees
            SET name = ?, grade = ?, gpa = ?, honors_classes = ?, homeroom_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.grade,self.gpa,self.honors_classes,
                             self.homeroom_id, self.id))
        CONN.commit()
    
    def delete(self):
        """Delete the table row corresponding to the current Student instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM students
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, grade,gpa,honors_classes, homeroom):
        """ Initialize a new Student instance and save the object to the database """
        student = cls(name, grade,gpa,honors_classes, homeroom)
        student.save()
        return student

    @classmethod
    def instance_from_db(cls, row):
        """Return an Student object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        student = cls.all.get(row[0])
        if student:
            # ensure attributes match row values in case local instance was modified
            student.name = row[1]
            student.grade = row[2]
            student.gpa = row[3]
            student.honors_classes = row[4]
            student.homeroom_id = row[5]
        else:
            # not in dictionary, create new instance and add to dictionary
            student = cls(row[1], row[2], row[3],row[4],row[5])
            student.id = row[0]
            cls.all[student.id] = student
        return student

    @classmethod
    def get_all(cls):
        """Return a list containing one Student object per table row"""
        sql = """
            SELECT *
            FROM students
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    @classmethod
    def find_by_id(cls, id):
        """Return Student object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM students
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def find_by_name(cls, name):
        """Return Student object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM students
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
