#4.	Create a CSV file with Product, Price columns and print all prices.
#	Task: Create a CSV file named products.csv with the following data and print the Price column values:
#	Product, Price  
#	Laptop, 1000  
#	Phone, 500  
#	Headphones, 50  
#	Expected Output:
#	1000  
#	500  
#	50  
import csv
headers = ['product','price']
product_list = [['Lapotop', '1000'],
                ['phone', '500'],
                ['Headphones', '50']
]
with open('product.csv', 'w') as file:
    write_csv = csv.writer(file)
    write_csv.writerow(headers)
    write_csv.writerows(product_list)


