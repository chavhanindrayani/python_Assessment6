#4.	Extract all numbers from a string.
#	Task: Extract all numeric values (both single and multi-digit) from a string using regex.
#	Input: "I have 2 apples and 3 oranges."
#	Expected Output: ['2', '3']

import re           
input = "I have 2 apples and 3 oranges."
pattern = r'\d+'
matches = re.findall(pattern, input)
print(matches)