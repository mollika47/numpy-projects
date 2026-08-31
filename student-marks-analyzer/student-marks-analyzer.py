import numpy as np
subjects = np.array(["Math", "English", "Science", "Python"])
marks = np.array([
#sub[mat, eng, sci, pyt]
    [56, 60, 85, 76], #student 1
    [68, 56, 72, 59], #student 2
    [86, 64, 73, 56], #student 3
    [74, 83, 94, 69], #student 4
    [83, 78, 92, 87]  #student 5
])

def sub_wise_highest_marks():
    print("Subject-wise highest marks:")
    highest_marks = np.max(marks, axis=0)

    for sub, mark in zip(subjects, highest_marks):
        print(sub,"\b:", mark)
    print("\n")

def sub_wise_lowest_marks():
    print("Subject-wise lowest marks:")
    lowest_marks = np.min(marks, axis=0)

    for sub, mark in zip(subjects, lowest_marks):
        print(sub,"\b:", mark)
    print("\n")

def sub_wise_average_marks():
    print("Subject-wise average marks:")
    avg_marks = np.mean(marks, axis=0)

    for sub, mark in zip(subjects, avg_marks):
        print(sub,"\b:", mark)
    print("\n")

sub_wise_highest_marks()
sub_wise_lowest_marks()
sub_wise_average_marks()



