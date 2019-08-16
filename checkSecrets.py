import binwalk

friendFile = open('a_friend.docx', 'r')

if 'flag' in friendFile.read():
    print("True")

lines = []

for line in friendFile:
    line.rstrip('\n\r')
    lines.append(line)

#print lines
