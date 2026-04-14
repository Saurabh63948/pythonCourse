favourite_chais =[
  "Masala Chai",
  "Green Tea", 
  "Masala Chai",
  "Lemon Tea",
  "Green Tea",
  "Elachi Chai"
]

unique_chai={chai for chai in favourite_chais }
print(unique_chai)

recipes ={
  "masala chai":["ginger","cardmom","clove"],
  "Elaochi chai":["cardmom","milk"],
  "spicy chai":["ginger","black paper","clove"],
}

unique_spices ={spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)