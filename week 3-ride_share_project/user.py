from abc import ABC,abstractmethod
from datetime import datetime
class user(ABC):
    def __init__(self,name,email,nid,wallet) -> None:
        self.name=name
        self.email=email
        self.nid=nid
        self.wallet=wallet
        self.__id=0 #to do
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class rider(user):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.start_location=current_location
        self.wallet=0
    
    def display_profile(self):
        print(f"Rider name : {self.name}, Rider email : {self.email}")
    
    current_ride=None
    
    def request_ride(self,location,destination):
        if not self.current_ride:
            #todo:
            ride_request=ride_request(self,destination)
            ride_matcher=ride_matching()
            self.current_ride=ride_matcher.find_driver(ride_request)

    def load_cash(self,amount):
        if amount>0:
            self.wallet+=amount
    def update_location(self,current_location):
        self.start_location=current_location


class driver(user):
    def __init__(self, name, email, nid,location) -> None:
        self.location=location
        super().__init__(name, email, nid)
        self.wallet=0

    def display_profile(self):
        print(f"Driver : {self.name}")

    def accept_ride(self,ride):
        ride.set_driver(self)


class ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location=start_location
        self.end_location=end_location
        self.driver=None
        self.rider=None
        self.start_time=None
        self.endtime=None
        self.estimated_fare=None

    def set_driver(self,driver):
        self.driver=driver

    def start_ride(self):
        self.start_time=datetime.now()

    def end_ride(self,fare):
        self.endtime=datetime.now()
        self.pay_fare(fare)


    def pay_fare(self,fare):
        self.rider.wallet-=fare
        self.driver.wallet+=fare


class ride_request:
    def __init__(self,rider,end_location) -> None:
        self.end_location=end_location
    

class ride_matching:
    def __init__(self) -> None:
        self.available_drivers=[]
    
    def find_driver(self,ride_request):
        if len(self.available_drivers>0):
            #find the closest driver.
            selected_driver=self.available_drivers[0]
            set_ride=ride(ride_request.rider.start_location,ride_request.end_location)
            selected_driver.accept_ride(set_ride)


    

        
    

