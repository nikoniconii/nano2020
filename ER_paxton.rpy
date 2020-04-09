######################################################
############## P A X T O N ## R O U T E ##############
######################################################

label paxtonroute:

    ## Scene 1
    scene bg alex_room with fadee

    show alex unsure frown at Transform:
        linear 0.0 xalign 0.75 yalign 1.0
        linear 1.5 xalign 0.8
    with dissolve 
    an "..."
    an "..."
    show alex down frowntalk sweat  
    a "Mn..."
    show alex frown unsure 
    an "I know I'm supposed to finish this assignment soon, but..."
    show alex neutral smile -sweat  
    an "I can't focus. I keep remembering a few days ago, that night on the roof."
    show alex up 
    an "It was magical. I can't forget the way stars looked. As if the sky was clear just for me and..."
    show alex down shock sweat 
    a "Ugh, no! Focus, Alex! You need to finish your assignment, not dream about pretty people!"
    show alex down frown -sweat 
    an "My parents would be so angry if they saw me now."

    #phone buzz 
    
    show alex up shock 
    an "Oh... are they texting me to ask about school again?"
    show alex unsure frown 
    an "Mom already lectured me this morning about how I should've taken more lessons for the semester."
    show alex down frowntalk 
    an "I can't believe she's messaging me about it again."
    show alex frown 
    menu:
        "I reach to my phone.":
            an "I grab my phone from where it's laying on the table."
            show alex up shock 
            a "Oh, it's not mom. It's..."
            show alex up frown sweat
            show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
                linear 0.0 alpha 0.0 xalign 0.8 yalign 1.0 
                linear 1.5 alpha 1.0  
                linear 1.5 alpha 0.0 
            an "Paxton? I wonder why he's messaging me."
            hide ablush_temp 
            show alex -sweat 
            an "I click on the notification and read the message."
            show alex frown  
            an "He's asking if I can drop by the cafe. He wants to use me as{nw}"
            show alex shock unsure sweat 
            extend "... a guinea pig?"
            show alex up smile -sweat 
            an "Oh, for his latte experiments. Right,that makes sense."
            show alex talk 
            a "I should reply to him."
            show alex unsure frown
            an "I want to say yes, but what about my assignment?"
            show alex down 
            an "I look at the papers spread in front of me. Suddenly, I feel an urge to push them off the table."
            show alex unsure 
            an "Don't be an idiot, Alex. It'd take ages to put them back in order again."

        "I refuse to check the message.":
            an "I go back to studying."
            an "I write two more sentences before I get interrupted again."
            ## phone buzzing sound effect
            show alex frowntalk 
            a"Another message?"
            show alex frown 
            an "I sigh with defeat and check my phone."
            show alex shock up
            show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
                linear 0.0 alpha 0.0 xalign 0.8 yalign 1.0 
                linear 0.5 alpha 1.0 
                linear 0.5 alpha 0.0 
            an "Paxton?"
            hide ablush_temp 
            show alex frown
            an "He's asking if I can drop by the cafe in his first text. He wants to use me as a{nw}"
            show alex shock unsure sweat 
            extend "... guinea pig?"
            show alex smile up -sweat
            an "Oh, for his latte experiments. Right,that makes sense."
            show alex unsure frown 
            an "I throw a look at the papers spread on my desk hesitantly, then focus back to my phone."

    show alex up shock  
    an "The next message just says \'white chocolate???\'"
    show alex smile  
    an "Is that what he’ll use for the drink he's making?"
    show alex down frown 
    an "I look at my papers again, then push myself off of my chair."
    show alex unsure smile 
    an "I can complete my assignment later. I'm really curious about that drink."
    show alex up smile 
    an "I'll message him back to ask if he'll use whipped cream again. I should let him know that I'm lactose intolerant."
    ## phone buzzing sound effect
    show alex shock sweat 
    an "He replied with sad emojis?"
    ## phone buzzing sound effect
    show alex unsure smile  
    an "Hmm, he says he's sorry about that drink with whipped cream he gave me before and that he can make something that I can drink this time."
    show alex up smile -sweat 
    show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
        linear 0.0 alpha 0.0 xalign 0.8 yalign 1.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 0.0 
    an "I can't wait to try it."
    hide ablush_temp 
    show alex up talk 
    a"I should get ready."
    
    ## Scene 2
    scene bg cafe with fadee
    
    show alex at Transform:
        linear 0.0 xalign 0.75 yalign 2.0
        linear 1.5 xalign 0.8 
    with dissolve 
    an "I arrived at the cafe not even 30 minutes later."
    ## clinking sound effect, coming from the bell on the cafe's door when Alex opens it
    show alex unsure frown
    an "I hope I didn't take too long to arrive..."
    show alex up frowntalk 
    an "I wonder where Paxton is. I can't see him from here."
    show alex frown  
    an "I walk towards the counter. Maybe I can find him there."
    ## Alex, surprised
    show alex up shock 
    an "There he is!"
    show paxton down frown apron at Transform:
        linear 0.0 xalign 0.15 yalign 1.0 
        linear 1.5 xalign 0.1 
    with dissolve 
    show alex frown 
    an "He seems focused on making a drink."
    show alex smile 
    an "Well, that's not surprising. He's working right now, unlike me, who's ditching her assignment to go drink coffee."
    show alex unsure sweat 
    an "I really hope mom doesn't try to call me right now."
    show alex smile  -sweat up
    
    menu: 
        "Paxton, hi.":
            show paxton up frowntalk 
            show alex smile 
            p "Oh, hey!"
            show paxton talk at Transform: 
                linear 1.5 xalign 0.2 
            p "Glad you could make it, I was just preparing your latte."
            show paxton smile 
            an "He seems excited. It seems like he really wants me to enjoy the latte he'll prepare."
        "Booo!":
            show paxton up frowntalk at Transform: 
                linear 0.2 xalign 0.11 
                linear 0.4 xalign 0.09 
                linear 0.2 xalign 0.1 
            show alex talk down 
            p "Ah!"
            show paxton frown 
            show alex up smile 
            an "Paxton flinches and turns towards me quickly."
            show paxton smile at Transform: 
                linear 1.5 xalign 0.2 
            show alex talk down 
            a"Sorry, did I scare you?"
            show paxton unsure frowntalk 
            show alex smile up 
            p "Alex! Don't do that, I almost dropped the cup!"
            show paxton smile 
            show alex talk neutral 
            a"Sorry, sorry."
            show alex up smile 
            show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
                linear 0.0 alpha 0.0 xalign 0.8 yalign 2.0 
                linear 0.5 alpha 1.0 
                linear 0.5 alpha 1.0 
                linear 0.5 alpha 0.0 
            an "He looks so cute when he's trying to scold me."
            hide ablush_temp 

    show alex talk up -sweat -blush 
    show paxton smile up 
    a"Well, what's up with that cup you have? Is it for me{nw}"
    show alex shock
    extend"— {w}wait, did you know I was going to arrive just now?"
    show paxton talk 
    show alex smile 
    p "I didn't. I just wanted to try making that latte and see if it tasted okay. If I messed it up, I was going to dump it into trash and be glad that you weren't here to see it."
    show paxton smile 
    show alex talk 
    a"Sorry, I ruined your plans."
    show alex smile 
    show paxton down talk 
    p "I can never recover from a blow to my pride, so just try it and act like it's decent if you hate it."
    show paxton frown up 
    show alex neutral frown 
    an "He seems hesitant about putting a lid on the cup. I wonder why?"
    show alex up 
    an "He ended up putting it on. Should I ask him about it?"
    show paxton talk 
    p "Here you go."
    show paxton smile 
    show alex smile up 
    an "He looks too eager to see me try the latte. Maybe I can ask him about it later."
    an "I take the cup from his hands. It feels hot in my hands, almost enough to burn."
    ## Paxton, excited/lifting eyebrows/blushing a little? Any of these
    hide paxton 
    show expression "images/sprites/paxton base.png" as pbase at Transform:
        xalign 0.2 yalign 1.0 
    show expression "images/sprites/paxton expression2.png" as ptalk at Transform:
        xalign 0.2 yalign 1.0 
    show expression "images/sprites/paxton outfit1.png" as pglass at Transform: 
        xalign 0.2 yalign 1.0 
    show expression "images/sprites/paxton outfit3.png" as papr at Transform: 
        xalign 0.2 yalign 1.0 
    show expression "images/sprites/paxton brows1.png" as p_browup at Transform: 
        xalign 0.2 yalign 0.55
    show expression "images/sprites/paxton extra1.png" as p_blush at Transform: 
        linear 0.0 alpha 0.0 xalign 0.2
        linear 0.25 alpha 1.0 
    p "Tell me if you like it?"
    hide ptalk 
    show expression "images/sprites/paxton expression1.png" as psmile at Transform: 
        xalign 0.2 yalign 1.0 
    show alex neutral smile 
    an "Oh, he looks like an eager puppy."
    show alex neutral frown sweat 
    show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
        linear 0.0 alpha 0.0 xalign 0.8 yalign 2.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 0.0 
    an "God, what am I even thinking? Come on Alex, get yourself together."
    hide ablush_temp 
    hide pbase 
    hide psmile 
    hide pglass 
    hide papr
    hide p_browup 
    hide p_blush
    show paxton unsure frowntalk apron at leftt
    show alex -sweat 
    p "Is it too hot to drink?"
    show paxton unsure frown 
    show alex neutral shock sweat 
    a "No, sorry! I was just..."

    menu:
        "Curious about what you used to make this.":
            show alex unsure smile sweat 
            show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
                alpha 0.5 xalign 0.8 yalign 2.0 
            an "I hope I'm not blushing..."
            show paxton up frowntalk 
            p "Well, it's white chocolate matcha latte with almond milk. You can drink up without fearing for your life."
            show alex up talk 
            show paxton up frown 
            a "Lucky me."
            hide ablush_temp 

        "Uh... nothing.":
            show alex frown 
            show paxton frowntalk unsure 
            p "You sure?"
            show paxton frown 
            show alex unsure talk blush 
            a "Yeah, don't worry."
            show alex neutral frown 
            an "This isn't one of my greatest moments, but..."
            show alex unsure 
            an "I just can't find a proper excuse when he's looking at me. I feel like when he looks at me, my skin is tingling."
            show alex neutral at Transform:
                linear 0.2 yalign 2.05 
                linear 0.4 yalign 1.95 
                linear 0.2 yalign 2.0 
            an "I look down, hoping to hide my blush."
            
    show alex -blush neutral frowntalk -sweat 
    an "I take a sip."
    show alex up 
    an "Wow..."
    show alex talk 
    a "This tastes delicious!"
    show alex smile 
    show paxton up talk 
    p "So you like it?"
    show paxton smile 
    show alex down shock 
    a "Like? No..."
    show paxton unsure frowntalk at Transform: 
        linear 0.2 xalign 0.21 
        linear 0.4 xalign 0.19 
        linear 0.2 xalign 0.2
    ## Paxton, worried
    show alex frown 
    p "Wha— um, is it too, I don't know, sweet or—?"
    show paxton frown 
    show alex up smile 
    an "Aw, he looks really worried."
    ## Alex, smiling
    an "I shouldn't feel this amused when he's like this, but I can't help it."
    an "Enough playing around, I shouldn't make him worry too much..."
    show alex talk 
    a "I don't like it Paxton, I {i}love{/i} it!"
    show alex smile 
    show paxton talk at Transform: 
        linear 0.25 yalign 1.6 
        linear 0.25 yalign 1.0 
    ## Paxton, smiling
    p "You're worse than Zaina— you know that, right?"
    show paxton smile 
    menu:
        "I like her.":
            show alex down talk 
            a "She's a badass, you and Finn probably couldn't survive urbexing if not for her."
            show paxton unsure frowntalk 
            show alex smile 
            p "Hey, that's not-"
            show paxton frown 
            p "..."
            show paxton frowntalk 
            p "Okay, you might be right just a little bit."
            show paxton smile up 
            show alex at Transform: 
                linear 0.25 yalign 2.4 
                linear 0.25 yalign 2.0 
            an "Heh, called it."
            show paxton talk 
            p "Stop looking so smug..."
            show paxton smile 
            show alex talk 
            a "You're just jealous of how badass she is."
            show alex smile 
            show paxton down talk 
            p "Well, who isn't?"

        "I'll take that as a compliment.":
            show paxton down talk 
            p "You better. Zaina could kick both of our asses without even blinking."
            show paxton smile 
            show alex neutral frown 
            a "..."
            show alex frowntalk 
            a "Don't you go to the gym as a hobby?"
            show alex frown 
            show paxton frowntalk 
            p "Alex. She has a motorcycle."
            show paxton frown up 
            show alex unsure smile 
            an "Okay, valid."
            show alex down talk 
            a "I can picture her shutting down both you and Finn down."
            show paxton up talk at Transform: 
                linear 0.2 xalign 0.21 
                linear 0.4 xalign 0.19
                linear 0.2 xalign 0.2 
            show alex smile 
            ## Paxton, laughing
            p "Well, you got us down pretty well. That's our gang in a nutshell."
            show paxton smile 
            show alex up 
            an "He seems to care about Finn and Zaina a lot... I know they've been friends for some time, but they really fit each other."
            
    show paxton talk up 
    show alex smile up 
    p "Anyway, does this mean you're agreeing to help me with my other drink experiments?"
    show paxton smile 
    show alex up shock 
    an "Oh, so that's why he seemed so excited to see my reaction to his latte."
    show alex smile 
    an "But I can't deny I enjoyed being his guinea pig.{nw}"
    show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
        linear 0.0 alpha 0.0 xalign 0.8 yalign 2.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 0.0
    extend " Getting to see him is also another bonus of this."
    hide ablush_temp 
    show alex unsure frowntalk sweat 
    an "Ugh, no. What am I even thinking?"
    show alex up frown -sweat 
    show paxton up talk 
    p "So, what do you say?"
    show alex unsure frown sweat 
    an "I probably shouldn't accept this. If he keeps messaging me everytime I sit down to study, my grades will suffer."
    show alex neutral -sweat 
    an "But on the other hand..."
    show alex unsure smile 
    show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
        linear 0.0 alpha 0.0 xalign 0.8 yalign 2.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 0.0
    an "His eyes are literally sparkling. How can I say no when he's using puppy eyes?"
    hide ablush_temp 
    show alex talk up 
    a "Sure. It's not like I'm going to turn down free lattes."
    show alex smile 
    show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
        linear 0.0 alpha 0.0 xalign 0.8 yalign 2.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 1.0 
        linear 0.5 alpha 0.0
    an "Maybe I can enjoy a break from my studies now and then. I'm sure it'll be fine."
    hide ablush_temp 
    ## Paxton, grinning
    show paxton talk up at Transform: 
        linear 0.2 xalign 0.21 
        linear 0.4 xalign 0.19
        linear 0.2 xalign 0.2 
    p "Awesome. Now, tell me more about what you can taste in this..."

    ## Scene 3 
    scene bg amusementpark with fadee 
    
    show alex unsure frown at Transform:
        linear 0.0 xalign 0.95 yalign 2.0
        linear 1.5 xalign 1.0 
    with dissolve 
    ## Alex, worried/frowning
    an "We arrive at the old amusement park. I look around, but all I can see is dusty, old machines. {nw}"
    show alex smile 
    extend "They're fascinating— once, they were the source of hundreds' happiness.{nw}"
    show alex frown 
    extend " Now they're just empty, old metal pieces."
    show finn down talk at Transform: 
        linear 0.0 xalign 0.00 yalign 1.0 
        linear 1.5 xalign -0.05
    with dissolve 
    f "I can't wait to climb one of these..."
    show finn smile 
    show alex neutral frown sweat 
    an "I know I've been urbexing with the gang for these last few times, but I still can't get used to Finn's thirst for danger."
    show alex up -sweat
    an "This amusement park looks old, but really interesting. I'd love to explore it more, but I don't want to do it alone."
    show alex down 
    an "And I have a feeling Finn already has a plan in his mind— it's probably not exploring this place, though."
    show alex up sweat 
    an "He looks interested in the old roller coaster tracks. What is he thinking?"
    show zaina up frowntalk at Transform: 
        linear 0.0 xalign 0.35 yalign -2.0 #size(356.25, 714.4)
        linear 1.5 xalign 0.3 
    with dissolve 
    show alex -sweat 
    z "So, where do we start from?"
    show zaina talk 
    show paxton up frowntalk hat at Transform: 
        linear 0.0 xalign 0.65 yalign 1.0
        linear 1.5 xalign 0.7 
    with dissolve 
    show alex smile 
    p "How about the horror tunnel right there? It doesn't look like it'll fall apart while we're inside."
    show paxton frown 
    show alex frown 
    show finn down frowntalk 
    f "It's probably a lame ride with plastic spiders and scarecrows."
    show finn smile 
    show paxton unsure frowntalk sweat 
    p "Hey! I like horror tunnels..."
    show paxton frown 
    show finn down frowntalk 
    f "God, there are so many things wrong with that sentence. Not even Cerberus would be scared of them— that's a big turn-off, wouldn't you say?"
    show finn frown 
    show alex shock 
    a "Cerberus? Who is that?"
    show alex frown 
    show paxton up frowntalk -sweat 
    p "Cerberus i—"
    show paxton down frowntalk 
    show finn unsure frowntalk 
    show zaina frown unsure
    f "Nothing."
    show paxton frown 
    show finn frown 
    show alex neutral frown sweat 
    an "..."
    show alex unsure 
    an "Why did Finn stop Paxton from explaining?"
    show paxton frowntalk 
    p "Whatever..."
    show paxton frown 
    show finn frowntalk down 
    show zaina down 
    f "Anyway, horror tunnels suck. End of the story."
    show finn frown 
    show paxton frowntalk 
    p "Stop with the sass, will you?"
    show paxton frown 
    show zaina down frowntalk 
    z "C'mon you two, stop it. I'm sure we can check out multiple rides before we need to go back."
    show zaina frown 
    show alex shock up 

    menu:
        "Well... if it helps, I like horror tunnels too.":
            show alex up frown sweat 
            show zaina down frowntalk   
            ## Zaina, smirking
            z "Well, that makes two of you. I can't understand what you enjoy so much about them— they're not even {i}scary.{/i}"
            show finn down talk 
            show zaina talk 
            show alex up shock sweat 
            f "It's just that Paxton hates spiders."
            show finn smile 
            show paxton down frowntalk at Transform: 
                linear 0.2 xalign 0.71 
                linear 0.4 xalign 0.69 
                linear 0.2 xalign 0.7 
            p "Hey! I don’t, I just... {nw}"
            show paxton sweat unsure 
            extend "don't like them."
            show alex unsure frown -sweat 
            show paxton -sweat frown 
            show finn talk 
            ## Finn, grinning
            f "Sure, and the water is just a little wet."
            show finn smile 
            show zaina frowntalk 
            z "Stop making fun of him about this, Finn— Paxton gets nightmares about spiders whenever you start talking about them."
            show zaina talk up 
            show alex smile up 
            show paxton unsure frowntalk  
            ## Paxton pouting/frowning
            p "C'mon Zaina, you too? I thought we were on the same side!"
            show paxton unsure frown 
            show zaina frowntalk 
            z "Well, you thought wrong."
            show zaina talk 
            show finn smile up 
            show alex talk 
            show paxton at Transform: 
                linear 0.2 xalign 0.71 
                linear 0.4 xalign 0.69 
                linear 0.2 xalign 0.7 
            an "I chuckle with Finn and Zaina as Paxton pouts."

        "To be honest, I don't mind horror tunnels.":
            show alex up smile -sweat 
            show zaina frowntalk up 
            show finn unsure 
            z "And that's why I like you the most in our group. You're the only person that makes sense if you don't count me."
            show zaina talk 
            show paxton talk up 
            ## Paxton, grinning
            p "More like \'if you especially count her.\'"
            show paxton smile 
            show zaina down frowntalk 
            z "Ugh, shut up."
            show zaina frown 
            show finn unsure frowntalk 
            f "I can't see why it doesn't make sense to not like horror tunnels. They're just... unlikeable. Very dislikeable. Whatever."
            show finn frown 
            show zaina frowntalk down at Transform:
                linear 0.3 xalign 0.25 
                linear 0.3 xalign 0.3 
            z "You shut up, too."
            show zaina talk up
            show finn frowntalk at Transform: 
                linear 0.25 yalign 1.5
                linear 0.25 yalign 1.0 
            f "I'm just saying! They're supposed to be scary, but they're not. They had one job, and they screwed it up."
            show finn frown 
            show zaina frowntalk 
            z "Okay, seriously. Shut up. I'm not going to listen to you lecturing us about horror tunnels— {nw}"
            show zaina down 
            extend "{i}again.{/i}"

        "Finn has never been more right than now.":
            show alex down talk -sweat
            show finn smile down 
            show paxton unsure frowntalk 
            a "Horror tunnels are awful."
            show paxton down frown 
            show alex smile 
            show finn talk 
            f "Oh, look! Another person with common sense!"
            show finn smile 
            show zaina down frowntalk 
            show paxton up smile 
            z "You're the last person that can make such a comment."
            show zaina frown 
            show paxton unsure talk 
            ## Paxton, grinning
            p "Wow, I think our friendship should end here, Alex. I feel betrayed."
            show paxton up smile 
            show zaina unsure frowntalk 
            z "Then what? You start, I don't know, being lovers or something? {nw}"
            show zaina up frowntalk 
            extend "You {i}do{/i} seem to have a slow burn or something going.."
            show zaina talk  
            show paxton up frowntalk blush #at Transform:
                #linear 0.2 xalign 0.71 
                #linear 0.4 xalign 0.69 
                #linear 0.2 xalign 0.7
            show alex up frowntalk blush #at Transform: 
                #linear 0.2 xalign 0.99 
                #linear 0.4 xalign 1.01 
                #linear 0.2 xalign 1.0 
            ## Paxton & Alex blushing
            pa "{size=+10}Zaina!{/size}" with hpunch
            show paxton frown unsure
            show alex frown unsure 
            show zaina unsure frowntalk 
            z "{i}What?{/i} You know I'm right."
            show zaina talk  
            show finn talk 
            f "Well, she has a point."
            show finn smile 

    show finn talk up 
    f "Whatever. I don't know about you all, but I want to try climbing the roller coaster tracks."
    show finn smile 
    show paxton -blush sweat unsure frown 
    show alex -blush -sweat up frown 
    ## Paxton, frowning/looking worried
    p "..."
    show paxton -sweat 
    show alex neutral frowntalk 
    a "That sounds... dangerous."
    show finn down talk 
    show alex frown 
    f "I know this'll surprise you, but this whole \'checking out old places\' thing is dangerous."
    show finn smile 
    show zaina unsure frowntalk 
    z "You won't change your mind no matter what we say, will you?"
    show zaina smile 
    show finn talk up 
    ## Finn, grinning
    f "You know me so well."
    show finn smile 
    show paxton sweat at Transform: 
        linear 0.2 xalign 0.71 
        linear 0.4 xalign 0.69 
        linear 0.2 xalign 0.7
    p "..."
    show paxton -sweat 
    show alex unsure 
    an "Paxton looks like he wants to say something."
    show alex neutral smile   
    an "I'm sure he'll tell Finn not to do it. He's way too cautious to let Finn do something like this."
    show finn talk up 
    f "I know what I'm doing. People besides us have been here recently and they all said the rides are in good shape— it should be safe to climb on the tracks."
    show finn smile 
    show zaina up frowntalk 
    show alex frown 
    z "At least you did your research."
    show zaina talk 
    show finn talk 
    f "I always do, and you know that."
    show finn smile 
    show zaina frowntalk 
    z "Well, I'm not coming. Try not to fall, will you?"
    show zaina talk 
    show paxton at Transform: 
        linear 0.2 xalign 0.71 
        linear 0.4 xalign 0.69 
        linear 0.2 xalign 0.7
    p "..."
    show alex unsure sweat 
    an "Why is Paxton hesitating? He should say something if he wants to stop Finn from going."
    show paxton frowntalk -sweat 
    show alex -sweat 
    p "Finn... be careful."
    show alex shock 
    an "He didn't tell Finn to stop?{nw}"
    show alex frown sweat 
    extend " But why?"
    show alex -sweat 
    show finn talk down 
    ## Finn, grinning/winking
    f "When am I not careful?"
    show finn smile 
    show zaina down frowntalk 
    z "How about always?"
    show zaina frown 
    hide finn with dissolve 
    show alex neutral frown sweat 
    an "I watch Finn walking away from us towards the roller coaster. His steps are filled with confidence, but I feel worried."
    scene bg amusementpark with fade 
    an "Finn starts climbing. I can't keep my eyes off of him— what if he slips?"
    an "He's moving too fast. He should be more careful."
    scene bg amusementpark with fade 
    show alex unsure frown at Transform: 
        linear 0.0 xalign 0.95 yalign 2.0 
        linear 1.5 xalign 1.0 
    with dissolve 
    $ renpy.pause(delay=1.5, hard=False) 
    show zaina down frowntalk at Transform: 
        linear 0.0 xalign 0.05 yalign -2.0 
        linear 1.5 xalign 0.0 
    with dissolve 
    z "He's being reckless."
    show zaina frown 
    show paxton down frowntalk hat at Transform: 
        linear 0.0 xalign 0.45 yalign 1.0 
        linear 1.5 xalign 0.5 
    with dissolve 
    p "Are you surprised that he is?"
    show paxton frown 
    show alex frowntalk 
    a "What if he slips?"
    show alex frown 
    show paxton frowntalk 
    p "Don't worry. It's not like the tracks are wobbling or anything. He should be fine."
    show paxton frown 
    show zaina up frowntalk 
    z "Yeah. Finn sometimes does things like this, don't worry about it too much."
    show zaina talk 
    show alex neutral sweat 
    a "..."
    show paxton at Transform: 
        linear 0.2 xalign 0.51 
        linear 0.4 xalign 0.49 
        linear 0.2 xalign 0.5
    ## Paxton, frowning
    p "..."
    show zaina frowntalk
    z "You can go take a walk, if you want. I'll keep an eye on Finn."
    show zaina talk 
    show paxton unsure frowntalk 
    p "You sure?"
    show paxton frown 
    show zaina frowntalk 
    z "Yeah, go on. I'll call for you if something happens."
    show zaina talk 
    show paxton talk up at Transform: 
        linear 1.5 xalign 0.55 
    p "Alright. Alex, want to come with me?"
    show paxton smile 
    show alex up frown blush 
    an "Me? Why would he ask me?"
    show alex unsure -sweat 
    ## Alex frowning/worried
    an "I still want to explore the amusement park... but is it okay to leave Finn like that? He can injure himself."
    show zaina frowntalk 
    z "Geez, don't look so worried. I got him, just go and have fun."
    show zaina talk 
    show alex -blush up shock 
    an "Oh... Did my face show what I was thinking? {nw}"
    show alex frown neutral blush 
    extend "How embarrassing."
    show alex -blush 
    show paxton talk 
    ## Paxton, smiling slightly
    p "Yeah, he'll be fine. So, want to explore this place with me?"
    show paxton smile 
    show alex smile up 
    show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
        alpha 0.0 xalign 1.0 yalign 2.0 
        linear 0.25 alpha 1.0 
        linear 0.25 alpha 1.0 
        linear 0.25 alpha 0.0 
    an "His smile helps me calm down. How does he do that?"
    hide ablush_temp 
    show alex unsure
    an "I really want to go. What's the worst thing that could happen if I agreed?"
    show alex up talk 
    a "Sure."
    show alex smile 
    scene bg amusementpark with fade 
    an "Paxton turns away from the roller coaster and starts walking away. I follow him right behind, trying to make sure we don't get separated."
    show alex at Transform: 
        xalign 0.5 yalign 2.0 
        linear 1.25 xalign 0.65 
    with dissolve 
    $ renpy.pause(delay=1.5, hard=False) 
    show paxton hat at Transform:
        xalign 0.5 yalign 1.0 
        linear 1.25 xalign 0.35 
    with dissolve 
    an "I try to walk by his side while looking around. In the distance, I can see a big Ferris wheel— it's lights aren’t on, but the view of it is still amazing despite how old and dirty it looks."
    show paxton talk  
    p "I used to come here when I was a little kid."
    show paxton smile 
    show alex shock at Transform: 
        linear 0.2 yalign 1.7 
        linear 0.2 yalign 2.0
    an "I jump a little when Paxton talks suddenly, startling me out of my thoughts."
    show alex frown blush 
    show paxton unsure talk 
    ## Paxton,smiling slightly
    p "Sorry, did I scare you?"
    show paxton smile 
    show alex talk 
    a "No, I was just looking around."
    show alex shock -blush 
    an "Does he want to tell me about his childhood?"
    show alex frown 
    menu:
        "Did your parents used to bring you here?":
            show alex smile 
            show paxton up talk 
            p "Yeah. I was so excited to see this place—it used to be very popular back then."
            show paxton smile 
            an "Imagining a small Paxton running around in an amusement park... {nw}"
            show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
                alpha 0.0 xalign 0.65 yalign 2.0 
                linear 0.25 alpha 1.0 
                linear 0.25 alpha 1.0 
                linear 0.25 alpha 0.0
            extend "he must've been adorable."
            hide ablush_temp 
            show alex talk 
            a "Did you have fun?"
            show alex smile 
            show paxton unsure talk at Transform: 
                linear 0.2 xalign 0.36 
                linear 0.4 xalign 0.34 
                linear 0.2 xalign 0.35 
            ## Paxton, laughing/smiling
            p "Are you kidding? No, I was scared to death! There were huge machines everywhere, and I saw a girl crying and throwing up at the entrance— I was {i}terrified{/i}."
            show paxton smile 
            show alex at Transform: 
                linear 0.2 yalign 1.9 
                linear 0.2 yalign 2.0 
            an "I can't keep myself from chuckling a little when I try to picture a small, wide-eyed Paxton, looking at Ferris wheel with horror."
            show alex talk 
            a "Well, how about now? Are you still scared?"
            show alex smile 
            show paxton talk unsure 
            p "This place is pretty much abandoned— everything's old, dusty and broken. It's like a horror movie."
            show paxton smile 
            show alex talk 
            a "I take that as a yes."
            show alex smile 
            show paxton up talk 
            ## Paxton, laughing/smiling
            p "You better."
            show paxton smile 
            show alex neutral 
            an "He's not wrong. Now that I think of it, this place could scare me a lot if I was alone. If Paxton wasn't here, it'd probably be terrifying."
            show paxton talk 
            p "How about you? Are you scared?"
            show paxton smile 
            show alex unsure frown 
            an "Am I scared?"


        "Did you like amusement parks?":
            ## Paxton, smiling
            show paxton up frowntalk 
            p "No, the opposite, actually. I was scared of them a lot."
            show paxton smile 
            show alex shock up
            an "Scared?"
            show alex frowntalk unsure 
            a "But why?"
            show alex frown 
            show paxton unsure frowntalk 
            p "I don't know. They just seemed too... busy. Too much. I didn't like seeing huge machines that threw people around."
            show paxton smile 
            show alex up 
            an "Now that he says it like that, I can see his point. It could be too much for a child."
            show paxton talk 
            p "I still don't like amusement parks that much. Only horror tunnels make me feel the way it's supposed to make me feel."
            show paxton smile 
            an "I wonder if he ever tried riding the Ferris wheel. {nw}"
            show alex neutral smile 
            show expression "images/sprites/alex extra1.png" as ablush_temp at Transform:
                alpha 0.0 xalign 0.65 yalign 2.0 
                linear 0.25 alpha 1.0 
                linear 0.25 alpha 1.0 
                linear 0.25 alpha 0.0
            extend "Maybe he can ride it with me one day?"
            hide ablush_temp 
            show paxton frowntalk 
            p "I'm a little nervous even now... How about you? Are you scared?"
            show paxton frown 
    show alex up talk 
    a "No. You're here, so I feel safe."
    show alex smile 
    ## Paxton, blushing
    show paxton up frowntalk blush at Transform: 
        linear 0.2 xalign 0.36 
        linear 0.4 xalign 0.34 
        linear 0.2 xalign 0.35 
    p "You— you do?"
    show paxton frown 
    show alex frown 
    an "He stopped walking. Why is he— {nw}" 
    show alex shock 
    extend "oh."
    an "I'm an idiot."
    show alex frown sweat blush 
    an "But it's not like what I said was a lie. I {i}do{/i} feel safe because he's here."
    show alex unsure frowntalk sweat 
    a "It's not like a murderous clown can attack me with you here. You can beat them up and save the day."
    show alex frown -sweat 
    show paxton talk 
    ## Paxton, grinning
    p "Yeah, I've been working out for so long {i}just{/i} to kick some clown's ass."
    show paxton smile -blush 
    show alex talk at Transform: 
        linear 0.2 yalign 1.9 
        linear 0.2 yalign 2.0 
    ## Alex, smiling
    an "I can’t help but laugh a little."
    show alex up smile 
    an "His eyes are shining... Is it because of the moonlight?"
    show alex neutral blush 
    an "He's also looking at me. This is so awkward, but at the same time I can feel how fast my heart beats."
    show alex unsure frown 
    an "I need to say something... but what?"
    ## Paxton, blushing/shy
    show paxton unsure frowntalk blush 
    p "Uh, we should get back. Finn's probably done with climbing around."
    show paxton frown 
    show alex frowntalk 
    a "Yeah, you're right."
    show alex up smile -blush 
    show paxton up smile -blush 
    an "We turn back and start walking towards where we left Zaina and Finn. The weird air dissipates."
    show alex talk 
    a "Can I ask you a question?"
    show alex smile 
    show paxton talk 
    p "Sure, shoot."
    show paxton smile 
    show alex talk 
    a "The lattes you make... why do you always put whipped cream or a lid on them?"
    show alex frown 
    hide paxton 
    show expression "images/sprites/paxton base.png" as pbase at Transform:
        xalign 0.35 yalign 1.0 
    show expression "images/sprites/paxton expression4.png" as ptalk at Transform:
        xalign 0.35 yalign 1.0 
    show expression "images/sprites/paxton outfit1.png" as pglass at Transform: 
        xalign 0.35 yalign 1.0 
    show expression "images/sprites/paxton brows1.png" as p_browup at Transform: 
        xalign 0.35 yalign 0.55
    show expression "images/sprites/paxton outfit2.png" as phat at Transform: 
        xalign 0.35 yalign 1.0 
    ## Paxton, surprised
    an "Why does he look so surprised that I noticed? Obviously something was up with how he always tried to distract me whenever I tried to look under the lid."
    hide pbase 
    hide ptalk 
    hide pglass 
    hide p_browup 
    hide phat 
    show paxton unsure sweat hat frowntalk at Transform: 
        xalign 0.35 yalign 1.0 
    p "The lid? It was— well, nothing, just cafe rules, y'know."
    show paxton frown 
    show alex unsure frown 
    an "{i}Cafe rules?{/i} Really? Couldn't he come up with something else?"
    show alex down frowntalk 
    a "A lid rule?"
    show alex frown 
    show paxton frowntalk at Transform: 
        linear 0.2 xalign 0.36 
        linear 0.4 xalign 0.34 
        linear 0.2 xalign 0.35 
    ## Paxton, panicked
    p "Yeah, exactly. It’s a safety thing. The lid, anyway."
    show paxton frown 
    show alex down 
    an "But I’ve been to cafes where they didn’t put a lid on... What is he trying to keep me from learning?"
    #programmed stop 

