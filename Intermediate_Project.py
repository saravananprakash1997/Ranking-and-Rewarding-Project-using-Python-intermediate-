#intermediate Python Project
#get the total marks of the students
#Rank them and highlight the top three
#Reward the top three with 1000$, 500$ and 250$ respectively
import operator
def student_details():
    print()
    number_of_students=int(input("Enter the number of students :"))
    students_records={}
    for x in range(1,number_of_students+1):
        name=input('Enter the name of the Student '+str(x)+" :")
        marks=int(input("enter the marks of the students:"))
        students_records[name]=marks
    print()
    return students_records

def rank_the_students(students_records):
    print()
    sorted_students_records=sorted(student_records.items(),key=operator.itemgetter(1),reverse=True)
    print(sorted_students_records)
    print("{} has been ranked first scoring {} marks".format(sorted_students_records[0][0],sorted_students_records[0][1]))
    print("{} has been ranked first scoring {} marks".format(sorted_students_records[1][0],sorted_students_records[1][1]))
    print("{} has been ranked first scoring {} marks".format(sorted_students_records[2][0],sorted_students_records[2][1]))
    print()
    return sorted_students_records
def reward_students(sorted_student_records,rewards):
    print()
    print("Congrats {} for scoring {} marks.You have been rewarded {}$ ".format(sorted_students_records[0][0],sorted_students_records[0][1],rewards[0]))
    print("Congrats {} for scoring {} marks.You have been rewarded {}$ ".format(sorted_students_records[1][0],sorted_students_records[1][1],rewards[1]))
    print("Congrats {} for scoring {} marks.You have been rewarded {}$ ".format(sorted_students_records[2][0],sorted_students_records[2][1],rewards[2]))
    print()

    print()
rewards=(1000,500,250)
students_records=student_details()
sorted_students_records=rank_the_students(students_records)
reward_students(sorted_students_records,rewards)

