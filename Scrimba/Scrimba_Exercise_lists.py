sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

sales_w2.append(int(input("Enter sale for day 7: ")))
#print(sales_w2) #to check if above command worked as expected

sales = sales_w1.copy()
sales.extend(sales_w2)
#print(sales) #to check if the lists were combined in the appropriate order

print(f'On my best sale, per week, I made {max(sales_w1)*1.5} $ on week 1 and {max(sales_w2)*1.5} $ on week 2')
print(f'On my worst sale, per week, I only made {min(sales_w1)*1.5} $ on week 1 and {min(sales_w2)*1.5} $ on week 2')
print(f'This means that in my short life as a lemonade salesman my profits ranged between {min(sales)*1.5} $ and {max(sales)*1.5} $. Not bad hein! ;)')