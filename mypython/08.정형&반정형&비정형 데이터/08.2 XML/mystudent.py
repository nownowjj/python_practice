from xml.etree.ElementTree import parse

tree = parse('mystudent.xml')
myroot = tree.getroot()
print(myroot)

one_student = myroot.findall('student')
# print(one_student)

for profile in one_student:
    print(profile[0].text)
    print(profile[1].text)
    print(profile[2].text)
    print(profile[3].text)
    print('-'*30)