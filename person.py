


# The python language is serious when in comes to indention and hence the format of the file should seriously be followed
# this is a function and it is going to be used to call out certain values
# This program is going to be used to prompt  a user to enter their name and country and age and  city
def main():
   
   name,country = get_person()
   print(f"Name is{name} country{country}")
   
    
def get_person():
    name= input("What is your name?")
    age =int(input("'What is your name?"))
    country =input("What is your country?")
    city = input("Which city are you from?")
    return name,country,age,city

main()
