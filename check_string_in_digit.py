#2.	Check if a string contains only digits.
#	Task: Create a regex pattern to verify if a given string is composed solely of numeric digits (0-9).
#	Input: "12345"
#	Expected Output: True
#	Input: "123a5"
#	Expected Output: False

"""import re
texts = "12345"
pattern = r'^\d+$'
matches = re.findall(pattern, texts)
print(f"True {matches}")"""

import re
def check_string_in_digits(t):
    return bool(re.fullmatch(r'\d+',t))

print(check_string_in_digits("12345"))
#ptint(check_string_in_digits("123a5"))