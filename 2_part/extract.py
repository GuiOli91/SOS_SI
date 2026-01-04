import re

# Read the file
with open('/home/guilherme/Projects/2025W/SOS_SI/2_part/classical_cancer.txt', 'r') as file:
    content = file.read()

# Regex pattern to match the line and capture the number
pattern = r"Accuracy Classic-NN: (\d+\.\d+)"
matches = re.findall(pattern, content)

# Print the extracted values
for match in matches:
    print(match)