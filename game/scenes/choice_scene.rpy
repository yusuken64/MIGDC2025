label choice_scene:
    scene bg room
    "Which document will you publish?"

    call screen document_choice_screen

    menu:
        "Publish a Greedy money document":
            jump choice_scene_money

        "Publish altruistic helpful document":
            jump choice_scene_truth

screen document_choice_screen():
    modal True
    
    imagebutton:
        idle "document_money.png"
        hover "document_money_hover.png"
        action Show("money_details")
        xpos 100
        ypos 200

    imagebutton:
        idle "document_truth.png"
        hover "document_truth_hover.png"
        action Show("truth_details")
        xpos 400
        ypos 200

    # Menu choices inside the screen
    vbox:
        xpos 0.5
        ypos 0.8
        spacing 10

        textbutton "Publish a Greedy money document":
            action Jump("choice_scene_money")

        textbutton "Publish altruistic helpful document":
            action Jump("choice_scene_truth")

# Detail screens for the documents
screen money_details():
    modal True
    add "document_money_details.png" at truecenter
    textbutton "Back" action Hide("money_details") xpos 0.45 ypos 0.85

screen truth_details():
    modal True
    add "document_truth_details.png" at truecenter
    textbutton "Back" action Hide("truth_details") xpos 0.45 ypos 0.85

label choice_scene_money:
    "You let the corporate money influence you."
    $ money += 500  # Increment money by 500
    jump choice_scene_end

label choice_scene_truth:
    "You publish the damning truth about an evil organization."
    $ truth += 500  # Increment money by 500
    jump choice_scene_end

label choice_scene_end:
    "Whatever path you chose, you must live with the consequences."
    return
