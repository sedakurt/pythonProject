#comparison Operastors
'''
print(1 < 1)
print(1 <= 1)
print(1 > 1)
print(1 >= 1)
print(1 == 1)
print(1 != 1)
'''

##if, elif, else code block

#if
name = input("What is your name? ")
if name == "Seda":
    print("Hello, nice to see you {}".format(name))
elif name == "Bayraktar":
    print("Hello, you are a surname!")
elif name == "Kurt":
    print("Hi, {}, you are a second surname for Seda".format(name))
elif name != "Özcan":  #en baştan conditionları çalıştırır yani bir order içerisinde akış devam edeceğinden ilk if e göre çalışır. Bu sorgu eğer koşullar arasında olmayan bir name değeri input olarak verirsem çalışacaktır.
    '''    
    What is your name? sdsdasda
You are not Özcan!
'''
    print("You are not Özcan!")
print("\nHave a nice day!")

