# def observed():
#     obs = set()
#     obs = {"Flying Car", "Sky Scraper", "Sky Scraper", "Laser", "Dome", "Dome"}
#     return obs
#
# def run():
#     x=observed()
#     print(x)
# run()

# def observed():
#     obs = []
#     x=0
#     while x<5:
#         observ=input("what was your observation:")
#         obs.append(observ)
#         x=x+1
#     return obs
#
# def remove_ob(obs):
#     loop = True
#     while loop == True:
#         choice = input("Do you wish to remove an observation? yes/no")
#         if choice == "yes":
#             obs.remove(input("what do you wish to remove: "))
#         elif choice == "no":
#             loop = False
#         else:
#             print("incorrect choice try again")
#             loop = True
#
# def run():
#     obs=observed()
#     remove_ob(obs)
#     ob_set = set()
#     for observ in obs:
#         data = (observ, obs.count(observ))
#         ob_set.add(data)
#     for data in sorted(ob_set):
#         print(f"{data[0]} observed {data[1]} times.")
#
#
# run()

def pattern():
    seq = {'Short Sequence': 3, 'Medium Sequence': 2, 'Long Sequence': 1}
    return seq

def display_keys(seq):
    print("key: ")
    for key in seq:
        print(key)

def display_values(seq):
    print("value: ")
    for value in seq.values():
        print(value)

def display_items(seq):
    print("items: ")
    v=1
    for key in seq:  ##doesnt work
        k =key
        val = seq.values()
        print(f"{k}:{val}")
        v=v+1

def run():
    seq = pattern()
    display_keys(seq)
    display_values(seq)
    display_items(seq)

run()

