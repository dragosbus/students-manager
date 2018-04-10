class Student():
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
    def print_student(self):
        print("{} {}".format(self.first_name, self.last_name))