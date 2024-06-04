from random import choice, randint
# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 5)

print(f"actually_sick = {actually_sick}")
print(f"kinda_sick = {kinda_sick}")
print(f"hate_your_job = {hate_your_job}")
print(f"sick_days = {sick_days}")

calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!

# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if sick_days:
    if actually_sick or (kinda_sick and hate_your_job):
        calling_in_sick = True
    else:
        calling_in_sick = False
else:
    calling_in_sick = False

print()
print(f"calling_in_sick = {calling_in_sick}")