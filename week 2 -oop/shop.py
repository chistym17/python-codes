from abc import ABC,abstractclassmethod
class product(ABC):
    product_list={}
    def __init__(self) -> None:
        pass
    def add_product(self,product,price):
        self.product=product
        self.product_list[product]=price
    @abstractclassmethod
    def view_products(self):
        pass
            


class shop(product):
    def __init__(self) -> None:
        super().__init__()
    
    def buy_product(self,product_name):
        if self.check_if_availaible(product_name) is True:
            print(f"Congress! Product is available. The price of the product is : {self.product_list[product_name]}")
            self.check_out(product_name)
        else:
            print("Sorry,product not available")


    def check_if_availaible(self,name):
        if name in self.product_list:
            return True
        else:
            return False
    
    def check_out(self,bought_item):
        print("Please enter the amount of the product : ")
        amount=int(input())
        real_price=self.product_list[bought_item]
        if amount<real_price:
            print("payment short!")
            while amount<real_price:
                print("please enter sufficient amount : ")
                amount=int(input())
        
        print("Here  is your product.")
    
    def view_products(self):
        print("Available products:")
        for product, price in self.product_list.items():
            print(f"Product: {product}, Price: {price}")

        
    
        
mr_store=shop()
mr_store.add_product("ice-cream",40)
mr_store.add_product("chocolate",25)
mr_store.add_product("pen",15)

customer1=shop()
customer1.buy_product("chocolate")


    
