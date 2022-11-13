print("Store Management System")

item1 = "Phone"
item1_type = "IPhone"
item1_price = 300000
item1_quantity = 100

print(item1)
print(item1_price)
print(item1_quantity)

class Item:
    # Adding Behaviour to the objects
    def __init__(self):
        print("Hey you have created")
   
#    def calculate_discount(self,x,y):
#        return x*y
# this command  is later called to calculate the discounts of the chosen values
   
       
phone = Item()
phone.name = "Itel6"
phone.version ="Android 12"
phone.price = 2000
earphones =Item()
earphones.price = 5000


# print(earphones.calculate_discount(0.2,earphones.price))
# print(phone.calculate_discount(0.8,phone.price))
# 

print(phone.name)
print(phone.price)
print(phone.version)
