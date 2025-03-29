label talk_scene:
    
    define guy = Character("Bad guy")
    #scene bg classroom
    show badguy at right

    guy "Hey, brother can you run this article for our company?"

    guy "I'll make it worht your while"
    e "But sir those are lies and this may be unethical"
    guy "but what if I give you 5 dollars"

    "You contemplate what to do."
    jump choice_scene
    
    return