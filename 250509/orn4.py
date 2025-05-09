sayilar1=[11,12,13,14,15,16,17,18,19,20]
sayilar2=[21,22,23,24,25]
sayilar1.extend(sayilar2)
for i in sayilar1:
    if i %4 ==0:
        print(i)