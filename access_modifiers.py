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
#     in this case i request that you try the following steps
# #   class Person:
#     def __init__(self,name,age,country):
#         if(value not in ['Uganda','Kenya','Tanzania','congo']):
#             raise exception("Country is not in East Africa")   
#         self.name = name
#         self.age = age
#         self.country = country
#    def __repr__(self):
#         return f'Name is {self.name} and age is {self.age} and country is {self.country}'

# person1 = Person('John Doe',16,'Uganda')
# person1.name ='Saidi'
# person1.age = 40
# person1.country = 'Canada'
# print(person1)
# The result will print out the country canada despite it  not being among the listed countries
# That is because the command only works for the defined person who is John Doe 
# to confirm this remove uganda and replace it with any other country that was not listed
# and that will then create and error because that country is not among the listed countries


