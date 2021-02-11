def user_info(name, age, city):
    '''This function prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info("Seda", 33, "Trabzon")

#Keyword Arguments#
user_info(age=25, name= 'Ayşe', city= 'Bursa' )

# *args ve **kwargs
'''
*args
Sınırsız sayıda parametreli fonksiyon oluşturmak için parametremizin önüne tek yıldız (*) koyabiliriz.
'''
def rakamlari_goster(*rakamlar):
    print(rakamlar)

rakamlari_goster(1, 2, 3, 4)
rakamlari_goster(15, 'seda')
# Sonuç
# (1, 2, 3, 4)
# (15, 'seda')

#Burada, fonksiyon parametresinden önce tek yıldız(*) kullandığımız için sonucumuz tuple(çok-ögeli, değişken grubu) olarak döner.
#Burada liste nin uzunluğunu değiştirsekte fonksiyon çalışmaya devam eder.


'''
**kwargs
Çift yıldızlı (**) parametrelerin tek yıldızlı (*) parametrelerden en önemli farkı, fonksiyonu çağırırken anahtar değer ilişkisiyle çağırabilmemizdir.
'''

def fonksiyon1(**parametre):
    print(parametre)

fonksiyon1(değer1='seda', deger2=20)
fonksiyon1(değer1='seda', deger2=20, deger3=True, deger4=15.2)

#Burada, fonksiyon parametresinden önce çift yıldız(**) kullandığımız için sonucumuz sözlük (dictionary) olarak döner.

#*args ve **kwargs beraber kullanımı
'''
İkisi beraber kullanılmak istendiğinde *args daha önce parametre olarak belirtilmelidir.
'''
def fonksiyon(*args, **kwargs):
    for i in args:
        print(i)
    for k, v in kwargs.items():
        print('anahtar: ', k, ' => Degerimiz: ', v)

fonksiyon(1, 2, 3, 'args', deger ='kwargs', deger2 ='kwargs2')

# Sonuç

# 1
# 2
# 3
# args
# anahtar: deger Degerimiz: kwargs