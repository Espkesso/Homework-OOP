class Student:
    all_students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.all_students.append(self)

    def rate_lecture(self, lecturer, course, grade):       # Method for evaluating lecturers
        if (isinstance(lecturer, Lecturer) and isinstance(grade, int) and course in self.courses_in_progress
                and course in lecturer.courses_attached and 0 < grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def mid_rate(self):        # Method for calculating a student's grade point average
        total_summ = 0
        total_length = 0
        for values in self.grades.values():
            total_summ += sum(values)
            total_length += len(values)
        return float(f"{total_summ / total_length:.2f}") if total_length > 0 else 0

    # We define magical methods for comparing students by grade point average.
    def __eq__(self, other):
        return self.mid_rate() == other.mid_rate()

    def __ne__(self, other):
        return self.mid_rate() != other.mid_rate()

    def __lt__(self, other):
        return self.mid_rate() < other.mid_rate()

    def __gt__(self, other):
        return self.mid_rate() > other.mid_rate()

    def __le__(self, other):
        return self.mid_rate() <= other.mid_rate()

    def __ge__(self, other):
        return self.mid_rate() >= other.mid_rate()

    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.mid_rate()}\n"
                f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {", ".join(self.finished_courses)}\n")

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    all_lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.all_lecturers.append(self)

    def mid_rate(self):        # Method for calculating a lecturer's grade point average
        total_summ = 0
        total_length = 0
        for values in self.grades.values():
            total_summ += sum(values)
            total_length += len(values)
        return float(f"{total_summ / total_length:.2f}") if total_length > 0 else 0

    # We define magical methods for comparing lecturers by grade point average.
    def __eq__(self, other):
        return self.mid_rate() == other.mid_rate()

    def __ne__(self, other):
        return self.mid_rate() != other.mid_rate()

    def __lt__(self, other):
        return self.mid_rate() < other.mid_rate()

    def __gt__(self, other):
        return self.mid_rate() > other.mid_rate()

    def __le__(self, other):
        return self.mid_rate() <= other.mid_rate()

    def __ge__(self, other):
        return self.mid_rate() >= other.mid_rate()

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mid_rate()}\n"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

    def rate_student(self, student, course, grade):        # Method for evaluating students
        if (isinstance(student, Student) and isinstance(grade, int) and course in self.courses_attached
                and course in student.courses_in_progress and 0 < grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

# We add objects and call all created methods
student_1 = Student("Филипп", "Свистопляска", "М")
student_2 = Student("Жанна", "Кукуцаполь", "Ж")
student_3 = Student("Пьер", "Монперансье", "М")
student_4 = Student("Зинаида", "Тузембобель", "Ж")
lecturer_1 = Lecturer("Тимур", "Анвартдинов")
lecturer_2 = Lecturer("Евгений", "Зачетный")
lecturer_3 = Lecturer("Олеся", "Хабибулаева")
lecturer_4 = Lecturer("Константин", "Токсичный")
reviewer_1 = Reviewer("Игнат", "Крамольный")
reviewer_2 = Reviewer("Григорий", "Переподвыподвертов")
reviewer_3 = Reviewer("Криштиану", "Роналдо")
reviewer_4 = Reviewer("Антонина", "Борошмель")

student_1.courses_in_progress += ["Python", "C#", "Scala", "Kotlin"]
student_2.courses_in_progress += ["Python", "C++", "Java"]
student_3.courses_in_progress += ["Java", "C++", "Scala", "Kotlin"]
student_4.courses_in_progress += ["Python", "C#", "Java"]
student_1.finished_courses += ["C++"]
student_2.finished_courses += ["C#"]
student_3.finished_courses += ["Python"]
student_4.finished_courses += ["Scala"]
lecturer_1.courses_attached += ["Python", "C#", "C++"]
lecturer_2.courses_attached += ["Java", "Scala", "Kotlin"]
lecturer_3.courses_attached += ["Python", "Kotlin", "Scala"]
lecturer_4.courses_attached += ["Java", "C#", "C++"]
reviewer_1.courses_attached += ["C++", "C#", "Scala"]
reviewer_2.courses_attached += ["Python", "Java", "Kotlin"]
reviewer_3.courses_attached += ["Scala", "C#", "Kotlin", "C++"]
reviewer_4.courses_attached += ["Python", "C#", "C++"]

reviewer_1.rate_student(student_1, "C#", 8)
reviewer_1.rate_student(student_2, "C++", 7)
reviewer_1.rate_student(student_3, "Scala", 9)
reviewer_1.rate_student(student_4, "C#", 10)
reviewer_2.rate_student(student_1, "Kotlin", 6)
reviewer_2.rate_student(student_2, "Python", 9)
reviewer_2.rate_student(student_3, "Kotlin", 8)
reviewer_2.rate_student(student_4, "Java", 10)
reviewer_3.rate_student(student_1, "C#", 8)
reviewer_3.rate_student(student_2, "C++", 5)
reviewer_3.rate_student(student_3, "Scala", 6)
reviewer_3.rate_student(student_4, "C#", 8)
reviewer_4.rate_student(student_1, "Python", 6)
reviewer_4.rate_student(student_2, "C++", 7)
reviewer_4.rate_student(student_3, "C++", 10)
reviewer_4.rate_student(student_4, "Python", 5)

student_1.rate_lecture(lecturer_1, "Python", 10)
student_1.rate_lecture(lecturer_2, "Scala", 8)
student_1.rate_lecture(lecturer_3, "Kotlin", 7)
student_1.rate_lecture(lecturer_4, "C#", 10)
student_2.rate_lecture(lecturer_1, "C++", 7)
student_2.rate_lecture(lecturer_2, "Java", 10)
student_2.rate_lecture(lecturer_3, "Python", 9)
student_2.rate_lecture(lecturer_4, "C++", 8)
student_3.rate_lecture(lecturer_1, "C++", 9)
student_3.rate_lecture(lecturer_2, "Kotlin", 6)
student_3.rate_lecture(lecturer_3, "Scala", 10)
student_3.rate_lecture(lecturer_4, "Java", 7)
student_4.rate_lecture(lecturer_1, "Python", 8)
student_4.rate_lecture(lecturer_2, "Java", 6)
student_4.rate_lecture(lecturer_3, "Python", 10)
student_4.rate_lecture(lecturer_4, "C#", 8)

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(lecturer.grades)  # {'Python': [7]}
print()
print(student_1)
print(lecturer_1)
print(reviewer_1)
print(student_2)
print(lecturer_2)
print(reviewer_2)
print(student_1 == student_2)
print(student_1 != student_2)
print(student_1 > student_2)
print(student_1 < student_2)
print(student_1 >= student_2)
print(student_1 <= student_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 != lecturer_2)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 >= lecturer_2)
print(lecturer_1 <= lecturer_2)

st_avg_course = input("Введите курс для подсчета среднего балла у студентов: ")
lt_avg_course = input("Введите курс для подсчета среднего балла у лекторов: ")

def students_avg_grade(st_avg_course, student_list: list):
    """A function for determining the average grade point average (GPA) for a given course among students. The course
    is passed in the {st_avg_course variable}. It returns the average grade for the course {total / counter} if students
    have the course, or the text "Такого курса нет" if the course does not exist.
    :param st_avg_course: the course for which the average grade among all students needs to be determined
           student_list: the list of students whose GPA needs to be calculated
    :return: total / counter: average course grade among selected students

    """
    total = 0
    counter = 0
    for student in student_list:
        for st in Student.all_students:
            if student == (st.name + " " + st.surname):
                for course, grade in st.grades.items():
                    if st_avg_course == course:
                        total += sum(grade) / len(grade)
                        counter += 1
    return f"Средний балл по курсу {st_avg_course} среди студентов: {total / counter:.2f}" if counter > 0 \
        else "Такого курса нет"

def lecturers_avg_grade(lt_avg_course, lecturer_list: list):
    """A function for determining the average grade point average (GPA) for a given course lecturers. The course
    is passed in the {lt_avg_course variable}. It returns the average grade for the course {total / counter} if
    lecturers have the course, or the text "Такого курса нет" if the course does not exist.
    :param lt_avg_course: the course for which the average grade among all lecturers needs to be determined
           lecturer_list: the list of lecturers whose GPA needs to be calculated
    :return: total / counter: average course grade among selected lecturers

    """
    total = 0
    counter = 0
    for lecturer in lecturer_list:
        for lt in Lecturer.all_lecturers:
            if lecturer == (lt.name + " " + lt.surname):
                for course, grade in lt.grades.items():
                    if lt_avg_course == course:
                        total += sum(grade) / len(grade)
                        counter += 1
    return f"Средний балл по курсу {lt_avg_course} среди лекторов: {total / counter:.2f}" if counter > 0 \
        else "Такого курса нет"

print(students_avg_grade(st_avg_course, ["Филипп Свистопляска", "Жанна Кукуцаполь"]))
print(lecturers_avg_grade(lt_avg_course, ["Тимур Анвартдинов", "Олеся Хабибулаева"]))