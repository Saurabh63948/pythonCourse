def calculate_bill(cups,price_per_cup):
    return cups * price_per_cup

price=calculate_bill(3,15)
print(price)

def add_vat(price,vat_rate):
    return price * (100 + vat_rate)/100

orders=[100,150,200]
totat=sum(orders)
print(totat)
for price in orders:
    final_amount=add_vat(price,10)
    print(f"Original val : {price} Final with vat is {final_amount}")