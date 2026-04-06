chai_order=dict(type="Masala Chai" , size="Large",sugar=2)

print(f"Chai order : {chai_order}")

chai_recipe ={}
chai_recipe["base"] ="black tea"
chai_recipe["liquid"] ="milk"

print(f"recipe base :{chai_recipe['base']}")
print(f"recipe base :{chai_recipe}")
del chai_recipe['liquid']
print(f"recipe base :{chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order={"type":"Ginger Chai" , "size":"Medium","sugar":2}

# print(F"Oder detils (keys):{chai_order.keys()}")
# print(F"Oder detils (values):{chai_order.values()}")
# print(F"Oder detils (items):{chai_order.items()}")

last_item =chai_order.popitem()
print(f"Removed last item :{last_item}")

extra_spices ={"cardamom":"crushed","ginger":"sliced"}

chai_size =chai_order["sizenk"]
print(f"Chai size is : {chai_size}")