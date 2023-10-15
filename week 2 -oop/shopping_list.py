#instance//method attributes
class shop:
    def __init__(self,owner):
        self.owner=owner
        self.cart=[]
    def add_items(self,*items):
        self.cart.append(items)
    def show_items(self):
        print(self.owner)
        print(self.cart)

customer_1=shop("niaz")
customer_1.add_items("phone","shoes","camera")
customer_1.show_items()
print("\n")
customer_2=shop("mehedi")
customer_2.add_items("biscuit","milk")
customer_2.show_items()