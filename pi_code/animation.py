import random

# Play one of the contained animations randomly. Called after a successful
# cheer condition is met
def play_animation():
    animation_number = random.randint(0, 1)

    if animation_number == 0:
        print("Cheer 1 Placeholder!")

    if animation_number == 1:
        print("Cheer 2 Placeholder!")
