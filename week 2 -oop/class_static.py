class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_adult(cls, name,age):
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        return age >= 18

person1 = Person("Alex", 25)
print(person1.name)  
print(person1.age)   

print(Person.is_adult(31))  

