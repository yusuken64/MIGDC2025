label choice_scene:
    scene bg room
    "Which document will you publish?"

    if day == 1:
        e "Okay, it seems like today I’ll be covering some stories regarding the city’s past…"
        call screen document_choice_screen

        menu:
            "Publish a Greedy money document":
                jump choice_scene_money

            "Publish altruistic helpful document":
                jump choice_scene_truth

    elif day == 2:
        e "Maybe today will run a bit more smoothly…Something in the present might be a bit easier, right?"
        call screen document_choice_screen

        menu:
            "Publish a Greedy money document":
                jump choice_scene_money

            "Publish altruistic helpful document":
                jump choice_scene_truth

    elif day == 3:
        e "Let’s see, the stories today involve the future of the city. Everything is on my hands…"
        call screen document_choice_screen

        menu:
            "Publish a Greedy money document":
                jump choice_scene_money

            "Publish altruistic helpful document":
                jump choice_scene_truth

screen document_choice_screen:
    modal True

    # Display the day at the top
    text "Day: [day]" xalign 0.5 ypos 50

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
screen money_details:
    modal True

    frame:
        xalign 0.5
        yalign 0.4
        xsize 1000
        ysize 800

        viewport:
            draggable True
            scrollbars "vertical"

            vbox:
                if day == 1:
                    text "Steel Industry Boosts Economy" size 100 bold True
                    window:
                        xsize 800
                        ysize 2000
                        text """
Studies have recently revealed that by allocating 11% of the cities’ budget, the steel industry can thrive in the city once more. By reducing unnecessary funding in areas like the local high school’s art program, it is estimated that the annual city budget could increase by 35%.

Despite initial concerns about safety, it is estimated that any potential injuries on the job would be negligible compared to the revitalization of the city. We thank the local steel mill for their contribution to our studio.
                        """
                    
                elif day == 2:
                    text "Celebration of the West Hower Bridge" size 100 bold True
                    window:
                        xsize 800
                        ysize 2000
                        text """
We are pleased to announce that the West Hower Bridge will be having its twentieth-year anniversary on Friday, there will be a live performance on the bridge to showcase just how resilient our city is in times of crisis and how together we can build a better tomorrow.

We hope to see you there, as Milton Construction Co. has spared no expense in setting up a wonderful time for anyone to enjoy, admittance to the festival will be free, but there will be nearby parking for $5.

                    """
                
                elif day == 3:
                    text "The Many Benefits of AI" size 100 bold True
                    window:
                        xsize 800
                        ysize 2000
                        text """
With the rise of Artificial Intelligence being on the mind of many people, we at the news station wanted to share some useful information on how it can be used in your day to day and professional life. Here’s Alex Zephyr, CEO of the nearby animation studio

‘I think it [AI] has been a wonderful addition to our company. I mean, we’re able to create our films without having to hire as much staff, pretty soon we won’t need any of them

                    """

    textbutton "Back":
        action Hide("money_details")
        xpos 0.45
        ypos 0.85
        xpadding 20
        ypadding 10
        background "#0078D4"

screen truth_details:
    modal True

    frame:
        xalign 0.5
        yalign 0.4
        xsize 1000
        ysize 800

        viewport:
            draggable True
            scrollbars "vertical"

            vbox:
                if day == 1:
                    text "Abandoned Steel Mill Turned into Community Center" size 100 bold True
                    window:
                        xsize 800
                        ysize 2000
                        text """
Son of one of the city’s most prominent steel mill owners, Alex Ferrus, has announced that he plans on dedicating the abandoned General Forge steel mill, which has laid dilapidated for years, to be refurbished into a place where the community can rebuild after recent unrest.

‘I think it will be an excellent opportunity for people to come together and make something special. Our city has a prominent place in history, and I would like to cherish that so the future generations can understand its’ significance

                        """
                
                elif day == 2:
                    text "West Hower Bridge Warning" size 100 bold True
                    window:
                        xsize 800
                        ysize 2000
                        text """
This is a warning regarding the condition of the West Hower Bridge. While the bridge has been faithfully helping people cross the Lian River for the past twenty years, a private investigation has revealed that the bridge will be in need of repairs due to degradation in the bridge’s foundation. Please refrain from driving on the bridge and consider taking a detour to your destination while we take time to assess damages

While it will take a substantial amount of time and money to repair the bridge, it serves as both a crucial point of travel for the city and also as a marvel of architectural design that has made it a landmark of the city.
                        """
                
                elif day == 3:
                    text "Artist Lawsuit Won" size 100 bold True
                    window:
                        xsize 800
                        ysize 2000
                        text """
With the rise of Artificial Intelligence being a concern for many people, some have turned to more legislative means to keep this new technology in check.

A group of artists launched a class action lawsuit against ChippGPT, a new AI model that has been accused of copyright infringement as the model supposedly used stolen art to fill out its prompts. The artists won their case and as a result ChippGPT is forced to pay compensation for every artwork that has been used by the AI model…

                        """

    textbutton "Back":
        action Hide("truth_details")
        xpos 0.45
        ypos 0.85
        xpadding 20
        ypadding 10
        background "#0078D4"

label choice_scene_money:
    "You let the corporate money influence you."
    $ money += 500
    $ money -= 50
    $ trust -= 50
    jump choice_scene_end

label choice_scene_truth:
    "You publish the damning truth about an evil organization."
    $ trust += 40
    $ money -= 50
    jump choice_scene_end

label choice_scene_end:
    "Whatever path you chose, you must live with the consequences."
    jump results_scene
    return
