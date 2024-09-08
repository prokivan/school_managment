class Student:
    __students = []
    __STUDENT_ID = 1

    def __init__(self, name, last_name, name_class):
        self.name = name
        self.last_name = last_name
        self.name_class = name_class

    def create_student(self):
        self.__students.append(
            {
                self.__STUDENT_ID: [self.name, self.last_name, self.name_class]
            }
        )
        Student.__STUDENT_ID += 1

    def get_student(self, name_class):
        for student in self.__students:
            for data in student.values():
                if name_class in data:
                    print(f'Student name: {data[0]} {data[1]}')

    def schedule(self, name, last_name, teacher):
        for student in self.__students:
            for data in student.values():
                if name == data[0] and last_name == data[1]:
                    return teacher.get_program(data[2])


class Teacher:
    __teachers = []
    __TEACHER_ID = 1

    def __init__(self, name, last_name, specialization, classes):
        self.name = name
        self.last_name = last_name
        self.specialization = specialization
        self.classes = classes

    def create_teacher(self):
        self.__teachers.append(
            {
                self.__TEACHER_ID: [self.name, self.last_name, self.specialization, self.classes]
            }
        )
        Teacher.__TEACHER_ID += 1

    def get_classes(self, name, last_name):
        for teacher in self.__teachers:
            for data in teacher.values():
                if name in data and last_name in data:
                    print(data[-1])

    def get_program(self, name_class):
        for teacher in self.__teachers:
            for data in teacher.values():
                if name_class in data[-1]:
                    print(f'Teacher: {data[0]} {data[1]}\nLesson name: {data[2]}')


class Educator:
    __educators = []
    __EDUCATOR_ID = 1

    def __init__(self, name, last_name, name_class):
        self.name = name
        self.last_name = last_name
        self.name_class = name_class

    def create_educator(self):
        self.__educators.append(
            {
                self.__EDUCATOR_ID: [self.name, self.last_name, self.name_class]
            }
        )
        Educator.__EDUCATOR_ID += 1

    def get_class(self, name_class):
        for educator in self.__educators:
            for data in educator.values():
                if name_class in data:
                    print(f'Educator name: {data[0]} {data[1]}')

    def get_class_students(self, name, last_name, student):
        for educator in self.__educators:
            for data in educator.values():
                if name in data and last_name in data:
                    return student.get_student(data[-1])


def main():
    while True:
        print('\nChoice option:\n1)Create person\n2)Manage process\n3)End\n')
        option = input('Input option (1,2,3): ')
        if option == '3':
            print('End...')
            break

        if option == '1':
            while True:
                print('\nOptions:\n1)Create student\n2)Create teacher\n3)Create educator\n4)End')
                option = input('Input option (1,2,3,4): ')
                if option == '4':
                    break

                if option == '1':
                    name = input('Input student name: ').capitalize()
                    last_name = input('Input student last name: ').capitalize()
                    name_class = input('Input name of the class: ')
                    student = Student(name, last_name, name_class)
                    student.create_student()
                    print('Added!')
                elif option == '2':
                    name = input('Input teacher name: ').capitalize()
                    last_name = input('Input teacher last name: ').capitalize()
                    specialization = input('Input specialization: ').capitalize()
                    classes = []
                    while True:
                        name_classes = input('Input names of the classes: ')
                        if not name_classes:
                            break
                        classes.append(name_classes)
                    teacher = Teacher(name, last_name, specialization, classes)
                    teacher.create_teacher()
                    print('Added!')
                elif option == '3':
                    name = input('Input educator name: ').capitalize()
                    last_name = input('Input educator last name: ').capitalize()
                    name_class = input('Input name of the class: ')
                    educator = Educator(name, last_name, name_class)
                    educator.create_educator()
                    print('Added!')
        elif option == '2':
            while True:
                print('\nChoice option:\n1)Class\n2)Student\n3)Teacher\n4)Educator\n5)End')
                option = input('Input option (1,2,3,4,5): ')
                if option == '5':
                    print('End...')
                    break

                if option == '1':
                    name_class = input('Input name of the class: ')
                    print('Students:')
                    student.get_student(name_class)
                    print('Educator:')
                    educator.get_class(name_class)
                elif option == '2':
                    student_name = input('Input student name: ').capitalize()
                    student_last_name = input('Input student last name: ').capitalize()
                    student.schedule(student_name, student_last_name, teacher)
                elif option == '3':
                    teacher_name = input('Input teacher name: ').capitalize()
                    teacher_last_name = input('Input teacher last name: ').capitalize()
                    print('Classes:')
                    teacher.get_classes(teacher_name, teacher_last_name)
                elif option == '4':
                    educator_name = input('Input educator name: ').capitalize()
                    educator_last_name = input('Input educator last name: ').capitalize()
                    print('Students:')
                    educator.get_class_students(educator_name, educator_last_name, student)


if __name__ == '__main__':
    main()
