import random

# Play one of the contained animations randomly. Called after a successful
# cheer condition is met
def play_animation():
    animation_number = random.randint(0, 1)

    # A pretty basic bugle call and CHARGE! cheer
    if animation_number == 0:
        print("Cheer 1 Placeholder!")

    # A cheer that involved an audio file I don't have the right to distribute
    if animation_number == 1:
        print("Cheer 2 Placeholder!")
