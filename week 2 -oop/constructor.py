class phone:
    def __init__(self,owner,brand,price):#constructor/ a template to create diffferent objects
        self.owner=owner
        self.price=price
        self.brand=brand
    def print_info(self):
        print(self.owner,self.brand,self.price)

        
    

my_phone=phone("mahi",1000,"nokia")
my_phone.print_info()



        
            
        