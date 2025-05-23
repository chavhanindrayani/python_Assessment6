#3.	Read and print the Name column from a CSV file.
#	Task: Read a CSV file named students.csv and print only the values from the Name column.
#	Expected Output:
#	Alice  
#	Bob  
#	Charlie  
import csv
filename = "indra.csv"
with open(filename, 'r') as file:
    read_csv = csv.DictReader(file)
    for line in read_csv:
        print(line["name"])
        
