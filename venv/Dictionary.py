stuff = {"food": 15, "energy": 100, "enemies":3}

#print(stuff.get("food"))
'''15'''

#print(stuff.items())
'''dict_items([('food', 15), ('energy', 100), ('enemies', 3)])'''

#print(stuff.keys())
'''dict_keys(['food', 'energy', 'enemies'])'''

#print(stuff.popitem())
'''('enemies', 3)'''
#print(stuff)
'''{'food': 15, 'energy': 100}'''

#print(stuff.setdefault("food"))
#print(stuff)
#print(stuff.setdefault("friends",123))
#print(stuff)
'''
15
{'food': 15, 'energy': 100, 'enemies': 3}
123
{'food': 15, 'energy': 100, 'enemies': 3, 'friends': 123}
'''

new_item = {"rocks": 4, "arrows": 18}
stuff.update(new_item)
print(stuff)
'''{'food': 15, 'energy': 100, 'enemies': 3, 'rocks': 4, 'arrows': 18}'''

new_items = {"rocks": 5, "arrows": 10}
stuff.update(new_items)
print(stuff)
'''{'food': 15, 'energy': 100, 'enemies': 3, 'rocks': 5, 'arrows': 10}'''

up_new = {"food": 3, "webs":2}
stuff.update(up_new)
print(stuff)
'''{'food': 3, 'energy': 100, 'enemies': 3, 'rocks': 5, 'arrows': 10, 'webs': 2}'''


stuff.update(food = 450, cookies = 6)
print(stuff)
'''{'food': 450, 'energy': 100, 'enemies': 3, 'rocks': 5, 'arrows': 10, 'webs': 2, 'cookies': 6}'''