#print("Program Started!")
# char = input("Enter a single character")
# if len(char) != 1:
#     print("incorrect length")
#
# else:
#     print("correct length")
#     print(f"The ascii code for {char} is: {ord(char)}")
# print("ended")
#
# ascii = int(input("enter an ascii code"))
# if ascii >= 32 and ascii <=126:
#     print("working")
#     print(f"The character represented by the ascii {ascii} is {chr(ascii)}")
# else:
#     print("error")
# print("ended")

# def listen():
#     sound=input("enter a sound")
#     print(f"That was loud {sound}!")
# listen()

# def identify():
#     see=input("what do you see")
#     if see == "a large boulder":
#         print("run")
#     else:
#         print("We'll be fine")
# # identify()

# def escape_by(plan):
#     if plan == "jumping over":
#         print("no")
#     elif plan == "going deeper":
#         print("works")
#     else:
#         print("stuck")
# plan = input("how to escape?")
# escape_by(plan)

# def cross_bridge(steps):
#     if steps > 5:
#         x=5
#         while x != 0:
#             print("step taken")
#             x=x-1
#         print("bridge is collapsing")
#     elif steps <= 0:
#         print("really")
#     else:
#         while steps != 0:
#             print("step")
#             steps = steps-1
#         print("keep going")
#
# steps = int(input("input number of steps"))
# cross_bridge(steps)

# def climb(remaining, crossed):
#     if remaining < crossed:
#         print("Over half way")
#     elif crossed == remaining:
#         print("halfway")
#     else:
#         print("barely started")
#
# remaining=int(input("remaining?"))
# crossed=int(input("crossed?"))
# climb(remaining, crossed)

# def display(steps):
#     while steps != 0:
#         print("""| |
# +++""")
#         steps = steps-1
#
# def create():
#     steps = int(input("how many steps?"))
#     display(steps)
# create()

# def sum_weights(beepW, boopW):
#     weight = beepW + boopW
#     return weight
# def avgW(beepW, boopW):
#     avgweight=(sum_weights(beepW, boopW))//2
#     print(avgweight)
# def run():
#     beepW = int(input("weight 1:"))
#     boopW = int(input("weight 2:"))
#     choice = input("average or sum")
#     if choice == "average":
#         print(avgW(beepW, boopW))
#     elif choice == "sum":
#         print(sum_weights(beepW, boopW))
#     else:
#         print("incorrect choice")
# run()

def box(y):
    print(f"""
__________________
|                 |
|{y}|
|                 |
__________________""")

def lower(y):
    print(y.lower())

def upper(y):
    print(y.upper())

def mirror(y):
    y.mirror() #dont know

def repeat(y):
    times = int(input("how many times to repeat?"))
    while times != 0:
        print(y)
        times = times-1

def main():
    x = input("box, lower, upper, mirror ,repeat?")
    y = input("input a word")
    if x == "box":
        box(y)
    elif x == "lower":
        lower(y)
    elif x == "upper":
        upper(y)
    elif x == "mirror":
        mirror(y)
    elif x == "repeat":
        repeat(y)
main()




