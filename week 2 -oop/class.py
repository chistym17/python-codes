#method (self),class attributes,fixed attributes,only one unique object possible
class phone:
    price=2000
    color="blue"
    brand="1200"

    def call_phone(self,number):
        print("my number"+ number)


    
my_phone=phone()
print(my_phone.brand,my_phone.price)
my_phone.call_phone("1234")