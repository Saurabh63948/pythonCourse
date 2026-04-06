essential_spices = {"cardamon","ginger","cinnamon"}
optional_spices = {"cloves","ginger","black pepper","cinnamon"}

all_spices =essential_spices | optional_spices

print(f"All Spices ; {all_spices}")
only_in_essential = essential_spices -optional_spices
print(f"All Spices ; {only_in_essential}")

print(f"Is 'cloves' in essential spices ? {'cloves' in optional_spices}")