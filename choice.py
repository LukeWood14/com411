#type = input("what type of books do you like?")
#if type == "adventure":
#    print("I like adventure books!")
#else:
#    print("I prefer adventure")
#print("Finished reading")

#activity = input("please enter activity to be performed:")
#if activity == ("calculate"):
#    print("performing calculations")
#else:
#    print("performing activity")
#print("activity complete")

#direction = input("up, down, left or right?")
#if direction == "up":
#    print("painting up")
#elif direction == "down":
#    print("painting down")
#elif direction == "left":
#    print("painting left")
#elif direction == "right":
#    print("painting right")
#else:
#    print("incorrect input")

#no=int(input("input whole number"))
#print(no)
#if no%2==0:
#    print("even")
#else:
#    print("odd")

#no1=int(input("enter a number"))
#no2=int(input("enter another number"))
#if no1 > no2:
#    print("the second number is smaller")
#elif no1 < no2:
#    print("the first number is smaller")
#elif no1 == no2:
#    print("equal")
#else:
#    print("error")

x=0
odd=0
even=0
while x<3:
    n=int(input("enter a number"))
    if n%2==0:
        even=even+1
    else:
        odd=odd+1
    x=x+1
print(f"there were {odd} odds and {even} evens")
