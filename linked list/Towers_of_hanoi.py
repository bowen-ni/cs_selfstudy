# Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks.
#
# The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.
#
# The game follows three rules:
#
# Only one disk can be moved at a time.
# Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# No disk may be placed on top of a smaller disk.

from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Create the Stacks

left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks = [left_stack, middle_stack, right_stack]
# Set up the Game
num_disks = int(input("\nHow many disks do you want to play with?\n"))
while num_disks < 3:
    num_disks = int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks,0,-1):
    left_stack.push(i)
num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {} moves".format(num_optimal_moves))



# Get User Input
def get_input():
    choices = []
    for i in stacks:
        choices.append(i)

    while True:

    return (input("Choose a stack for the game, enter L for left, M for middle, and R for right."))

# Play the Game