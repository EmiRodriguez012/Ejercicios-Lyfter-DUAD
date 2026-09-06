import csv 
from student import Student

def export_data_csv(students_list):

    students_data = []

    for student in students_list:
        students_data.append(student.convert_to_dict())

    with open("students.csv", "w", newline= "") as file:
            
        columns = [
            "name",
            "section",
            "spanish_grade",
            "english_grade",
            "social_stds_grade",
            "science_grade"
        ]
        
        writer = csv.DictWriter(file, fieldnames=columns)

        writer.writeheader()
        writer.writerows(students_data)


              
def import_data_csv():
    try:
        with open("students.csv", "r") as file:
            reader= csv.DictReader(file)
            students_data= list(reader)

            students_list = []
            
            for student_data in students_data:
                student = Student.convert_from_dict(student_data)
                students_list.append(student)

        return students_list
    
    except FileNotFoundError:
        print("students.csv was not found.")
        return []
    