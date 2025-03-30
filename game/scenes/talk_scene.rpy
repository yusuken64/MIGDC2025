label talk_scene:
    define guy = Character("Bad guy")

    if day == 1:
        #scene bg classroom
        show badguy at right

        guy "Hey, brother can you run this article for our company?"

        guy "I'll make it worht your while"
        e "But sir those are lies and this may be unethical"
        guy "but what if I give you 500 dollars"

        "You contemplate what to do."

    elif day == 2:
        show badguy at right
        guy "Bad guy came to talk you again on day 2"
        guy "Bruh just help brother out"
        e "I'm just a girl I can't handle the pressure"
        guy "but what if I give you 500 dollars"
        "You contemplate what to do."

    
    elif day == 3:
        show badguy at right
        guy "Bad guy came to talk you again on day 3"
        e "please sir I can't keep doing this."
        e "I'm have anxiety and stress from this pressure"
        guy "but what if I give you 500 dollars"
        "You contemplate what to do."
    
    else:
        guy "Today is day [day]."

    jump choice_scene