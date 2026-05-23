class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}      # {course: [grades]}

    def average_grade(self):

        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        avg = self.average_grade()
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg}"


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}      # оценки за ДЗ от reviewer

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_hw_grade(self):

        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if not all_grades:
            return 0.0
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        avg_hw = self.average_hw_grade()
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses) if self.finished_courses else "нет"
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_hw}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")


    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_hw_grade() < other.average_hw_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_hw_grade() <= other.average_hw_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_hw_grade() > other.average_hw_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_hw_grade() >= other.average_hw_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_hw_grade() == other.average_hw_grade()



def average_hw_grade_for_course(students, course_name):

    all_grades = []
    for student in students:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if not all_grades:
        return 0.0
    return round(sum(all_grades) / len(all_grades), 1)


def average_lecture_grade_for_course(lecturers, course_name):

    all_grades = []
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    if not all_grades:
        return 0.0
    return round(sum(all_grades) / len(all_grades), 1)


if __name__ == "__main__":
    # Создаём 2 ревьюеров
    reviewer1 = Reviewer("Анна", "Морозова")
    reviewer2 = Reviewer("Игорь", "Сидоров")
    reviewer1.courses_attached.extend(["Python", "Git"])
    reviewer2.courses_attached.append("Java")

    lecturer1 = Lecturer("Дмитрий", "Петров")
    lecturer2 = Lecturer("Елена", "Смирнова")
    lecturer1.courses_attached.extend(["Python", "Git"])
    lecturer2.courses_attached.extend(["Python", "Java"])


    student1 = Student("Ольга", "Алёхина", "Ж")
    student2 = Student("Иван", "Кузнецов", "М")
    student1.courses_in_progress.extend(["Python", "Git"])
    student1.finished_courses.append("Введение в программирование")
    student2.courses_in_progress.extend(["Python", "Java"])
    student2.finished_courses.append("Основы алгоритмов")

    reviewer1.rate_hw(student1, "Python", 9)
    reviewer1.rate_hw(student1, "Python", 8)
    reviewer1.rate_hw(student1, "Git", 10)
    reviewer2.rate_hw(student2, "Python", 7)
    reviewer2.rate_hw(student2, "Java", 9)

    student1.rate_lecture(lecturer1, "Python", 8)
    student1.rate_lecture(lecturer1, "Python", 9)
    student1.rate_lecture(lecturer1, "Git", 10)
    student2.rate_lecture(lecturer1, "Python", 9)
    student2.rate_lecture(lecturer2, "Python", 9)
    student2.rate_lecture(lecturer2, "Java", 8)

    print("=== Ревьюеры ===")
    print(reviewer1, "\n")
    print(reviewer2, "\n")
    print("=== Лекторы ===")
    print(lecturer1, "\n")
    print(lecturer2, "\n")
    print("=== Студенты ===")
    print(student1, "\n")
    print(student2, "\n")

    print("=== Сравнение лекторов ===")
    print(f"{lecturer1.name} {lecturer1.surname} лучше {lecturer2.name} {lecturer2.surname}? {lecturer1 > lecturer2}")
    print(f"Средняя оценка {lecturer1.name}: {lecturer1.average_grade()}")
    print(f"Средняя оценка {lecturer2.name}: {lecturer2.average_grade()}")

    print("\n=== Сравнение студентов ===")
    print(f"{student1.name} {student1.surname} лучше {student2.name} {student2.surname}? {student1 > student2}")
    print(f"Средняя оценка {student1.name}: {student1.average_hw_grade()}")
    print(f"Средняя оценка {student2.name}: {student2.average_hw_grade()}")

    print("\n=== Средние оценки по курсам ===")
    students_list = [student1, student2]
    lecturers_list = [lecturer1, lecturer2]

    print(f"Средняя оценка за ДЗ по курсу Python: {average_hw_grade_for_course(students_list, 'Python')}")
    print(f"Средняя оценка за ДЗ по курсу Git: {average_hw_grade_for_course(students_list, 'Git')}")
    print(f"Средняя оценка за лекции по курсу Python: {average_lecture_grade_for_course(lecturers_list, 'Python')}")
    print(f"Средняя оценка за лекции по курсу Git: {average_lecture_grade_for_course(lecturers_list, 'Git')}")
    print(f"Средняя оценка за лекции по курсу Java: {average_lecture_grade_for_course(lecturers_list, 'Java')}")
