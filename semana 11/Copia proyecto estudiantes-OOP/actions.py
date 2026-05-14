from data import export_data_csv, import_data_csv
from student import Student

students_list = []


def save_students_csv(students_list):
    export_data_csv(students_list)
    print ("Students data saved successfully")

def load_students_csv():
    students_list= import_data_csv()

    if len(students_list) > 0 :
        print ("Students data loaded successfully")
    else:
        print ("No data loaded.")

    return students_list



def get_valid_grade(subject):
    
    while True:
        
        try:
            value = int(input(f"Please enter {subject} (0 to 100): "))
            if  0 <= value <= 100:
                return value
            else:
                print ("Invalid number, please try again")
        except ValueError:
            print ("Incorrect value, please enter a valid number: ")
            

              
def create_student():
    name = input("Enter student name: ")
    section = input("Enter student section: ") 
    spanish_grade = get_valid_grade("spanish_grade: ")
    english_grade = get_valid_grade("english_grade: ")
    social_stds_grade = get_valid_grade ("social_stds_grade: ")
    science_grade = get_valid_grade ("science_grade: ")
    
    student_to_add = Student(name, section, spanish_grade, english_grade, social_stds_grade, science_grade)

    return student_to_add
   

def show_students(students_list):
    if len(students_list)== 0:
        print("Students not found")
    else:
        for index, student in enumerate (students_list, start=1):
            print(f"\n---Student number: {index}---")
            print(f"Name: {student.name}")
            print(f"Section: {student.section}")
            print(f"Spanish grade: {student.spanish_grade}")
            print(f"English grade: {student.english_grade}")
            print(f"Social Studies grade: {student.social_stds_grade}")
            print(f"science grade: {student.science_grade}")
        
       

def calculate_student_ponderate(student):
    grade_1= student.spanish_grade
    grade_2= student.english_grade
    grade_3= student.social_stds_grade
    grade_4= student.science_grade
        
    ponderate= (grade_1 + grade_2 + grade_3 + grade_4) / 4
        
    return ponderate


def show_top3_students(students_list):
    results = []
    if len(students_list) == 0:
        print ("Students not found")
        return
    else:
        for student in students_list:
            ponderate = calculate_student_ponderate(student)
            results.append((student, ponderate))
        
    results.sort(key= lambda x: x[1], reverse= True)
    counter = 0
    for student, score in results[:3]:
        counter +=1
        print(f" Student {counter}: {student.name} Score: {score}")

        
def show_students_ponderates_average(students_list):
    if len(students_list) == 0:
        print ("Students not found")
        return
    else:
       ponderates_average = []
       for student in students_list:
          ponderate = calculate_student_ponderate (student)
          ponderates_average.append(ponderate)
    
    print (f"The combined students ponderate is {sum(ponderates_average)/len(ponderates_average)}")


