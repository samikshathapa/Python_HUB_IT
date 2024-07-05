# grades_dict = {
#     "Alice": {"Math": 90, "Science": 85, "Literature": 88},
#     "Bob": {"Math": 78, "Science": 82, "Literature": 80},
#     "Charlie": {"Math": 92, "Science": 91, "Literature": 94}
# }

# def calculate_percentage(**grades):
#     total = sum(grades.values())
#     number_of_subjects = len(grades)
#     percentage = total / number_of_subjects
#     return percentage

# for student, grades in grades_dict.items():
#     percentage = calculate_percentage(**grades)
#     print(f"{student}: {percentage:.2f}%")

grades_dict = {
    "Alice": {"Math": 90, "Science": 85, "Literature": 88},
    "Bob": {"Math": 78, "Science": 82, "Literature": 80},
    "Charlie": {"Math": 92, "Science": 91, "Literature": 94}
}

for student, grades in grades_dict.items():
    total = sum(grades.values())
    number_of_subjects = len(grades)
    percentage = total / number_of_subjects
    print(f"{student}: {percentage:.2f}%")
