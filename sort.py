import re

lines = open("file.txt", "r").read()
lines = str(lines)
lines = [int(s) for s in re.findall(r'-?\b\d+\b', lines)]
lines.sort()
lines = str(lines)
lines = re.sub("\[", "", lines)
lines = re.sub("]","", lines)
with open("write.txt", "w") as out:
        out.writelines(lines)