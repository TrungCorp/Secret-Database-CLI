from models.__init__ import CURSOR, CONN

class Homeroom:
    all ={}

    def __init__(self,room,teacher,floor,id = None):
        self.id = id
        self.room = room
        self.teacher = teacher
        self.floor = floor


    def __repr__(self):
        return (
            f"{self.id}.<Homeroom :Room: {self.room},Floor Level: {self.floor}, {self.teacher}>"
        )

    @property 
    def room(self):
        return self._room
    @room.setter
    def room(self,room):
        if isinstance(room,int) :
            self._room = room
        else:
            raise ValueError(
                "Room must be a non-empty integer value"
            )

    @property 
    def floor(self):
        return self._floor
    @floor.setter
    def floor(self,floor):
        if isinstance(floor,int) :
            self._floor = floor
        else:
            raise ValueError(
                "Floor must be a non-empty integer value"
            )
    
    @property
    def teacher(self):
        return self._teacher
    @teacher.setter
    def teacher(self,teacher):
        if isinstance(teacher,str) and len(teacher):
            self._teacher = teacher
        else:
            raise ValueError(
                "Teacher must be of type string and not empty"
            )

    
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS homerooms (
                id INTEGER PRIMARY KEY,
                room INTEGER,
                teacher TEXT,
                floor INTEGER)
            """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod 
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS homerooms;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO homerooms (room,teacher,floor)
            VALUES (?,?,?)
        """
        CURSOR.execute(sql,(self.room,self.teacher,self.floor))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    @classmethod
    def create(cls,room,teacher,floor):
        homeroom = cls(room,teacher,floor)
        homeroom.save()
        return homeroom
    
    def update(self):
        sql = """
            DELETE FROM homerooms 
            WHERE id = ?
        """
        CURSOR.execute(sql,(self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls,row):
        homeroom = cls.all.get(row[0])
        if homeroom:
            homeroom.room = row[1]
            homeroom.teacher = row[2]
            homeroom.floor = row[3]
        else:
            homeroom = cls(row[1],row[2],row[3])
            homeroom.id = row[0]
            cls.all[homeroom.id] = homeroom
        return homeroom

    @classmethod 
    def get_all(cls):
        sql = """
            SELECT * 
            FROM homerooms
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls,id):
        sql ="""
            SELECT *
            FROM homerooms
            WHERE id = ?

        """
    
        row = CURSOR.execute(sql,(id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_room(cls,room):
        sql = """
            SELECT * 
            FROM homerooms
            WHERE room is ?
        """
        row  = CURSOR.execute(sql,(room,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def students(self):
        from models.student import Student
        sql = """
            SELECT * FROM students
            WHERE homeroom_id = ?
        """
        CURSOR.execute(sql, (self.homeroom.id,),)
        rows = CURSOR.fetchall()
        return [
            Student.instance_from_db(row) for row in rows
        ]