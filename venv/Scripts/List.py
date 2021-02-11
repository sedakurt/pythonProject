#listmethods

fruits = ["peaches", "pears", "apples"]
years = [3,"1998",2.5,987,"1994"]

print("apple" in fruits) #it is false
print("apples" in fruits) #it is false

print(fruits.count("apples")) #It turns how many "apples" item
print(fruits.index("apples")) #"apples" itemı kaçıncı indexte bilgisini verir




"""
print(fruits,years)

fruits.append("oranges") #append; add a new item to fruits list
print(fruits)

fruits.extend(years) # combine years list and fruits list, adding years to fruits
print(fruits)

'''
fruits.remove("orange") #orange adında bir item olmadığında hata verir bizim burada exact match olan item bilgisini girmemiz gerekir.
print(fruits)
'''

fruits.remove("oranges")
print("\n",fruits)

fruits.pop(0)  #If we want to remove the first item from a list, then we will use the pop method and indicate which items.
print("\n",fruits)

fruits.pop(-1)#If we want to remove the last item from a list, then we will use the pop method include -1
print(fruits)

#sort
numbers = [20, 3, 4.5, 12, 45.67]
numbers.sort()
print(numbers)
'''[3, 4.5, 12, 20, 45.67]'''
"""