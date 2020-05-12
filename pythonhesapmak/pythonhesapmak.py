# BASİT HESAP MAKİNESİ

sayi1=int(input("1. sayıyı giriniz : "))
sayi2=int(input("2. sayıyı giriniz : "))
print("***")

print("Toplama -> 1 \nÇıkarma -> 2 \nÇarpma -> 3 \nBölme -> 4")

islem = input("yapılacak işlemi girin : ")

if int(islem)==1:
    print("toplama seçtiniz : ",sayi1+sayi2)
elif int(islem)==2:
    print("çıkarma seçtiniz : ",sayi1-sayi2)
elif int(islem)==3:
    print("çarpma seçtiniz : ",sayi1*sayi2)
elif int(islem)==4:
    print("bölme seçtiniz : ",sayi1/sayi2)
else:
    print("verilen değerleri girmediniz")