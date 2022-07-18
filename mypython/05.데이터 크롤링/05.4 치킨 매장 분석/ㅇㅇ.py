str = "JAVASCRIPT:codeAddress('경기도용인시기흥구마북로98');"
apos = str.find("(")
dpos = str.find(")")
result =str[apos+1:dpos].replace("'","")
print(result)