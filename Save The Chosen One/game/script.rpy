# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lloyd", color="#ffcc00")
define k = Character("King Stoic", color="#0f1954")
define mc = Character("You")
define v = Character("Villain", color="#800000")
define h = Character("Henchman", color="#2607b3")
define z = Character("Zorro", color="#5500aa")

default element = "none"
init:
    $ score = 0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image castleoutside = im.Scale("castleoutside.png", 1920, 1080)
    scene castleoutside
    with fade 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "{i}In a land filled with ancient magic, mysterious creatures, and precious artifacts. A young prince, born to be the prophesied Golden Protector of the realm, was taken by the evil elemental master of Wind, Zorro, who has begun draining his golden powers.{/i}"
    "{i}As one of his sworn protectors, using your unique elemental abilities, you must make your way through perilous challenges, solve intricate puzzles, and confront formidable foes.{/i}"
    "{i}Will you rescue the Chosen One and restore balance to the realm before it's too late?{/i}"
    jump start_adventure


label start_adventure:

    "{i}What elemental power will you choose to aid you on your quest to save Lloyd?{/i}"

    menu:
        "Fire":
            $ element = "Fire"
            show fireelement at Position(xpos=0.5, ypos=0.6)
            mc "Can you handle this heat? I am the master of Fire!"
            
        "Ice":
            $ element = "Ice"
            show iceelement at Position(xpos=0.5, ypos=0.8)
            mc "The Ice never bothers me, I am the master of Ice!"
        "Earth":
            $ element = "Earth"
            show earthelement at Position(xpos=0.5, ypos=0.7)
            image earthelement = im.Scale("earthelement.png", 400, 400)
            mc "The Earth keeps me grounded, I am the master of Earth!"
        "Lightning":
            $ element = "Lightning"
            show lightelement at Position(xpos=0.5, ypos=0.6)
            image lightelement = im.Scale("lightelement.png", 400, 400)
            mc "Watch out for my lightning strikes! I am the master of Lightning!"

    "{i}You can feel your [element] powers coursing through your veins, you're ready to Save the Chosen One!{/i}"

    jump start_story
    
label start_story:

    image castle_interior = im.Scale("castle_interior.jpg", 1920, 1080)
    scene castle_interior
    with fade

    show king_stoic 
    image king_stoic = im.Scale("king_stoic.png", 800, 800)
    show king_stoic at left
    k "Ah finally, you're here. Come closer, we have little time to discuss. Last night, Prince Lloyd was taken by the evil elemental master of Wind, Zorro. We believe he is after his golden power."
    k "As one of his sworn protectors, you must use your [element] abilities to rescue him. The fate of the realm rests in your hands."

    "{i}Are you ready to begin your quest?{/i}"
    menu:
        "Yes":
            mc "I'm ready. I'll save Lloyd and help restore balance to the realm!"
            k "Good. May the realm be safe in your hands."
            jump adventure_begins

        "No":
            mc "I need more time to prepare."
            k "Time is of the essence. The longer we wait, the stronger Zorro becomes. Please come back when you're ready."
            jump start_story

label adventure_begins:

    image castleoutside = im.Scale("castleoutside.png", 1920, 1080)
    scene castleoutside 
    with fade

    "{i}As you look back one last time at the castle, you set out towards the dark enchanted forest where Zorro is rumored to have his lair. The journey ahead may be long and perilous, but your determination to save Lloyd fuels your every step.{/i}"
    
    jump enchanted_forest

label enchanted_forest:
    image enchanted_forest = im.Scale("enchanted_forest.png", 1920, 1080)
    scene enchanted_forest
    with fade 
    show screen score_display

    show villain1 
    image villain1 = im.Scale("villain1.png", 600, 600)
    show villain1 at left
    show villain2
    image villain2 = im.Scale("villain2.png", 600, 600)
    show villain2 at right
    "{i}As you get deeper into the enchanted forest, the trees begin dying and the air grows thick with dark magic. Suddenly, a group of shadowy creatures emerge from the shadows, blocking your path but not yet spotting you.{/i}"
    v "Zorrow said the Chosen One's protector would come. When they get here we'll take them by surprise and capture them too! Maybe Zorro will finally make us henchmen!"


    menu:
        "Use your [element] powers to fight them.":
            "{i}You jump out ready to fight Zorro's minions.{/i}"
            v "Well well well, Zorro was right, the Chosen One's protector has arrived! Lets get them!"
            mc "Feel the wrath of my [element] powers!"
            "{i}You unleash a powerful attack, using your [element] abilities they dissipate into the darkness, clearing your path forward.{/i}"
            v "How could this happen?!"
            $ score += 10
            jump deeper_forest
        "Try to sneak around them.":
            mc "{i}I should try sneaking by, don't wanna burn myself out too soon.{/i}"
            "{i}Using the cover of the dense foliage, you carefully navigate around the shadowy creatures, avoiding confrontation and continuing your journey deeper into the forest.{/i}"
            $ score += 15
            jump deeper_forest

label deeper_forest:

    image dark_cave = im.Scale("dark_cave.jpg", 1920, 1080)
    scene dark_cave
    with fade

    "{i}After hours of searching, you think you've found the entrance to Zorros lair, how should you proceed?{/i}"

    menu:
        "Rush in like a [element] tornado!":
            mc "LETS GOOOOOOOOOOO"
            "{i}You charge in with a loud battle cry, your [element] powers pulsating ready to strike Zorrow down!{/i}"
            $ score += 10
            jump cave_interior
        
        "Sneakily enter the cave.":
            mc "{i}I should be quiet, don't wanna alert Zorro of my presence.{/i}"
            "{i}Carefully, you head into the cave, hiding in shadows and using your [element] abilities to stay silent.{/i}"
            $ score += 15
            jump cave_interior

label cave_interior:
    image cave_interior = im.Scale("cave_interior.jpg", 1920, 1080)
    scene cave_interior
    with fade

    "{i}As you enter the cave, it's empty, almost like nobody was ever here. You start to look around and investigate more.{/i}"
    jump investigate_cave

label investigate_cave:
    image investigate_cave = im.Scale("investigate_cave.png", 1920, 1080)
    scene investigate_cave
    with fade

    "{i}While looking at the walls, you notice strange markings that seem to pulse with dark energy. Is this where Zorro is keeping Lloyd? You must find out.{/i}"

    menu:
        "Strike the markings with your [element] powers.":
            mc "Take this!"
            "{i}Using a burst of your [element] energy, you unleash a powerful attack on the markings. Now they're glowing brighter, revealing a hidden passageway leading deeper into the cave.{/i}"
            $ score += 10
            jump find_lloyd
        "Look more closely.":
            mc "I need a better look."
            "{i}While examining the markings, you sense a magical attack and quickly dodge it! As the dust settles, you see one of Zorros henchmen emerge.{/i}"
            jump henchman_battle

label henchman_battle:
    show henchmen
    image henchmen = im.Scale("henchmen.png", 600, 600)
    show henchmen at right

    h "End of the line!"
    "{i}He must be one of Zorros henchmen, you must {b}take him down!{/b}{/i}"

    menu:
        "Use a powerful blast of [element]":
            mc "Take this!"
            "{i}You unleash a powerful blast of [element], the henchman is flung back and knocked out cold.{/i}"
            hide henchmen
            h "ahhhhhhh....."
            
            "{i}The energy from your [element] attack appears to have powered the secret passageway.{/i}"
            $ score += 25
            jump find_lloyd
        "Try to outsmart him.":
            mc "Haha you can't hit me!"
            "{i}As he gets angry from the teasing, he unknowingly stands near a steep ledge. You quickly try to hit him with a blast of [element], but he dodges it!{/i}"
            h "hahahah You're too slow!"
            jump henchman_battle2

label henchman_battle2:

    "What now?"
    menu:
        "Strike again with a huge burst of [element]":
            mc "I got you this time!"
            "{i}You gather all your strength and unleash a massive burst of [element]! The henchman is knocked back, losing his balance and falling off the ledge{/i}"
            "{i}You see a pulsating light from the markings, the energy from your [element] attack appears to have powered a secret passageway.{/i}"
            $ score += 15
            jump find_lloyd
        "Try to tire him out.":
            mc "Still can't hit me!"
            "{i}As you jump around dodging his attacks, he makes a misstep and you quickly hit him with a blast of [element] that sends him tumbling off the ledge.{/i}"
            "{i}The energy from your [element] attack appears to have powered a secret passageway.{/i}"
            h "Noooo!"
            $ score += 10
            jump find_lloyd

label find_lloyd:
    image find_lloyd = im.Scale("find_lloyd.png", 1920, 1080)
    scene find_lloyd
    with fade

    "{i}You go through the passageway and the cave opens up into a large chamber. In the center, you see Lloyd, chained and guarded by Zorro himself.{/i}"
    show zorro
    image zorro = im.Scale("zorro.png", 800, 800)
    show zorro at right
    z "It was so nice of you to come all this way. But, I'm afraid your journey ends here. I will take Lloyd's powers and {i}finally{/i} become the ultimate elemental master!"

    hide zorro
    show lloyd 
    image lloyd = im.Scale("lloyd.png", 600, 600)
    show lloyd at right
    "{i}Lloyd looks weak but relieved to see you.{/i}"
    l "you came... thank you... please save me..."
    mc "Don't worry Lloyd, I'll save you!"
    hide lloyd

    show zorro at right
    z "{b}ENOUGH!{/b} I have begun the draining process, soon Lloyds golden powers will be mine! All I have to do now is squash you like the insignificant insect you are!"
    mc "We'll see about that Zorro!"
    

    "{i}What will you do?{/i}"

    menu:
        "Try to reason with Zorro.":
            mc "Zorro, this isn't the way! Lloyd was chosen to protect the realm for the greater good. We cannot change destiny!"
            z "You {b}FOOL!{/b} I will change my destiny! I was meant to be the Chosen One and now {b}I WILL BE!{/b}"
            "Zorro quickly attacks you, but using your [element], you were able to dodge it."
            $ score += 10
            jump zorro_battle
        
        "Ready yourself":
            mc "If I must fight you to save Lloyd, then so be it! I swore to protect him with my life!"
            z "Very well fool, prepare to {b}DIE!{/b}"
            "Zorro lunges at you with his wind powers, using your [element], you were able to dodge it. The wind is kicking up!"
            $ score += 15
            jump zorro_battle

label zorro_battle:
    hide zorro     

    "{i}The battle for good and evil begins! Use your [element] powers wisely and you will emerge victorious!{/i}"
    show zorro

    menu:
        "Quickly attack with [element]":
            mc "Hi-ya!"
            "{i}With a swift strike from your [element], Zorro is thrown back but quickly recovers.{/i}"
            z "Was that the best you could do? Ha!"
            "{i}Zorro uses the wind to throw you off balance then quickly lunges at you!{/i}"
            mc "Ah!"
            $ score += -10
            jump zorro_battle2
        "Defend and counterattack":
            mc "You won't get away with this!"
            "{i}You brace yourself against Zorro's wind attack, using your [element] to shield yourself. As he recovers, you see an oppurtunity to strike back with a powerful [element] kick!{/i}"
            $ score += 10
            jump zorro_battle2

label zorro_battle2:
    "{i}The battle rages on, both you and Zorro are showing signs of fatigue. Make your next move count!{/i}"

    menu:
        "Unleash a powerful [element] attack.":
            mc "This ends now!"
            "{i}With all your strength, you channel your [element] powers into a devastating attack. Zorro is caught off guard and is thrown back, seemingly unconscious.{/i}"
            z "Ugh... no... I won't be defeated..."
            $ score += 30
            jump rescue_lloyd
        "Defend and wait for another opening.":
            mc "I'm not giving up yet!"
            "{i}You focus on defending against Zorro's attacks, waiting for the perfect moment, but he is faster than you think and lands a heavy blow that sends you reeling.{/i}"
            mc "Ugh!"
            $ score += -15
            jump zorro_battle3

label zorro_battle3:
    "{i}You're badly hurt, but you can't give up now! Summon all your strength for one final push!{/i}"

    menu:
        "Gather all of your remaining [element] power for the ultimate strike.":
            mc "This is for Lloyd!"
            "{i}With sheer determination, you gather all your remaining [element] power and unleash a powerful final strike. Zorro is overwhelmed and collapses, defeated.{/i}"
            hide zorro
            z "No... this can't be... I was meant to be the Chosen One..."
            $ score += 20
            jump rescue_lloyd

label rescue_lloyd:
    hide zorro
    show lloyd
    image lloyd = im.Scale("lloyd.png", 600, 600)
    show lloyd at right

    "{i}You rush to Lloyd, quuickly releasing him from his chains.{/i}"
    l "You saved me... thank you... the realm is in your debt."
    












        




    # These display lines of dialogue.



    # This ends the game.

    return
