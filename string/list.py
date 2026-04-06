ingredients =['water','milk','black tea']

ingredients.append("sugar")
# Output: ['water', 'milk', 'black tea', 'sugar']

ingredients.remove("water")
# Output: ['milk', 'black tea', 'sugar']

# To get the total size of the list:
print(len(ingredients)) 

# To count a specific item (e.g., how many times 'milk' is there):
print(ingredients.count("milk"))
ingredients.insert(2,"chini")
print(ingredients)

last_added =ingredients.pop()
print(last_added)
ingredients.reverse()
print(f"{ingredients}")

base_liquid =['water','milk']
extra_falvor=['ginger']
full_liquid_mix=base_liquid + extra_falvor

print(full_liquid_mix)
strong_brew =['black tea','water'] * 3

print(strong_brew)

"CINNAMON"
raw_spice_data=bytearray(b"CINNAMON")
raw_spice_data=raw_spice_data.replace(b"CINNA",b"CARD")
print(raw_spice_data)