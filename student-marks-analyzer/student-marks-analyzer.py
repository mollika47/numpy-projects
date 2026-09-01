import numpy as np

subjects = np.array(["Math", "English", "Science", "Python"])
students = np.array(["Henry", "Isabella", "Millie", "Joe"])
marks = np.array([
    #sub →
    [56, 60, 85, 76], #students ↓
    [68, 56, 72, 59],
    [86, 64, 73, 56],
    [74, 83, 94, 69],
    [83, 78, 92, 87]
])

print("---------- STUDENT MARKS ANALYZER ----------\n")

total_st = np.size(students)
print("Total Students: ",total_st)

total_sub = np.size(subjects)
print("Total Subjects: ",total_sub)

def sub_wise_highest_marks():
    print("\nSubject-wise highest marks:")
    highest_marks = np.max(marks, axis=0)

    for sub, mark in zip(subjects, highest_marks):
        print(sub,"\b:", mark)

def sub_wise_lowest_marks():
    print("\nSubject-wise lowest marks:")
    lowest_marks = np.min(marks, axis=0)

    for sub, mark in zip(subjects, lowest_marks):
        print(sub,"\b:", mark)

def sub_wise_average_marks():
    print("\nSubject-wise average marks:")
    avg_marks = np.mean(marks, axis=0)

    for sub, mark in zip(subjects, avg_marks):
        print(sub,"\b:", mark)

sub_wise_highest_marks()
sub_wise_lowest_marks()
sub_wise_average_marks()



