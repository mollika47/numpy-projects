import numpy as np

products = np.array(["Laptop", "Phone", "Tablet", "Headphone"])
months = np.array(["January", "February", "March", "April"])
sales = np.array([
    [12, 15, 10, 18],  # January
    [14, 18, 13, 20],  # February
    [10, 16, 15, 17],  # March
    [18, 20, 17, 22]   # April
])

def products_info():
    total_products = np.size(products)
    print("Total Products:", total_products)

    total_months = np.size(sales, axis=0)
    print("Total Months:", total_months)

    print("Array Shape:", np.shape(sales))

def product_analysis():
    print("\nTotal Sales of Each Product:")
    total = np.sum(sales, axis=0)
    for p, t in zip(products, total):
        print(p,"\b:", t)

    print("\nAverage Sales of Each Product:")
    avg = np.mean(sales, axis=0)
    for p, a in zip(products, avg):
        print(p,"\b:", a)

    print("\nHighest Sales of Each Product:")
    highest = np.max(sales, axis=0)
    for p, h in zip(products, highest):
        print(p,"\b:", h)

    print("\nLowest Sales of Each Product:")
    lowest = np.min(sales, axis=0)
    for p, l in zip(products, lowest):
        print(p,"\b:", l)

def month_analysis():
    print("\nTotal Sales of Each Month:")
    total = np.sum(sales, axis=1)
    for m, t in zip(months, total):
        print(m,"\b:", t)

    print("\nAverage Sales of Each Month:")
    avg = np.mean(sales, axis=1)
    for m, a in zip(months, avg):
        print(m, "\b:", a)

    print("\nBest Sales Month:")
    top = np.max(total)
    top_index = np.argmax(total)
    print(months[top_index],"\b:", top)

    print("Worst Sales Month:")
    down = np.min(total)
    down_index = np.argmin(total)
    print(months[down_index], "\b:", down)

print("-------- Sales Data Analyzer --------\n")

products_info()
product_analysis()
month_analysis()