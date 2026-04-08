# for token in range(1,11):
#   print(f"Serving chai to token #{token}")

# for batch in range(1,5):
#   print(f"prepairing chai for batch ${batch}")

# orders=["saurabh","anama","carlos"]

# for item in orders:
#   print(f"hey mr {item} your order is ready")

# menu_list =["chai","coffee","cold-coffee","hot-milk"]

# for index,menu in enumerate(menu_list,start=1):
#   print(f"the index of item is {index} , and the item is {menu}")

customer_name=["saurabh","anama","carlos"]
customer_bill=[12,45,60]

# for i in range(3):
#   print(f"{customer_name[i]} and bill is {customer_bill[i]}")

for idx,(name,bill) in enumerate(zip(customer_name,customer_bill),start=1):
  print(f"{idx} :-{name} : {bill}")