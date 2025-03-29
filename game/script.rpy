﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default money = 100
default trust = 100 

# The game starts here.

label start:

    transform scroll_down:
        ypos 0
        zoom 8
        linear 5.0 ypos -4000

    show bg scroll at scroll_down        

    $ renpy.pause(8.0)

    show screen hud
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show bg office at truecenter:
        zoom 4
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show smiley

    # These display lines of dialogue.

    e "Hello MIGDC 2025! test2"
    
    "You find yourself at a crossroads."

    menu:
        "Go to Choice Scene":
            "You decide to go left and see where the path takes you."
            jump choice_scene
    
        "Go to talk Scene":
            "You choose to talk to the guy"
            jump talk_scene
    
        "Stay put":
            "You decide to stay put, waiting for something to happen."

    "Whatever you choose, your journey continues..."

    return
