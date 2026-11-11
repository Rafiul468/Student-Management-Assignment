class StudentDatabase:
    student_list =[]

    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)


class Student:
    def __init__(self, student_id, name, department, is_enrolled = False):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    def get_student_id(self):
        return self.__student_id
    
    def enroll_student(self):
        if self.__is_enrolled:
            print('Error: Student is already enrolled')
        else:
            self.__is_enrolled = True
            print(f'Student: {self.__name} ID: {self.__student_id} has been enrolled')

    def drop_student(self):
        if not self.__is_enrolled:
            print('Error: Student is not enrolled.')
        else:
            self.__is_enrolled = False
            print(f'student: {self.__name} ID: {self.__student_id} has been dropped.')

    def view_student_info(self):
        print(f'ID: {self.__student_id} , Name: {self.__name} , Department: {self.__department} , Enrolled: {self.__is_enrolled}')

def find_student(student_id):
    for student in StudentDatabase.student_list:
        if student.get_student_id() ==  student_id:
            return student

    return None


def menu():
    while True:
        print('\n---Student Managment Menu---')
        print('1. View All Students')
        print('2. Enroll Student')
        print('3. Drop Student')
        print('4. Exit')
        choice = input('Enter your choice (1-4): ')


        if choice == '1':
            for student in StudentDatabase.student_list:
                student.view_student_info()

        elif choice == '2' or choice == '3':
            sid = input('Enter student ID: ').strip()
            student = find_student(sid)
            
            if student is None:
                print('Error: Invalid student ID.')
            elif choice == '2':
                student.enroll_student()
            else:
                student.drop_student()

        elif choice == '4':
            print('GoodBye')
            break
        else:
            print('Invalid choice, try again.')

s1 = Student('s101', 'Alice Smith', 'Computer Science', True)
s2 = Student('s102', 'Bob Johnson', 'Mathmatics', False)
s3 = Student('s103', 'Charlie Lee', 'Physic', True)

menu()



        
