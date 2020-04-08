###################################################################################################################
#######################                                                                 ###########################
#######################                         Finn's Route                            ###########################
#######################                                                                 ###########################
###################################################################################################################

label finnroute:
    ## scene 1
    
    scene bg classroom
    with fadee

    ##TODO A slow or solemn tune should play here to set a 'down' mood

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
    scene bg finn_room
    with fadee

    an "Jeez, it's quiet even in the dorms now because of midterms. I hope Finn isn't {i}too{/i} stressed."

    ##A 'knocking' sound effect and/or screen shake could be cool here
    "Knock, knock..." with vpunch

    show finn up smile at leftt
    with dissolve

    f talk "Alex!"
    show finn smile

    a "Whoa—hi."

    f talk "Come in, come in."
    hide finn with dissolve

    an "He ushers me in and sits me down before I even have a chance to really greet him."

    an "What's he being so friendly for? He was stressed just this morning!"

    show alex up at closeright:
        yalign -0.25
    show finn smile at closeleft
    with dissolve

    a up talk "Oh, what's that smell?"
    show alex smile

    an "Something distractingly delicious gifts the air around his apartment...the oven-kissed scent of rich chocolate and vanilla."

    f talk "Huh? Oh. I made cookies. They're vegan, so it should be fine if you have diet restrictions or anything."
    show finn smile

    an "That's so cute!"

    ##choice
    menu:
        "They smell amazing.":
            f unsure frowntalk "Mhmm. That's strange though, you didn't smell them from outside?"
            show finn smile

            a neutral frowntalk "I didn't. I only smelled them after I came in."
            show alex frown

            f down frowntalk "I see..."
            show finn smile

            a unsure frowntalk "Why? Was I supposed to?"
            show alex frown

            f up frowntalk "No. It's just there's a neighbor who always seems to know when I'm baking. I figured he could smell it."
            show finn smile

            a neutral talk "Maybe he has a really strong sense of smell?"
            show alex smile

            f frowntalk "I hope so."
            show finn smile

            a unsure talk "Haha, 'hope so'?"
            show alex smile

            f frowntalk "I swear he knows before I even put it in the oven. Maybe I'm being watched."
            show finn smile

            a down frowntalk "That'd be creepy."
            show alex frown

            f talk "Yeah. Guess that means I shouldn't do anything incriminating with you."
            show finn smile

            show alex blush with Dissolve(0.1)
            a up shock "H-huh?"
            show alex smile
            ##end choice

        "What kind of cookies are they?.":
            f up talk "Dark chocolate-and-vanilla pinwheel."
            show finn smile

            a neutral talk "Nice! You didn't use box mix, did you?"
            show alex smile

            f talk "Oh, I made them from scratch."
            show finn smile

            a up shock "Seriously?! From scratch?"
            show alex smile

            f talk "Yeah. It's cheaper than the ready-made and refrigerated stuff."
            show finn smile

            a neutral talk "Wow, I didn't know you had a bunch of flour and stuff sitting around."
            show alex smile

            f talk "Well, it's 'cause I have to keep them hidden away, can't have food out here."
            show finn smile

            a unsure sweat talk "Ah, yeah, the bugs would get to it."
            show alex smile

            f talk "Heh, something like that."
            show finn smile
            ##end choice

        "Do you have diet restrictions?":
            f unsure frowntalk "Not really... I prefer to eat vegan when I can though. It's just too expensive."
            show finn frown

            a unsure sweat talk "Understandable. Even vegetarian stuff gets marked up a lot around here."
            show alex smile

            f talk "No kidding. What about you?"
            show finn smile

            show alex -sweat
            a unsure talk "Hm, me?"
            show alex smile

            f talk "Yeah, are there things you can't eat or whatever?"
            show finn smile

            a up shock "Why, are you planning to make me food?"
            show alex smile

            f down talk "Tch. Not anymore."
            show finn frown

            a down frowntalk "Aww, that's mean. You really wouldn't?"
            show alex frown

            f unsure talk "Guess we'll find out in the future."
            show finn smile
            ##end choice

    f up talk "Anyway, you can have as many cookies as you like, doesn't matter to me."
    show finn smile

    show alex -sweat
    a up talk "Really? Thanks!"

    hide finn with dissolve
    hide alex with dissolve

    an "Hm, this study session isn't starting quite what I expected, but it's nice to just talk like this."

    an "I eat a cat-shaped cookie as I lay out my textbooks and notes. There's so much to do, I wonder how long it'll take to review everything."

    an "My focus goes in and out when Finn sits beside me. I tell myself I'm checking up on him, but I'm really just looking at his concentrated face."

    an "We don't really talk at all. It's completely different from our usual sessions. Oh well, it's still nice to study together like this, even though my phone remains the ominous threat that it is."

    an "Hours pass before I know it when Finn suddenly groans and stretches."

    show alex unsure at closeright:
        yalign -0.25
    show finn up smile at closeleft
    with dissolve

    a unsure frowntalk "Finn?"
    show alex frown

    f up frowntalk "I think we've done enough for today. We've done all we could."
    show finn smile

    a up shock "Oh! I didn't realize it was so late already. Sorry."
    show alex frown

    f up talk "No... it's fine, I'm glad."
    show finn smile

    a unsure talk "Glad?"
    show alex smile

    f unsure talk sweat "Oh. Uh. I just meant..."
    show finn smile

    a up talk "... Yesssssss?"
    show alex smile

    f talk "It went well, right? The study session, I mean."
    show finn smile

    an unsure frown "What's gotten into him?"

    a frowntalk "It did. Why?"
    show alex frown

    show finn -sweat
    f down frowntalk "I kind of wanted a re-do from before. When I yelled at you."
    show finn smile

    an neutral "Oh, when he snapped at me for using my phone when I was getting bombarded by my parents... Has he felt guilty about it this whole time?"

    a unsure talk "Thanks, Finn. It went great. Is that what the cookies were for?"
    show alex smile

    ##Blushing/flustered Finn
    show finn blush with Dissolve(0.1)
    f unsure talk "What? No. No!"
    show finn frown

    a up talk "Aww but they were so cute. I was honored you baked me cookies."
    show alex smile

    f down talk "I just {i}happened{/i} to make them and you just {i}happened{/i} to be here."
    show finn frown

    a unsure talk "Hehe, so you just like baking cookies? Cause I didn't see you eat a single one."
    show alex smile

    f unsure talk "Baking is... good for stress... and stuff."
    show finn smile

    a up talk "Haha. Is that so? Does that mean I can join you for baking next time?"
    show alex smile

    f down frowntalk "{size=12}Don't taunt!{/size}"
    show finn smile

    an unsure "He says something so quietly I can't catch it."

    ##Alex genuinely didn't hear, sprite should be confused/shocked/etc.
    a unsure frowntalk "Huh? What was that?"
    show alex frown

    f up talk "I said 'Don't taunt!'"
    show finn smile

    a up talk "Haha, sorry."
    show alex smile

    an "It's strange that I'm laughing even though midterms are tomorrow. I cling to this feeling, hoping to bring it with me when I go to bed so that I can still have it in the morning."

    hide finn
    hide alex
    with dissolve

    ## Scene 3
    ##Classroom bg
    scene bg classroom
    with fadee

    show alex neutral frown backpack at closeright:
        yalign -0.25
    show finn down frown at closeleft
    with dissolve

    f frowntalk "Ugh..."
    show finn frown

    a down frowntalk "You said it. I feel like I just ran a marathon."
    show alex frown

    f up talk "I feel like I just got attacked by otherworldly forces without my trusty vampire steed."
    show finn smile

    an unsure"That's certainly one way to describe it!"

    a up talk "At least it's done. We crossed the finish line."
    show alex smile

    f down sweat talk "{i}You{/i} crossed it."
    show finn smile

    a talk "Haha, I'm sure you 'defeated' your enemy, too."
    show alex smile

    show finn -sweat
    f talk "Maybe. We'll have to see our test scores."
    show finn smile

    a neutral talk "I'm just so glad it's over."
    show alex smile

    f down frowntalk "Which means it's time to get back to business."
    show finn smile

    a unsure frowntalk "Are you talking about... you know?"
    show alex smile

    f up talk "You're coming, right?"
    show finn smile

    an "Finn's lighthearted smile brightens my own. He seems geared up to go on our next trespassing adventure, it's kind of cute."

    a up talk "Of course. Where to next?"
    show alex smile

    f down frowntalk "Not so loud, come here."

    hide finn with dissolve
    hide alex with dissolve

    an "He leads me to the corner of the classroom and leans in. He's... really close!"

    ##Move the sprites closer
    show alex unsure sweat backpack at closeright:
        yalign -0.15
        zoom 1.2
    show finn down frowntalk at closeleft:
        zoom 1.2
    with dissolve

    a unsure sweat frowntalk "You're making me nervous. Is it super dangerous or something?"
    show alex smile

    f up talk "An amusement park."
    show finn smile

    show alex -sweat
    a up shock "An actual abandoned {i}amusement{/i} park? The kind with rides and cotton candy?"
    show alex shock

    f down frowntalk "Even better—rusty tracks and funnel cake mold."
    show finn smile

    a down sweat frowntalk "Gross..."
    show alex frown

    f down talk "I'm just kidding. The most you could find is probably toxic waste."
    show finn smile

    a unsure talk "... You're still joking, aren't you?"
    show alex smile

    f up frowntalk "Definitely. See you tonight?"
    show finn smile

    show alex -sweat
    a neutral talk "I'm coming."
    show alex smile

    ##Finn smiling/soft here
    
    an "Finn's smile looks overly soft when he looks down at me. His hand pats my head affectionately and I can't help but feel like some kind of puppy."

    f up talk "... Cool."

    ##Alex flustered/blushing here
    show finn smile
    show alex blush with Dissolve(0.1)
    a up talk "C-Cool."
    show alex up smile

    hide finn with easeoutleft

    an "He leaves first, leaving me way too flustered for someone who was just talking with a friend. I go home and make sure to grab shoes I wouldn't mind stepping in funnel cake mold with."
    
    hide alex with dissolve

    ## Scene 4
    ##Amusement park bg
    scene bg amusementpark
    with fadee

    ##All 4 sprites are here
    show finn up smile:
        xalign 0.05
        yalign 1.0
    show paxton unsure smile:
        xalign 0.35
        yalign 1.0
    show zaina up smile:
        xalign 0.65
        yalign -1.5
    with dissolve

    p up talk "Not that one, the third latte—er, picture down. With the red cup. Do you think it'd look nice?"
    show paxton smile

    z unsure talk "Is that supposed to be a dog?"
    show zaina neutral

    p unsure talk "It's an elephant."
    show paxton smile

    f unsure sweat frowntalk "I thought it was a rabbit."
    show finn smile

    z up talk "Oh, yes I can see that."
    show zaina smile

    f up talk -sweat "It's the ears."
    show finn smile

    p down frowntalk "You guys...{i}Just when the world needed Alex the most, she vanished.{/i}"
    show paxton frown

    ## Finn and Zaina are speaking at the same time. This is the only instance of this, format as needed!
    show finn unsure frowntalk
    show zaina unsure frowntalk
    "{color=#bd8be7}Finn{/color} {color=#FFF}&{/color} {color=#62baf0}Zaina{/color}" "?"

    show alex up smile:
        xalign 1.15
        yalign 1.0
    with dissolve

    a talk "Err—no, I'm right here!"

    show alex down smile with dissolve:
        xalign 0.85

    f unsure talk "Huh? How long have you been standing there?"
    show finn smile
    show zaina smile

    ##Tearful/overjoyed Paxton
    p up smile "Alex...!"
    show paxton smile

    a up talk "Not long, a minute or so.  You all seemed so deep in your conversation that I didn't want to interrupt."
    show alex smile

    z down frowntalk "That was {i}not{/i} a real conversation."
    show zaina frown

    p unsure talk "It was supposed to be."
    show paxton frown

    f up talk "Anyway... ready to get started?"
    show finn smile

    ##choice
    menu :
        "As long as there's no toxic waste.":
            z unsure frowntalk "What...?"
            show zaina frown
            p down frowntalk "I'm pretty sure I used to have nightmares about this."
            show paxton frown
            an "Finn just bursts out laughing before quickly covering it with a disinterested cough, surprising everyone including me."
            show finn unsure
            z unsure talk "What did you say to her, Finn?"
            show zaina smile
            f up talk "Nothin'."
            show finn smile
            a unsure talk "Just a joke...but Paxton, what do you mean 'used to?'"
            show alex smile
            p up talk "Oh, I actually used to go to this park as a child."
            show paxton smile
            z up smile "Whoa—really?"
            show zaina smile
            an "He shrugs with a small smile, not elaborating on the topic. I wonder what he thinks of coming back here, I'm sure it looks completely different than before."
            ##end choice

        "As ready as I can be.":
            f unsure talk "Having second thoughts?"
            show finn smile
            a up talk "No, I'm just nervous about stepping on something I shouldn't."
            show alex smile
            z up talk "If anything happens to your shoes, I can take you directly home on my motorcycle."
            show zaina smile
            a up shock "On your motorcycle? That's kind of you."
            show alex smile
            z unsure talk "Sure but like...try not to lose your shoes?"
            show zaina smile
            p up talk "Alex, stepping on something like what?"
            show paxton smile
            f up talk "Moldy funnel cake."
            show finn smile
            ##Paxton sprite expression change
            p unsure frowntalk "..."
            show zaina unsure frown
            show alex unsure
            ##Paxton sprite expression change
            p down frowntalk "I could've gone my whole life without that mental image."
            show paxton down frown
            an "Paxton shivers and Zaina's nose scrunches. I think we all could've gone without that mental image."
            ##end choice

        "What were you guys talking about?":
            z up talk "Paxton was showing us latte art on some girl's cafe page."
            show zaina smile
            f unsure talk "Yeah...of a rabbit."
            show finn smile
            p down frowntalk "It was definitely an elephant, you guys."
            show paxton smile
            a unsure talk "You make latte art, Paxton?"
            show alex smile            
            p unsure talk "It's just an interest...I work in a cafe after all."
            show paxton smile
            z up talk "Must be nice that your interests align."
            show zaina smile
            p up talk "I suppose."
            show paxton smile
            f up talk "I have an interest that we can follow right now."
            show finn smile
            ##end choice

    f up talk "Anyway, we're all here. So good—this way!"
    show finn smile

    hide alex
    hide paxton
    hide zaina
    hide finn
    with dissolve
    an "Finn grabs my hand and starts running off before I have a chance to ask his plan. I don't expect it but neither do Paxton nor Zaina based on their shocked faces."
    #Zaina and Paxton sprites disappear

    show finn up smile at closeleft
    show alex up smile at closeright:
        yalign -0.25
    with dissolve

    a unsure talk "F-Finn?"
    show alex smile

    an "He just shoots me a small smile before slowing down as we approach a rollercoaster."

    f up talk "Aaaaand here is where I want to start."
    show finn smile

    an "He lets go of my hand and looks up the beginning of the tracks, spiraling and rusty like a beaten, ancient nail from a world of giants."

    a unsure talk "You want to {i}climb{/i} these?"
    show alex smile

    #Zaina and Paxton sprites reappear
    hide alex
    hide finn
    with dissolve

    show finn up smile:
        xalign 0.05
        yalign 1.0
    show zaina unsure frown:
        xalign 0.85
        yalign -1.5
    show paxton up smile:
        xalign 0.55
        yalign 1.0
    show alex unsure smile:
        xalign 0.33
        yalign 1.0
    with dissolve

    z unsure frowntalk "Jeez, you didn't have to run...! What the hell is this?"
    show zaina frown

    p up talk "Whoa...it's still standing."
    show paxton smile

    z unsure frowntalk "Are you serious, Finn? The tracks?"
    show zaina frown

    f up talk "Would I be here if I wasn't?"
    show finn smile

    p unsure frowntalk "I think I'll pass, I don't have the luck stat for this."
    show paxton frown

    z up talk "Yeah, I'm with whatever Paxton just said. And you, Alex?"
    show zaina smile

    a unsure frowntalk sweat "Well..."
    show alex frown

    show finn unsure frown
    an "Finn looks directly at me, determination in his gaze. I shouldn't leave him to go alone."

    ##Determined/smiling Alex
    a up talk -sweat "I'll go with you, Finn."
    show alex smile

    f up talk "Knew I could count on you."
    show finn smile

    z unsure talk "Sigh... well, be careful, you two. I want to check out the stalls."
    show zaina smile

    p up talk "Yes. We're going to keep exploring here."

    p unsure talk "On the ground."

    p unsure talk "Away from the tracks."
    show paxton smile

    a up talk "Okay, we will. See you soon."
    show alex smile

    hide alex
    hide finn
    hide paxton
    hide zaina
    with dissolve

    an "Finn leads the way, one step at a time, following the small-sloped hills as we pass under the shadows of the tracks. He chooses a track part that curves upwards instead of spiraling and we start climbing." 

    an "It's... thrilling."

    an "I can already see how the stars of the night cast an ethereal sheen on the Ferris wheel that sits not too far away. I bet the view further up is going to be amazing. If we make it there, anyway."

    an "I watch his back and hope to find it reassuring, but I can't help but notice how my steps are not as confident and my hands are not as steady. These tracks don't look like they can carry bodies, let alone a speeding cart full of them."

    an "Am I nervous or excited?"

    show finn up smile at closeleft
    show alex up smile at closeright:
        yalign -0.25
    with dissolve

    ##Phone buzz/screen shake
    a up shock "Ah!" with vpunch
    show alex shock

    an "Ugh, my phone surprised me. I'm getting distracted. I need to be careful, what if I miss a step?"
    show alex smile

    f unsure frowntalk "Alex? Are you okay?"
    show finn frown

    a unsure talk sweat "Y-yes. I'm fine..."
    show alex smile

    an "Finn stops at the top of one of the flatter dips and turns to face me. What's with that concerned look?"

    f unsure talk "Hm... if you say so."
    show finn smile

    an unsure smile "Pull yourself together, Alex."
    show alex -sweat

    f up talk "Here, take my hand. Let's climb this part together."
    show finn smile

    show alex blush with Dissolve(1.0)
    a up talk "Oh. Okay..."
    
    hide alex
    hide finn
    with dissolve

    an "I'm not sure this will actually help but I guess it's fine. It's the second time he's taken my hand tonight and it doesn't make me feel any less nervous."

    an "We climb the track slowly even though my cold fingers keep shaking in his. One step. Two steps. Three steps. These gaps sure are big..."

    show finn down frown at closeleft
    show alex up smile at closeright:
        yalign -0.25
    with dissolve

    ##Finn frowning
    f down frown "..."
    show finn frown

    a unsure frowntalk "Huh? Why'd you stop?"
    show alex smile

    f unsure frowntalk "... Alex."
    show finn frown

    a unsure frowntalk "Yes?"
    show alex frown

    f down frowntalk "You're still shaking. It's dangerous if you slip and cut yourself here, it's really rusted."
    show finn frown

    a talk "Oh... sorry. Maybe I'm just cold."
    show alex smile

    f unsure frowntalk "Hmph."
    show finn frown

    ##Finn smiling
    f up talk "Hey, Alex. Come here."
    show finn smile

    ##Maybe move the sprites closer here
    show alex unsure sweat at closeright:
        yalign -0.15
        zoom 1.2
    show finn down frowntalk at closeleft:
        zoom 1.2
    with dissolve

    a unsure talk sweat "What?"
    show alex smile

    an "Finn's hands cover both of mine. They're not much warmer but it's a start. But then he leans in-"
    
    hide alex
    hide finn
    with dissolve    

    ##EVENT IMAGE: FIRST KISS
    ##note to programmers, this didn't get made into an event image but leave the placeholder in case it gets added later?
    scene cg first kiss
    with dissolve

    an "-and kisses me."

    a "Mm?"

    an "What...? Finn's mouth is like frosted tulips against my own, soft and gentle yet bitten by cold. It's only his breath of heated sugar that sends warmth straight from my lips to my cheeks."

    an "I know it must've only been a moment, but it feels like a lifetime."

    an "He pulls away and I don't know what to think or feel."
    
    scene bg amusementpark
    with fadee

    show alex unsure smile blush at closeright:
        yalign -0.25
    show finn up smile at closeleft
    with dissolve

    f up talk "Haha..."
    show finn smile

    a unsure frowntalk "Huh? What was that for? What are you-?"
    show alex smile

    f up talk "You should see your face right now."
    show finn smile

    a down frowntalk "Because you {i}kissed{/i} me!"
    show alex frown

    f unsure talk "Yeah. But at least you're not shaking anymore."
    show finn smile

    an unsure smile -blush "What? Oh, he's right, I'm not."

    f up talk "Come on, we're almost done with our climb."
    show finn smile

    a up talk "Uh... okay..."
    show alex smile

    hide alex
    hide finn
    with dissolve

    an "It's all I can manage to say as we finish the climb. Not that I remember it well. My mind is elsewhere, and I'm still in a daze even when we meet back up with Zaina and Paxton."

    an "As if nothing ever happened. But who forgets a kiss like that, alone together under the stars?"

    ## Scene 5
    ##Classroom bg
    scene bg classroom
    with fadee

    show alex unsure frown backpack at closeright:
        yalign -0.25
    with dissolve

    ##A very serious/concentrated Alex
    a "..."

    an "Don't freak out."

    "Classmate1" "I'm dropping out."

    an unsure "Don't freak out., don't freak out. Whatever you do-"

    "Classmate2" "Don't you dare. Your parents would kill you."

    "Classmate1" "But I failed my midterm! My life is over!"

    "Classmate2" "We'll figure something out! We still have half the semester!"

    "Classmate1" "My GPA... what's the point..."

    a "..."

    a "..."

    an unsure sweat "Oh no, oh no. I'm freaking out. Just check the grade. You can do this."

    a "..."

    an down "It's... a 90. This is the lowest grade I've gotten in a while. Ugh."

    show alex -sweat
    an unsure "Maybe I should be going out less and focusing on studying. But... I was so miserable then."

    ##Alex smiling
    an smile "Well... a 90 isn't really a bad grade, is it? I can work with this. Besides... if I went out less, my social life would be over. Again. No more late-night adventures and shenanigans with Zaina and Paxton and... Finn..."

    ##Alex blushing
    an blush "Finn... the last time we went out he—and I—we... Ahh... I don't even know how to face him properly."

    ##Finn serious expression
    f talk "Alex!"
    
    an shock sweat "Gah! The devil hears my thoughts!"

    show finn unsure frown at closeleft
    with dissolve

    f unsure frowntalk "Alex..."
    show finn frown

    a unsure talk -blush "H-hello, Finn."
    show alex smile

    f down frowntalk "I got my test scores back. I got... a C."
    show finn frown

    show alex -sweat
    an down frown "Oh no..."

    a down frowntalk "Finn..."
    show alex frown

    ##Finn smiling
    f up talk "I didn't think I was going to pass at all!"
    show finn smile

    an unsure "Finn is positively beaming and I stare at him in shock, even as he pats my head again."

    f up talk "It's all thanks to you. You're the best study partner ever."
    show finn smile

    a unsure talk sweat "What? Uh, congratulations?"
    show alex smile

    f up talk "You know what this means? We should celebrate."
    show finn smile

    show alex -sweat
    a unsure talk "Celebrate?"
    show alex smile

    f up talk "I found a new place for us."
    show finn smile

    a unsure talk "Already?"
    show alex smile

    f unsure talk "Naturally. Are you busy tomorrow night?"
    show finn smile

    a up talk "No. I'll come!"
    show alex smile

    f up talk "See ya, lab partner."
    show finn smile

    ##Finn sprite exit
    hide finn
    with dissolve

    an down "I'm a total idiot for ever being nervous around Finn. He's still patting me like a pet dog!"

    an unsure "Yeah, I'm the one being awkward. Maybe the kiss really didn't mean anything. Or maybe I imagined it ever happening. Ah, so frustrating."

    hide alex
    with dissolve

    an "I push it to the back of my mind where I hope I can forget it ever even happened, and then hope it doesn't reappear in my dreams."

    ## Scene 6
    ##Mansion bg
    scene bg mansion
    with fadee

    ##COMMON EVENT: The fifth site they go to is another old mansion near the university. 
    show zaina unsure frown:
        xalign 0.85
        yalign -1.5
    show paxton unsure frown:
        xalign 0.55
        yalign 1.0
    show alex down smile:
        xalign 0.33
        yalign 1.0
    with dissolve

    z unsure frown "..."

    p unsure frown "..."

    z down frowntalk "No way. I think I'd remember something so awkward."
    show zaina frown

    p up talk "Go through the logs, I swear you uploaded a weird Halloween selfie. It looked like a goose face or whatever it's called."
    show paxton smile

    z unsure talk "Why would I do something like that?!"

    z up talk "Alex! Tell Paxton he's imagining things."
    show zaina frown

    a unsure talk sweat "Oops, sorry, I zoned out. What's going on?"
    show alex smile -sweat

    p unsure talk "Zaina doesn't remember when she uploaded some blurry Halloween selfie to the group chat."
    show paxton smile

    z down frowntalk "Yeah, cause it {i}didn't happen.{/i}"
    show zaina frown

    p up talk "Pics or it didn't happen, huh? I bet I can find it."
    show paxton smile

    a unsure talk "Halloween selfie? Zaina, you like to dress up?"
    show alex smile

    z unsure frowntalk sweat "What? N-no, of course not. I used to get bored, that's all."
    show zaina frown

    an up "Cute...!"

    a up talk "Haha, I'd love to see it some day. Honestly, I'd follow any picture account you had!"
    show alex smile

    show zaina -sweat
    z up talk "Right. T-thanks. Uh, anyway, where in the world is Finn?"
    show zaina smile

    ##Screen shake
    an "The main doors to the mansion bang before slowly opening up. Once again, the devil somehow knows my thoughts." with vpunch

    ##Finn sprite appears
    show finn up smile:
        xalign 0.05
        yalign 1.0
    with dissolve

    an "Finn's there, brushing dust off his hands and ... incredibly late."

    z down frowntalk "You were supposed to be here almost 30 minutes ago, Finn. Jeez."
    show zaina frown

    f unsure talk "Sorry."
    show finn frown

    p unsure talk "Did you get lost?"
    show paxton smile

    f unsure talk "Nah."
    show finn smile

    a unsure talk "Well, what happened?"
    show alex smile

    f up talk "The oven took much longer than I thought to clean. Had to wait."
    show finn smile

    show zaina unsure frown
    show paxton unsure frown
    show alex unsure frown

    z "..."

    p "..."

    a "..."

    f up talk "Thanks for waiting. Let's go."
    show finn smile

    a up talk "Good idea."
    show alex smile

    hide alex
    hide paxton
    hide finn
    hide zaina
    with dissolve

    an "He shoots me a smile, completely oblivious to the death glare Zaina is shooting him."

    an "The place is so old that there's no avoiding the draft. It's like a chill is purposely wired through, ugh."

    show finn up smile:
        xalign 0.05
        yalign 1.0
    show zaina unsure smile:
        xalign 0.85
        yalign -1.5
    show paxton unsure smile:
        xalign 0.55
        yalign 1.0
    show alex unsure smile:
        xalign 0.33
        yalign 1.0
    with dissolve

    p unsure talk "Looks like we weren't the first ones here, look at this graffiti."
    show paxton smile

    f unsure talk "Well, this {i}is{/i} near the university."
    show finn smile

    z unsure talk "It's so dusty, you'd think this place was really remote."
    show zaina smile

    hide paxton
    hide zaina
    with dissolve

    an "I'm trying to look around, but it's hard to concentrate."

    f down talk "Alex. Psst."
    show finn smile

    a up frowntalk "Huh? Why are we whispering?"
    show alex smile

    hide finn with dissolve

    an "He waves me over without explanation, pointing at the sturdiest-looking stairs I've seen thus far. We go up..."

    hide alex
    scene black
    with dissolve

    ##Black screen/sprites disappear with shakes to indicate stepping
    a "Finn?"

    f "Don't worry, it's sturdy."

    a "How can you even tell?!"

    f "There was no sagging on the wood and there are support beams under the stairs."

    a "Oh, really?"

    f "We're here."

    ##Sprites reappear
    scene cg finn rooftop
    with dissolve

    #show bg mansion
    #show alex up at closeright:
    #    yalign -0.25
    #show finn smile at closeleft
    #with dissolve

    a "Oh, wow, it's the roof..."

    an "We look out over the roof, still beautiful even though it has holes."

    f "Gotta be careful with roofs, they're usually some of the first parts to go. You look and feel for cracks and holes. Leaks are a dead giveaway of damage."

    a "Huh... noted. You're always giving me good advice, Finn."

    f "Mhm... Hey, are you cold?"

    a "Oh—it's fine."

    f "It's not."

    ##I rewrote this cause I forgot the Finn rooftop CG was promo art and not part of the game but it'd be a cute concept here ajdsosia

    a "Finn? I'm okay, really."

    f "Just take it."

    an "He drapes his jacket gently over my shoulders and I exhale once I feel how much warmer it is. It even smells like Finn, which shouldn't be a surprise but it still makes me feel... strange."

    ##choice
    menu:
        "But what about you?":
            f "What about me?"
            a "I mean, aren't you cold?"
            f "Nah, I'm fine. Doesn't matter."
            an "Why wouldn't that matter, Finn...?"
            an "I can't bring myself to argue with him when he looks at me like that. Instead, my head focuses on disagreeing with the butterflies in my chest."
            ##end choice

        "(Put hands in pockets)":
            a "Huh...? What's a carrot doing in here?"
            f "Hm. That's a good question."
            a "Do you like eating raw carrots as a snack?"
            f "Not particularly."
            an "What kind of answer is that?!"
            f "Do you want it?"
            a "I don't!"
            f "If you want it, you can."
            a "I'm telling you I don't!"
            an "Finn chuckles and moves to pat my head but I gently swat him away, which seems to only amuse him more."
            ##end choice

        "Your jacket smells nice.":
            f "Yeah? And what does it smell like?"
            a "Um, I guess like you? It's hard to describe."
            f "You saying I smell good?"
            a "U-um..."
            an "I wish he'd stop teasing me before I say something I'll regret!"
            f "Stop getting so nervous around me or I'll start thinking you like me."
            a "I'm not nervous."
            f "Good."
            an "Jeez..."
            ##end choice

    scene black
    with dissolve

    an "An excited shout from Paxton draws our attention."

    an "We hurriedly return from the roof with Finn leading the way. In a way, I'm glad for it. I don't want him to notice how cozy I feel in his jacket."

    ##Mansion bg
    scene bg mansion
    with fadee

    show finn up smile:
        xalign 0.05
        yalign 1.0
    show zaina up smile:
        xalign 0.85
        yalign -1.5
    show paxton up smile:
        xalign 0.55
        yalign 1.0
    show alex up smile:
        xalign 0.33
        yalign 1.0
    with dissolve

    p up talk "Wow, there's a bunch of books hidden here in the sofa!"
    show paxton smile

    f unsure talk "Hah. Gross."
    show finn smile

    z down talk "Hold on, I'll take some pictures."
    show zaina smile

    a down talk "Oh—uh, that plank you put your tripod on looks like it's sagging...?"
    show alex smile

    z up talk "Whoa! Thanks, that could've been bad."
    show zaina smile

    show alex up smile
    show finn up smile
    show paxton up smile

    ##Finn smiling
    f "..."

    z up talk "There we go. Perfect."
    show zaina smile

    p unsure talk "At least we found something."
    show paxton smile

    a unsure talk "Why did you look in the sofa anyway?"
    show alex smile

    p down talk "Uh... I ran out of options. I would love some soap and a sink now, though."
    show paxton smile

    f unsure talk "Yeah, I think we're done here. Let's go."
    show finn smile

    ##Zaina and Paxton should be smiling
    z up talk "Yup, let's pack it up."
    show zaina smile

    p up talk "Right behind you."
    show paxton smile

    ##Zaina and Paxton sprite exit, Finn expression serious
    hide zaina
    hide paxton
    with dissolve

    f down talk "... Alex."
    show finn frown

    a unsure talk "Yes?"
    show alex smile

    f unsure talk "Can you go on a walk with me? Please?"
    show finn frown

    a up talk "Oh, sure."
    show alex smile

    hide finn
    hide alex
    with dissolve

    ## Scene 7
    ##Outside campus bg ?
    scene bg outside_campus
    with fadee

    an "I'm not sure why Finn asked me to walk with him, but I like the excuse to stay nice and warm under his jacket. He looks so serious, I wish I knew what to say."

    an "This crush is getting out of control..."

    show alex up at closeright:
        yalign -0.25
    show finn smile at closeleft
    with dissolve

    a unsure talk "Finn? Are you alright?"
    show alex smile

    f down frowntalk "... Not really."
    show finn frown

    a down frowntalk "What's wrong?"
    show alex frown

    f unsure talk "Eh, this is awkward, but..."

    f up talk "You know I care about you, right?"
    show finn frown

    a up frowntalk "And I care about you but what's this about?"
    show alex frown

    f down frowntalk "I, uh, I feel like if we're going to keep doing all this dangerous stuff together that I should be upfront about something. Paxton and Zaina already know, but..."
    show finn frown

    a unsure frowntalk "A-are you sick?"
    show alex frown

    an "My stomach flips. I wasn't expecting this at all, but if Finn wants to open up to me I would never complain about it."

    f unsure frowntalk "A bit. Is it okay if I tell you something... heavy?"
    show finn frown

    ##choice
    menu:
        "Yes, that's fine.":
            show finn unsure smile
            an "He gives a faint smile at my response and gently lifts a side of my lips with a teasing finger."
            f down talk "Don't frown too much, it makes it harder."
            show finn smile
            a up talk "I'm just trying to take you seriously."
            show alex frown
            an "He chuckles at that."
            f talk "I know... thank you."
            show finn down frown
            an "Finn finally gets serious again and takes a deep breath before starting."
            ##end choice

        "If you have to.":
            an "Finn hesitates after my response and sighs."
            f talk "I feel like I do. I guess I feel close enough to you to talk about it."
            f talk "Um... anyway..."
            show finn smile
            an "Finn takes a deep breath before starting."
            ##end choice

        "I'm freaking out a bit.":
            an "I didn't mean to, but I know my words wound him when he seems to flinch."
            f down frowntalk "That's the last thing I want to do... I promise I'll keep it short."
            show finn frown
            a unsure frowntalk "Alright."
            show alex frown
            an "Finn nods, then takes a deep breath before starting."
            ##end choice

    f unsure frowntalk "Before I came here, I wasn't in a good place mentally."

    f down frowntalk "I was lost, depressed, and... suicidal. My boyfriend of many years and I broke up right before I moved here on top of it."
    show finn frown

    a down frowntalk "I'm so sorry, Finn..."
    show alex frown

    f unsure frowntalk "And the thing is—I still am all of those things. I manage a lot better these days but that's all it is... managing."
    show finn down frown

    an "He pauses after his confession. I can see in his eyes that his thoughts on the matter are bittersweet. They see something that I can't."

    an "But he doesn't linger. Finn looks directly at me—maybe even through me—and I know that he sees everything as it is now in the present."

    a unsure talk "I'm here for you, Finn."
    show alex frown

    f up talk "I know you are. And that means the world to me because... I like you."
    show finn smile

    ##Finn smiling, Alex shocked
    show alex blush with Dissolve(1.0)
    a up shock "W-what? I mean, I like you too..."

    an "Where is this coming from? For a moment there I thought he was saying something else."

    f up talk "As more than a friend. And I'm happy that I {i}can{/i} like you, because I was so sure that part of me was broken, Alex."
    show finn smile

    an -blush "My brain feels like it's short-circuiting. I'm so thrown off that the first thing out of my mouth is a diversion from admitting that a confession even happened."

    a unsure frowntalk "W-wow, was your ex... not a good person?"
    show alex smile

    show finn unsure
    an "He shakes his head at that and gives a self-deprecating laugh that breaks my heart."

    f unsure talk "No, it wasn't like that. I was in a very bad place at that time and my ex couldn't deal with it. It wasn't his fault and I'd never want to drag someone down with me." 

    f down frowntalk "Especially someone I cared so much about."
    show finn frown

    a unsure frowntalk "But..."
    show alex frown

    f up talk "He left for his own sanity, which was for the best. I'd never blame him for leaving no matter how much it hurt me."

    f unsure talk "Um—will you come in?"
    show finn smile

    a up talk "Oh, y-yes."
    show alex smile

    hide alex
    hide finn
    scene black
    with dissolve

    an "I know I should say something about his confession but my heart is pounding so much that I can't think clearly."

    an "He just told me something so personal and then told me he liked me? What am I supposed to do here?!"

    ## Scene 8
    ##Finn's room bg
    scene bg finn_room
    with fadee

    show alex up smile at closeright:
        yalign -0.25
    show finn up smile at closeleft
    with dissolve

    ##Both surprised
    a up frowntalk "Wha-?"
    show alex frown

    f down frowntalk "... Shit!"
    show finn frown

    a up shock "Eek!"

    an "When we enter, there's some sort of animal darting around Finn's room."

    a unsure "What {i}is{/i} that?!"

    f unsure frowntalk "Ah, close the door will you? It's alright."
    show finn frown

    hide finn with dissolve

    an unsure frown "I do as he says but why is he so calm? He runs to the kitchen and returns with a carrot, which doesn't make the situation any less bizarre."

    show finn at closeleft
    with dissolve

    f down talk "Come here, Cerberus... Ah, you made a mess."
    show finn frown

    an "The running animal leaps into Finn's outstretched arms..."

    hide alex
    hide finn
    with dissolve

    ##EVENT IMAGE: FINN HOLDING THE RABBIT
    scene cg finn rabbit
    with dissolve

    an "... and it's the most adorable rabbit I've ever seen."

    an "I stare in awe at the purring bunny that so clearly knows Finn... and looks like him too. I can't believe it has built-in eyeliner!"

    a "You have a pet bunny...?"

    f "Huh? No. Er—I mean, Cerberus von Fluffykins must have escaped. He's not really a pet."

    "Cerberus" "{i}Churrr.{/i}"

    an "Cerberus von... Fluffykins? Finn definitely named it and it's definitely his!"

    f "I'm just—he's just—I saved him, nursing him back to health."

    a "He looks pretty healthy to me..."

    f "Well, I'm just making sure. It's not a big deal, he's not... anyway, Alex, you'll keep this a secret, right?"

    a "Right, animals are against dorm rules. Of course I will."

    f "Thank you..."

    an "Finn continues feeding Cerberus, the softest expression I've seen on him in a long time. Cerberus looks so comfortable in his arms."

    an "He's sincere when he wants to be. His actions tell me how he feels all the time now that I think about it."

    an "... Finn's been honest with me, and I should do the same."

    ##Back to sprites by now so they can b l u s h
    ##Blushing Alex

    scene bg finn_room
    with fadee

    show alex unsure smile blush at closeright:
        yalign -0.25
    show finn unsure smile at closeleft
    with dissolve

    a up talk "Finn—I like you too."
    show alex smile

    ##Surprised Finn
    show finn up sweat with Dissolve(1.0)

    an "I guess we didn't know how the other felt after all. Finn looks at me in shock and it only makes me regret not saying anything. Cerberus jumps out of his arms, the movement seeming to bring him back to his senses."

    f unsure talk "You... do?"
    show finn smile

    a down talk "I'm sorry I didn't say so earlier. I think I've liked you for awhile and I, uh, honestly, would really like to learn more about you."
    show alex smile
    show finn -sweat

    ##Blushing Finn
    show finn blush with Dissolve(1.0)

    f up talk "Oh..."
    show finn smile

    a "..."

    f "..."

    a unsure talk -blush "Uh, so what now?"
    show alex smile

    f down frown -blush "Mm..."

    f unsure talk "How about you stay the night?"
    show finn smile

    a up shock sweat "Wha-?"

    f down frowntalk "I-I mean just... to talk."
    show finn smile

    show alex -sweat
    a unsure talk "You're going to give me a heart attack."
    show alex smile

    f up talk "Ha ha... why, disappointed?"
    show finn smile

    a down frowntalk "You're teasing me when I'm being serious!"
    show alex frown

    f talk "What, I can't tease my future girlfriend?"

    show alex blush with Dissolve(1.0)
    a up shock "Girlfriend?"

    show finn down frown
    an unsure frown "Finn's teasing smirk disappears as he leans closer, looking at me with a completely earnest expression."

    f unsure frowntalk "Alex..."
    show finn frown

    an "He gently takes my hands in his and lifts them to his cheeks."

    a up shock -blush "You're burning up, Finn!"

    f up talk "I just wanted you to know how serious I am right now. Even though I'm always teasing you and messing with you..."

    f unsure talk "Will you go out with me? You can say no of course but..."
    show finn frown

    ##Move sprite closer
    show alex unsure frown at closeright:
        yalign -0.15
        zoom 1.2
    show finn unsure frowntalk at closeleft:
        zoom 1.2
    with dissolve

    f unsure talk "I'd prefer if you didn't. I know I'm far from perfect but I'd really like to... try. With you."
    show finn smile 

    an smile "When I look back into Finn's blue eyes, I can see that I'm smiling. It's like they're the ocean waters themselves and reflecting a calm back into my heart."

    an "It's a calm that makes it as easy as breathing to respond, all my troubles bobbing away on those ocean waves."

    a up talk "How can I possibly say no?"
    show alex smile

    hide alex
    hide finn
    scene black
    with Dissolve(2.0)

    ##Maybe a screen fade to show a passage of time
    #show bg finn_room
    #show alex up smile at closeright:
    #    yalign -0.25
    #show finn up smile at closeleft
    #with Dissolve(4.0)

    an "After playing with Cerberus for a while, we ended up in his bed without talking about anything specific. The weather, classes, our adventures... all of those things that seemed so ordinary now feel so precious."

    an "To think this all started because I wanted to escape my parents and do something new."

    a talk "Finn... are you awake?"

    f talk "..."

    a talk "I guess not, haha. Goodnight..."

    an "I don't really know if this is too sudden or fleeting but... I like Finn. It's nice to feel wanted, to have fun, to have friends, to have a boyfriend."

    an "Maybe my parents wouldn't approve of a trespassing vampire boyfriend but..."

    a talk "I don't care, do I?"

    f talk "... lex..."

    a talk "Finn?"

    f talk "Alex..."

    ##Alex blushing
    an"He's sleeptalking...? Haha." 

    a talk "Goodnight, Finn. Goodnight, Cerberus von Fluffykins."

    "Cerberus" "Churr..."

    an "With that, I feel myself drifting off, my hand warm in Finn's. I've never felt so relaxed and so... happy."

    ##Scene 9
    ##hospital bg
    scene bg hospital
    with fadee

    ##COMMON EVENT: The sixth site they go to is a sanitorium, ie where people used to go for treatment of tuberculosis

    an "The next place we go to is a bit more dangerous. The abandoned sanitorium looks like it'll collapse at any time and we're walking slowly up the stairs but..."

    show finn up smile:
        xalign 0.05
        yalign 1.0
    show zaina up smile:
        xalign 0.85
        yalign -1.5
    show paxton up frown:
        xalign 0.55
        yalign 1.0
    show alex up smile:
        xalign 0.33
        yalign 1.0
    with dissolve

    p unsure frowntalk "Alright. I'm done, I can't."
    show paxton frown

    a unsure frowntalk "Paxton?"
    show alex frown

    p up talk "I mean, y-you all can keep going if you want. If anything happens, it'll be good to have someone standby, right? You can count on me!"
    show paxton smile

    f unsure talk "If you say so."
    show finn smile

    z unsure frowntalk "If something looks dangerous, you can definitely give your opinion, you know."
    show zaina frown

    p unsure frowntalk "Y-yeah, sorry."
    show paxton smile

    a up talk "It's alright, we'll see you soon Paxton. Stay safe."
    show alex smile

    z up talk "Yell if you need us. Or maybe not, I'm scared it'll collapse the whole place."
    show zaina smile

    p down frowntalk "Not helping."
    show paxton frown

    f up talk "Let's keep moving."
    show finn smile

    hide finn
    hide paxton
    hide zaina
    hide alex
    with dissolve

    an "The next flight of stairs is worse than the last. Every plank looks unstable, like the air itself weighs too much and creaks before we even walk."

    show finn up smile:
        xalign 0.05
        yalign 1.0
    show zaina down frown:
        xalign 0.85
        yalign -1.5
    show alex up smile:
        xalign 0.40
        yalign 1.0
    with dissolve

    z unsure frowntalk "I think this is where I stop, too. I can't risk me {i}or{/i} my camera."
    show zaina frown

    f unsure talk "Are you sure? There's not much left, Zaina. The top looks so promising!"
    show finn smile

    a unsure talk "You're awfully excited about this."
    show alex smile

    an "He never looks worried about the danger. After knowing his history, it's a bit more concerning."

    f up talk "Of course I am."
    show finn smile

    z down frowntalk "Don't drag Alex into your nonsense. Come on guys, let's stop here."
    show zaina frown

    f down talk "No way."
    show finn smile

    a up talk "It's okay, I'll look out for him."
    show alex smile

    z unsure talk "Alex... Ugh, fine, if you insist. If you two lovebirds die I'm going to kill you."
    show zaina smile

    show alex blush with Dissolve(1.0)
    a up talk "L-lovebirds?"
    show alex smile

    hide zaina
    with dissolve

    an "She doesn't respond, simply rolls her eyes and waves us off. Are we really that obvious?"

    f talk "See ya."
    show finn smile

    hide alex
    hide finn
    with dissolve

    scene black
    with dissolve

    an "I'm trying to copy Finn's steps as much as I can. Skip that plank, careful and gentle steps on-!"

    #Screen shake?
    a talk "Ah!" with vpunch

    f talk "Alex!"

    scene bg sanitorium
    with fadee

    show alex unsure frown at closeright:
        yalign -0.25
    show finn unsure frown at closeleft
    with dissolve

    an "Finn rushes to catch me right after a step gives under."

    a down frowntalk "Owww..."
    show alex frown

    f down frowntalk "Alex! Alex, are you okay?"
    show finn frown

    an "He sits me down part way up the stairs and I realize I can't breathe, I can't even speak!"

    f unsure talk "It's okay, just relax. I'm here."
    show finn smile

    a down smile "..."

    an "Finn pats my head affectionately, letting his fingers thread through my hair until I finally feel my lungs working again."

    a unsure talk "That—{i}scared{/i} me."
    show alex smile

    f up frowntalk "I know..."
    show finn frown

    an "He gently pulls my leg on top of his, inspecting it."

    a down frowntalk "Oh, ow..."
    show alex frown

    f unsure frowntalk "You scraped your leg."
    show finn frown

    a unsure talk "I don't feel so good. Did I almost die?"
    show alex frown

    f up talk "Nah, of course not. I've already broken fingers doing this stuff. A scrape is nothing, you're lucky."
    show finn smile

    a up shock "Broken {i}fingers{/i}?!"

    f unsure talk "Sure, but I've broken more than that outside of adventuring."

    f down talk "When I was at the height of my depression, I'm sure I broke my arm, my leg...I failed a lot, so nothing {i}quite{/i} was enough to kill me."
    show finn smile

    an frown "What—what is he saying to me right now? And so casually? It's like he doesn't even care about his suicide attempts!"

    a unsure frowntalk "Is that... supposed to make me feel better?"
    show alex frown

    f unsure talk "Yes. Is it working?"
    show finn smile

    a down shock "No, Finn! It's not working! You're doing an awful job!"

    f down talk "Haha... I'm sorry."
    show finn frown

    an frown "And he's just laughing it off..."

    f unsure frowntalk "Let's go back down, I think that's enough for tonight."
    show finn frown

    a unsure frowntalk "Yeah... I think so."
    show alex frown

    scene black
    with dissolve

    an "We retrace our steps and meet up with Zaina and Paxton back on the first floor. No one is very enthused when they see me limping."

    scene bg sanitorium
    with fadee

    show finn down frown:
        xalign 0.05
        yalign 1.0
    show zaina down frown:
        xalign 0.85
        yalign -1.5
    show paxton down frown:
        xalign 0.55
        yalign 1.0
    show alex down frown:
        xalign 0.33
        yalign 1.0
    with dissolve

    z unsure frowntalk "Alex! What happened?!"
    show zaina frown

    p down frowntalk "You're bleeding!"
    show paxton frown

    z down frowntalk "Finnnnn..."
    show zaina frown

    an unsure "Uh oh, Zaina looks pretty mad...!"

    f up frowntalk "She's alright, it's just a scrape."
    show finn frown

    a down frowntalk "Yeah, I'm alright, it just stings a bit."
    show alex frown

    p unsure frowntalk "That's not the point..."
    show paxton frown

    z down frowntalk "Exactly. Finn, you're the one with experience, this is {i}your{/i} fault. I told you not to keep going and look what happened!"
    show zaina frown

    f unsure frown "..."

    p down frowntalk "We really need to treat that to make sure you don't get infected, Alex."
    show paxton frown

    a unsure frowntalk "Oh—yes, we should."
    show alex frown

    z unsure frowntalk "Right. Let's go, we don't have time to talk about this."
    show zaina frown

    ##Paxton and Zaina sprites disappear
    hide paxton
    hide zaina
    with dissolve

    ##choice
    menu:
        "They were pretty harsh.":
            f down frowntalk "... Nah."
            show finn frown
            a up frowntalk "They were! Zaina didn't need to talk to you like that."
            show alex frown
            f unsure frowntalk "Maybe..."
            show finn frown
            a unsure frowntalk "Should I talk to them about it?"
            show alex frown
            ##end choice
        "They're right, you know.":
            f down frowntalk "... I know."
            show finn frown
            a frowntalk "We should both be careful, not just you."
            f unsure frowntalk "Maybe."
            show finn frown
            a frowntalk "...Finn?"
            ##end choice
        "It's not your fault.":
            a frowntalk "Sorry that you got most of the blame, Finn... it really wasn't your fault."
            show alex frown
            f down frowntalk "... t'was."
            show finn frown
            a frowntalk "No, I decided to go with you, remember? You didn't force me."
            show alex frown
            f unsure frown "..."
            a frowntalk "Finn?"
            show alex frown
            ##end choice

    f down frowntalk "Let's just go..."
    show finn frown

    hide finn
    hide alex
    with dissolve

    scene black
    with dissolve

    an "It's an awkward time back. I get patched up by Zaina and offer to walk Finn back to his dorm, but he denies me."

    an "No matter what I do, Finn doesn't talk to me. With a hurt leg, I go back to my dorm to sleep..."

    an "It's not supposed to be a long walk, but each step is more painful than the last. Scratchy echoes suggest something else's staggering footsteps are behind me, even though I know I'm alone. There's only my shadow, limping behind me like a hunting monster under glowing street lamps and a gray sky."

    ##Scene 10
    ##Alex room bg or starting with a black screen if there's no night version
    scene bg alex_room_night
    with fadee

    ##Vibration/screen shake for phone
    "Bzz..." with vpunch

    a "Ugh... what time is it? Why is my phone vibrating?"

    a "..."

    a "Finn?"

    an "Why is he vague-texting me at midnight?"

    a "Do I want to meet him for another trespass? Just the two of us? {i}Now?{/i}"

    an "It's kind of like... an illegal date. Can't say I've ever done that before. Well, my leg is better but..."

    a "How... safe... is... it?"

    ##Phone vibration
    show bg alex_room_night
    with vpunch

    a "Not too old of a building, huh? Hmm..."

    an "I haven't seen him much outside of class after last time. I miss him."

    a "Alright... I'll get... ready and... meet you... there."

    ##Phone vibration
    show bg alex_room_night
    with vpunch

    a "Hehe... I... miss you... too."

    ##Scene 11
    ##Mansion bg
    scene bg mansion
    with fadee

    ##Alex happy/excited and Finn serious, keep their sprites separate

    an "There he is! Finn!"

    an "He's already picking the lock to get us in. I didn't know he could do that! I shouldn't be as impressed as I am, I'm pretty sure that's super illegal. Oh well... I'm too happy to see him again to really care right now."

    show alex up smile at closeright:
        yalign -0.25
    with dissolve

    a talk "Finn!"

    show finn up frown at closeleft
    with dissolve

    f unsure frowntalk "Hey."
    show finn frown

    an unsure "Huh? Just a 'hey'?"

    a up frowntalk sweat "It's great to see you again."
    show alex smile

    f down frowntalk "Yeah."
    show finn frown

    an unsure "?!"

    a unsure frowntalk "It's, uh, a nice mansion."
    show alex frown

    f unsure "..."

    an down -sweat "Grr..."

    ##Finn smiling 
    f up talk "Got it."
    show finn smile

    an "The lock snaps and Finn finally turns to face me, a damning smile on his face."

    ##Finn's sprite moves closer
    show finn up:
        xalign 0.20
    with dissolve
    f up talk "Alex."
    show finn smile

    ##Alex blushing and her sprite moves away
    show alex blush unsure:
        xalign 0.98
        zoom 1.3
        yalign -0.25
    with dissolve
    a unsure shock "W-what?"

    ##Finn's sprite moves close to her again
    show finn:
        xalign 0.30
    with dissolve
    f down talk "I'm really glad you came."
    show finn smile

    a up talk sweat "Oh... really?"
    show alex smile

    f up frowntalk "I missed you. A lot. I was losing it, I even forgot to put on my eyeliner yesterday."
    show finn frown

    a unsure talk -sweat "I-is that so?"
    show alex smile

    f down talk "Mhmm..."
    show finn smile

    an "He laces his fingers through mine and brings my hand to his lips for a gentle kiss that's far more princely than it has any right to be."

    a up shock "Wha..."

    f unsure talk "Wanna hold hands?"
    show finn smile

    an frown sweat "{i}I'm{/i} the one losing my mind! He's unbearably handsome with the way he's looking at me. I feel like a teenager right now..."

    a unsure talk "S-sure."
    show alex smile

    f up talk "Let's go."
    show finn smile

    hide alex
    hide finn
    with dissolve

    an "We walk inside and he was right, the first floor is incredibly stable. The mansion couldn't have been abandoned too long ago, even the mildew isn't that strong."

    an "Finn leads me around the place as my loving guide who won't let go of my hand even when it's inconvenient."

    show alex up smile -blush at closeright:
        yalign -0.25
    show finn up smile at closeleft
    with dissolve

    f down talk "It's said this place was passed down generation-by-generation, only forfeited by delinquent grandchildren who spent all the inheritance and went into unspeakable debt."
    show finn smile

    a unsure talk "That sounds like the set-up of a crime drama show."
    show alex smile

    f up talk "Heh. Then I guess you'll be pleased to know the family was full of wine tycoons."
    show finn smile

    a up talk "Ooh, scandalous."
    show alex smile

    f down talk "Very. There are rumors there were even punishments carried out in this very building to those who fell out of their favor."
    show finn smile

    a unsure talk "Like..."
    show alex smile

    an "I make a gesture, dragging my thumb across my neck and Finn laughs."

    f up talk "More like..."
    show finn smile

    an "His fingers move to the side of my neck before tickling it, his flirty smile contagious if I wasn't already laughing."

    a up shock "H-hey! Stop that before I tickle you back."

    f unsure talk "Oh yeah? Try it."
    show finn smile

    a unsure talk "I warned you!"
    show alex smile

    an "I move to carry out my threat but Finn snatches my free hand in his, pulling me forward into his chest."

    a down frowntalk "That's cheating!"
    show alex frown

    f up talk "Telling me I'm cheating is like admitting I won."
    show finn smile

    a up frowntalk "It is not. I'm simply recognizing your abhorrent conduct."
    show alex frown

    f unsure talk "Uh huh. Since I won, can I have my prize now?"
    show finn smile

    a unsure talk "Since when was this a competition? What prize?"
    show alex smile

    f up talk "My kiss. What, not going to give me one?"
    show finn smile

    a up shock "You...!"

    an smile "Alright, so maybe he has won because there's nothing more I want right now other than to kiss him."

    an "He smirks down at me but I give into it, leaning up and planting a soft kiss to his lips."

    ##Finn blushing
    f smile blush "..."

    a unsure talk "You're blushing after all that smack talk?"
    show alex smile

    f unsure talk "I am not. A-anyway, I should show you... more."
    show finn smile

    a up talk "Hehe yeah... do you think there's a wine cellar here?"
    show alex smile

    f down talk -blush "Good point. Let's start with the basement."
    show finn smile

    an "Finn takes me to the basement, testing out the stairs and staying ahead of me. When we make it down, it's hard to see anything at all in the darkness. I'm glad for flashlights."

    a unsure frowntalk "This place is..."
    show alex smile

    f up talk "... so cool."
    show finn smile

    a up talk "Pfft."
    show alex smile

    f unsure frowntalk "What?"
    show finn frown

    a down talk "Of course you'd like it. Do you want to live in a dark and brooding vampire mansion like this?"
    show alex smile

    f up talk "Ha. That's a bit much but..."
    show finn smile

    a unsure talk "But what?"
    show alex smile

    f down talk "Hm. I wouldn't mind if it was with you."
    show finn smile

    a up talk "Hehe..."
    show alex smile

    f unsure talk "Huh, there's still a few bottles here."
    show finn smile

    a up shock "Ah! Take a picture."
    show alex smile

    f up talk "Haha. How about I hold it and you take the shot?"
    show finn smile

    a unsure talk "Sure."
    show alex smile

    an "Finn gingerly takes one of the dusty bottles off the rack and tilts it back, miming chugging."

    a up talk "These are going to come out so good."
    show alex smile

    f unsure talk "Nice. Shall I pour you a glass of our finest chardonnay, ma'am?"
    show finn smile

    an "Finn grins at me as he takes on a terrible impersonation of an aristocratic butler."

    a down frowntalk "Absolutely not, sir. Your moldy wine does not suit my palate."
    show alex smile

    f down talk "Apologies for my insolence."
    show finn smile

    an "He returns the bottle so I can take one more picture and we go back to the first floor, still laughing and still holding hands."

    f unsure talk "Next floor?"
    show finn smile

    a up talk "Sure!"
    show alex smile

    f down talk "I think there should be bedrooms there..."
    show finn smile

    a unsure talk "Finn... you've really researched this place, huh?"
    show alex smile

    f unsure talk "Hm? Not more than usual."
    show finn smile

    ##choice
    menu:
        "How much is usual?":
            f down talk "Uh, well, I usually read up on the history of wherever we're going and the surrounding places."
            show finn smile
            a up shock "What? But you've never said this much before when we've been out!"
            f unsure talk "Yeah... cause no one asked."
            show finn smile
            a down talk "Well, I didn't ask cause I didn't know."
            show alex smile
            f up talk "Fair enough."
            show finn smile
            a unsure talk "You'll have to tell me everything from now on, okay?"
            show alex smile
            f unsure talk "Sure, if you want."
            show finn smile
            a up talk "And I bet Zaina and Paxton would love to know, too."
            show alex smile
            f down talk "Maybe."
            show finn smile
            a down frowntalk "You say 'maybe' but you never even mentioned it to them...?"
            show alex frown
            f unsure talk "I think I tried, once."
            show finn smile
            a unsure frowntalk "Really? Did something happen?"
            show alex frown
            f down talk "Yeah, it never sent. Think my connection went out."
            show finn smile
            a down smile "..."
            #Screen buzz/shake
            f up talk "Haha! Ow, ow, don't pinch me! I'm kidding!"
            show finn smile
            ##end choice
        "You're a history buff?":
            f down talk "Nah. I just like to know what I'm getting into."
            show finn smile
            a down talk "I'm not sure half of the stuff you told me tonight was relevant for exploring."
            show alex smile
            f up talk "Sure it was. You thought of the wine cellar 'cause of my research and I know how not to anger the ghosts now."
            show finn smile
            a up shock sweat "What...? Ghosts?"
            f unsure talk "Mhmm. Just don't touch the wine and we'll be fine."
            show finn smile
            a unsure froiwntalk "... We {i}did{/i} touch the wine!"
            show alex smile
            f up talk "Oh, really? Guess we're cursed now."
            show finn smile
            a down talk -sweat "Just you, goofball."
            show alex smile
            an "I can't keep a straight face around him..."
            ##end choice
        "The wine tycoons are common knowledge?":
            f down talk "I don't know? The local history books mentioned them often, though."
            show finn smile
            a up talk "You seriously go to the library for this?"
            show alex smile
            f unsure talk "What about it?"
            show finn smile
            a down talk "Nothing, it's cool. Although it does sound like it leaves an incriminating trail."
            show alex smile
            f up talk "That's assuming I check the books out."
            show finn smile
            a unsure talk "A-are you stealing library books?!"
            show alex smile
            an "Finn laughs and messes with my hair."
            f down talk "I'm a criminal but I have standards, I'd never steal from a library."
            show finn smile
            a up talk "Right."
            show alex smile
            f up talk "Just my neighbor. He doesn't use his card anyway."
            show finn smile
            a down talk "Dastardly!"
            show alex smile
            an "We both laugh and I can't help but wonder what his neighbor is like."
            ##end choice

    an "Finn eagerly leads me up the stairs. It's not as stable-looking as the first floor but there's not much to see either."

    f unsure frowntalk "Seems they didn't use the bedrooms much."
    show finn smile

    a unsure frowntalk "Hmm... do you say that because of the doors?"
    show alex smile

    f up talk "So you noticed them, too. Yeah, the doorknobs aren't as worn as the first floor's. I guess the kids didn't really stay here."
    show finn smile

    a down frowntalk "I wonder why..."
    show alex smile

    an "We go to the third floor, but it's even worse than the second. Noticeably so. I hesitate when we arrive and Finn lets go of my hand so easily that it kind of hurts."

    f up frowntalk "Take your time and be careful. I'll go first."
    show finn frown

    a unsure frowntalk "Alright... you too."
    show alex frown

    an "Finn doesn't agree to my request but I slowly walk along the edges of the floor behind him. Maybe it's my fear, but we sure feel far up now."

    an "A small drop calls my attention and I freeze, looking up to the roof. It's not leaking in one spot, but several."

    a unsure frowntalk "Finn...?"
    show alex frown

    f unsure talk "Want to go up to the roof as our last stop?"
    show finn smile

    a down frowntalk sweat "The r-roof? Finn, look up, it has a bunch of leaks."
    show alex smile

    an "Finn peers around the roof for a moment, but my stomach flips when he doesn't look deterred in the least."

    f up frowntalk "We can just go to the widow's walk. It's leaking but otherwise it looks like it's held up pretty well."
    show finn smile

    a unsure frowntalk -sweat "I really don't feel safe."
    show alex frown

    an "As if on cue, I feel a distant sting in my leg reminiscent of another time I was unsure."

    f unsure talk "Are you sure? It's probably fine. The view is going to be amazing, I really wanted to see it with you."
    show finn smile

    a down frowntalk "... I'm sorry, I can't. I have a really bad feeling about this."
    show alex frown

    f down frowntalk "Mm... alright. Well, I'll go first and make sure it's safe. Okay?"
    show finn frown

    a unsure shock "That doesn't sound like a good idea either!"
    show alex frown

    f unsure frowntalk "Just stay here, will you? I'll go check for us."
    show finn frown

    a down frowntalk "Finn...?"
    show alex frown

    an "It's pointless trying to talk him out of it. My protests become white noise to Finn's curiosity, as forgotten as the spiderwebs that do nothing to deter him."

    an "Cautiously, I follow and watch him go up to the widow's walk, praying nothing happens. From the bottom of the steps, I can see his legs carefully shifting around."

    f up talk "It's beautiful up here..."
    show finn smile

    a up talk "I'm sure it is."
    show alex smile

    f unsure talk "I'm going to get a bit closer, hold on."
    show finn smile

    a unsure shock "What? Finn, wait-!"
    show alex frown

    an "I scream before he does."

    ##Screen shake
    a down shock "Finn!" with vpunch
    show alex frown

    f down frowntalk "Ah!"
    show finn frown

    an "Finn's shoe falls with a deafening thud nearby, sending up dust before the floorboard it fell on cracks."

    an "He's halfway through the ceiling, hanging onto a support beam that can't do the one job it's supposed to."

    an "Finn is going to fall and it won't just be through the third floor."

    a unsure shock "Hold on, Finn! Oh my God, please don't let go."
    show alex frown

    f unsure frowntalk "I-I don't think I can for much longer."
    show finn frown

    a up frowntalk "I-I'll call for help!"
    show alex frown

    f down frowntalk "Alright..."
    show finn frown

    an "I open up my phone to call 911 but..."

    ##Screen shake
    an "I hear the beam crack a little more just as more tiles of the roof fall through. They'll never get here in time. I have to at least try to help him." with vpunch

    a down frowntalk "Finn, I'm coming to get you."
    show alex frown

    f unsure frowntalk "It's too dangerous. Ah!"
    show finn frown

    a up frowntalk "I don't care!"
    show alex frown

    an "A panicked voice that doesn't feel like my own shouts at him. I hurry up the short stairs to the widow's walk, watching every step I take like Finn's life depends on it..."

    an "... because it does."

    a down frowntalk "Don't move, Finn."
    show alex frown

    f down frown "..."

    an "Finn's teachings come to me in a blur. That step doesn't look safe, my feet shuffle and distribute my weight evenly, look for and avoid everything damaged..."

    an "I don't have time to tremble but my hands shake anyway when I finally reach him."

    a unsure frowntalk "I want you to... t-take my hand, Finn."
    show alex frown

    f up frowntalk "... Thank you."
    show finn frown

    an "I reach for him, crawling on my knees and reaching both my hands out to his."

    an "He gathers himself a moment. There's only one chance. If I don't help him—if I don't save him now—I'll never see him again."

    an "Finn takes a deep breath before jumping for me and letting go of the beam."

    ##Screen shake
    an "The movement is enough to send the support beam screeching down in a cloudy abyss of dust." with vpunch

    a up frowntalk "Ah! I've got you...!"
    show alex frown

    an "As the new support beam, I fear I can't help him either. Finn is heavy—too heavy, and I desperately tug him toward me until me and my limbs are screaming from the pain."

    an "What's left of the widow's walk floor creaks around me and I shift my left knee away to see the spot where I was kneeling  collapsing. I... I almost just fell with him..."

    an "I don't have time to panic. Finally—miraculously, after one last tug—I pull him onto the stairs and into the safety of my arms that I definitely can't feel anymore."

    a down shock "Let's get out of here!"
    show alex frown

    an "I loop his arm around my shoulder for support as we leave the rooftop. Not too far behind us, I can hear more cracks as if they're chasing us. Will any of these steps be our last?"

    an "It's only two mostly-solid steps onto the third floor until we collapse, both out of breath and in shock."

    a unsure frowntalk "I-I should... take up... weight lifting..."
    show alex frown

    f unsure frowntalk "I can't... tell if I'm... alive yet..."
    show finn frown

    hide alex
    hide finn
    with dissolve

    ##EVENT IMAGE: A bruised/bleeding Finn staring and smiling lovingly at Alex while she is still worried/angry at him
    ##programmer note: leave the placeholder but we do NOT have an event image for this
    scene cg finn hurt
    with dissolve

    a "Finn. As absolutely exhilarating as that was, I never ever {i}ever{/i} want to do it again!"

    an "It's the first time I've ever been so angry at Finn but it's also the first time I've ever been so scared."

    f "I know."

    an "Finn's voice cracks and I look over to see his bruised and shivering hand reaching to brush away a tear I didn't know I had. I see them roll down his cheeks as if he's taken them from me."

    f "Alex, I'm so so sorry. I'm an idiot, I was being stupid and I almost got you hurt because I didn't listen to you."

    f "I drag you out here in the middle of the night like an asshole and almost get you hurt and that's the worst thing I can imagine."

    f "I don't even care if I die but I'd never forgive myself if you did. Alex... I'm so sorry. I'm so sorry."

    a "Finn... stop."

    f "No, no, I can't. I'm so... sorry... If I died it'd be fine, but you? You're so beautiful and amazing and I—"

    a "No! No, stop. How dare you!"

    f "I... I'm sorry, you're right. I don't even deserve to praise you after tonight."

    a "Not that Finn... how dare you talk about the person I love like this!"

    f "What...? How can you still want to be with me after tonight?"

    an "I know he's heard it all before, but...I have to tell him."

    a "The thing I want the most is for you to value your life as I do."

    f "... I don't know if I can do that, Alex."

    an "I squeeze his hands in mine and he squeezes back as if I'm a lifeline. He's hurting so much and I can't fix that but at the very least..."

    a "I know, Finn. But it doesn't matter. I'm not going anywhere, okay? I'm going to be here the whole time even when you're being stupid."

    f "Alex..."

    a "And I don't—I can't—if you died, I... I feel like I'd die with you. I was so worried, Finn."

    an "I can't hold my tears back anymore. Finn almost died right in front of me and..."

    an "... I still feel like he could fall away at any moment. I'm desperately holding onto his hands as if he's still on that support beam. I can feel every painful breath in my chest."

    f "... Alex. You have to know I'm still going to want to go to dangerous places and be a pain in the ass."

    a "Sure. That's who you {i}are{/i}, but—"

    f "But..."

    an "He pulls my aching body closer, despite his own obvious exhaustion. His arms hug me against his chest and he buries his face in my shoulder."

    f "But I really like you, too. And I appreciate you. I'm sorry if that's not obvious. You saved my life..."

    f "And maybe I should care about that more, but..."

    f "You save my life every day in a way, you know? You were brilliant today. And I'll never forget what you did for me."

    a "Just please be careful from now on."

    f "I will... You've become an amazing partner-in-crime."

    an "He pulls away and pats my head with a small smile. His hand is... heavy."

    a "As your partner-in-crime, I demand you to listen to me when I say something is too risky."

    f "Yeah."

    an "I don't know what else to say to his soft affirmation. Instead, I lean in and kiss my idiot boyfriend, feeling closer to him than I ever have before even though in an instant he was almost just taken away."

    ##Scene 12
    ##Alex room bg
    scene bg alex_room
    with fadee

    an "Finn ended up having to go to the hospital for two fractured fingers, a lucky break from a snapped neck."

    an "We told the doctors he slammed his hand in a door and it wasn't long until rumors circulated about the return of ghosts of people wronged by wine tycoons breaking roofs."

    an "Finn ended up telling Zaina and Paxton about what happened on his own, but luckily I wasn't there for that conversation."

    an "They've seemed to calm down as finals have approached, but none of us have been out exploring since."

    a "Oh... hey, what are you doing here, silly?"

    "Cerberus" "Churr..."

    an "Cerberus von Fluffykins sometimes stays with me despite the danger of sneaking him over. I think Finn realized how much I love his little goth friend. I'm honored he trusts me with him."

    "Cerberus" "Churrrrrrrrr."

    a "Oops, you're right, time for class!"

    ##Scene 13
    ##Classroom bg
    scene bg classroom
    with fadee

    show alex up smile backpack at closeright:
        yalign -0.25
    show finn up smile at closeleft
    with dissolve

    f up frowntalk "Hey, Alex."
    show finn frown

    a up talk "Good morning! Are you ready for our final lab?"
    show alex smile

    f unsure frown "Mm."

    a unsure frowntalk "Oh—your little finger casts are finally off?"
    show alex smile

    f up frowntalk "Yeah."
    show finn frown

    ##Alex angry/pouting face
    a down frown "..."

    ##Alex sprite moves closer to Finn, screen shake
    show alex at closeright with hpunch:
        yalign -0.25
        xalign 0.80

    f unsure frowntalk "O-ow? What?"
    show finn frown

    a unsure frowntalk "One-word responses mean you want to be pinched."
    show alex frown

    f up frowntalk "No?"
    show finn smile

    ##Screen shake
    f down talk "Ow! Okay, okay! Sorry!" with vpunch
    show finn smile

    a up talk "Haha..."
    show alex smile

    ##Finn smiling
    f unsure talk "Silly... Hey, Alex. Uh, do you want to do something fun tonight... and not life-threatening, I mean?"
    show finn smile

    a unsure talk "Oh—of course, if you're interested. What is it?"
    show alex smile

    f down talk "Mm, I'll talk to you about it later. Meet me at my apartment after your last class?"
    show finn smile

    a up talk "Sure thing."
    show alex smile

    hide finn with easeoutleft

    an "Why is he being vague again? Suspicious!"

    an "I open my mouth to ask him for a little more detail but Finn bops me on the nose before walking off to our station."

    an "I huff but I can't even get mad at him."

    ##Screen fade to show a passage of time
    hide alex with dissolve
    scene black with dissolve

    an "Our final lab class is a huge success. Between Finn's attention to detail and my meticulous notes, I can't have asked for a better partner... even if he wasn't my boyfriend."

    an "I have no doubt we'll get an A."

    ##Scene 14
    ##Finn dorm bg
    scene bg finn_room
    with fadee

    show alex up smile at closeright:
        yalign -0.25
    show finn up smile at closeleft
    with dissolve

    a unsure talk "Finn? I brought... you-know-who."
    show alex smile

    f unsure frowntalk "So you did. Were you followed?"
    show finn frown

    a down talk "No, I wasn't."
    show alex smile

    f down frowntalk "Are you sure?"
    show finn frown

    a up talk "Absolutely."
    show alex smile

    f unsure frowntalk "Then who's that behind you?"
    show finn frown

    ##Surprise/shock sprite
    a unsure shock sweat "What?!"

    f up talk "Haha, you actually looked..."
    show finn smile

    a down frowntalk -sweat "H-hey!"
    show alex frown

    f unsure talk "Heh. I'll take Cerberus now, thanks."
    show finn smile

    an smile "I can't help but smile through my defeated sigh as I close the door to give us privacy."

    a unsure talk "Alright, Mr. Vampire, what is this secret event you couldn't tell me about in class?"
    show alex smile

    f up talk "Right. I wanted to invite you to... a party."
    show finn smile

    a up talk "Oh, a party?"
    show alex smile

    f unsure talk "They're not my scene, but... I'm making an exception if you promise to go with me and stick with me the whole time."
    show finn smile

    a unsure talk "That sounds fun. But what's the catch? Why were you being so shady about it?"
    show alex smile

    f up talk "Well, it's a... goth party."
    show finn smile

    a unsure talk "G-goth? It's a dress-up party?"
    show alex smile

    f unsure talk "Sort of... half of the people there will be actual goths. But anyone can come."
    show finn smile

    an "I did say I wanted to get to know him better..."

    a down talk "Sure, but I-I don't know if I have the right clothes for this."
    show alex smile

    f up talk "I know. I have stuff for you to try on here."
    show finn smile

    a unsure talk "Letting me into your infamous closet cave, huh?"
    show alex smile

    f down talk "Anything for you."
    show finn smile

    a up talk "Haha... let's see what we have here then! I'm sure something will fit."
    show alex smile

    f unsure talk "Mm... Doubtful. Just cause I'm not as built as Paxton doesn't mean I'm scrawny."
    show finn smile

    ##choice
    menu:
        "I don't know...":
            show finn frown
            an "Finn frowns at me and I can't help but giggle. Something I said got to him...!"
            f down frowntalk "Are you calling me scrawny?"
            show finn frown
            a unsure talk "Well..."
            show alex smile
            f up talk "Do I need to take my shirt off for you?"
            show finn smile
            a down talk sweat "No need, I think I have an idea."
            show alex smile
            f unsure talk "And here I thought you couldn't pass up the chance..."
            show finn smile
            an unsure -sweat "Very tempting...!"
            a up talk "Are you trying to impress me?"
            show alex smile
            f up talk "Maybe. The important thing is that you don't forget I can climb around abandoned buildings with ease. Just like I can do... this!"
            show finn smile
            ##end choice

        "Paxton's a high bar.":
            f down talk "... Yeah, yeah, I know that. But how do {i}you{/i} know that?"
            show finn smile
            a down talk "I have eyes."
            show alex smile
            f unsure talk "I'm not sure I like that."
            show finn smile
            a unsure talk "You don't like that I have {i}eyes{/i}?"
            show alex smile
            f down talk "No. Take them off."
            show finn smile
            a down frowntalk "I can't take them off!"
            show alex smile
            f up talk "Sure you can, come here."
            show finn smile
            a up shock "Eek!"
            show alex smile
            ##end choice

        "That's not what I meant.":
            f down talk "Yeah? Then what did you mean?"
            show finn smile
            a down talk "That surely I can make something look acceptable."
            show alex smile
            f down  talk "Mm. I think you'd look acceptable in anything."
            show finn smile
            a unsure talk "... No way."
            show alex smile
            f up talk "Yep."
            show finn smile
            a down talk "Nuh uh, I have to put effort into my outfits to look good."
            show alex smile
            f up talk "And I'm saying it's unfair 'cause you'll look good no matter what."
            show finn smile
            show alex blush with Dissolve(1.0)
            a unsure talk "Y-you're being ridiculous."
            show alex smile
            f unsure talk "Not as ridiculous as you implying I'm scrawny."
            show finn smile
            a up shock "I'm telling you I didn't!"
            show alex frown
            f up talk "Well... I should make sure to prove it."
            show finn smile
            a unsure talk -blush "What are you-?!"
            show alex smile
            ##end choice

    #Screen shake
    an "Finn flashes me a grin, my only warning before he lifts me easily off the ground." with vpunch

    a down shock "Gah! Okay, I get it, I get it, not scrawny!"
    show alex frown

    f unsure talk "Do you?"
    show finn smile

    a down frowntalk "Yes, now kindly put me down."
    show alex smile

    f down talk "Hm... nah. You can still see my closet, right? Keep looking. We're gonna go for a one-size look, maybe use a shirt as a dress."
    show finn smile

    a unsure frowntalk "What...? Ugh, fine."
    show alex smile

    an "Awkwardly, I let Finn keep lifting me while I shuffle through his closet. Everything is black, even his socks. He has way more tank tops than I thought he did—which was none. Exactly when does he wear these?"

    a up talk "Oh!"
    show alex smile

    an "I find exactly what I'm going to wear. It's not a flashy top, but it'd look cute as a dress or tucked into pants. I pull it out and show Finn."

    f up talk "... Nice choice. Okay, you're heavy, putting you down now."
    show finn smile

    ##Screen shake
    a unsure talk "What happened to comparing yourself to Paxton?" with vpunch
    show alex smile

    f down talk "Won't happen again, I can assure you. Alright... hm..."
    show finn smile

    f unsure talk "Is it okay if I pick out your jewelry for you?"
    show finn smile

    a unsure talk "Oh, sure."
    show alex smile

    an "Finn nods and opens up a small case of jewelry, far more than the selection he usually wears."

    a up talk "Wow, I didn't know you had so much...!"
    show alex smile

    f down talk "It's a longtime collection. I don't like looking at a lot of them anymore."
    show finn smile

    a unsure talk "Why's that?"
    show alex smile

    f up talk "Well... honestly, a lot of them were gifts and a bit painful to look at. But..."
    show finn smile

    an "Finn smiles and pulls out a sparkling pair of earrings, holding them next to my face."

    f unsure talk "I guess I don't mind anymore. Will you wear these?"
    show finn smile

    a up talk "Oh! These are so gorgeous!"
    show alex smile

    f up talk "Yeah. I want you to have them, actually."
    show finn smile

    a unsure frowntalk "What... are you sure?"
    show alex frown

    f unsure talk "I am. They suit you. It'd make me a lot happier to see you enjoying them than stuffing them away to rot."
    show finn smile

    a up talk "Well... if you say so. Thank you."
    show alex smile

    an "I take them gingerly. I just know I'll treasure these for a long time."

    a down talk "Hehe... is this everything then? Or are you going to do my makeup too?"
    show alex smile

    f up talk "I am."
    show finn smile

    a unsure talk "Just ki—what?"
    show alex smile

    f unsure talk "Come sit on my bed, I already have my makeup bag out."
    show finn smile

    a up talk "R-really?"
    show alex smile

    f up talk "Of course."
    show finn smile

    a unsure talk "What about your chair?"
    show alex smile

    f down talk "Nah. This is comfier."
    show finn smile

    a up talk sweat "Er—alright!"
    show alex smile -sweat

    an "I sit on the bed and sure enough, his makeup supplies are ready and waiting for me. I've never seen him put on his makeup before, I wonder what he looks like without it..."

    f unsure talk "See that bottle on your left? It's moisturizer and primer, you can go ahead and put it on."
    show finn smile

    a up shock "This is an expensive brand...!"
    show alex smile

    f up talk "Mhm. The power of off-season clearance sales."
    show finn smile

    an "Jeez, I feel like this party's going to be a big deal already. I put the moisturizer on and watch Finn as he checks over his extremely brand name possessions."

    an "Oh... this feels great, actually!"

    f unsure talk "Now look up a bit and just relax, okay? It won't take long."
    show finn smile

    a unsure talk "If you say so."
    show alex smile

    an "I do as he says, stealing peeks at him pulling out black brushes—of course, they're black—and dabbing them across different shades of foundation."

    a down talk "I didn't know you did a full routine every day..."
    show alex smile

    f up talk "Nah. Special occasions. I haven't even used this set yet, it's brand new."
    show finn smile

    an "He comes back into view, one gentle hand under my chin to tilt my face up as the other slowly brushes foundation across my skin."

    show alex blush with Dissolve(1.0)
    an "This is... not what I expected. Finn's face is so close to mine now. And his lips look really inviting... and his fingers feel like they're brushing teasingly against me!"

    f unsure talk "Haha... why are you blushing?"
    show finn smile

    a up frowntalk sweat "A-am not..."
    show alex smile

    an -sweat "He swaps to the concealer, ever so feather-light, and before I know it he's already moving away, finished with whatever he was doing before I was... distracted."

    f up talk "There we go. Now all that's left is some black lipstick if you want some."
    show finn smile

    a up talk "Ah... sure..."
    show alex smile

    an "I don't even know if I want some or not, all I know is that I didn't want him to stop touching me..."

    f down talk "Cool."
    show finn smile

    an "Finn dips his forefinger in a small jar before he's back in my space—even more than before."

    f unsure talk "Be still..."
    show finn smile

    an "I want to tell him I have been but I absolutely freeze up as Finn's knees push more and more over the edge of the bed... until he's straddling me."

    a unsure frown "?!"

    an "I stare at his own lips as his finger delicately swipes lipstick across mine."

    an up "I think I'm going to explode!"

    f up talk "There we go. Perfect."
    show finn smile

    a unsure talk "Ah..."
    show alex smile

    f unsure frowntalk "Hm? What was that?"
    show finn smile

    a up shock "Y-you're doing this on purpose...!"
    show alex frown

    f up talk "Am I?"
    show finn smile

    an smile "Definitely. Finn's knowing smirk is insufferable. He doesn't move even after he's done and instead..."

    an "... He pulls me into an effortless kiss that makes us have to start the lipstick process all over again."

    hide alex
    hide finn
    with dissolve

    ##Scene 15
    ##Not sure about bg, possibly classroom/dorm or whatever else we have?
    scene bg amusementpark
    with fadee

    show alex up smile at closeright:
        yalign -0.25
    show finn up smile at closeleft
    with dissolve

    an "When we arrive to the party, I'm still shocked by the elaborate goth outfits despite knowing the theme."

    a up talk "Wow... everyone looks amazing!"
    show alex smile

    f down talk "All the closet goths are out and about, I see."
    show finn smile

    a down talk "I recognize classmates here."
    show alex smile

    f unsure talk "Really?"
    show finn smile

    a unsure talk "Yeah! Do you see that girl with the tall boots over there?"
    show alex smile

    f up talk "Yeah?"
    show finn smile

    a up talk "She's one of the people from lab."
    show alex smile

    f down talk "... Whoa, you're right. I didn't recognize her at all."
    show finn smile

    f unsure talk "Oh, look at that guy over there. Sweet plugs. Think I've seen him around."
    show finn smile

    a unsure talk "Those are {i}enormous.{/i} Are his ears safe?"
    show alex smile

    f up talk "They are. Haha..."
    show finn smile

    a down talk "Already laughing at me?"
    show alex smile

    f down talk "Nah. I'm... having fun already."
    show finn smile

    a unsure talk "Heh... me too. Oh, let me turn off my phone alerts."
    show alex smile

    f unsure talk "Are you sure?"
    show finn smile

    an "I'm glad I've gotten to the point where I don't feel the need to check every few minutes, but the notifications still make me nervous."

    a up talk "... I am. I want to give you my full attention."
    show alex smile

    f up talk "Enticing."
    show finn smile

    "Classmate1" "Oh—hey Finn!"

    an "Two people I don't recognize come rushing up to Finn, huge smiles on their faces. I wonder where he knows them from? They're way too friendly just to be acquaintances."

    "Classmate2" "We weren't sure you'd come, but we're glad you did."

    "Classmate1" "Yeah, we were just talking about you."

    f unsure talk "Oh, hey guys. Nice outfits."
    show finn smile

    "Classmate2" "Haha, thanks... who's this?"

    an "They notice me at his side and I awkwardly give them a wave."

    a unsure talk "Hello, I'm Alex. Nice to meet you."
    show alex smile

    "Classmate1" "Oh, hi! Are you a biology major, too?"

    a down talk "No, I'm actually in nursing."
    show alex smile

    "Classmate2" "Oh wow, that's hard, too. Good luck!"

    a unsure talk "I'm managing, thanks."
    show alex smile

    "Classmate1" "So anyway, Finn, do you remember what the professor said about curving our grades?"

    "Classmate2" "We have to tell you about this rumor we heard from the upperclassmen...!"

    an "My getup is awkward enough, but I'm definitely third-wheeling it right now. I have no idea what they're talking about. I guess I should let them catch up?"

    a down talk "Uh, I'll go get us drinks."
    show alex smile

    f up talk "Oh, alright..."
    show finn smile

    hide alex
    hide finn
    with dissolve

    an "I leave quickly to the snack bar and am pleasantly surprised by the selection. Hah, they even dyed the soda black, that's cute."

    an "I look over to watch Finn talking to the small group forming around him. Everyone looks so nice together. He really fits in here."

    an "With a smile I find myself watching a little longer, a bit nostalgic and not wanting to interrupt. I'm really glad I met Finn and his friends... our friends. I bet Zaina and Paxton would look great in goth outfits."

    f "... ex."

    a "Huh?"

    f "Alex."

    ##Finn sprite close up
    show alex up smile at closeright:
        yalign -0.15
        zoom 1.2
    show finn up smile at closeleft:
        zoom 1.2
    with dissolve

    a unsure frowntalk "Gah, Finn? What are you doing?"
    show alex smile

    f down talk "You promised."
    show finn smile

    a unsure talk "Promised?"
    show alex smile

    f unsure talk "You promised to stay by my side the whole time, remember?"
    show finn smile

    hide alex
    hide finn
    with dissolve

    ##EVENT IMAGE: Finn pulling Alex into his arms, one hand tilting her chin up for a kiss in the middle of the goth party
    ##programming note again: leave this bit but we don't have an event image for it
    scene cg finn party
    with dissolve

    f "So keep your end of the bargain."

    an "Finn sweeps me forward and I go tumbling into his arms. He laughs at my confusion, wrapping one arm around my waist and the other once again tilting my chin up toward him."

    a "What are you doing in the middle of the party? Do I need more lipstick or something?"

    f "Good question."

    an "He kisses my lips abruptly in front of everyone and I can feel my face burning."

    f "Is that answer good enough?"

    ##choice
    menu:
        "(Yes)":
            a "Yes... uh, no!"
            an "He laughs again and starts tugging me back toward his friends."
            f "At least now everyone knows who my girlfriend is."
            a "Was that your goal with that?"
            f "Sure."
            an "Of course he gives me a non-answer... what a tease."
            a "I was just trying to give you space to catch up with your friends, you know."
            f "Don't care about that."
            a "What?"
            f "Just stay with me or I'll kiss you again in front of everyone."
            an "I'm not sure if that's supposed to be a threat or not...!"
            ##Alex smiling
            a "Yeah, alright."
            ##end choice

        "(No)":
            a "No it was not!"
            f "Aw, really...? Okay."
            an "I halfway expect it, but even if I did I know it wouldn't have changed anything... He laughs again before planting yet another kiss to my lips."
            f "How about now?"
            a "Mm...!"
            f "No? How about one more?"
            a "D-don't you dare!"
            f "Haha... that's disappointing."
            a "I-I think people are staring."
            f "Let them. I'm here for you, remember?"
            a "I was only trying to let your friends catch up with you..."
            f "Don't care about that. So stay with me this time."
            ##Alex smiling
            a "Yeah, alright."
            ##end choice

    scene black
    with dissolve

    an "We end up staying for hours at the party, just laughing and talking. His classmates and acquaintances aren't as intimidating as I thought, I even get along with many of them."

    an "It's funny, though, because even though we were mingling, I'm pretty sure Finn and I ended up talking to each other the most."

    an "It's hard to remember anything else..."

    ##Scene 16
    ##Finn's room bg
    scene bg finn_room
    with fadee

    show alex up smile at closeright:
        yalign -0.25
    show finn up frown at closeleft
    with dissolve

    f down talk "I'm exhausted..."
    show finn frown

    a down talk "Me, too. Thanks for lending me your clothes."
    show alex smile

    f up talk "Anytime."
    show finn smile

    an "Finn checks on Cerberus, yawning, before flopping down on his bed with closed eyes. He's still smiling..."

    a up smile "Hehe..."

    f unsure frown "Hm?"

    a unsure talk "You're still smiling. Did you have a good time?"
    show alex smile

    f up talk "Mm... I spent a long time there, I guess."
    show finn smile

    a up talk "Yeah but you had a lot of fun, right?"
    show alex smile

    f down talk "... Wasn't terrible."
    show finn smile

    a down frown "Hmph..."

    an smile "I join him on the bed and see how much of an easy target he is. Payback time... I kiss his cheek. Startled, he opens his eyes again and stares up at me."

    a up talk "Answer the question."
    show alex smile

    ##Finn blushing sprite
    f unsure talk blush "I-I, uh... what was the question?"
    show finn smile

    a unsure talk "I was just asking if you had fun, silly."
    show alex smile

    f down talk "Well, yeah kind of..."
    show finn smile

    a up talk "Kind of?"
    show alex smile

    an "Finn gives a wry smile and reaches up to tuck a piece of hair back behind my ear, fingers lingering there long enough to lend me their heat."

    f unsure talk -blush "Honestly, the best part of the night was knowing you were leaving with me. I kept thinking 'Wow, how lucky am I?'"
    show finn smile

    ##Alex blushing sprite
    a unsure frowntalk blush "What...?"
    show alex smile

    f up talk "I love you, Alex."
    show finn smile

    a down talk "Finn..."
    show alex smile

    f unsure talk "Do you want to... stay the night again?"
    show finn smile

    a up talk "I'd love to."
    show alex smile

    show finn smile

    hide finn
    hide alex
    with dissolve

    scene black
    with dissolve

    an "Finn doesn't need to pull me into his arms. I readily join him, snuggling against his warm chest and feeling more relaxed than I have in a while."

    an "It's not until the next afternoon that I realize—for the first time—not only did I forget to check my phone but... that I also don't care."

    ##END.
    return
