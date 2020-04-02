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
    scene bg finn_apartment
    with fadee

    an "Jeez, it’s quiet even in the dorms now because of midterms. I hope Finn isn’t {i}too{/i} stressed."

    ##A ‘knocking’ sound effect and/or screen shake could be cool here

    show finn up smile at leftt
    with dissolve

    f talk "Alex!"

    show finn smile

    a "Whoa—hi."

    f talk "Come in, come in."

    hide finn with dissolve

    an "He ushers me in and sits me down before I even have a chance to really greet him."

    an "What’s he being so friendly for? He was stressed just this morning!"

    show alex up at closeright
    show finn smile at closeleft
    with dissolve

    a unsure talk "Oh, what’s that smell?"

    show alex neutral smile

    an "Something distractingly delicious gifts the air around his apartment...the oven-kissed scent of rich chocolate and vanilla."

    f talk "Huh? Oh. I made cookies. They’re vegan, so it should be fine if you have diet restrictions or anything."

    show finn smile

    an "That’s so cute!"


    ##choice
    menu:
        "They smell amazing.":
            f unsure frowntalk "Mhmm. That’s strange though, you didn’t smell them from outside?"
            show finn frown
            a frowntalk "I didn’t. I only smelled them after I came in."
            show alex frown
            f down frowntalk "I see..."
            show finn frown
            a unsure frowntalk "Why? Was I supposed to?"
            show alex frown
            f up frowntalk "No. It’s just there’s a neighbor who always seems to know when I’m baking. I figured he could smell it."
            show finn frown
            a neutral talk "Maybe he has a really strong sense of smell?"
            show alex frown
            f frowntalk "I hope so."
            show finn frown
            a unsure talk "Haha, ‘hope so’?"
            show alex frown
            f frowntalk "I swear he knows before I even put it in the oven. Maybe I’m being watched."
            show finn frown
            a down frowntalk "That’d be creepy."
            show alex frown
            f talk "Yeah. Guess that means I shouldn’t do anything incriminating with you."
            show finn smile
            a up blush shock "H-huh?"
            show alex shock
            ##end choice

        "What kind of cookies are they?.":
            f "Dark chocolate-and-vanilla pinwheel."
            a "Nice! You didn’t use box mix, did you?"
            f "Oh, I made them from scratch."
            a "Seriously?! From scratch?"
            f "Yeah. It’s cheaper than the ready-made and refrigerated stuff."
            a "Wow, I didn’t know you had a bunch of flour and stuff sitting around."
            f "Well, it’s ‘cause I have to keep them hidden away, can’t have food out here."
            a "Ah, yeah, the bugs would get to it."
            f "Heh, something like that."
            ##end choice

        "Do you have diet restrictions?":
            f "Not really... I prefer to eat vegan when I can though. It’s just too expensive."
            a "Understandable. Even vegetarian stuff gets marked up a lot around here."
            f "No kidding. What about you?"
            a "Hm, me?"
            f "Yeah, are there things you can’t eat or whatever?"
            a "Why, are you planning to make me food?"
            f "Tch. Not anymore."
            a "Aww, that’s mean. You really wouldn’t?"
            f "Guess we’ll find out in the future."
            ##end choice

    f "Anyway, you can have as many cookies as you like, doesn’t matter to me."

    a "Really? Thanks!"

    an "Hm, this study session isn’t starting quite what I expected, but it’s nice to just talk like this."

    an "I eat a cat-shaped cookie as I lay out my textbooks and notes. There’s so much to do, I wonder how long it’ll take to review everything."

    an "My focus goes in and out when Finn sits beside me. I tell myself I’m checking up on him, but I’m really just looking at his concentrated face."

    an "We don’t really talk at all. It’s completely different from our usual sessions. Oh well, it’s still nice to study together like this, even though my phone remains the ominous threat that it is."

    an "Hours pass before I know it when Finn suddenly groans and stretches."

    a "Finn?"

    f "I think we’ve done enough for today. We’ve done all we could."

    a "Oh! I didn’t realize it was so late already. Sorry."

    f "No... it’s fine, I’m glad."

    a "Glad?"

    f "Oh. Uh. I just meant..."

    a "... Yesssssss?"

    f "It went well, right? The study session, I mean."

    an "What’s gotten into him?"

    a "It did. Why?"

    f "I kind of wanted a re-do from before. When I yelled at you."

    an "Oh, when he snapped at me for using my phone when I was getting bombarded by my parents... Has he felt guilty about it this whole time?"

    a "Thanks, Finn. It went great. Is that what the cookies were for?"

    ##Blushing/flustered Finn
    f "What? No. No!"

    a "Aww but they were so cute. I was honored you baked me cookies."

    f "I just {i}happened{/i} to make them and you just {i}happened{/i} to be here."

    a "Hehe, so you just like baking cookies? Cause I didn’t see you eat a single one."

    f "Baking is... good for stress... and stuff."

    a "Haha. Is that so? Does that mean I can join you for baking next time?"

    an "He says something so quietly I can’t catch it."

    ##Alex genuinely didn’t hear, sprite should be confused/shocked/etc.
    a "Huh? What was that?"

    f "I said ‘Don’t taunt!’"

    a "Haha, sorry."

    an "It’s strange that I’m laughing even though midterms are tomorrow. I cling to this feeling, hoping to bring it with me when I go to bed so that I can still have it in the morning."

    return
