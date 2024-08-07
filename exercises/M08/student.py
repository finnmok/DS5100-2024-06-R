class Student:
    
    # constructor
    def __init__(self, name, courses=None):
        self.name = name # string type
        self.courses = [] if courses is None else courses # list of strings
        self.num_courses = len(self.courses)
        
    # enroll in a course
    def enroll_in_course(self, course_name): 
        self.courses.append(course_name)
        self.num_courses += 1 # increment the number of courses

    def unenroll_in_course(self,course_name):
        if course_name not in self.courses:
            raise ValueError("This course is not in course list")
    
        self.courses.remove(course_name)
        self.num_courses -= 1
    