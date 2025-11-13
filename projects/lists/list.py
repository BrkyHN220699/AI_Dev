import random

# List yani liste data structure'ını gösteren bir Python dosyası

türkiyeŞehirleri = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya"]

print(türkiyeŞehirleri)

print()

# Bu şekilde istediğim indisteki elemanı değiştirebilmekteyim

türkiyeŞehirleri[3] = "Antep"

print(türkiyeŞehirleri)
print()


# Eğer bu listeye yeni bir elemman ekleyecek olsaydım:
# Bunu append() methodu ile yapabilirim

türkiyeŞehirleri.append("Kütahya")

print(türkiyeŞehirleri)

print()
# Bu listenin istediğim elemanına indis numarasına göre de direkt olarak erişebilirim

print(türkiyeŞehirleri[2])  
print(türkiyeŞehirleri[-1])  # Son elemanı verir    


print()
print()
print()



# Şimdi bir restoranda hesabı kimin ödeyeceğini rastgele seçen bir program yazalım

yemekSiparişiVerenler = ["Berkay", "Murat", "Musa", "Hanımşah", "Kaju"]

hesapİçinİndis = random.randint(0,4)  # 0 ile 4 arasında rastgele bir sayı seçer

print("Bu akşam hesabı ödeyecek kişi:", yemekSiparişiVerenler[hesapİçinİndis])

print()

# Ya da random.choice() methodunu kullanarak da aynı sonucu elde edebilirim. Bir random integer üreterek indis 
# seçmek yerine direkt olarak listeden rastgele bir eleman seçerek işlemi gerçekleştiriyorum.

hesapSahibi = random.choice(yemekSiparişiVerenler)
print("Bu akşam hesabı ödeyecek kişi (choice ile):", hesapSahibi)