eren = {
 "name": "Eren",
 "homework": [90.0,97.0,75.0,92.0],
 "quizzes": [88.0,40.0,94.0],
 "tests": [75.0,90.0]
}

mikasa = {
"name": "Mikasa",
"homework": [100.0, 92.0, 98.0, 100.0],
"quizzes": [82.0, 83.0, 91.0],
"tests": [89.0, 97.0]
}

armin = {
"name": "Armin",
"homework": [0.0, 87.0, 75.0, 22.0],
"quizzes": [0.0, 75.0, 78.0],
"tests": [100.0, 100.0]
}

students = [eren ,mikasa, armin]

for student in students:
    print("Students Name:",student["name"])
    print("HomeWork:",student["homework"])
    print("Quizzes:",student["quizzes"])
    print("Tests:",student["tests"])

def average(numbers:list):
    total = sum(numbers)
    #print(total)
    total = float(total)
    #print(total)
    result = total / len(numbers)
    return result

def get_average(average:student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    score = (homework*10/100) + (quizzes*30/100) + (tests*60/100)
    return score
    
def get_letter_grade(get_average:average):
    if get_average >= 90:
        return "A"
    elif get_average >= 80:
        return "B"
    elif get_average >= 70:
        return "C"
    elif get_average >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results = []
    
    for student in students:
        results.append(average(get_average(students)))
    return results

print('Class average:'+str(get_class_average([students])))
print('Class average:'+str(get_letter_grade(get_class_average([students]))))