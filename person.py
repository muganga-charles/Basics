


# The python language is serious when in comes to indention and hence the format of the file should seriously be followed
# this is a function and it is going to be used to call out certain values
# This program is going to be used to prompt  a user to enter their name and country and age and  city
# This is the main function used to call values from the inner function
def main():
   
   
   name,country = get_person()
   print(f"Name is{name} country{country}")
   
#   This is an inner function  used by the ser to input values   
def get_person():
#    prompts user to enter name 
    name= input("What is your name?")
   
#    prompts user to enter age
    age =int(input("'What is your age?"))
   
#    prompts user to enter country
    country =input("What is your country?")
#    prompts user to enter city
    city = input("Which city are you from?")
    return name,country,age,city
# and the return helps display the mentioned values on the console
main()
