from data import export_data_csv, import_data_csv




def save_students_csv(students):
    export_data_csv(students)
    print ("Students data saved successfully")

def load_students_csv():
    students= import_data_csv()

    if len(students) > 0 :
        print ("Students data loaded successfully")
    else:
        print ("No data loaded.")

    return students



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
    keys= ["full_name", "section", "spanish_grade", "english_grade","social_stds_grade", "science_grade"]
    student = {}
    for key in keys:
        if "grade" in key:
            value = get_valid_grade(key)
            
        else:
            value = input(f"Enter {key}: ")
        
        student[key]=value

    return student 

def show_students(students):
    if len(students)== 0:
        print("Students not found")
    else:
        for index, student in enumerate (students, start=1):
            print(f"\n---Student number: {index}---")
            
            for key, value in student.items():
                print(f"{key}: {value}")


def calculate_student_ponderate(student):
    grade_1= student.get("spanish_grade")
    grade_2= student.get("english_grade")
    grade_3= student.get("social_stds_grade")
    grade_4= student.get("science_grade")
    
    ponderate= (grade_1 + grade_2 + grade_3 + grade_4) / 4

    return ponderate

def show_top3_students(students):
    results = []
    if len(students) == 0:
        print ("Students not found")
        return
    else:
        for student in students:
            ponderate = calculate_student_ponderate(student)
            results.append((student, ponderate))
        
    results.sort(key= lambda x: x[1], reverse= True)
    counter = 0
    for student, score in results[:3]:
        counter +=1
        print(f" Student {counter}: {student ['full_name']} Score: {score}")

        
def show_students_ponderates_average(students):
    if len(students) == 0:
        print ("Students not found")
        return
    else:
       ponderates_average = []
       for student in students:
          ponderate = calculate_student_ponderate (student)
          ponderates_average.append(ponderate)
    
    print (f"The combined students ponderate is {sum(ponderates_average)/len(ponderates_average)}")


