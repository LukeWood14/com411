# def directions():
#     directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
#     return directions
#
# def run():
#     print(directions())
# run()

# def movements():
#     path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
#     return path
#
# def run():
#     print("Moving...")
#     path = movements()
#     print(f"{path[0]} for {path[1]} steps " )
#
# run()

# def directions():
#     directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
#     return directions
#
# def menu():
#     local_directions = directions()
#     x=0
#     while x < len(local_directions):
#         print(f"{x+}: {local_directions[x]}")
#         x=x+1
# def run():
#     menu()
# run()

# def directions():
#     directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
#     return directions
#
# def menu():
#     print("Please choose a location using the index")
#     local_directions = directions()
#     x=0
#     while x < len(local_directions):
#         print(f"{x}: {local_directions[x]}")
#         x=x+1
#     choice = int(input("Choice: "))
#     return local_directions[choice]
#
# def run():
#     print("working out route")
#     route=[]
#     run_x = 0
#     while run_x < 5:
#         route.append(menu())
#         run_x=run_x+1
#     print(f"the route is: {route}")
#
# run()

# def likelihood():
#     likelihoods = (50, 38, 27, 99, 4)
#     return min(likelihoods), max(likelihoods)
#
# def run():
#     likeli = likelihood()
#     print(f"Minimum likelihood of falling: {likeli[0]}% and max is {likeli[1]}%")
#
# run()

# def steps():
#     chance=[("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 4)]
#     return chance
#
# def run():
#     chance=steps()
#     good_steps=[]
#     bad_steps=[]
#     for step in chance:
#         if (step[1] >= 50):
#             bad_steps.append(step)
#         else:
#             good_steps.append(step)
#     print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")
#
# run()

