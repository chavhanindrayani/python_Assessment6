#1.	Read a CSV file and print all rows.
#	Task: Write a Python program to open and read a CSV file named data.csv and print each row.
#	Sample Data (data.csv):
#	Name, Age, Grade  
#	John, 18, A  
#   Jane, 19, B  
#	Mark, 17, A  

#	Expected Output:
#	['Name', 'Age', 'Grade']  
#	['John', '18', 'A']  
#	['Jane', '19', 'B']  
#	['Mark', '17', 'A']  
import csv
header = ["name", "age", "grade"]
new_row = [
    ["John", "18", "A"],
    ["Jane", "19", "B"],
    ["Mark", "17", "A"],
]
with open("indra.csv", "w", newline="") as file:
    write = csv.writer(file)
    write.writerow(header)
    write.writerows(new_row)
    
"""import csv

header = ["name", "age", "grade"]
new_row = [
    ["John", "18", "A"],
    ["Jane", "19", "B"],
    ["Mark", "17", "A"],
]
with open("data.csv", "a", newline="") as file:
    write = csv.writer(file)
    write.writerow(header)
    write.writerows(new_row)"""