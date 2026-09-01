import numpy as np

products = np.array(["Laptop", "Phone", "Tablet", "Headphone"])
sales = np.array([
    [12, 15, 10, 18],  # January
    [14, 18, 13, 20],  # February
    [10, 16, 15, 17],  # March
    [18, 20, 17, 22]   # April
])

def products_info():
    total_products = np.size(products)
    print("Total Products: ", total_products)

    total_months = np.size(sales, axis=0)
    print("Total Months: ", total_months)

    print("Array Shape: ", np.shape(sales))


products_info()