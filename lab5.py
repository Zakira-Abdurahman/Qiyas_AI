import numpy as np
sales = np.array([
    [120, 130, 125,140,150], #coffee
    [200, 210, 190, 220, 230], #milk
    [90, 100, 95, 110, 120 ],#bread
    [150, 160, 155, 170, 180]#sugar
])

#part 1
print("full sales data:\n" , sales)
print("sales of product B:" , sales[1])
print("sales for day 3:" , sales[:, 2])
print("last 2 days sales:\n" , sales[:, 3:])

#part 2
print("total sales per product:\n" , np.sum(sales, axis=1))
print("total sales per day:\n" , np.sum(sales, axis=0))
print("which day had the highest sales:\n" , np.argmax(np.sum(sales, axis=0)))
print("average daily sales per product:\n" , np.mean(sales, axis=1))
