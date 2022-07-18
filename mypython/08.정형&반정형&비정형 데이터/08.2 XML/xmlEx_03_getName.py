from xml.etree.ElementTree import parse

tree = parse('xmlEx_03.xml')
myroot = tree.getroot()
print(type(myroot))
print('-'*30)

families = myroot.findall('가족')
print(type(families))
print('-'*30)

print(families)
print('-'*30)

for onefamily in families:  # 가족 태그가 2개 존재함 onefamily는 가족 하나
    for onesaram in onefamily:  # 가족에서 한 사람
        if len(onesaram) >= 1:
            print(onesaram[0].text)
        else:
            print(onesaram.attrib['이름'])
    print('-'*30)