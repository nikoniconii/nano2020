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
    scene bg finn_apartment
    with fadee

    an "Jeez, it's quiet even in the dorms now because of midterms. I hope Finn isn't {i}too{/i} stressed."

    ##A 'knocking' sound effect and/or screen shake could be cool here

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

    show finn -sweat
    f up talk "It's the ears."
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
    show alex -sweat
    a up talk "I'll go with you, Finn."
    show alex smile

    f up talk "Knew I could count on you."
    show finn smile

    z unsure talk "Sigh... well, be careful, you two. I want to check out the stalls."
    show zaina smile

    p up talk "Yes. We're going to keep exploring here."
    show paxton smile

    p unsure talk "On the ground."
    show paxton smile

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
    a up shock "Ah!"
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
    with fadee

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

    show alex -blush
    an unsure smile "What? Oh, he's right, I'm not."

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
    show alex smile -blush

    a unsure talk "H-hello, Finn."
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
    show zaina frown

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
    an "The main doors to the mansion bang before slowly opening up. Once again, the devil somehow knows my thoughts."

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
    with fadee

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
    show finn frown

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

    show alex -blush
    an "My brain feels like it's short-circuiting. I'm so thrown off that the first thing out of my mouth is a diversion from admitting that a confession even happened."

    a unsure frowntalk "W-wow, was your ex... not a good person?"
    show alex smile

    show finn unsure
    an "He shakes his head at that and gives a self-deprecating laugh that breaks my heart."

    f unsure talk "No, it wasn't like that. I was in a very bad place at that time and my ex couldn't deal with it. It wasn't his fault and I'd never want to drag someone down with me." 
    show finn frown

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
    with fadee

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

    show alex -blush with Dissolve(1.0)

    a unsure talk "Uh, so what now?"
    show alex smile

    show finn -blush with Dissolve(1.0)

    f down frown "Mm..."
    show finn frown

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

    show alex -blush with Dissolve(1.0)
    a up shock "You're burning up, Finn!"

    f up talk "I just wanted you to know how serious I am right now. Even though I'm always teasing you and messing with you..."
    show finn smile

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

    p talk "Alright. I'm done, I can't."

    a talk "Paxton?"

    p talk "I mean, y-you all can keep going if you want. If anything happens, it'll be good to have someone standby, right? You can count on me!"

    f talk "If you say so."

    z talk "If something looks dangerous, you can definitely give your opinion, you know."

    p talk "Y-yeah, sorry."

    a talk "It's alright, we'll see you soon Paxton. Stay safe."

    z talk "Yell if you need us. Or maybe not, I'm scared it'll collapse the whole place."

    p talk "Not helping."

    f talk "Let's keep moving."

    an "The next flight of stairs is worse than the last. Every plank looks unstable, like the air itself weighs too much and creaks before we even walk."

    z talk "I think this is where I stop, too. I can't risk me {i}or{/i} my camera."

    f talk "Are you sure? There's not much left, Zaina. The top looks so promising!"

    a talk "You're awfully excited about this."

    an "He never looks worried about the danger. After knowing his history, it's a bit more concerning."

    f talk "Of course I am."

    z talk "Don't drag Alex into your nonsense. Come on guys, let's stop here."

    f talk "No way."

    a talk "It's okay, I'll look out for him."

    z talk "Alex... Ugh, fine, if you insist. If you two lovebirds die I'm going to kill you."

    a talk "L-lovebirds?"

    an "She doesn't respond, simply rolls her eyes and waves us off. Are we really that obvious?"

    f talk "See ya."

    an "I'm trying to copy Finn's steps as much as I can. Skip that plank, careful and gentle steps on-!"

    #Screen shake?
    a talk "Ah!"

    f talk "Alex!"

    an "Finn rushes to catch me right after a step gives under."

    a talk "Owww..."

    f talk "Alex! Alex, are you okay?"

    an "He sits me down part way up the stairs and I realize I can't breathe, I can't even speak!"

    f talk "It's okay, just relax. I'm here."

    a talk "..."

    an "Finn pats my head affectionately, letting his fingers thread through my hair until I finally feel my lungs working again."

    a talk "That—{i}scared{/i} me."

    f talk "I know..."

    an "He gently pulls my leg on top of his, inspecting it."

    a talk "Oh, ow..."

    f talk "You scraped your leg."

    a talk "I don't feel so good. Did I almost die?"

    f talk "Nah, of course not. I've already broken fingers doing this stuff. A scrape is nothing, you're lucky."

    a talk "Broken {i}fingers{/i}?!"

    f talk "Sure, but I've broken more than that outside of adventuring."

    f talk "When I was at the height of my depression, I'm sure I broke my arm, my leg...I failed a lot, so nothing {i}quite{/i} was enough to kill me."

    an "What—what is he saying to me right now? And so casually? It's like he doesn't even care about his suicide attempts!"

    a talk "Is that... supposed to make me feel better?"

    f talk "Yes. Is it working?"

    a talk "No, Finn! It's not working! You're doing an awful job!"

    f talk "Haha... I'm sorry."

    an "And he's just laughing it off..."

    f talk "Let's go back down, I think that's enough for tonight."

    a talk "Yeah... I think so."

    an "We retrace our steps and meet up with Zaina and Paxton back on the first floor. No one is very enthused when they see me limping."

    z talk "Alex! What happened?!"

    p talk "You're bleeding!"

    z talk "Finnnnn..."

    an "Uh oh, Zaina looks pretty mad...!"

    f talk "She's alright, it's just a scrape."

    a talk "Yeah, I'm alright, it just stings a bit."

    p talk "That's not the point..."

    z talk "Exactly. Finn, you're the one with experience, this is {i}your{/i} fault. I told you not to keep going and look what happened!"

    f talk "..."

    p talk "We really need to treat that to make sure you don't get infected, Alex."

    a talk "Oh—yes, we should."

    z talk "Right. Let's go, we don't have time to talk about this."

    ##Paxton and Zaina sprites disappear

    ##choice
    menu:
        "They were pretty harsh.":
            f talk "... Nah."
            a talk "They were! Zaina didn't need to talk to you like that."
            f talk "Maybe..."
            a talk "Should I talk to them about it?"
            ##end choice

        "They're right, you know.":
            f talk "... I know."
            a talk "We should both be careful, not just you."
            f talk "Maybe."
            a talk "...Finn?"
            ##end choice

        "It's not your fault.":
            a talk "Sorry that you got most of the blame, Finn... it really wasn't your fault."
            f talk "... t'was."
            a talk "No, I decided to go with you, remember? You didn't force me."
            f talk "..."
            a talk "Finn?"
            ##end choice

    f talk "Let's just go..."

    an "It's an awkward time back. I get patched up by Zaina and offer to walk Finn back to his dorm, but he denies me."

    an "No matter what I do, Finn doesn't talk to me. With a hurt leg, I go back to my dorm to sleep..."

    an "It's not supposed to be a long walk, but each step is more painful than the last. Scratchy echoes suggest something else's staggering footsteps are behind me, even though I know I'm alone. There's only my shadow, limping behind me like a hunting monster under glowing street lamps and a gray sky."

    ##Scene 10
    ##Alex room bg or starting with a black screen if there's no night version
    scene bg alex_room_night
    with fadee

    ##Vibration/screen shake for phone

    a talk "Ugh... what time is it? Why is my phone vibrating?"

    a talk "..."

    a talk "Finn?"

    an "Why is he vaguetexting me at midnight?"

    a talk "Do I want to meet him for another trespass? Just the two of us? {i}Now?{/i}"

    an "It's kind of like... an illegal date. Can't say I've ever done that before. Well, my leg is better but..."

    a talk "How... safe... is... it?"

    ##Phone vibration
    a talk "Not too old of a building, huh? Hmm..."

    an "I haven't seen him much outside of class after last time. I miss him."

    a talk "Alright... I'll get... ready and... meet you... there."

    ##Phone vibration
    a talk "Hehe... I... miss you... too."

    ##Scene 11
    ##Mansion bg
    scene bg mansion
    with fadee

    ##Alex happy/excited and Finn serious, keep their sprites separate

    an "There he is! Finn!"


    an "He's already picking the lock to get us in. I didn't know he could do that! I shouldn't be as impressed as I am, I'm pretty sure that's super illegal. Oh well... I'm too happy to see him again to really care right now."

    a talk "Finn!"

    f talk "Hey."

    an "Huh? Just a 'hey'?"

    a talk "It's great to see you again."

    f talk "Yeah."

    an "?!"

    a talk "It's, uh, a nice mansion."

    f talk "..."

    an "Grr..."

    ##Finn smiling 
    f talk "Got it."

    an "The lock snaps and Finn finally turns to face me, a damning smile on his face."

    ##Finn's sprite moves closer
    f talk "Alex."

    ##Alex blushing and her sprite moves away
    a talk "W-what?"

    ##Finn's sprite moves close to her again
    f talk "I'm really glad you came."

    a talk "Oh... really?"

    f talk "I missed you. A lot. I was losing it, I even forgot to put on my eyeliner yesterday."

    a talk "I-is that so?"

    f talk "Mhmm..."

    an "He laces his fingers through mine and brings my hand to his lips for a gentle kiss that's far more princely than it has any right to be."

    a talk "Wha..."

    f talk "Wanna hold hands?"

    an "{i}I'm{/i} the one losing my mind! He's unbearably handsome with the way he's looking at me. I feel like a teenager right now..."

    a talk "S-sure."

    f talk "Let's go."

    an "We walk inside and he was right, the first floor is incredibly stable. The mansion couldn't have been abandoned too long ago, even the mildew isn't that strong."

    an "Finn leads me around the place as my loving guide who won't let go of my hand even when it's inconvenient."

    f talk "It's said this place was passed down generation-by-generation, only forfeited by delinquent grandchildren who spent all the inheritance and went into unspeakable debt."

    a talk "That sounds like the set-up of a crime drama show."

    f talk "Heh. Then I guess you'll be pleased to know the family was full of wine tycoons."

    a talk "Ooh, scandalous."

    f talk "Very. There are rumors there were even punishments carried out in this very building to those who fell out of their favor."

    a talk "Like..."

    an "I make a gesture, dragging my thumb across my neck and Finn laughs."

    f talk "More like..."

    an "His fingers move to the side of my neck before tickling it, his flirty smile contagious if I wasn't already laughing."

    a talk "H-hey! Stop that before I tickle you back."

    f talk "Oh yeah? Try it."

    a talk "I warned you!"

    an "I move to carry out my threat but Finn snatches my free hand in his, pulling me forward into his chest."

    a talk "That's cheating!"

    f talk "Telling me I'm cheating is like admitting I won."

    a talk "It is not. I'm simply recognizing your abhorrent conduct."

    f talk "Uh huh. Since I won, can I have my prize now?"

    a talk "Since when was this a competition? What prize?"

    f talk "My kiss. What, not going to give me one?"

    a talk "You...!"

    an "Alright, so maybe he has won because there's nothing more I want right now other than to kiss him."

    an "He smirks down at me but I give into it, leaning up and planting a soft kiss to his lips."

    ##Finn blushing
    f talk "..."

    a talk "You're blushing after all that smack talk?"

    f talk "I am not. A-anyway, I should show you... more."

    a talk "Hehe yeah... do you think there's a wine cellar here?"

    f talk "Good point. Let's start with the basement."

    an "Finn takes me to the basement, testing out the stairs and staying ahead of me. When we make it down, it's hard to see anything at all in the darkness. I'm glad for flashlights."

    a talk "This place is..."

    f talk "... so cool."

    a talk "Pfft."

    f talk "What?"

    a talk "Of course you'd like it. Do you want to live in a dark and brooding vampire mansion like this?"

    f talk "Ha. That's a bit much but..."

    a talk "But what?"

    f talk "Hm. I wouldn't mind if it was with you."

    a talk "Hehe..."

    f talk "Huh, there's still a few bottles here."

    a talk "Ah! Take a picture."

    f talk "Haha. How about I hold it and you take the shot?"

    a talk "Sure."

    an "Finn gingerly takes one of the dusty bottles off the rack and tilts it back, miming chugging."

    a talk "These are going to come out so good."

    f talk "Nice. Shall I pour you a glass of our finest chardonnay, ma'am?"

    an "Finn grins at me as he takes on a terrible impersonation of an aristocratic butler."

    a talk "Absolutely not, sir. Your moldy wine does not suit my palate."

    f talk "Apologies for my insolence."

    an "He returns the bottle so I can take one more picture and we go back to the first floor, still laughing and still holding hands."

    f talk "Next floor?"

    a talk "Sure!"

    f talk "I think there should be bedrooms there..."

    a talk "Finn... you've really researched this place, huh?"

    f talk "Hm? Not more than usual."

    ##choice
    menu:
        "How much is usual?":
            f talk "Uh, well, I usually read up on the history of wherever we're going and the surrounding places."
            a talk "What? But you've never said this much before when we've been out!"
            f talk "Yeah... cause no one asked."
            a talk "Well, I didn't ask cause I didn't know."
            f talk "Fair enough."
            a talk "You'll have to tell me everything from now on, okay?"
            f talk "Sure, if you want."
            a talk "And I bet Zaina and Paxton would love to know, too."
            f talk "Maybe."
            a talk "You say 'maybe' but you never even mentioned it to them...?"
            f talk "I think I tried, once."
            a talk "Really? Did something happen?"
            f talk "Yeah, it never sent. Think my connection went out."
            a talk "..."
            #Screen buzz/shake
            f talk "Haha! Ow, ow, don't pinch me! I'm kidding!"
            ##end choice

        "You're a history buff?":
            f talk "Nah. I just like to know what I'm getting into."
            a talk "I'm not sure half of the stuff you told me tonight was relevant for exploring."
            f talk "Sure it was. You thought of the wine cellar 'cause of my research and I know how not to anger the ghosts now."
            a talk "What...? Ghosts?"
            f talk "Mhmm. Just don't touch the wine and we'll be fine."
            a talk "... We {i}did{/i} touch the wine!"
            f talk "Oh, really? Guess we're cursed now."
            a talk "Just you, goofball."
            an "I can't keep a straight face around him..."
                ##end choice

        "The wine tycoons are common knowledge?":
            f talk "I don't know? The local history books mentioned them often, though."
            a talk "You seriously go to the library for this?"
            f talk "What about it?"
            a talk "Nothing, it's cool. Although it does sound like it leaves an incriminating trail."
            f talk "That's assuming I check the books out."
            a talk "A-are you stealing library books?!"
            an "Finn laughs and messes with my hair."
            f talk "I'm a criminal but I have standards, I'd never steal from a library."
            a talk "Right."
            f talk "Just my neighbor. He doesn't use his card anyway."
            a talk "Dastardly!"
            an "We both laugh and I can't help but wonder what his neighbor is like."
            ##end choice

    an "Finn eagerly leads me up the stairs. It's not as stable-looking as the first floor but there's not much to see either."

    f talk "Seems they didn't use the bedrooms much."

    a talk "Hmm... do you say that because of the doors?"

    f talk "So you noticed them, too. Yeah, the doorknobs aren't as worn as the first floor's. I guess the kids didn't really stay here."

    a talk "I wonder why..."

    an "We go to the third floor, but it's even worse than the second. Noticeably so. I hesitate when we arrive and Finn lets go of my hand so easily that it kind of hurts."

    f talk "Take your time and be careful. I'll go first."

    a talk "Alright... you too."

    an "Finn doesn't agree to my request but I slowly walk along the edges of the floor behind him. Maybe it's my fear, but we sure feel far up now."

    an "A small drop calls my attention and I freeze, looking up to the roof. It's not leaking in one spot, but several."

    a talk "Finn...?"

    f talk "Want to go up to the roof as our last stop?"

    a talk "The r-roof? Finn, look up, it has a bunch of leaks."

    an "Finn peers around the roof for a moment, but my stomach flips when he doesn't look deterred in the least."

    f talk "We can just go to the widow's walk. It's leaking but otherwise it looks like it's held up pretty well."

    a talk "I really don't feel safe."

    an "As if on cue, I feel a distant sting in my leg reminiscent of another time I was unsure."

    f talk "Are you sure? It's probably fine. The view is going to be amazing, I really wanted to see it with you."

    a talk "... I'm sorry, I can't. I have a really bad feeling about this."

    f talk "Mm... alright. Well, I'll go first and make sure it's safe. Okay?"

    a talk "That doesn't sound like a good idea either!"

    f talk "Just stay here, will you? I'll go check for us."

    a talk "Finn...?"

    an "It's pointless trying to talk him out of it. My protests become white noise to Finn's curiosity, as forgotten as the spiderwebs that do nothing to deter him."

    an "Cautiously, I follow and watch him go up to the widow's walk, praying nothing happens. From the bottom of the steps, I can see his legs carefully shifting around."

    f talk "It's beautiful up here..."

    a talk "I'm sure it is."

    f talk "I'm going to get a bit closer, hold on."

    a talk "What? Finn, wait-!"

    an "I scream before he does."

    ##Screen shake

    a talk "Finn!"

    f talk "Ah!"

    an "Finn's shoe falls with a deafening thud nearby, sending up dust before the floorboard it fell on cracks."

    an "He's halfway through the ceiling, hanging onto a support beam that can't do the one job it's supposed to."

    an "Finn is going to fall and it won't just be through the third floor."

    a talk "Hold on, Finn! Oh my God, please don't let go."

    f talk "I-I don't think I can for much longer."

    a talk "I-I'll call for help!"

    f talk "Alright..."

    an "I open up my phone to call 911 but..."

    ##Screen shake

    an "I hear the beam crack a little more just as more tiles of the roof fall through. They'll never get here in time. I have to at least try to help him."

    a talk "Finn, I'm coming to get you."

    f talk "It's too dangerous. Ah!"

    a talk "I don't care!"

    an "A panicked voice that doesn't feel like my own shouts at him. I hurry up the short stairs to the widow's walk, watching every step I take like Finn's life depends on it..."

    an "... because it does."

    a talk "Don't move, Finn."

    f talk "..."

    an "Finn's teachings come to me in a blur. That step doesn't look safe, my feet shuffle and distribute my weight evenly, look for and avoid everything damaged..."

    an "I don't have time to tremble but my hands shake anyway when I finally reach him."

    a talk "I want you to... t-take my hand, Finn."

    f talk "... Thank you."

    an "I reach for him, crawling on my knees and reaching both my hands out to his."

    an "He gathers himself a moment. There's only one chance. If I don't help him—if I don't save him now—I'll never see him again."

    an "Finn takes a deep breath before jumping for me and letting go of the beam."

    ##Screen shake

    an "The movement is enough to send the support beam screeching down in a cloudy abyss of dust."

    a talk "Ah! I've got you...!"

    an "As the new support beam, I fear I can't help him either. Finn is heavy—too heavy, and I desperately tug him toward me until me and my limbs are screaming from the pain."

    an "What's left of the widow's walk floor creaks around me and I shift my left knee away to see the spot where I was kneeling  collapsing. I... I almost just fell with him..."

    an "I don't have time to panic. Finally—miraculously, after one last tug—I pull him onto the stairs and into the safety of my arms that I definitely can't feel anymore."

    a talk "Let's get out of here!"

    an "I loop his arm around my shoulder for support as we leave the rooftop. Not too far behind us, I can hear more cracks as if they're chasing us. Will any of these steps be our last?"

    an "It's only two mostly-solid steps onto the third floor until we collapse, both out of breath and in shock."

    a talk "I-I should... take up... weight lifting..."

    f talk "I can't... tell if I'm... alive yet..."

    ##EVENT IMAGE: A bruised/bleeding Finn staring and smiling lovingly at Alex while she is still worried/angry at him
    ##programmer note: leave the placeholder but we do NOT have an event image for this

    a talk "Finn. As absolutely exhilarating as that was, I never ever {i}ever{/i} want to do it again!"

    an "It's the first time I've ever been so angry at Finn but it's also the first time I've ever been so scared."

    f talk "I know."

    an "Finn's voice cracks and I look over to see his bruised and shivering hand reaching to brush away a tear I didn't know I had. I see them roll down his cheeks as if he's taken them from me."

    f talk "Alex, I'm so so sorry. I'm an idiot, I was being stupid and I almost got you hurt because I didn't listen to you."

    f talk "I drag you out here in the middle of the night like an asshole and almost get you hurt and that's the worst thing I can imagine."

    f talk "I don't even care if I die but I'd never forgive myself if you did. Alex... I'm so sorry. I'm so sorry."

    a talk "Finn... stop."

    f talk "No, no, I can't. I'm so... sorry... If I died it'd be fine, but you? You're so beautiful and amazing and I—"

    a talk "No! No, stop. How dare you!"

    f talk "I... I'm sorry, you're right. I don't even deserve to praise you after tonight."

    a talk "Not that Finn... how dare you talk about the person I love like this!"

    f talk "What...? How can you still want to be with me after tonight?"

    an "I know he's heard it all before, but...I have to tell him."

    a talk "The thing I want the most is for you to value your life as I do."

    f talk "... I don't know if I can do that, Alex."

    an "I squeeze his hands in mine and he squeezes back as if I'm a lifeline. He's hurting so much and I can't fix that but at the very least..."

    a talk "I know, Finn. But it doesn't matter. I'm not going anywhere, okay? I'm going to be here the whole time even when you're being stupid."

    f talk "Alex..."

    a talk "And I don't—I can't—if you died, I... I feel like I'd die with you. I was so worried, Finn."

    an "I can't hold my tears back anymore. Finn almost died right in front of me and..."

    an "... I still feel like he could fall away at any moment. I'm desperately holding onto his hands as if he's still on that support beam. I can feel every painful breath in my chest."

    f talk "... Alex. You have to know I'm still going to want to go to dangerous places and be a pain in the ass."

    a talk "Sure. That's who you {i}are{/i}, but—"

    f talk "But..."

    an "He pulls my aching body closer, despite his own obvious exhaustion. His arms hug me against his chest and he buries his face in my shoulder."

    f talk "But I really like you, too. And I appreciate you. I'm sorry if that's not obvious. You saved my life..."

    f talk "And maybe I should care about that more, but..."

    f talk "You save my life every day in a way, you know? You were brilliant today. And I'll never forget what you did for me."

    a talk "Just please be careful from now on."

    f talk "I will... You've become an amazing partner-in-crime."

    an "He pulls away and pats my head with a small smile. His hand is... heavy."

    a talk "As your partner-in-crime, I demand you to listen to me when I say something is too risky."

    f talk "Yeah."

    an "I don't know what else to say to his soft affirmation. Instead, I lean in and kiss my idiot boyfriend, feeling closer to him than I ever have before even though in an instant he was almost just taken away."


    ##Scene 12
    ##Alex room bg
    scene bg alex_room
    with fadee

    an "Finn ended up having to go to the hospital for two fractured fingers, a lucky break from a snapped neck."

    an "We told the doctors he slammed his hand in a door and it wasn't long until rumors circulated about the return of ghosts of people wronged by wine tycoons breaking roofs."

    an "Finn ended up telling Zaina and Paxton about what happened on his own, but luckily I wasn't there for that conversation."

    an "They've seemed to calm down as finals have approached, but none of us have been out exploring since."

    a talk "Oh... hey, what are you doing here, silly?"

    "Cerberus" "Churr..."

    an "Cerberus von Fluffykins sometimes stays with me despite the danger of sneaking him over. I think Finn realized how much I love his little goth friend. I'm honored he trusts me with him."

    "Cerberus" "Churrrrrrrrr."

    a talk "Oops, you're right, time for class!"

    ##Scene 13
    ##Classroom bg
    scene bg classroom
    with fadee

    f talk "Hey, Alex."

    a talk "Good morning! Are you ready for our final lab?"

    f talk "Mm."

    a talk "Oh—your little finger casts are finally off?"

    f talk "Yeah."

    ##Alex angry/pouting face
    a talk "..."

    ##Alex sprite moves closer to Finn, screen shake
    f talk "O-ow? What?"

    a talk "One-word responses mean you want to be pinched."

    f talk "No?"

    ##Screen shake
    f talk "Ow! Okay, okay! Sorry!"

    a talk "Haha..."

    ##Finn smiling
    f talk "Silly... Hey, Alex. Uh, do you want to do something fun tonight... and not life-threatening, I mean?"

    a talk "Oh—of course, if you're interested. What is it?"

    f talk "Mm, I'll talk to you about it later. Meet me at my apartment after your last class?"

    a talk "Sure thing."

    an "Why is he being vague again? Suspicious!"

    an "I open my mouth to ask him for a little more detail but Finn bops me on the nose before walking off to our station."

    an "I huff but I can't even get mad at him."

    ##Screen fade to show a passage of time

    an "Our final lab class is a huge success. Between Finn's attention to detail and my meticulous notes, I can't have asked for a better partner... even if he wasn't my boyfriend."

    an "I have no doubt we'll get an A."

    ##Scene 14
    ##Finn dorm bg
    scene bg finn_room
    with fadee

    a talk "Finn? I brought... you-know-who."

    f talk "So you did. Were you followed?"

    a talk "No, I wasn't."

    f talk "Are you sure?"

    a talk "Absolutely."

    f talk "Then who's that behind you?"

    ##Surprise/shock sprite
    a talk "What?!"

    f talk "Haha, you actually looked..."

    a talk "H-hey!"

    f talk "Heh. I'll take Cerberus now, thanks."

    an "I can't help but smile through my defeated sigh as I close the door to give us privacy."

    a talk "Alright, Mr. Vampire, what is this secret event you couldn't tell me about in class?"

    f talk "Right. I wanted to invite you to... a party."

    a talk "Oh, a party?"

    f talk "They're not my scene, but... I'm making an exception if you promise to go with me and stick with me the whole time."

    a talk "That sounds fun. But what's the catch? Why were you being so shady about it?"

    f talk "Well, it's a... goth party."

    a talk "G-goth? It's a dress-up party?"

    f talk "Sort of... half of the people there will be actual goths. But anyone can come."

    an "I did say I wanted to get to know him better..."

    a talk "Sure, but I-I don't know if I have the right clothes for this."

    f talk "I know. I have stuff for you to try on here."

    a talk "Letting me into your infamous closet cave, huh?"

    f talk "Anything for you."

    a talk "Haha... let's see what we have here then! I'm sure something will fit."

    f talk "Mm... Doubtful. Just cause I'm not as built as Paxton doesn't mean I'm scrawny."

    ##choice
    menu:
        "I don't know...":
            an "Finn frowns at me and I can't help but giggle. Something I said got to him...!"
            f talk "Are you calling me scrawny?"
            a talk "Well..."
            f talk "Do I need to take my shirt off for you?"
            a talk "No need, I think I have an idea."
            f talk "And here I thought you couldn't pass up the chance..."
            an "Very tempting...!"
            a talk "Are you trying to impress me?"
            f talk "Maybe. The important thing is that you don't forget I can climb around abandoned buildings with ease. Just like I can do... this!"
            ##end choice

        "Paxton's a high bar.":
            f talk "... Yeah, yeah, I know that. But how do {i}you{/i} know that?"
            a talk "I have eyes."
            f talk "I'm not sure I like that."
            a talk "You don't like that I have {i}eyes{/i}?"
            f talk "No. Take them off."
            a talk "I can't take them off!"
            f talk "Sure you can, come here."
            a talk "Eek!"
            ##end choice

        "That's not what I meant.":
            f talk "Yeah? Then what did you mean?"
            a talk "That surely I can make something look acceptable."
            f talk "Mm. I think you'd look acceptable in anything."
            a talk "... No way."
            f talk "Yep."
            a talk "Nuh uh, I have to put effort into my outfits to look good."
            f talk "And I'm saying it's unfair 'cause you'll look good no matter what."
            a talk "Y-you're being ridiculous."
            f talk "Not as ridiculous as you implying I'm scrawny."
            a talk "I'm telling you I didn't!"
            f talk "Well... I should make sure to prove it."
            a talk "What are you-?!"
            ##end choice

    #Screen shake
    an "Finn flashes me a grin, my only warning before he lifts me easily off the ground."

    a talk "Gah! Okay, I get it, I get it, not scrawny!"

    f talk "Do you?"

    a talk "Yes, now kindly put me down."

    f talk "Hm... nah. You can still see my closet, right? Keep looking. We're gonna go for a one-size look, maybe use a shirt as a dress."

    a talk "What...? Ugh, fine."

    an "Awkwardly, I let Finn keep lifting me while I shuffle through his closet. Everything is black, even his socks. He has way more tank tops than I thought he did—which was none. Exactly when does he wear these?"

    a talk "Oh!"

    an "I find exactly what I'm going to wear. It's not a flashy top, but it'd look cute as a dress or tucked into pants. I pull it out and show Finn."

    f talk "... Nice choice. Okay, you're heavy, putting you down now."
    ##Screen shake

    a talk "What happened to comparing yourself to Paxton?"

    f talk "Won't happen again, I can assure you. Alright... hm..."

    f talk "Is it okay if I pick out your jewelry for you?"

    a talk "Oh, sure."

    an "Finn nods and opens up a small case of jewelry, far more than the selection he usually wears."

    a talk "Wow, I didn't know you had so much...!"

    f talk "It's a longtime collection. I don't like looking at a lot of them anymore."

    a talk "Why's that?"

    f talk "Well... honestly, a lot of them were gifts and a bit painful to look at. But..."

    an "Finn smiles and pulls out a sparkling pair of earrings, holding them next to my face."

    f talk "I guess I don't mind anymore. Will you wear these?"

    a talk "Oh! These are so gorgeous!"

    f talk "Yeah. I want you to have them, actually."

    a talk "What... are you sure?"

    f talk "I am. They suit you. It'd make me a lot happier to see you enjoying them than stuffing them away to rot."

    a talk "Well... if you say so. Thank you."

    an "I take them gingerly. I just know I'll treasure these for a long time."

    a talk "Hehe... is this everything then? Or are you going to do my makeup too?"

    f talk "I am."

    a talk "Just ki—what?"

    f talk "Come sit on my bed, I already have my makeup bag out."

    a talk "R-really?"

    f talk "Of course."

    a talk "What about your chair?"

    f talk "Nah. This is comfier."

    a talk "Er—alright!"

    an "I sit on the bed and sure enough, his makeup supplies are ready and waiting for me. I've never seen him put on his makeup before, I wonder what he looks like without it..."

    f talk "See that bottle on your left? It's moisturizer and primer, you can go ahead and put it on."

    a talk "This is an expensive brand...!"

    f talk "Mhm. The power of off-season clearance sales."

    an "Jeez, I feel like this party's going to be a big deal already. I put the moisturizer on and watch Finn as he checks over his extremely brand name possessions."

    an "Oh... this feels great, actually!"

    f talk "Now look up a bit and just relax, okay? It won't take long."

    a talk "If you say so."

    an "I do as he says, stealing peeks at him pulling out black brushes—of course, they're black—and dabbing them across different shades of foundation."

    a talk "I didn't know you did a full routine every day..."

    f talk "Nah. Special occasions. I haven't even used this set yet, it's brand new."

    an "He comes back into view, one gentle hand under my chin to tilt my face up as the other slowly brushes foundation across my skin."

    an "This is... not what I expected. Finn's face is so close to mine now. And his lips look really inviting... and his fingers feel like they're brushing teasingly against me!"

    f talk "Haha... why are you blushing?"

    a talk "A-am not..."

    an "He swaps to the concealer, ever so feather-light, and before I know it he's already moving away, finished with whatever he was doing before I was... distracted."

    f talk "There we go. Now all that's left is some black lipstick if you want some."

    a talk "Ah... sure..."

    an "I don't even know if I want some or not, all I know is that I didn't want him to stop touching me..."

    f talk "Cool."

    an "Finn dips his forefinger in a small jar before he's back in my space—even more than before."

    f talk "Be still..."

    an "I want to tell him I have been but I absolutely freeze up as Finn's knees push more and more over the edge of the bed... until he's straddling me."

    a talk "?!"

    an "I stare at his own lips as his finger delicately swipes lipstick across mine."

    an "I think I'm going to explode!"

    f talk "There we go. Perfect."

    a talk "Ah..."

    f talk "Hm? What was that?"

    a talk "Y-you're doing this on purpose...!"

    f talk "Am I?"

    an "Definitely. Finn's knowing smirk is insufferable. He doesn't move even after he's done and instead..."

    an "... He pulls me into an effortless kiss that makes us have to start the lipstick process all over again."

    ##Scene 15
    ##Not sure about bg, possibly classroom/dorm or whatever else we have?
    scene bg classroom
    with fadee

    an "When we arrive to the party, I'm still shocked by the elaborate goth outfits despite knowing the theme."

    a talk "Wow... everyone looks amazing!"

    f talk "All the closet goths are out and about, I see."

    a talk "I recognize classmates here."

    f talk "Really?"

    a talk "Yeah! Do you see that girl with the tall boots over there?"

    f talk "Yeah?"

    a talk "She's one of the people from lab."

    f talk "... Whoa, you're right. I didn't recognize her at all."

    f talk "Oh, look at that guy over there. Sweet plugs. Think I've seen him around."

    a talk "Those are {i}enormous.{/i} Are his ears safe?"

    f talk "They are. Haha..."

    a talk "Already laughing at me?"

    f talk "Nah. I'm... having fun already."

    a talk "Heh... me too. Oh, let me turn off my phone alerts."

    f talk "Are you sure?"

    an "I'm glad I've gotten to the point where I don't feel the need to check every few minutes, but the notifications still make me nervous."

    a talk "... I am. I want to give you my full attention."

    f talk "Enticing."

    "Classmate1" "Oh—hey Finn!"

    an "Two people I don't recognize come rushing up to Finn, huge smiles on their faces. I wonder where he knows them from? They're way too friendly just to be acquaintances."

    "Classmate2" "We weren't sure you'd come, but we're glad you did."

    "Classmate1" "Yeah, we were just talking about you."

    f talk "Oh, hey guys. Nice outfits."

    "Classmate2" "Haha, thanks... who's this?"

    an "They notice me at his side and I awkwardly give them a wave."

    a talk "Hello, I'm Alex. Nice to meet you."

    "Classmate1" "Oh, hi! Are you a biology major, too?"

    a talk "No, I'm actually in nursing."

    "Classmate2" "Oh wow, that's hard, too. Good luck!"

    a talk "I'm managing, thanks."

    "Classmate1" "So anyway, Finn, do you remember what the professor said about curving our grades?"

    "Classmate2" "We have to tell you about this rumor we heard from the upperclassmen...!"

    an "My getup is awkward enough, but I'm definitely third-wheeling it right now. I have no idea what they're talking about. I guess I should let them catch up?"

    a talk "Uh, I'll go get us drinks."

    f talk "Oh, alright..."

    an "I leave quickly to the snack bar and am pleasantly surprised by the selection. Hah, they even dyed the soda black, that's cute."

    an "I look over to watch Finn talking to the small group forming around him. Everyone looks so nice together. He really fits in here."

    an "With a smile I find myself watching a little longer, a bit nostalgic and not wanting to interrupt. I'm really glad I met Finn and his friends... our friends. I bet Zaina and Paxton would look great in goth outfits."

    f talk "... ex."

    a talk "Huh?"

    f talk "Alex."

    ##Finn sprite close up

    a talk "Gah, Finn? What are you doing?"

    f talk "You promised."

    a talk "Promised?"

    f talk "You promised to stay by my side the whole time, remember?"

    ##EVENT IMAGE: Finn pulling Alex into his arms, one hand tilting her chin up for a kiss in the middle of the goth party
    ##programming note again: leave this bit but we don't have an event image for it

    f talk "So keep your end of the bargain."

    an "Finn sweeps me forward and I go tumbling into his arms. He laughs at my confusion, wrapping one arm around my waist and the other once again tilting my chin up toward him."

    a talk "What are you doing in the middle of the party? Do I need more lipstick or something?"

    f talk "Good question."

    an "He kisses my lips abruptly in front of everyone and I can feel my face burning."

    f talk "Is that answer good enough?"

    ##choice
    menu:
        "(Yes)":
            a talk "Yes... uh, no!"
            an "He laughs again and starts tugging me back toward his friends."
            f talk "At least now everyone knows who my girlfriend is."
            a talk "Was that your goal with that?"
            f talk "Sure."
            an "Of course he gives me a non-answer... what a tease."
            a talk "I was just trying to give you space to catch up with your friends, you know."
            f talk "Don't care about that."
            a talk "What?"
            f talk "Just stay with me or I'll kiss you again in front of everyone."
            an "I'm not sure if that's supposed to be a threat or not...!"
            ##Alex smiling
            a talk "Yeah, alright."
            ##end choice

        "(No)":
            a talk "No it was not!"
            f talk "Aw, really...? Okay."
            an "I halfway expect it, but even if I did I know it wouldn't have changed anything... He laughs again before planting yet another kiss to my lips."
            f talk "How about now?"
            a talk "Mm...!"
            f talk "No? How about one more?"
            a talk "D-don't you dare!"
            f talk "Haha... that's disappointing."
            a talk "I-I think people are staring."
            f talk "Let them. I'm here for you, remember?"
            a talk "I was only trying to let your friends catch up with you..."
            f talk "Don't care about that. So stay with me this time."
            ##Alex smiling
            a talk "Yeah, alright."
            ##end choice


    an "We end up staying for hours at the party, just laughing and talking. His classmates and acquaintances aren't as intimidating as I thought, I even get along with many of them."

    an "It's funny, though, because even though we were mingling, I'm pretty sure Finn and I ended up talking to each other the most."

    an "It's hard to remember anything else..."

    ##Scene 16
    ##Finn's room bg
    scene bg finn_room
    with fadee

    f talk "I'm exhausted..."

    a talk "Me, too. Thanks for lending me your clothes."

    f talk "Anytime."

    an "Finn checks on Cerberus, yawning, before flopping down on his bed with closed eyes. He's still smiling..."

    a talk "Hehe..."

    f talk "Hm?"

    a talk "You're still smiling. Did you have a good time?"

    f talk "Mm... I spent a long time there, I guess."

    a talk "Yeah but you had a lot of fun, right?"

    f talk "... Wasn't terrible."

    a talk "Hmph..."

    an "I join him on the bed and see how much of an easy target he is. Payback time... I kiss his cheek. Startled, he opens his eyes again and stares up at me."

    a talk "Answer the question."

    ##Finn blushing sprite
    f talk "I-I, uh... what was the question?"

    a talk "I was just asking if you had fun, silly."

    f talk "Well, yeah kind of..."

    a talk "Kind of?"

    an "Finn gives a wry smile and reaches up to tuck a piece of hair back behind my ear, fingers lingering there long enough to lend me their heat."

    f talk "Honestly, the best part of the night was knowing you were leaving with me. I kept thinking 'Wow, how lucky am I?'"

    ##Alex blushing sprite
    a talk "What...?"

    f talk "I love you, Alex."

    a talk "Finn..."

    f talk "Do you want to... stay the night again?"

    a talk "I'd love to."

    an "Finn doesn't need to pull me into his arms. I readily join him, snuggling against his warm chest and feeling more relaxed than I have in a while."

    an "It's not until the next afternoon that I realize—for the first time—not only did I forget to check my phone but... that I also don't care."

    ##END.


    return
