###################################################################################################################
#######################                                                                 ###########################
#######################                         Finn's Route                            ###########################
#######################                                                                 ###########################
###################################################################################################################

label finnroute:
    ## scene 1
    
    scene bg classroom
    with fadee

    ##TODO A slow or solemn tune should play here to set a ‘down' mood

    an "The days pass as they normally do. Some slow, some way too fast..."
    an "So when this day comes, I should have expected it."
    an "But who can ever truly predict the end of the world?"

    ##TODO More upbeat or normal music starts playing for the joke

    show alex up frown backpack at closeright:
        yalign -0.25                    ## alex and zaina's sprites need to be set to a lower height than the boys!
    show finn up frown at closeleft
    with dissolve

    a down frowntalk "Oh no! It's happening?"

    show alex frown

    f frowntalk "It's over for me, I just know it."

    show finn frown

    a unsure frowntalk "Finn, you have to hold on!"

    show alex frown

    f frowntalk "Bury me with my sunscreen so that I can rest in peace."

    show finn frown

    a frowntalk "You can't give up before we even {i}start{/i} midterms."

    show alex frown

    ##Finn is smiling/teasing here
    f talk "Oh please, you're just as anxious as I am."

    show finn smile

    an smile "He's got me there."

    a up talk "That's not the point. We'll be fine in the end because...!"

    show alex smile

    menu:
        "We've been studying so much.":
            a talk "Because we've been studying so much!"
            show alex smile
            f frowntalk "We've been surprisingly diligent..."
            show finn frown
            a frowntalk "Huh? Why is that a surprise?"
            show alex frown
            f frowntalk "Because I distinctly remember spending many nights out at-"
            show finn frown
            a unsure frowntalk "H-hey! Not so loud."
            show alex frown
            f talk "Hah."
            show finn smile
            a up talk "Anyway, we'll be fine. We're going to do great."
            show alex smile
            ##end choice

        "Failure is not an option.":
            a frowntalk "Failure is not an option."
            show alex frown
            f frowntalk "Strong words from the woman who used to look like she was going to cry when she got a new text."
            show finn frown
            a unsure frowntalk "H-hey, I never cried! I'm just stressed!"
            show alex frown
            f frowntalk "I said {i}looked like.{/i}"
            show finn frown
            a frowntalk "Yeah, well so did you a couple minutes ago... anyway, I have faith in us. I really think we'll be fine."
            show alex up smile
            ##end choice

        "I'll definitely lose it otherwise.":
            a unsure frowntalk "I'll definitely lose it otherwise."
            show alex frown
            f frowntalk "Mhmm... well, if we both fail, we can have one last hurrah and explore a nuclear plant or something."
            show finn frown
            a frowntalk "What?! Absolutely not!"
            show alex frown
            f frowntalk "Just kidding... mostly."
            show finn frown
            a frowntalk "Put that energy into midterms instead."
            show alex frown
            f frowntalk "Did you just make a power plant joke?"
            show finn frown
            a frowntalk "I don't know, did I?"
            show alex frown
            ##end choice


    ##Finn is back to sad now

    f frowntalk "Anxious and still trying to comfort me. Like a living tryptophan amino acid..."

    show finn frown

    an frown "I'm losing him. Quick, a distraction!"

    a up talk "Hey, Finn. Wasn't there something you wanted to ask me before class?"

    show alex smile

    f unsure frowntalk "Huh...?"
    f up "Oh! Alex!"

    show finn frown

    a unsure frowntalk "Uh, yes?"

    show alex frown

    f frowntalk "Come home with me tonight."

    show finn frown

    a down frowntalk "{i}W-what?{/i}"

    show alex frown

    f frowntalk "We can study together. You'll come, right?"

    show finn frown

    a up frowntalk "Oh. Of course, that's what you meant."

    show alex frown

    f frowntalk "What?"

    show finn frown

    a frowntalk "Yes. I'll come, sure."

    show alex frown

    f frowntalk "Great. I like it when you come hang out with me you know."

    show finn frown

    an sweat "W-where is this coming from...?"

    an "Why am I being weird? Of course he's just talking about studying... right?"

    show alex blush frown with Dissolve(0.1)

    an "What if he didn't? What if it's kissing?"
    an "Wait—do I {i}want{/i} to kiss Finn? Since when do I have a crush on him?!"
    show finn smile
    an "Finn chuckles and softly flicks my forehead, distracting me from whatever nonsense I was just thinking."

    f frowntalk "Are you having a stroke or are you practicing for a mime routine?"

    show finn frown

    a frowntalk "Neither!"

    show alex frown

    f talk "Or maybe it's a bad thing you make me happy?"

    show finn smile

    a frowntalk "No... of course not."

    show alex frown

    an "Definitely just want to study."
    an "Mostly anyway."

    f talk "Uh huh. Well, see ya later then."

    show finn smile

    a talk "See you."

    show alex smile

    hide finn with easeoutleft

    hide alex with dissolve

    an "I need to calm down."
    an "It's just... a little hard when I keep thinking about him in the middle of my classes."

    ## scene 2

    return
