#5.	Append a new row to an existing data.csv file.
#	Task: Write a Python program to append the following data to an existing data.csv file:
#	Name, Age, Grade  
#	Dave, 23, B  
#	Expected Output: The file data.csv should have the new data appended as the last row.
import csv

filename = "data.csv"
new_row = ["indrayani", "23","A+"]
with open(filename, 'a') as file:
    writer_csv = csv.writer(file)
    writer_csv.writerows(new_row)
    
print(f"new row appended to {filename}")
    