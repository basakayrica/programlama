ifade = input("Bir ifade giriniz: ")
aranan_harf = "A"
sayac = 0
for harf in ifade:
    if harf == aranan_harf:
        sayac += 1
print("Girilen ifadede ",aranan_harf," harfi ",sayac," kez geçmektedir.")