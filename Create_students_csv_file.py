#2.	Create a students.csv file with Name, Age, Grade data.
#	Task: Write a Python program to create a CSV file named students.csv with the following data:
#	Name, Age, Grade  
#	Alice, 20, B  
#	Bob, 22, A  
#	Charlie, 21, C  
#	Expected Output: The file students.csv should be created with the given data.
import csv
list = [["alice", "20","B"],
        ["Bob", "22", "A"],
        ["Charlie", "21","C"]
        ]
with open('indra.csv','a',newline='') as f:
    write = csv.writer(f)
    write.writerows(list)
    