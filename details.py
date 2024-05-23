# Get the following input from user: name, age, house number and street name.
# Then print this information in one sentence as an output for the user to see.

# request input from user
name = input("What is your name? ")

age = input("How old are you? ")

house_num = input("What is your door number? ")

street_name = input("Which street do you live on? ")

# if all input is received by user print output sentence with user input
print(f"This is {name}, he is {age} years old and lives at house number \
      {house_num} on {street_name}")
