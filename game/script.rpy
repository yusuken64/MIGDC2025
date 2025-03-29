# The script of the game goes in this file.

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
    
    show bg room at truecenter:
        zoom 8

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
