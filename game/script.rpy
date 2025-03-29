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

    e "Oh man I just got a job as an editor how exciting"
    
    "I better choose carefully what articles to accept/reject or it may have dire consequences!!"
    
    "A bad man came and made you an offer."
    jump talk_scene

    return
