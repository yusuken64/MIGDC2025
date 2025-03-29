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
                text "Synergenix Global Initiates Project Green Future" size 100 bold True
                window:
                    xsize 800
                    ysize 2000
                    text """
At Synergenix Global, we are committed to enhancing operational efficiency while maximizing value for our stakeholders. As part of our ongoing initiative to optimize land utilization, we are proud to announce Project Green Future, a transformative endeavor aimed at reimagining our natural resource management strategies.
In alignment with our commitment to sustainable growth, Project Green Future will facilitate the repurposing of underperforming ecosystems. By redirecting these spaces towards high-yield, infrastructure-centric solutions, we will significantly increase productivity while supporting the long-term viability of our production pipelines.
Our dedicated Environmental Recalibration Team has identified several regions where biodiversity density is disproportionately high, resulting in resource inefficiencies and maintenance overhead. Through proactive ecosystem restructuring, we will ensure that these areas meet our enhanced productivity benchmarks, minimizing the environmental volatility caused by unmanaged flora and fauna.
Synergenix Global is proud to be at the forefront of responsible land stewardship. While temporary disruptions to local wildlife patterns may occur, we are excited to offer relocation support to all displaced organisms through our Wildlife Optimization Protocol, ensuring that the transition process aligns with our vision of a more streamlined natural world.
As part of our ongoing transparency commitment, we will continue to engage with local communities through stakeholder consultation forums, where we will outline the projected socio-environmental benefits of our revitalized landscapes. We remain dedicated to maintaining a balanced dialogue as we move forward with this exciting new chapter in sustainable development.
Together, we are shaping a future where nature and industry coexist in a harmonized, efficient ecosystem.
                    """
                    
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
                text "Synergenix Global’s 'Green Future' Is Just a Greenwash for Destruction" size 100 bold True
                window:
                    xsize 800
                    ysize 2000
                    text """
In a move that reeks of corporate greed and environmental negligence, Synergenix Global has launched Project Green Future—a so-called initiative that hides its true purpose: the mass destruction of ecosystems to make way for corporate expansion.
Under the guise of "enhancing operational efficiency" and "maximizing value," Synergenix is bulldozing thriving, biodiverse habitats to build factories and infrastructure, all in the name of profit. The company claims that these areas—deemed "underperforming ecosystems"—are somehow hindering progress. What they conveniently fail to mention is that these ecosystems are alive, diverse, and irreplaceable, providing shelter to countless species and maintaining the delicate balance of the environment.
Instead of taking responsibility for the ecological devastation they're causing, Synergenix has devised a euphemistic spin. They refer to their land grabs as "proactive ecosystem restructuring" and claim they will "optimize" the local wildlife with their Wildlife Optimization Protocol—a term that sounds more like a euphemism for displacement and destruction than any genuine conservation effort. While they pretend to offer "relocation support," it’s clear that they have no real interest in preserving biodiversity. They’re clearing the land for short-term gain without regard for the long-term environmental costs.
Synergenix’s so-called transparency is nothing more than a PR strategy. Despite claiming to engage with local communities through “stakeholder consultation forums,” the company’s actions speak louder than their carefully crafted words. They’re not interested in dialogue; they’re interested in unchecked expansion and profit at the expense of everything else.
The true impact of Project Green Future is clear: Synergenix is erasing nature in favor of their own bottom line, and their so-called "sustainability" is a thinly veiled attempt to whitewash the destruction they’re causing. The future they’re creating is one where corporate interests come before the planet, and the true cost of this ‘progress’ will be borne by the environment, local wildlife, and future generations.
It’s time for Synergenix Global to stop pretending that they’re saving the planet and start facing the reality of their harmful actions.
                    """

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
