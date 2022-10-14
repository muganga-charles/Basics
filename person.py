



def main():
   name,country = get_person()
   print(f"Name is{name} country{country}")
   
    
def get_person():
    name= input("What is your name?")
    country =input("What is your country?")
    return name,country

main()
