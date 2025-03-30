label results_scene:
    # Check the value of the variable
    if money <= 0:
        "Your org ran out of money"
        jump gameover_scene
    elif trust <= 0:
        "The people no longer trust you"
        jump gameover_scene
    else:
        "Day passes and you are still in business."
    
    if day == 3:
        "You've made 3 choices and the world was effeced by your choices"
        "You have reached the end of the story."
        $ renpy.quit()

    $ day += 1 
    jump talk_scene