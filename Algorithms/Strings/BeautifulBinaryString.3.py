import re

n = int(input().strip())
b = input().strip()

x = re.findall(r'010', b)
print(len(x))
