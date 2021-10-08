# Display message to the standard output
print("System Failure Imminent!")
print("System reboot has been initiated...")
print()
print("...rebooting sensory system")
print("...rebooting output motors")
print("...rebooting hover engine")
print()
print("system online")

# Display escape characters
print("\n Displays a new line")
print("\t Displays a tab space")
print("\\ Displays a back slash")
print("\" Displays a double quote")
print("\' Displays a single quote")
print()
print(" I am Beep!")

# Display a box
print("##########")
print("#        #")
print("#        #")
print("##########")


print("What is your name human?")
name = input()
print(f"It is nice to meet you human {name}")
eye=input("please enter  character for the eye")
print("Beep's expression is now:")
print("##########")
print("# ",eye, eye ,"  #")
print("#  ----  #")
print("##########")
# Ask user to enter their name
age = int(input("age?"))
height = float(input("height? (meters)"))
weight = (float(input("weight? (kg)")))
bmi=weight/(height*height)
print(name," you are ", age," years old and your bmi is ", bmi)

health = int(input("number of lives?"))
energy = int(input("energy level?"))
shield = int(input("shield level?"))
print("health set")
