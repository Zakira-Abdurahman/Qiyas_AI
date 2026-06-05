import numpy as np
sales = np.array([
    [120, 130, 125,140,150], #coffee
    [200, 210, 190, 220, 230], #milk
    [90, 100, 95, 110, 120 ],#bread
    [150, 160, 155, 170, 180]#sugar
])
# Each row = product
#  Each column = day


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
print("highest single day sale for each product:\n", np.max(sales, axis=1))
print("lowest single day sale for each product:\n", np.min(sales, axis=1))


#part3

print("total sales per day:\n", np.sum(sales, axis=0))
print("which day had the highest sales:\n", np.argmax(np.sum(sales, axis=0)))
print("average sales per day:\n", np.mean(sales, axis=0))

#part4
print("best selling product:\n", np.argmax(np.sum(sales, axis=1)))
print("worest selling product:\n", np.argmin(np.sum(sales, axis=1)))
print("best performing day:\n", np.argmax(np.sum(sales, axis=0)))
print("worst performing day:\n", np.argmin(np.sum(sales, axis=0)))

#part5
print("products with any day sales greater than 200:\n", np.any(sales > 200, axis=1))
products = np.array(["Coffee", "Milk", "Bread", "Sugar"])
print("products with any day sales greater than 200:\n", products[np.any(sales > 200, axis=1)])
print("products that never crossed 100 units in any day:\n", np.all(sales < 100, axis=1))
print("products that never crossed 100 units in any day:\n", products[np.all(sales < 100, axis=1)])
print("days where total store sales exceeded 500:\n", np.sum(sales, axis=0) > 500)
print("days where total store sales exceeded 500:\n", np.where(np.sum(sales, axis=0) > 500)[0])
print("days where total store sales exceeded 500:\n", np.array(["Day1", "Day2", "Day3", "Day4", "Day5"])[np.where(np.sum(sales, axis=0) > 500)[0]])


