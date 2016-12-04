import re

ins = str(input())

while ins != "":
    ins0 = re.sub(r'(.)\1', '', ins)
    if ins == ins0:
        break
    ins = ins0
else:
    ins = "Empty String"
print(ins)