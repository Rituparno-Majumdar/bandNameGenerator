#This is a simple program that suggests Band Name in terms of one's city and pet name

print('Welcome to the Band Name Generator! ')
#This will ask the name of the city they grew in 

print('what is the name of the city you grew up in?  ')
#This will take the input from the keyboard
cityName = input()

#This will print their city name
print(cityName)

#This will ask their pet's name
print('What is your Pet Name? ')

#This will take the input from the keyboard
petName = input()

#This will print their pet's name
print(petName)

#This will suggest their band's name based on thrir city and pet's name
print('Your Band Name could be: ')
print(cityName + " " + petName)