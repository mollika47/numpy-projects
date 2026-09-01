import numpy as np

subjects = np.array(["Math", "English", "Science", "Python"])
students = np.array(["Henry", "Isabella", "Millie", "Joe", "Zendaya"])
marks = np.array([
    #sub →
    [56, 60, 85, 76], #students ↓
    [68, 56, 72, 59],
    [86, 64, 73, 56],
    [74, 83, 94, 69],
    [83, 78, 92, 87]
])

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

def total_marks():
    print("\nTotal marks:")
    total = np.sum(marks, axis=1)
    for s, t in zip(students, total):
        print(s,"\b:", t)


def student_avg():
    print("\nStudent average:")
    s_avg = np.mean(marks, axis=1)
    for s, mark in zip(students, s_avg):
        print(s,"\b:", mark)

    best_index = np.argmax(s_avg)
    worst_index = np.argmin(s_avg)
    print("\nBest Scorer: ", students[best_index], s_avg[best_index])
    print("Worst Scorer: ", students[worst_index], s_avg[worst_index])

print("---------- STUDENT MARKS ANALYZER ----------\n")

total_st = np.size(students)
print("Total Students: ",total_st)

total_sub = np.size(subjects)
print("Total Subjects: ",total_sub)

sub_wise_highest_marks()
sub_wise_lowest_marks()
sub_wise_average_marks()
total_marks()
student_avg()

print("\nAbove 80: ", marks[marks >= 80])
print("Total above 80: ", np.sum([marks >= 80]))
print("Standard Deviation (sub): ", np.std(marks, axis=0))
print("Standard Deviation (stu):", np.std(marks, axis=1))




