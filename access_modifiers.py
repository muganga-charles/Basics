class Person:
    def __init__(self,name,age,country):
        
        self.name = name
        self.age = age
        self.country = country
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self,value):
       if(value not in ['Uganda','Kenya','Tanzania','congo']):
            raise("Country is not in East Africa")      
       self.__country =value
    
    def __repr__(self):
        return f'Name is {self.name} and age is {self.age} and country is {self.country}'
    
person1 = Person('John Doe',16,'Uganda')
person1.name ='Saidi'
person1.age = 40
person1.country = 'Tanzania'
print(person1)
    