import re
txt = "use of python in machine learning"
x=re.search("^python.*rohith$",txt)
if (x):
    print("YES! We have a match!")
else:
    print("no match")