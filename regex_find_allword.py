#1.Extract all words starting with 'a' from a sentence
#  Task: Write a regex pattern to find all words that start with the letter 'a', regardless of case, in a given sentence.
#  Input: "Apple and avocado are amazing fruits."
#  Expected Output: ['Apple', 'and', 'avocado', 'are', 'amazing']
import re
sentence = "Apple and avocado are amazing fruits."
pattern = r'\b[aA]\w*'
matches = re.findall(pattern, sentence)
print(matches)
