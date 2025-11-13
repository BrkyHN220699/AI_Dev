# Nested List data structure'ını gösteren bir Python dosyası


ekşiMeyveler = ["Limon", "Portakal", "Greyfurt"]
tatlıMeyveler = ["Elma", "Armut", "Muz", "Karpuz"]
tropikalMeyveler = ["Mango", "Ananas", "Papaya"]
                    
meyveListesi = [ekşiMeyveler, tatlıMeyveler, tropikalMeyveler]
print(meyveListesi)

print(meyveListesi[0])  # Ekşi meyveler listesi
print(meyveListesi[7])  # Ekşi meyveler listesi
print(meyveListesi[1][2])  # Tatlı meyvelerden Muz - Yani ilk indis listeler için, 
                           # ikinci indis ise o listedeki elemanlar için kullanılır.