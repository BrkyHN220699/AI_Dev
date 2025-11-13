türkiyeŞehirleri = ["İstanbul", "Ankara", "İzmir", "Bursa", "Antalya" , "Adana", "Trabzon",
                     "Samsun", "Gaziantep", "Diyarbakır", "Mersin", "Konya", "Kayseri", "Eskişehir",
                     "Çanakkale", "Edirne", "Kırklareli", "Tekirdağ", "Balıkesir", "Manisa", "Aydın",]


print(len(türkiyeŞehirleri))

lengthTürkiyeŞehirleri = len(türkiyeŞehirleri)

print(türkiyeŞehirleri[22])  # Hata: Liste indexi 0'dan başlar, bu yüzden 22. indeks yoktur.

print(türkiyeŞehirleri[lengthTürkiyeŞehirleri] - 1) # Doğru: Son elemanı almak için length - 1 kullanılır.