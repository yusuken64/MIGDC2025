# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show smiley

    # These display lines of dialogue.

    e "Hello MIGDC 2025!"
    
    "You find yourself at a crossroads."

    menu:
        "Go to Choice Scene":
            "You decide to go left and see where the path takes you."
            jump choice_scene
    
        "Go right":
            "You choose to go right, curious about what lies ahead."
    
        "Stay put":
            "You decide to stay put, waiting for something to happen."

    "Whatever you choose, your journey continues..."

    return
