import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
first_sales_items = sorted_list[:math.floor(num_of_sales/2)]
last_sales_items = sorted_list[-(math.floor(num_of_sales/2)):]
median = sorted_list[math.floor(num_of_sales/2):(math.floor(num_of_sales/2)+1)]

print(sorted_list)
print(num_of_sales) 
print(first_sales_items)
print(last_sales_items)
print(median)