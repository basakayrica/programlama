notlar= []
for i in range(6):
    notlar.append(int(input("dersn notlarınızı giriniz")))
for not1 in notlar:
    if not1 <=50:
        print("kaldığınız dersler:",notlar)