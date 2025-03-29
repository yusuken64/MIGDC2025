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
    
    # Set xalign to percentages (0.0 is far left, 1.0 is far right)
    imagebutton:
        idle "document_money.png"
        hover "document_money_hover.png"
        action Show("money_details")
        xalign 0.25  # 25% from the left
        ypos 200     # Keep vertical position at 200 pixels

    imagebutton:
        idle "document_truth.png"
        hover "document_truth_hover.png"
        action Show("truth_details")
        xalign 0.75  # 75% from the left
        ypos 200     # Keep vertical position at 200 pixels

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

    frame:
        xalign 0.5
        yalign 0.4
        xsize 700
        ysize 700

        viewport:
            draggable True
            scrollbars "vertical"

            vbox:
                text "Here are your money details. You can list your data here."
                text "You can add as much text as you need, and it will be scrollable."
                text "Line 3: More details here."
                text "Line 4: Additional information."
                text "Line 5: Financial summary."
                text "Line 6: Expenses and income breakdown."

    textbutton "Back":
        action Hide("money_details")
        xpos 0.45
        ypos 0.85
        xpadding 20
        ypadding 10

screen truth_details():
    modal True

    frame:
        xalign 0.5
        yalign 0.4
        xsize 700
        ysize 700

        viewport:
            draggable True
            scrollbars "vertical"

            vbox:
                text "Here are your money details. You can list your data here."
                text "You can add as much text as you need, and it will be scrollable."
                text "Line 3: More details here."
                text "Line 4: Additional information."
                text "Line 5: Financial summary."
                text "Line 6: Expenses and income breakdown."

    textbutton "Back":
        action Hide("truth_details")
        xpos 0.45
        ypos 0.85
        xpadding 20
        ypadding 10

label choice_scene_money:
    "You let the corporate money influence you."
    $ money += 500  # Increment money by 500
    jump choice_scene_end

label choice_scene_truth:
    "You publish the damning truth about an evil organization."
    $ trust += 500  # Increment money by 500
    jump choice_scene_end

label choice_scene_end:
    "Whatever path you chose, you must live with the consequences."
    jump results_scene
    return
