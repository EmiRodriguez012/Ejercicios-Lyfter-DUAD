import csv 


def export_data_csv(students):
    with open ("students.csv", "w", newline= "") as file:
        columns = ["full_name", "section", "spanish_grade", "english_grade","social_stds_grade", "science_grade"]
        writer = csv.DictWriter(file, fieldnames= columns)

        writer.writeheader()
        writer.writerows(students)
               
def import_data_csv():
    try:
        with open("students.csv", "r") as file:
            reader= csv.DictReader(file)
            students= list(reader)
            
            for student in students:
                student ["spanish_grade"]= int(student["spanish_grade"])
                student ["english_grade"]= int(student["english_grade"])
                student ["social_stds_grade"]= int(student["social_stds_grade"])
                student ["science_grade"]= int(student["science_grade"])

        return students
    except FileNotFoundError:
        print("students.csv was not found.")
        return []
