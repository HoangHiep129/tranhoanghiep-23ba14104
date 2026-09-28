numberstudent = int(input('Enter the number of class:'))
students = []
for i in range(1,numberstudent + 1):
    print('Enter the information of studennt', str(i))
    name=input('Enter the name')
    id=input('Enter the id')
    dob=input('Enter the DoB')
    student = {
        'name': name,
        'id': id,
        'dob': dob,
        'scores': {}
    }

    students.append(student)
numbercourse = int(input('Enter the number of course:'))
courses = []
for y in range(1, numbercourse + 1):
    print('Enter the information of course',str(y))
    namec= input('Enter the name course:')
    idc= input('Enter the ID course:')
    course = {
         'name':namec,
         'id':idc
    }
    courses.append(course)

for student in students:
    print('\nEnter scores for', student['name'])

    for course in courses:
        score = float(input(
            'Enter the score of ' + course['name'] + ': '
        ))
        student['scores'][course['id']] = score
print('\n===== LIST OF COURSES =====')
for course in courses:
    print(course['id'], '-', course['name'])

print('\n===== LIST OF STUDENTS =====')
for student in students:
    print(student['id'], '-', student['name'], '-', student['dob'])

course_id = input('\nEnter course ID: ')
course_found = None
for course in courses:
    if course['id'] == course_id:
        course_found = course
        break
if course_found is None:
    print('Course not found!')
else:
    print('\n===== STUDENT MARKS =====')
    print('Course:', course_found['name'])
    for student in students:
        score = student['scores'][course_id]
        print( student['id'], '-', student['name'], ':', score )
