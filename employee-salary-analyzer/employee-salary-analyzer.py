import numpy as np

employees = np.array(["Henry", "Joe", "Kiara", "Sarah", "Jayson", "Lucia", "Arthur", "Thomas"])
months = np.array(["January", "February", "March", "April"])
salaries = np.array([
    [40000, 40000, 42000, 45000],
    [30000, 30500, 31000, 33000],
    [40000, 40000, 40000, 42000],
    [50000, 55000, 55000, 60000],
    [20000, 26000, 26500, 29000],
    [15000, 15500, 15500, 20000],
    [30000, 31000, 31000, 35000],
    [20000, 20000, 20000, 25000]
])

def employee_analysis():
    print("\nAverage salary of each employee:")
    avg_salary = np.mean(salaries, axis=1)
    for emp, avg in zip(employees, avg_salary):
        print(emp,"\b:", avg)

    print("\nHighest salary of each employee:")
    max_salary = np.max(salaries, axis=1)
    for emp, max_s in zip(employees, max_salary):
        print(emp, "\b:", max_s)

    print("\nLowest salary of each employee:")
    min_salary = np.min(salaries, axis=1)
    for emp, min_s in zip(employees, min_salary):
        print(emp, "\b:", min_s)

    print("\nEmployee with the highest overall average salary:")
    max_avg_s = np.max(avg_salary)
    print(employees[np.argmax(avg_salary)], "\b:", max_avg_s)

    print("\nEmployee with the lowest overall average salary:")
    min_avg_s = np.min(avg_salary)
    print(employees[np.argmin(avg_salary)], "\b:", min_avg_s)

def month_analysis():
    print("\nAverage salary for each month:")
    monthly_avg = np.mean(salaries, axis=0)
    for m, avg in zip(months, monthly_avg):
        print(m, "\b:", avg)

    print("\nHighest salary paid in each month:")
    monthly_max_s = np.max(salaries, axis=0)
    max_sal_emp = employees[np.argmax(salaries, axis=0)]
    for m, max_s, emp in zip(months, monthly_max_s, max_sal_emp):
        print(f"{m}: {max_s} ['{emp}']")

    print("\nTotal salary paid each month:")
    monthly_total = np.sum(salaries, axis=0)
    for m, t in zip(months, monthly_total):
        print(f"{m}: {t}")

def overall_analysis():
    overall_avg = np.mean(salaries)
    print("\nOverall Average:", overall_avg)
    print("Employees whose average salary is above the overall average:", employees[np.mean(salaries, axis=1) > overall_avg])

    print("Total salary paid across all 4 months:", np.sum(salaries))

    print("Standard deviation of salaries:", np.std(salaries))


print("-------- Employee Salary Analyzer --------")

employee_analysis()
month_analysis()
overall_analysis()