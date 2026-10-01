import os
import gzip
import pickle
import tarfile

if os.path.exists('students.dat'):
    with tarfile.open('students.dat', 'r:gz') as archive:
        archive.extractall()

    students = []
    courses = []

    print('Previous student data loaded.')

else:
    students = []

    numberstudent = int(input('Enter the number of students:'))

    for i in range(1, numberstudent + 1):
        print('Enter the information of student', str(i))

        name = input('Enter the name: ')
        id = input('Enter the id: ')
        dob = input('Enter the DoB: ')

        student = {
            'name': name,
            'id': id,
            'dob': dob,
            'scores': {}
        }

        students.append(student)
        with open("students.txt", "w", encoding="utf-8") as f:
            for student in students:
                f.write(f"{student['id']}|{student['name']}|{student['dob']}\n")

    numbercourse = int(input('Enter the number of course:'))

    courses = []

    for y in range(1, numbercourse + 1):
        print('Enter the information of course', str(y))

        namec = input('Enter the name course: ')
        idc = input('Enter the ID course: ')

        course = {
            'name': namec,
            'id': idc
        }

        courses.append(course)
        with open("Courses.txt",'w') as f:
            for course in courses:
                f.write(f"{course['name']}|{course['id']}\n");
    
    # Enter scores
    for student in students:
        print('\nEnter scores for', student['name'])

        for course in courses:
            score = float(input(
                'Enter the score of ' + course['name'] + ': '
            ))

            student['scores'][course['id']] = score
            with open("marks.txt",'w') as f:
                for student in students:
                    for course in courses:
                        f.write(f"{course['name']}-{student['name']} : {score}\n");



print('\n===== LIST OF COURSES =====')

for course in courses:
    print(course['id'], '-', course['name'])


print('\n===== LIST OF STUDENTS =====')

for student in students:
    print(
        student['id'],
        '-',
        student['name'],
        '-',
        student['dob']
    )

    course_id = input('\nEnter course ID: ').strip()

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

            if course_id in student['scores']:
                score = student['scores'][course_id]

                print(
                    student['id'],
                    '-',
                    student['name'],
                    ':',
                    score
                )
            else:
                print(
                    student['id'],
                    '-',    
                    student['name'],
                    ': No score'
                )

with tarfile.open("students.dat", "w:gz") as archive:
    archive.add("students.txt")
    archive.add("Courses.txt")
    archive.add("marks.txt")

print("\nAll files have been compressed into students.dat")





