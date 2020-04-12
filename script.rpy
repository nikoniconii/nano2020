﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("ALEX", color="#ffff66", image="alex")
define an = Character(" ", color="#ffff66", image="alex")
define f = Character("FINN", color="#bd8be7", image="finn")
define z = Character("ZAINA", color="#62baf0", image="zaina")
define p = Character("PAXTON", color="#cca3a3", image="paxton")

define Classmate1 = Character("CLASSMATE 1", color="#fff")
define Classmate2 = Character("CLASSMATE 2", color="#fff")
define c = Character("CUSTOMER", color="#ffffff")

define light = Fade(1.0, 0.3, 0.6, color="#fff3c9")
define fadee = Fade(1.0, 1.0, 1.0, color="#000")
define sideswipe = ImageDissolve("gradient2.png", 1.0)
define sidefade = ImageDissolve("gradient2.png", 1.0)

define pa = Character("{color=#ffff66}ALEX{/color} {color=#ffffff}&{/color} {color=#cca3a3}PAXTON{/color}")
define fpz = Character("{color=#bd8be7}FINN{/color} {color=#ffffff}&{/color} {color=#cca3a3}PAXTON{/color} {color=#ffffff}&{/color} {color=#62baf0}ZAINA{/color}")

transform rightt:
    xalign 0.80
    yalign 1.0
    
transform leftt:
    xalign 0.20
    yalign 1.0

## a closer left/right than the typical "at left"

transform closeright:
    xalign 0.95
    zoom 1.3
    yalign 0.1
    
transform closeleft:
    xalign 0.05
    zoom 1.3
    yalign 0.1

## an already defined zoomed-in left/right

label examplescene:     ## examples~

    scene bg amusementpark at center
    with fadee

    ## longer fade- please use this to show the passage of time, such as a frowntalk falling asleep!

    show alex frown

    "The night breeze is cool but feels perfect. It's hard to imagine kids running around this place in its heyday."

    show alex up smile at rightt
    show finn up frown at leftt
    with dissolve

    ## in most cases you'll want to show scenes with a fade and sprites with a dissolve

    a talk "It's such a beautiful night out, isn't it?"

    show alex smile

    f frowntalk "It's alright."

    show finn frown

    scene bg zaina_room
    with fade

    show zaina unsure frown at closeleft
    show alex up smile at closeright
    with dissolve

    z frowntalk "Welcome to my home, I guess."

    show zaina frown 

    a talk "It's cute here!"

    show alex smile

    scene bg mansion
    with fadee

    show zaina angry frown at center
    show alex up frown at right
    show finn unsure frown at left
    with dissolve

    f frowntalk "Watch where you step. The rotting floorboards are the least of our problems."

    show finn frown

    return


label start:    ## start of the game!

    stop music fadeout 1
    
    menu:
        "Finn Route":
            jump finnroute
        "Paxton Route":
            jump paxtonroute
        "Zaina Route":
            jump zainaroute

