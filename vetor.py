altitudes=[792,801,798,805,810,799,803,807,812]
soma=0
for i in altitudes:
    soma=soma+i
    if i > 800:
        print(i)
print(soma/len(altitudes))