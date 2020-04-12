###################################################################################################################
#######################                                                                 ###########################
#######################                         Paxton's Route                          ###########################
#######################                                                                 ###########################
###################################################################################################################

label paxtonroute:

######################################################
############## P A X T O N ## R O U T E ##############
######################################################

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

    play sound "phonevibrate.mp3"
    
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
            play sound "phonevibrate.mp3"
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
    play sound "phonevibrate.mp3"
    show alex shock sweat 
    an "He replied with sad emojis?"
    play sound "phonevibrate.mp3"
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
    
    show alex backpack at Transform:
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
    a "Well, what's up with that cup you have? Is it for me{nw}"
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
    # show paxton unsure frowntalk at Transform: 
    #     linear 0.2 xalign 0.21 
    #     linear 0.4 xalign 0.19 
    #     linear 0.2 xalign 0.2
    # ## Paxton, worried
    # show alex frown 
    # p "Wha— um, is it too, I don't know, sweet or—?"
    # show paxton frown 
    # show alex up smile 
    # an "Aw, he looks really worried."
    # ## Alex, smiling
    # an "I shouldn't feel this amused when he's like this, but I can't help it."
    # an "Enough playing around, I shouldn't make him worry too much..."
    # show alex talk 
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
    
    show alex unsure frown backpack at Transform:
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
    an "Oh... did my face show what I was thinking? {nw}"
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
    hide alex with dissolve 
    hide paxton with dissolve 
    $renpy.pause(delay=0.5, hard=False)
    show alex frown blush at closeright:
        yalign -0.7
    with dissolve 
    show paxton unsure talk hat at closeleft with dissolve 
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
            show expression "images/sprites/alex extra1.png" as ablush_temp at closeright:
                alpha 0.0 yalign -0.7
                linear 0.25 alpha 1.0 
                linear 0.25 alpha 1.0 
                linear 0.25 alpha 0.0
            extend "he must've been adorable."
            hide ablush_temp 
            show alex talk 
            a "Did you have fun?"
            show alex smile 
            show paxton unsure talk at Transform: 
                linear 0.2 xalign 0.06 
                linear 0.4 xalign 0.04 
                linear 0.2 xalign 0.05 
            ## Paxton, laughing/smiling
            p "Are you kidding? No, I was scared to death! There were huge machines everywhere, and I saw a girl crying and throwing up at the entrance— I was {i}terrified{/i}."
            show paxton smile 
            show alex at closeright: 
                linear 0.2 yalign -0.65 
                linear 0.2 yalign -0.7
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
            show expression "images/sprites/alex extra1.png" as ablush_temp at closeright:
                alpha 0.0 yalign -0.7  
                linear 0.25 alpha 1.0 
                linear 0.25 alpha 1.0 
                linear 0.25 alpha 0.0
            extend "Maybe he can ride it with me one day?"
            hide ablush_temp 
            show paxton frowntalk 
            p "I'm a little nervous even now... how about you? Are you scared?"
            show paxton frown 
    show alex up talk 
    a "No. You're here, so I feel safe."
    show alex smile 
    ## Paxton, blushing
    show paxton up frowntalk blush at Transform: 
        linear 0.2 xalign 0.06 
        linear 0.4 xalign 0.04 
        linear 0.2 xalign 0.05 
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
    show alex talk at closeright: 
        linear 0.2 yalign -0.65 
        linear 0.2 yalign -0.7 
    ## Alex, smiling
    an "I can’t help but laugh a little."
    show alex up smile 
    an "His eyes are shining... is it because of the moonlight?"
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
    show expression "images/sprites/paxton base.png" as pbase at closeleft
    show expression "images/sprites/paxton expression4.png" as ptalk at closeleft
    show expression "images/sprites/paxton outfit1.png" as pglass at closeleft
    show expression "images/sprites/paxton brows1.png" as p_browup at closeleft:
        yalign 0.11
    show expression "images/sprites/paxton outfit2.png" as phat at closeleft: 
    ## Paxton, surprised
    an "Why does he look so surprised that I noticed? Obviously something was up with how he always tried to distract me whenever I tried to look under the lid."
    hide pbase 
    hide ptalk 
    hide pglass 
    hide p_browup 
    hide phat 
    show paxton unsure sweat hat frowntalk at closeleft
    p "The lid? It was— well, nothing, just cafe rules, y'know."
    show paxton frown 
    show alex unsure frown 
    an "{i}Cafe rules?{/i} Really? Couldn't he come up with something else?"
    show alex down frowntalk 
    a "A lid rule?"
    show alex frown 
    show paxton frowntalk at Transform: 
        linear 0.2 xalign 0.06 
        linear 0.4 xalign 0.04 
        linear 0.2 xalign 0.05 
    ## Paxton, panicked
    p "Yeah, exactly. It’s a safety thing. The lid, anyway."
    show paxton frown 
    show alex down 
    an "But I’ve been to cafes where they didn’t put a lid on... what is he trying to keep me from learning?"

    menu:
        "The latte probably turns out to be a color it's not supposed to be.":
            show alex unsure frown 
            an "It'd explain why he always looks so worried before he puts the lid on."

        "Maybe he doesn't add the sauces he should've added on top?":
            show alex neutral frown 
            an "But that doesn't really seem like something Paxton'd do, does it?"
            
    show paxton up frowntalk 
    p "Anyway, what are you going to do when we're done here?"
    show paxton frown 
    show alex up smile 
    an "Good to know that he's awful at subtlety."
    show alex neutral 
    an "Well, I can try to ask him again later. Maybe I can peek under the lid the next time I visit him at the cafe?"
    show alex up talk 
    a "I don't know, I'll probably finish up my assignment. What about you?"
    show alex smile 
    show paxton talk -sweat
    p "I have a D&D session scheduled for tomorrow. I prepared a really cool boss—hopefully no one will try to seduce him into joining the party..."
    show paxton smile 

    ## Scene 4
    scene bg cafe with fadee 

    ## clinking sound effect, coming from the bell on the cafe's door when Alex opens it
    show alex unsure shock backpack at Transform: 
        xalign 0.75 yalign 2.0 
        linear 1.5 xalign 0.8 
    with dissolve 
    an "I slip inside the cafe with a sigh. I had to stay up late to finish my paper last night. My eyes are burning from sleep deprivation."
    show alex frown 
    an "Lately, my sleeping schedule is all messed up with urbexing and trying to catch up with school work."
    show alex up smile 
    an "Luckily, Paxton had already messaged me to ask me if I'd like to drop by the cafe when I woke up. He's literally a life saver."
    show alex frowntalk unsure 
    an "I really need a cup of coffee right now."
    show alex neutral frown 
    an "I walk deeper into the cafe. Just like I figured, {nw}"
    show alex up smile 
    extend "Paxton is standing at his usual place behind the counter with a cup in his hand."
    ## Paxton appears, serious/frowning/focused
    show paxton down frown apron at Transform: 
        xalign 0.25 yalign 1.0 
        linear 1.5 xalign 0.2 
    with dissolve 
    show alex talk 
    a "Please tell me that's for me."
    show alex smile 
    show paxton talk up 
    ## Paxton, smiling slightly
    p "Alex? Welcome back!"
    show paxton smile 
    show alex unsure 
    an "Oh, he also has bags under his eyes. He probably spent too much time working on creating a boss for his D&D campaign."
    show alex frown sweat 
    an "Mom would've been so shocked if she learned I knew so much about D&D. She'd tell me to go study instead of looking up games on the internet."
    show alex smile -sweat 
    an "But Paxton loves talking about it. I just don't want him to feel like he can't talk about his hobbies with me."
    show alex up 
    an "And he looks so happy when I surprise him with how much I know about the rules of D&D. His whole face lights up."
    show alex blush 
    an "I like making him happy."
    show alex talk -blush 
    a "So, is that for me?"
    show alex smile 
    show paxton talk 
    p "No, a customer called dibs on this one, sorry. But I can make you a drink right away."
    show paxton smile 
    show alex talk 
    a "Yes, please."
    show paxton frown down 
    show alex smile at Transform: 
        linear 1.0 xalign 0.78 
    an "I lean against the counter instead of going to sit down on one of the empty seats. I want to watch Paxton making the drink."
    show alex frown 
    an "Wow, he really knows what he's doing. He does everything so fast..."
    show alex unsure smile 
    an "What's with that serious look? It's like he's trying to keep someone from dying or something."
    show alex up blush 
    an "Seeing him so focused on making a latte is a little amusing."
    show alex -blush neutral frown 
    an "Will he put a lid on this time too? Maybe he'll forget and I'll get to see what he's trying to hide in that cup."
    ## Paxton, frowning
    show paxton unsure frown 
    show alex down 
    an "Oh no, he grabbed a lid again."
    show alex unsure 
    an "Well... next time, maybe."
    show paxton talk up
    p "Here you go."
    show paxton smile 
    show alex smile up
    an "I grab the cup from where he set it on the counter, careful not to burn my fingers."
    ## Alex, smiling
    show alex talk 
    a "Thanks."
    show alex smile 
    show paxton talk 
    ## Paxton, smiling slightly
    p "Anything for my guinea pig."
    show paxton smile 
    show alex frown blush 
    an "I can feel my breath getting caught in my throat. Drinking the latte now sounds like a good idea."
    show alex -blush down 
    an "Lifting the cup to my face, I throw a look towards Paxton."
    show paxton talk 
    ## Paxton, grinning
    p "Drink up."
    show paxton smile 
    show alex unsure 
    an "I can't lift the lid while he's looking... I can see that he knows I'm waiting for him to look away."
    show alex neutral frowntalk 
    an "Admitting defeat, I take a small sip from the latte. {nw}"
    show alex down frown 
    extend "{i}Next time, you'll find out what's under the lid, Alex. You really will.{/i}"
    show alex up 
    an "I can taste caramel? Mmm, this is so good..."
    show paxton frowntalk unsure 
    p "Did you like it?"
    show paxton frown 

    menu:
        "Yes, it's perfect! Thanks, Paxton.":
            ## Paxton, winking
            show alex smile 
            show paxton up talk 
            p "You're welcome—"
        "It could use a little bit more sugar, maybe?":
            ## Paxton, winking
            show alex unsure smile 
            show paxton unsure talk 
            p "Well, I'll make sure to note that down—"
            
    show paxton up frown 
    c "Hello, can I order, please?"
    show paxton talk 
    p "Enjoy your latte, Alex. Call for me if you need anything."
    show paxton smile 
    show alex talk 
    a "Okay."
    hide paxton with dissolve 
    show alex smile up 
    an "He's really good at his job, isn't he? Does he want to open his own cafe once he graduates?"
    show alex blush neutral 
    an "He looks good... being behind the counter suits him a lot."
    show alex up 
    an "I could get used to this—watching him work and drinking his lattes. It's so domestic and peaceful."
    show alex unsure frown -blush 
    an "This crush is getting out of hand... I should stop thinking about things like these. Mom would never approve of my feelings for Paxton."
    show alex neutral 
    an "She wants me to date a 'proper gentleman with a good career', whatever that means. She wouldn't like Paxton."
    show alex unsure 
    an "A creative writing major and a barista? Why did I have to pick him out of all these people?"
    an "..."
    show alex neutral 
    an "I take another sip from the latte. The drink feels like it's warming up my whole body."
    show alex unsure blush 
    an "But he's so sweet and caring and kind..."
    an "..."
    show alex smile 
    an "I could've done worse."
    show alex down frown -blush
    an "And it's not like Mom's the one who has a crush on Paxton. It's me who has to deal with these feelings. Shouldn't I be the judge of whether I like him or not?"
    an "..."
    show alex up smile blush 
    an "I really like his smile."
    an "Yeah, I could've done {i}a lot{/i} worse."

    
    ## Scene 5
    ## Old mansion bg
    scene bg mansion with fadee 

    show alex frown up backpack at Transform: 
        xalign 0.95 yalign 2.0 
        linear 1.5 xalign 1.0 
    with dissolve 
    an "This time, we're visiting an old mansion. I'm not sure whether we'll see anything interesting, since it's so close to our university—other students have surely visited this place before us."
    show alex down smile 
    an "Still, I can't wait to see more of it. The old mansions we see are always so fancy, despite how old and dirty they are."
    show alex up 
    an "Seeing the old rooms of the mansion's previous owners makes me feel... {nw}"
    show alex unsure 
    extend "nostalgic, maybe?"
    show alex frown 
    an "Just like I guessed, the building doesn’t look good on the inside either."
    show zaina down frowntalk at Transform: 
        xalign 0.0 yalign -2.2 
        linear 1.5 xalign -0.05 
    with dissolve 
    z "Watch your steps, everyone. The floor looks bad."
    show zaina talk 
    show finn down talk at Transform: 
        xalign 0.35 yalign 1.0 
        linear 1.5 xalign 0.3 
    with dissolve 
    f "Don't worry, what's the worst thing that could happen?"
    show finn smile 
    show zaina frowntalk 
    z "Ugh, don't jinx us, man."
    show zaina talk 
    show paxton hat down frowntalk at Transform: 
        xalign 0.65 yalign 1.0 
        linear 1.5 xalign 0.7 
    with dissolve 
    p "We should be careful. I can see a few holes in the floor ahead of us."
    show paxton frown 
    show alex up frown sweat 
    an "I look forward and realize that Paxton's right. Small holes litter the wooden floor, and it doesn't look stable enough to walk on."
    show finn up talk 
    f "As long as we watch our step, we should be—"
    show alex shock 
    an "Before Finn can finish his sentence, I feel myself tripping on something—"
    show alex unsure sweat frown
    show paxton frowntalk up 
    show finn talk up 
    show zaina frowntalk up 
    ## Alex, pained/worried/frowning I'm not sure??
    an "I try to throw my hands in front of myself to slow my fall, but it doesn't quite work out."
    show alex shock at Transform: 
        linear 0.5 yalign 4.0 
    with hpunch 
    a "Ah!"
    fpz "{size=+10}Alex!{/size}"
    show alex frown 
    show paxton frown 
    show finn frown 
    show zaina frown 
    an "My hands sting, braced on the floor, but I sigh with relief—I only fell on my knees and hands. It's not that bad."
    show alex frowntalk at Transform: 
        linear 0.2 xalign 1.01 
        linear 0.4 xalign 0.99 
        linear 0.2 xalign 1.0
    show paxton unsure 
    show finn unsure 
    show zaina unsure 
    a "Ugh, my hands..."
    show alex frown 
    an "I push myself back to sit back and take a look at my palms. The skin seems irritated, red around the parts that connected with the floor."
    ## Paxton, worried/frowning
    show paxton frowntalk unsure sweat 
    p "Alex, are you okay?"
    show paxton frown -sweat 
    show finn frowntalk down 
    f "You didn't get hurt, did you?"
    show finn frown 
    show alex unsure talk -sweat 
    a "I think I’m okay."
    show alex smile 
    show zaina frowntalk 
    z "Wait, I think I have a few bandages and some disinfectant in my bag."
    show zaina frown 
    show finn talk behind zaina 
    show paxton down 
    ## Finn, smiling a little
    f "You can thank me for that."
    show finn smile 
    show zaina down frowntalk at Transform: 
        linear 0.3 xalign 0.05 
        linear 0.3 xalign -0.05 
    z "It's not a good thing you get hurt so often that I need to carry a first aid kit with me, Finn."
    show zaina frown 
    show finn talk up 
    f "I think Alex disagrees with you right now."
    show finn smile 
    show alex up frown 
    an "Finn and Zaina seem to get along well. They tease each other and joke around a lot."
    show alex neutral 
    an "And they don't have that tense air Finn and Paxton do whenever they talk."
    show alex unsure 
    an "I can't help but wonder why..."
    show paxton down frowntalk 
    p "Zaina, can you give them here? I'll help patch up Alex— you can carry her backpack for her."
    show paxton frown 
    show alex frowntalk sweat -backpack 
    $ kneelflag = False 
    menu:
        "It's okay, I'm fine—":
            ## Paxton, smiling a little
            show alex unsure frown sweat 
            show paxton up talk behind alex at Transform: 
                linear 1.5 xalign 0.8 
            p "Don't worry, Alex. We'll just help you a little."
            show paxton smile 
            show alex neutral -sweat 
            an "..."
            show alex blush 
            an "His face is so warm and inviting..."
            show alex down 
            an "My heart is starting to beat so fast... c'mon, Alex, you're supposed to be injured here, not mooning over pretty boys.."

        "I think my hands are bleeding a little.":
            ## Paxton, frowning/worried
            show alex unsure frown sweat 
            show paxton unsure frowntalk behind alex at Transform: 
                linear 1.5 xalign 0.8 
                linear 0.75 yalign 3.5
            p "Here, let me take a look."
            show paxton frown 
            show alex -sweat 
            an "I let him grab my hands gently. He inspects the cuts on them."
            show paxton talk 
            p "It doesn't look too bad. It should be okay as long as we clean up the wounds properly."
            show paxton smile 
            $ kneelflag = True 
            
    show paxton talk up 
    p "Zaina, can you give the disinfectant to me?"
    show zaina up frowntalk at Transform: 
        linear 2.0 xalign 0.5 
    $renpy.pause(delay=0.5, hard=False) 
    if kneelflag == False: 
        show paxton smile at Transform: 
            linear 1.5 xalign 0.7 
    else: 
        show paxton smile at Transform: 
            linear 0.75 yalign 1.0 
            linear 1.5 xalign 0.7 
    show finn at Transform: 
        linear 1.5 xalign 0.1

    ## Zaina, lifting an eyebrow/frowning
    z "Sure, here. Take the bandages too."
    show zaina talk at Transform: 
        linear 1.5 xalign 0.3 
    $renpy.pause(delay=0.5, hard=False) 
    show finn at Transform: 
        linear 1.5 xalign -0.05 
    show paxton talk at Transform: 
        linear 1.5 xalign 0.8 
    p "Thanks."
    show paxton smile at Transform: 
        linear 0.75 yalign 3.5
    show alex frown up 
    an "Paxton kneels down in front of me and helps me sit more comfortably. Then, he takes my hands in his to check the damage."
    show alex blush 
    an "How embarrassing..."
    show alex -blush 
    show paxton talk 
    p "Well, you should be okay once we bandage these up. When we get back, we can clean it up properly— {nw}"
    show paxton down frowntalk 
    extend "it's too dark in here to see the wound clearly."
    show paxton frown 
    show finn up talk  
    f "We're done here, anyway. Zaina, let's take a look around to see if we left anything behind."
    show finn smile 
    show zaina frowntalk up 
    z "Sure, lead the way, captain."
    show zaina talk 
    show alex up frown 
    an "They're going together and joking around again... {nw}"
    hide finn with dissolve 
    hide zaina with dissolve 
    extend "I wonder why Paxton doesn't seem to want to join them with this— {nw}"
    show alex down shock sweat with hpunch
    extend "{i}ow!{/i}"
    
    hide alex with dissolve 
    hide paxton with dissolve 
    $renpy.pause(delay=0.25, hard=False)     
    show alex unsure shock sweat at closeright:
        yalign -0.7 
    with dissolve 
    show paxton down frown hat at closeleft with dissolve 
    a "It hurts!"
    show alex frown 
    show paxton unsure frowntalk 
    ## Paxton, worried/frowning
    p "I know, sorry—I had to use the disinfectant and thought it'd be better if I did it without warning you."
    show paxton frown 
    show alex down frowntalk -sweat 
    ## Alex, frowning/angry
    a "Why would you even think that?"
    show alex frown 
    show paxton unsure frowntalk 
    p "I just didn't want you to stress thinking over it. {nw}" 
    show paxton up talk 
    extend "Now it's all done, so we just need to bandage the wounds."
    show paxton smile 
    an "That's not a bad reason... still, I didn't expect him to do it so suddenly."
    show alex frowntalk 
    
    menu:
        "... alright.":
            show alex unsure frown 
            show paxton down frown 
            an "I watch his focused face as he wraps my hands and knees. The pain lessens, but the stinging I feel doesn't disappear."
        "Still... I could use a warning.":
            show paxton unsure talk 
            show alex frown  
            p "Sorry. I'll make sure to remember that if you get injured again."
            show paxton smile 
            show alex up smile 
            an "His eyes have such a kind look... I can feel myself losing my breath."

    show paxton talk up 
    p "There, all patched up."
    show paxton smile 
    show alex up talk 
    a "Thanks..."
    show alex smile 
    show paxton talk 
    ## Paxton, smiling a little
    p "Anytime. Now, to get you out of this place..."
    show paxton smile behind alex at Transform: 
        linear 2.0 xalign 0.6 
    show alex frown 
    an "He gets up from where he had been kneeling to lean down on me— and sneaks his arms behind my knees and back!"
    show alex shock unsure blush 
    a "W—wait!"
    show alex frown 
    show paxton down talk 
    ## Paxton, grinning
    p "Sorry, can't do that! You should've been more careful."
    scene PaxtonCG1
    with fade 
    #show paxton smile 
    an "He picked me up so easily! God, I can feel his muscles moving on my back..."
    ## Alex, blushing/embarrassed
    an "I know he works out a lot, but witnessing it first hand is... {nw}" 
    #show alex smile up 
    extend "{i}wow...{/i} I think I'm dying a little."
    scene PaxtonCG1 at Transform: 
        zoom 1.5 xpos -800 ypos 0
    with fade 
    #show paxton talk 
    p "Comfortable?"
    scene PaxtonCG1 at Transform: 
        zoom 1.5 xpos -900 ypos -300 
    with fade 
    #show paxton smile 
    #show alex down frown  
    an "This is so embarrassing!"
    #show alex frowntalk 
    a "P—put me down, I can walk. I just need a minute to rest, that's it!"
    #show alex frown 
    #show paxton talk 
    scene PaxtonCG1 at Transform: 
        zoom 1.5 xpos -800 ypos 0 
    with fade 
    p "Hmm... no, thank you, I'm quite happy right here."
    #show paxton smile 
    #show alex unsure -blush 
    scene PaxtonCG1 at Transform: 
        zoom 1.5 xpos -1280 ypos -300
        linear 5.0 zoom 0.8 xpos -250 ypos -50
    with fade 
    an "I should protest more, maybe I can make him listen to me."
    #show alex neutral 
    a "..."
    #show alex up blush 
    an "Well, it feels kind of warm and nice here. Maybe I can handle this treatment a little longer."
    #EVENT IMAGE: SOMETHING CUTE
    #Bridal carry!
    scene PaxtonCG1 with fadee 
    $renpy.pause(delay=5.0, hard=False) 
    ## black bg
    scene black with fadee 
    an "He carries me all the way out of the mansion, then to his car."
    show alex frown blush at closeright:
        yalign -0.7 
    with dissolve 
    show paxton frowntalk down hat at closeleft with dissolve 
    p "Let's get you to somewhere we can tend those wounds. You wouldn't want an infection, believe me."
    show paxton frown 
    show alex unsure shock 
    an "He seriously wants to accompany me all the way back?"
    show alex neutral frown 
    an "I can't even think of a reply..."
    show alex up frown -blush 
    an "He starts driving back— then I notice it!"
    show alex frowntalk 
    a "That's not the way to my apartment!"
    ## Paxton, frowning
    show alex frown 
    show paxton frowntalk up 
    p "Well, I didn't think you had everything we'd need to clean those scratches, so I'm driving back to my place. Is that okay?"
    show paxton frown 
    show alex unsure sweat 
    an "Is it? Can I trust him enough to go to his apartment?"
    show paxton unsure frowntalk 
    p "Just say the word, and I'll turn back. We can stop by a pharmacy and get everything you need."
    show paxton frown 
    a "..."
    show alex up frowntalk blush 
    a "No, it's okay. How much longer left until we arrive?"
    show alex unsure smile 
    ## Paxton, smiling slightly
    show paxton talk up 
    p "Not much, don't worry. {nw}"
    show paxton unsure frowntalk 
    extend "Does it hurt too much?"
    show paxton frown 
    show alex unsure talk 
    a "No, just stings."
    show alex smile 

    
    ## Scene 6
    ## Paxton's apartment bg
    scene black with fadee
    
    show alex frown up at Transform: 
        xalign 0.75 yalign 2.0 
        linear 1.5 xalign 0.8 
    with dissolve 
    an "Once we arrive at his apartment, Paxton allows me to walk to his flat's door from the car. I feel surprised that he let me do it."
    show paxton up talk hat at Transform: 
        xalign 0.25 yalign 1.0 
        linear 1.5 xalign 0.2 
    with dissolve 
    p "Here we are."
    show paxton smile 
    menu:
        "Are you sure I won't bother you? This is your flat, after all...":
            show paxton talk 
            p "Exactly— it's my flat, so it's okay. You won't bother me, don't worry."
            show paxton smile 
            show alex unsure 
            a "..."
            show paxton talk unsure 
            p "I'm serious. Stop frowning, it's fine. I'm not the one that should feel uncomfortable— you're in a guy's flat that you've known for not long at all."
            show paxton smile 
            show alex up talk 
            a "I trust you."
            show alex smile 
            show paxton blush talk 
            ## Paxton, blushing
            p "Y-you do?"
            show paxton smile 
            show alex neutral blush 
            an "I nod quietly."
            show paxton up talk 
            p "I’m glad."
            show paxton smile 

        "Why do you have enough things to take care of an injury in your flat?":
            show paxton down frowntalk 
            p "Well, it should be fairly obvious by now that Finn loves throwing himself into danger. Usually Zaina takes care of him, but sometimes we end up at my place instead."
            show paxton frown 
            show alex frowntalk 
            a "Huh... I guess that makes sense."
            show alex frown 
            show paxton frowntalk 
            p "Finn's reckless attitude gets old quick, believe me."
            show paxton frown 
    scene bg paxton_room night
    with fade
    #$renpy.pause(delay=3.0, hard=False)
    an "He opens the door, he helps me walk to a couch in his living room."
    show alex up frown at Transform: 
        xalign 0.75 yalign 2.0 
        linear 1.5 xalign 0.8 
    with dissolve
    $renpy.pause(delay=1.5, hard=False) 
    show paxton up frowntalk hat at Transform: 
        xalign 0.25 yalign 1.0 
        linear 1.5 xalign 0.2 
    with dissolve
    p "Sit here. I'll go get the first aid kit."
    show paxton frown 
    show alex frowntalk at Transform: 
        linear 1.5 yalign 3.0 
    a "Mhm."
    show alex frown 
    hide paxton with dissolve 
    ## Paxton disappears
    an "As he disappears behind a door, I study the room I'm in. Every item in the room seems to scream 'Paxton!'"
    show alex shock at Transform: 
        linear 0.2 yalign 2.9 
        linear 0.2 yalign 3.0 
    p "Found it!"
    show alex smile 
    show paxton up hat talk at Transform: 
        xalign 0.25 yalign 1.0 
        linear 1.5 xalign 0.2 
    with dissolve 
    ## Paxton appears
    p "Let's get you patched up."
    
    scene bg paxton_room night
    with dissolve 
    show alex neutral frown at closeright:
        yalign -0.9 xalign 0.8
    with dissolve 
    show paxton down frown hat behind alex at closeleft:
        xalign 0.5 
        linear 1.5 xalign 0.5 
        linear 1.5 yalign -0.3 
    with dissolve
    an "He kneels down in front of me and takes off the bandages to take a look at my knees. I can see some dried blood around the wound."
    show alex up 
    an "I watch him as he takes out new bandages, disinfectant, and a few more things I've never had to use before from the first aid kit."
    show alex unsure 
    an "I probably should learn how to take care of a wound if I want to continue urbexing with him and the others. I watch him carefully as he cleans up my knees."
    show alex up 
    show paxton up frowntalk 
    p "Tell me if it hurts, alright?"
    show paxton frown 
    show alex frowntalk 
    a "Okay."
    show alex neutral smile 
    an "Despite his warning, it barely hurts with how careful he is. The disinfectant is also not as painful since Paxton used it back at the mansion too."
    show paxton frowntalk 
    p "Alright, let me see your hands. They were hurt, too."
    show paxton frown 
    show alex up 
    an "I extend my hands to him wordlessly. He shows the same attention to them, gentle and patient."
    show paxton talk at closeleft: 
        linear 1.5 yalign 0.1 xalign 0.5
        linear 1.5 xalign 0.05 
    p "I think we're good now."
    show paxton smile 
    show alex talk 
    a "Thank you."
    show alex smile 
    show paxton talk 
    ## Paxton, smiling
    p "Don't even mention it. Now, are you hungry?"
    show paxton smile 
    show alex at closeright: 
        xalign 0.8 yalign -0.9
        linear 0.2 xalign 0.81 
        linear 0.2 xalign 0.8
    an "I shrug, but Paxton takes it as a yes."
    show paxton talk 
    p "Good! I can make a decent omelette— I'm no cook by any means; desserts and lattes are more of my expertise."
    show alex up frown 
    hide paxton with dissolve 
    ## Paxton disappears
    an "I wonder if he realizes that he's babying me?"
    show alex neutral 
    an "It kind of reminds me of Mom and Dad's demeanor. They always try to take care of me, too."
    show alex up 
    an "But for some reason, this doesn't feel as cloying and uncomfortable as it does when they do it."
    show alex smile 
    an "It's actually the opposite. When Paxton tries to take care of me, {nw}" 
    show alex blush 
    extend "it feels... nice."
    ## Paxton appears, smiling
    show alex -blush  
    show paxton up talk hat at closeleft with dissolve 
    p "Dinner—er, breakfast is ready!"
    show paxton smile 
    an "He comes out of the kitchen with two plates in his hands and gives one to me. {nw}"
    show alex frown 
    extend "He doesn't sit, though—I wonder why?"
    show paxton unsure talk 
    p "Don't judge me for making eggs—it's technically past midnight, so now's breakfast time."
    show paxton smile 
    ## Alex, smiling
    show alex talk 
    a "I can agree to that."
    show alex smile 
    an "I taste the omelette and let out an approving hum. It's good, and it makes me feel a bit better."
    show alex talk 
    a "Are you this nice to everyone?"
    show alex smile 
    show paxton talk 
    ## Paxton, laughing/smiling
    p "Nah, I just like being useful."
    show paxton smile 
    show alex shock 
    an "Useful?"
    ## Alex, smiling slightly
    show alex talk 

    menu:
        "Well, it'd be more useful if you could sit down with me.":
            ## Paxton, blushing/shy
            show paxton unsure frowntalk 
            show alex smile 
            p "Oh, um... you sure?"
            show paxton frown 
            show alex talk 
            a "Never been more sure. Come on."
            show alex smile 
            show paxton talk 
            p "Uh, okay."
            show paxton smile 
        "Why are you standing?":
            ## Paxton, blushing/shy
            show alex frown 
            show paxton talk blush unsure 
            p "Well, I don't know? I just didn't want to make you feel uncomfortable."
            show paxton smile 
            show alex smile blush 
            an "He's really sweet..."
            show alex talk -blush 
            a "It's okay. You shouldn't eat standing, anyway. Sit down with me?"
            show alex smile 
            show paxton talk -blush 
            p "Uh, alright..."
            show paxton smile 

    show alex up frown 
    show paxton at Transform: 
        linear 1.5 yalign -0.3 
    an "I've been sore and cold since we left the mansion, {nw}" 
    show paxton up talk 
    show alex smile 
    show paxton at Transform: 
        linear 0.2 xalign 0.06 
        linear 0.4 xalign 0.04 
        linear 0.2 xalign 0.05         
    extend "but when Paxton chuckles a little and settles down next to me, I forget how bad I feel."
    show paxton smile 
    an "We silently continue eating. By the time my plate is empty, I feel weariness settling over me like a heavy blanket."
    scene black with fadee 
    ## Black bg
    ## Paxton disappears
    an "{cps=1}...{/cps}"
    #an "..."
    #an "..."
    #an "..."
    an "I feel myself waking up when something moves under my head. I try to open my eyes tiredly."
    
    scene bg paxton_room night
    with dissolve 
    ## Paxton's apartment bg, but darker since the lights are turned off
    ## Paxton appears, smiling slightly/fondly 
    
    show alex neutral frowntalk behind black at closeright:
        yalign -0.9 xalign 0.8
    with dissolve
    show paxton apron behind black at closeleft with dissolve 
    a "...hmm?"
    show alex up frown 
    an "Did I fall asleep?"
    show paxton talk 
    p "Shh, it's okay. Go back to sleep, I'm just going to the cafe for my shift."
    show paxton smile 
    show alex neutral 
    an "I blink wearily and notice that he has a blanket in his hands. He slowly covers me with it."
    show alex frowntalk 
    a "Are you... leaving?"
    show alex frown 
    show paxton unsure talk 
    p "Yeah, sorry. "
    show paxton up 
    extend "I left something to eat in the fridge for when you wake up."
    show paxton smile 
    show alex up 
    a "..."
    show alex neutral  
    an "My eyes are closing, but I don't want to sleep again."
    show alex unsure 
    an "I want to go with him."
    show alex frowntalk 
    a "Can I come?"
    show alex frown 
    show paxton unsure talk 
    ## Paxton, smiling gently
    p "Maybe next time."
    show paxton smile behind alex at Transform: 
        linear 5.0 xalign 4.0
    an "He leans down, closer and closer to me— {nw}" 
    show paxton unsure frown blush at Transform: 
        linear 1.5 yalign -0.5 
    extend "then stops. I can feel his breath, but he doesn't move."
    show paxton talk 
    p "Can I have a goodbye kiss?"
    show paxton smile 
    show alex up 
    an "..."

    menu:
        "He doesn't even need to ask.":
            # scene paxtoncg2 at Transform: 
            #     xpos -851 ypos -480
            # with fade 
            an "Instead of answering, I tilt my head up to press my lips against his."
            # scene paxtoncg2_1 with fadee 
            # #EVENT IMAGE: FIRST KISS
            # $ renpy.pause(delay=5.0, hard=False)
            an "I feel sleep leaving my senses slowly. We don't move, enjoying the peaceful, warm moment."
            scene bg paxton_room night 
            with fade
            ## Paxton smiling
            show alex unsure blush at closeright: 
                yalign -0.9 xalign 0.8 
            with dissolve 
            show paxton apron blush at closeleft:
                yalign -0.3
            with dissolve 
            an "Paxton draws back at last. I open my eyes to see his small, kind smile."
        "I don't feel like kissing him on the lips, so I lean up to kiss his cheek.":
            ## Paxton, blushing/shy
            show alex unsure smile blush at Transform: 
                linear 0.3 xalign 0.75  yalign -0.9
                linear 0.3 xalign 0.8 yalign -0.9
            show paxton unsure talk blush 
            p "Thanks... I already feel like this is going to be a great day."
            show paxton smile 
            show alex neutral 
            an "My heart skips a beat. Blushing looks so good on him...  it's not fair."
            show alex up shock 
            an "He lowers his head to leave a kiss on my brow. My stomach lurches almost painfully, but I welcome the sensation."
            show alex frown 
            an "I really want to go and get some breakfast with him...{nw}"
            show alex unsure
            extend "it's just my luck that he needs to go to work."

    show paxton up talk -blush 
    p "See you at the sanitorium tonight."
    show paxton smile 
    show alex talk -blush 
    a "Have fun at work."
    show alex smile blush 
    show paxton blush behind alex: 
        linear 1.5 yalign 0.1 
        linear 3.0 xalign 0.7
        linear 1.5 yalign -0.3 
    an "He leaves another kiss on my nose, then stands up again."
    show paxton: 
        xalign 0.7 
        linear 1.5 yalign 0.1 
        linear 3.0 xalign 0.05
    $renpy.pause(delay=4.5, hard=False)
    hide paxton with dissolve 
    show alex unsure 
    an "As he leaves the flat, I realize that I won't be going back to sleep anytime soon."

    
    ## Scene 7
    scene bg hospital with fadee 

    show alex backpack at Transform: 
        xalign 0.95 yalign 2.0 
        linear 1.5 xalign 1.0 
    with dissolve 
    an "Our next visit is to an old sanitorium people used to go for the treatment of tuberculosis. I feel excited to explore it, despite how fragile the building looks."
    show alex neutral frown 
    show finn at Transform: 
        xalign 0.0 yalign 1.0 
        linear 1.5 xalign -0.05 
    with dissolve 
    an "Finn looks like he enjoys taking the risk that's climbing up high and higher. I'm worried about him."
    show alex unsure
    an "I wonder if he'll try to go up to the roof. What if the upper floors can't hold his weight?"
    an "I follow the group upstairs again. The floor feels unstable under my feet, and I can feel my heart ramming against my ribs."
    show paxton down hat frowntalk at Transform: 
        xalign 0.65 yalign 1.0 
        linear 1.5 xalign 0.7
    with dissolve 
    ## Paxton, frowning
    p "Well, I think that's it for me. I don't want to go up any higher."
    show paxton frown 
    show finn up frowntalk 
    f "Really? We're only halfway to the top."
    show finn frown 
    show paxton frowntalk 
    p "This seems too dangerous to me, Finn. We should stop here."
    show paxton frown 
    show finn down frowntalk 
    ## Finn, frowning
    f "I want to continue climbing a little more. The scene up there must be really cool."
    show finn frown 
    show zaina down frowntalk at Transform: 
        xalign 0.35 yalign -2.0 
        linear 1.5 xalign 0.3 
    with dissolve 
    z "We're not climbing all the way up, Finn."
    show zaina frown 
    show finn frowntalk 
    f "Why not? I'm careful enough."
    show finn frown 
    show zaina frowntalk 
    z "Paxton's right, it's too dangerous."
    show zaina frown 
    show finn frowntalk 
    f "Well, you don't have to come with me. I'll just take a quick look and come back down soon anyway."
    show finn frown 
    show zaina unsure frowntalk 
    z "If that's what you want..."
    show zaina frown 
    show paxton unsure frown 
    show alex neutral frown
    ## Paxton frowning/worried
    an "Paxton looks worried..."
    show alex unsure 
    an "I wonder what’s on his mind..."
    show finn frowntalk 
    f "C'mon, let's continue."
    show finn frown 
    show paxton down frowntalk 
    p "I'll be waiting here."
    show paxton frown 
    show zaina up frowntalk 
    z "Try not to injure yourself. We'll come back soon."
    show zaina frown 
    show alex up shock -sweat 
    an "We'll leave Paxton here alone?"

    menu:
        "I glance back to Paxton, then follow Finn and Zaina upstairs carefully.":
            ## Paxton is left behind
            show zaina at Transform: 
                linear 1.5 xalign 0.5 
            show alex unsure frown 
            hide paxton with dissolve 
            an "This really doesn't look safe. I can see cracks on the walls."
            show zaina unsure frowntalk 
            z "Hey, Finn."
            show zaina frown 
            show finn up talk 
            f "Hmm?"
            show finn frown 
            show zaina frowntalk 
            z "I'll stop here. I don't think any of us should go up further, the roof can collapse on us if we push our luck too much."
            show zaina frown 
            show finn unsure frowntalk 
            ## Finn, frowning
            f "Zaina..."
            show finn frown 
            show zaina down frowntalk 
            z "No, you can't convince me with your puppy eyes. Don't even try it."
            show zaina frown 
            show alex sweat at Transform: 
                linear 0.2 xalign 1.01 
                linear 0.4 xalign 0.99 
                linear 0.2 xalign 1.0 
            an "I think I should stop here, too. My heart feels like it's about to burst out of my chest."
            show alex down 
            an "This is enough of an adventure for me."
            show alex frowntalk -sweat 
            a "I'll stay here too."
            show alex frown 
            show finn down frowntalk at Transform: 
                linear 0.2 yalign 1.5 
                linear 0.2 yalign 1.0 
            ## Finn pouting/frowning
            f "I'll go alone, then."
            hide finn with dissolve 
            ## Finn leaves
            show zaina down frowntalk at Transform: 
                linear 1.5 xalign 0.2 
            $renpy.pause(delay=1.5, hard=False) 
            show alex at Transform: 
                linear 1.5 xalign 0.8 
            z "He just loves risking his life."
            show zaina frown 
            show alex unsure frowntalk 
            a "That doesn't sound good."
            show alex frown 
            show zaina frowntalk 
            z "Yeah, no kidding. Paxton hates when he does things like this."
            show zaina frown 
            show alex neutral
            an "But then why didn't he speak up when Finn told us he wanted to go all the way up?"
            show alex frowntalk 
            a "Is that why they don't get along like you and Finn do?"
            show alex frown 
            show zaina frowntalk 
            z "I'm down for a little bit of excitement." 
            show zaina unsure 
            extend "Paxton just doesn't like the thought of us getting hurt."
            show zaina frown 
            show alex up talk 
            a "You're his friends. Of course he doesn't like it."
            show alex smile 
            show zaina down frowntalk 
            z "Well, he doesn't act like it."
            show zaina frown 
            show alex shock 
            an "Huh?"
            show alex frowntalk 
            a "What do you mean?"
            show alex frown 
            show zaina frowntalk 
            z "You noticed it too, didn't you? Paxton always puts distance between us and him— he never lets us do things when he can do them himself."
            show zaina frown 
            show alex unsure sweat 
            an "... that's not entirely wrong. He did carry me all the way back when I could walk myself."
            show alex -sweat 
            show zaina frowntalk 
            z "Maybe he just doesn't trust us, I don't know."
            show zaina frown 
            show alex neutral 
            an "Is Zaina right? I don't feel like Paxton's that kind of person. I always feel like he cares about his friends so much."
            show alex frowntalk 
            a "Did you guys ever talk about it with Paxton?"
            show alex frown 
            show zaina down frowntalk 
            z "Paxton doesn't like talking about this stuff. And it must be fairly obvious, but neither does Finn."
            show zaina frown 
            show alex unsure 
            an "I can see what she's talking about..."
            show alex neutral 
            an "I wonder how Paxton is? Is he feeling sad that we left him downstairs?"
            show alex unsure 
            a "..."
            show alex frowntalk 
            a "Hey, I think I'll go check on Paxton."
            show alex frown 
            show zaina up frowntalk 
            ## Zaina, smiling slightly
            z "Okay. I'll go catch up with Finn and try to keep him from being an idiot. Be careful on your way."
            show zaina talk 
            show alex talk up
            ## Alex, smiling slightly
            a "You too."
            show alex smile 
            hide zaina with dissolve 
            ## Zaina leaves
            scene bg hospital with fade
            an "I slowly go back downstairs. The floor there feels more stable compared to the upper floors."
            ## Paxton appears, frowning/serious looking/miffed/annoyed, any of these work
            show alex backpack frown at Transform:
                xalign 0.75 yalign 2.0 
                linear 1.5 xalign 0.8 
            with dissolve 
            $renpy.pause(delay=1.5, hard=False) 
            show paxton hat down frown at Transform:
                xalign 0.25 
                linear 1.5 xalign 0.2
            with dissolve 
            an "I can see Paxton sitting on an old desk by the windows. I walk towards him with careful steps."
            show alex frowntalk 
            a "Hi."
            show alex frown 
            show paxton frowntalk 
            p "Oh, hey."
            show paxton frown 
            hide alex with dissolve 
            $renpy.pause(delay=0.5, hard=False)
            hide paxton with dissolve

        "I'll stay here, too.":
            ## Finn, frowning
            show alex frown 
            show finn down frowntalk 
            f "C'mon, Alex, not you too!"
            show finn frown 
            show paxton down frowntalk 
            p "It's her choice if she wants to have some common sense."
            show paxton frown 
            show finn frowntalk 
            f "We're trespassing in an abandoned sanitorium, Paxton. That stopped being a valid excuse the second you agreed to come here."
            show finn frown 
            show zaina down frowntalk with hpunch 
            ## Zaina, frowning/angry
            z "Boys! {nw}"
            extend "Stop acting like children!"
            show zaina frown 
            show paxton frowntalk at Transform: 
                linear 0.2 xalign 0.71 
                linear 0.4 xalign 0.69 
                linear 0.2 xalign 0.7 
            ## Paxton frowning/angry
            p "Whatever."
            show paxton frown 
            show alex unsure frown 
            an "I hesitate. Should I follow Finn and Zaina upstairs?"
            show zaina up frowntalk 
            z "Hey, Alex. You can stay here with Paxton. Finn and I will get back here soon, too."
            show zaina talk  
            show alex talk 
            a "Okay... be careful up there."
            show alex smile 
            show zaina frowntalk 
            z "Yeah, you two too. This place looks like it's looking for an excuse to fall apart."
            show zaina talk 
            show finn talk 
            f "That's what makes this more fun."
            show finn smile 
            show zaina down frowntalk 
            z "God, just shut up and continue walking before my patience snaps—"
            show zaina frown 
            show alex neutral smile 
            an "I watch them as they leave, then glance back to Paxton."
            hide zaina with dissolve 
            hide finn with dissolve 
            show alex unsure frown 
            show paxton up frown at Transform: 
                linear 2.0 xalign 0.2 
            an "He walks towards a dusty table by one of the broken windows to settle down on it."

            hide alex with dissolve 
            $renpy.pause(delay=0.5, hard=False)
            hide paxton with dissolve 
    show alex up frown blush at closeright:
        yalign -0.7 
    with dissolve 
    show paxton up frown hat at closeleft with dissolve 
    an "I join him by sitting on the table by his side. I can feel his thigh touching mine over the cloth."
    show paxton down frowntalk 
    show alex -blush
    p "Didn't want to continue going up?"
    show paxton frown 
    show alex frowntalk 
    a "No, I've had enough climbing for today."
    show alex frown 
    show paxton frowntalk 
    p "Well, that makes two of us."
    show paxton frown 
    show alex unsure sweat 
    an "He sounds annoyed. Is he angry at Finn for not stopping?"
    show alex -sweat frowntalk 
    a "Want to talk about it?"
    show alex frown 
    show paxton frowntalk 
    show alex neutral 
    p "No."
    show paxton unsure frown at Transform: 
        linear 0.25 xalign 0.06 
    p "..."
    show alex neutral 
    show paxton sweat at Transform: 
        linear 0.25 xalign 0.05
    ## Paxton, frowning
    p "..."
    show alex up 
    show paxton down frowntalk 
    p "It's just— he's so {i}annoying!{/i} He never listens to me, and I can't push him either because then— then he'd hate me and he's so stubborn!"
    show paxton -sweat at Transform: 
        linear 0.35 xalign 0.08 
    p "He's so frustrating and he makes me worry so much! {nw}"
    show paxton at Transform: 
        linear 0.2 xalign 0.08 
        linear 0.7 xalign 0.02 
    extend "I swear, I'm going to be bald by the time I'm 30 because of his reckless attitude. {nw}" 
    show paxton at Transform: 
        linear 0.2 xalign 0.02 
        linear 0.35 xalign 0.05 
    extend "I can take only so much of him being a daredevil!"
    show paxton frown 
    show alex neutral 
    an "..."
    show alex unsure 
    an "Wow... he's really done with how careless Finn is with his own life, isn't he?"
    show alex up 
    an "I can understand his worry. He just wants his friend to be safe."
    show alex frowntalk 
    a "Did you try to talk to Finn about this?"
    show alex frown 
    show paxton frowntalk 
    p "Of course not, I can't— {nw}" 
    show paxton unsure 
    extend "I don't want him to push me away just because I can't handle a little excitement."
    p "And if he decides I'm too much of a scaredy cat to hang out with him, Zaina'll also stop talking with me. They’re close."
    show paxton frown 
    show alex unsure 
    an "Does Paxton really think they would stop talking to him if he shows how worried he is for them?"
    show alex neutral 
    an "That doesn't sound right. They're friends, they should be there for each other..."
    show alex sweat 
    an "Poor Paxton... he seems like he's been thinking about this for some time. He must've stopped himself from showing how he actually feels for so long..."
    show alex -sweat unsure  
    an "He shouldn't feel like that. Zaina and Finn are his friends, no matter what. They care about Paxton too, I can see that."
    show alex down 
    an "I can't let him beat himself up over something like this. He did nothing wrong."
    show alex frowntalk 
    a "Paxton... listen."
    show alex unsure 
    a "I understand you're worried about losing them, but they're your {i}friends.{/i} They wouldn't ditch you just because you care about them too much."
    show alex down 
    a "Zaina wouldn't choose Finn over you, just like how she wouldn't choose you over Finn. She cares about you both."
    show alex up 
    a "And I think that even if Finn doesn't outright listen, he might take it to heart that someone is worried about him this much. {nw}" 
    show alex talk 
    extend "You should speak with him."
    show alex smile 
    show paxton down frown 
    p "..."
    show paxton unsure frowntalk 
    p "Maybe you're right, but if not, I might lose them. I don't want to risk losing my friends..."
    show paxton frown 
    show alex unsure 
    an "So that's the problem... he doesn't want to lose his friends."
    show alex up talk 
    a "Paxton... friends come and go. That's just how it is. You shouldn't try to be someone you're not just to keep them with you a little while longer."
    show alex smile 
    show paxton unsure frowntalk sweat 
    p "But if I stop them from doing dangerous things like this, they can just stop inviting me to go with them."
    show paxton frown 
    show alex talk 
    menu:
        "They wouldn't leave you behind. And you like urbexing, don't you?":
            show paxton frowntalk 
            show alex smile 
            p "I mean, it's fun when we do it together. I don't want to stop doing this."
            show paxton frown 
            show alex talk 
            a "Exactly. You don't want to stop them, you just want them to watch out for themselves more. There's nothing wrong with that."
            show alex smile 

        "You've been with them from the start. They wouldn't ditch you just like that.":
            show paxton frowntalk 
            show alex smile 
            p "Really? {nw}"
            show paxton down 
            extend "Because I don't feel like that's actually true."
            show paxton frown 
            show alex unsure shock 
            a "They wouldn't! You guys are friends— {nw}"
            show alex talk 
            extend "really close friends. Don't underestimate that relationship so easily."
            show alex up smile 

    show paxton -sweat frowntalk unsure at Transform: 
        linear 0.25 xalign 0.06 
        linear 0.5 xalign 0.04 
        linear 0.25 xalign 0.05
    show alex up smile 
    an "I can hear him sighing... {nw}" 
    show paxton frown 
    extend "maybe we're making progress here."
    show paxton frowntalk 
    p "Do you really think so?"
    show paxton frown 
    show alex up talk 
    a "I know so."
    show alex smile 
    show paxton talk 
    ## Paxton, smiling slightly
    p "Thanks, Alex."
    show paxton smile 
    show alex blush frown 
    an "His smile always manages to stun me, but this time... this time I can see his emotions playing on his face."
    show alex unsure smile 
    an "I feel like the air in my lungs isn't enough... his face is so open and inviting."
    show alex talk 
    a "You're welcome—"
    show zaina down frowntalk behind alex at Transform: 
        xalign 0.6 yalign -4.0  
    with dissolve 
    show alex shock -blush at closeright: 
        linear 0.2 yalign -0.6 
        linear 0.2 yalign -0.7 
    show paxton frowntalk up at Transform: 
        linear 0.2 yalign 0.2 
        linear 0.2 yalign 0.1 
    z "—my god, you need to stop being so damn stupid. I'm not putting up with this shit any longer, I swear..."
    show zaina frown 
    show finn up talk behind zaina at Transform: 
        xalign 0.75 zoom 0.8 yalign 1.0 
    with dissolve 
    f "Stop fretting, Zaina, I'm fine. You're worrying too much."
    show finn smile 
    ## Zaina and Finn appear. Zaina looks angry/frowning and Finn is bored
    an "I look towards the stairs and see Zaina and Finn coming down. Zaina seems to be poking Finn's arm angrily, but Finn is just waving her off."
    hide finn with dissolve 
    hide zaina with dissolve 
    hide paxton with dissolve 
    hide alex with dissolve 
    $renpy.pause(delay=0.5, hard=False) 
    show alex unsure frown at Transform: 
        xalign 0.95 yalign 2.0 
        linear 1.5 xalign 1.0 
    with dissolve 
    $renpy.pause(delay=1.5, hard=False) 
    show zaina frowntalk down at Transform: 
        xalign 0.0 yalign -2.0 
        linear 1.5 xalign -0.05 
    with dissolve 
    z "Well, I'll calm down when you stop being so stupid!"
    show zaina frown 
    show finn talk at Transform: 
        xalign 0.35 yalign 1.0 
        linear 1.5 xalign 0.3 
    with dissolve 
    f "So never, then?"
    show paxton unsure frown hat at Transform: 
        xalign 0.65 yalign 1.0 
        linear 1.5 xalign 0.7
    with dissolve 
    show finn smile 
    z "..." 
    show alex up frown 
    an "They're back... I look at Paxton to make sure he's okay."
    ## Paxton, looking worried
    show paxton unsure frown 
    show alex unsure 
    an "He seems uneasy... I hope he'll be okay."
    show alex shock 
    show paxton behind alex at Transform: 
        linear 1.5 xalign 0.75 
    an "Oh, he's looking back to me. Does he need some support?"
    show alex unsure frown blush 
    an "He has really effective puppy eyes. I want to go on and hug him until he feels better."
    show paxton up frowntalk 
    p "Hey..."
    show paxton frown 
    show alex shock up -blush 
    an "!!"
    show alex frown 
    an "Is he going to tell them how he's feeling? Did our talk really help him?"
    show alex smile 
    show finn talk up 
    f "Yeah?"
    show finn smile 
    show paxton down frowntalk 
    p "You two should be more careful."
    show paxton frown 
    show alex talk 
    an "!!"
    show alex smile 
    show finn down frown 
    f "..."
    show zaina frowntalk down 
    z "He's right."
    show zaina frown 
    show alex frown neutral 
    an "My stomach tightens with the rush of emotions I feel. It’s hard to really tell them apart, but there's one feeling that shows itself most."
    show alex smile 
    an "Paxton really voiced his opinion—it wasn't anything big, but it's still a start for them to fix their relationships with each other."
    show alex up blush
    an "I feel really proud of him for taking that step."

    ## Scene 8
    scene bg cafe with fadee 

    ## clinking sound effect, coming from the bell on the cafe's door when Alex opens it
    
    show alex backpack at Transform: 
        xalign 0.75 yalign 2.0 
        linear 1.5 xalign 0.8 
    with dissolve 
    an "I decided to visit Paxton at the cafe again. {nw}"
    show alex unsure frown 
    extend "The last time we saw each other, he was really stressed..."
    show alex up 
    an "He must be behind the counter. I'm getting used to dropping by here to see him."
    show alex smile blush 
    an "I'm strangely okay with that. I like seeing him."
    show alex -blush frown down sweat
    an "I should add that thought to the 'list of things Mom and Dad should never learn.'"
    show paxton down frown apron at Transform: 
        xalign 0.25 yalign 1.0 
        linear 1.5 xalign 0.2 
    with dissolve 
    show alex up smile -sweat 
    ## Paxton appears, looking angry
    an "There Paxton is!"
    show alex shock 
    an "Why is he frowning? That doesn't seem very... {nw}"
    show alex frown 
    extend "\'Paxton-like.\' Did something happen?"
    show alex frowntalk 
    a "Paxton?"
    show alex frown 
    show paxton frowntalk 
    p "Oh, welcome back, Alex."
    show paxton frown 
    show alex unsure 
    an "He doesn't sound really happy. The opposite, actually, he still looks angry."
    show alex frowntalk 

    menu: 
        "Is everything okay?":
            show paxton frowntalk 
            show alex frown 
            p "Yeah, sorry, I'm just— can we talk? On my break, I mean, I just..."

        "Did something happen?":
            show paxton frowntalk 
            show alex frown 
            p "No— well, kind of. Are you free at noon? We can talk about it on my break if you're okay with that."

    show alex neutral 
    show paxton frown 
    an "Alright, something definitely is wrong. I really hope it's nothing too awful."
    show alex unsure frowntalk 
    a "Yeah, of course."
    show alex frown 
    show paxton frowntalk 
    p "I'll be out in an hour— {nw}" 
    show paxton unsure 
    extend "uh, are you sure you're okay with waiting?"
    show paxton frown 
    show alex up talk 
    a "It's fine, I can wait!"
    show alex unsure smile 
    an "He looks like he could use getting away from the crowd in here. Maybe I can suggest something?"
    show alex up talk 
    a "Hey, are you hungry? I can make us some lunch, if that's okay."
    show alex smile 
    show paxton up frowntalk blush 
    ## Paxton, blushing
    p "I— um, sure."
    show paxton frown unsure 
    show alex blush 
    an "Ah, he's blushing... I think he feels a little better now. Good job, Alex!"
    show alex -blush talk 
    a "See you in an hour, then. Try not to break any cups."
    show alex smile 
    show paxton up talk 
    ## Paxton, smiling slightly
    p "I'll try my best."
    
    scene bg alex_room with fadee 
    
    an "I rush back to my apartment—I'm not sure how much time I have... less than an hour now."
    show alex unsure frown at Transform: 
        yalign 2.0 xalign 0.5 
    with dissolve 
    an "I may not be making anything too fancy, but I want to make sure Paxton at least enjoys the meal."
    show alex neutral sweat 
    an "Looking around the kitchen, I think of quick recipes I can use. Maybe I can make sandwiches? Or maybe pasta?"
    show alex up frowntalk -sweat 
    a "... sandwiches sound good."
    show alex smile 
    an "I gather up what I need and make four sandwiches—one for me, three for Paxton."
    an "I'm pretty sure he needs at least this much to make him feel full." 
    show alex talk 
    an "It's kind of amusing to watch him eat so much, then groan about going to the gym to burn calories."
    show alex smile 
    an "I leave the sandwiches on the table in the living room. I think it’ll be more comfortable for us to talk in there rather than the kitchen."
    
    ## doorbell ringing
    show alex shock 
    an "That must be him!"
    ## door opening sound
    ## Paxton appears, smiling
    show alex smile at Transform: 
        linear 1.5 xalign 0.8 
    $renpy.pause(delay=2.5, hard=False) 
    show paxton hat behind alex at Transform: 
        xalign 1.2 yalign 1.0  
    with dissolve 
 
    an "I was right! {nw}" 
    show alex shock 
    extend "Wait, why does he have a pair of paper cups in his hands? Did he bring drinks?"
    show alex smile 
    an "That's very thoughtful of him..."
    show paxton talk 
    p "Hey."
    show paxton smile 
    show alex talk 
    a "Hi! I hope you're hungry."
    show alex smile 
    show paxton at Transform: 
        linear 0.2 xalign 1.21 
        linear 0.4 xalign 1.19 
        linear 0.2 xalign 1.2 
    an "He chuckles as I open the door wider."
    show paxton talk 
    p "Starving, actually. Thanks for offering me free food."
    show paxton smile 
    an "I allow him to step inside and lead him towards the living room."
    hide alex with dissolve 
    hide paxton with dissolve 
    $renpy.pause(delay=0.5, hard=False) 
    show alex talk at closeright:
        yalign -0.7 
    with dissolve 
    show paxton hat at closeleft with dissolve 
    a "Are you feeling better now? {nw}" 
    show alex unsure
    extend "You looked pretty angry before."
    show alex smile 
    show paxton unsure frowntalk 
    p "Sorry about that. Finn texted me about going to an older mansion. That place is literally wrecked, and I know it's too dangerous— {nw}" 
    show paxton down 
    extend "I told him that I didn't want to go there."
    show paxton frown 
    show alex talk 
    
    menu:
        "I'm glad you voiced your opinion.":
            show alex up smile 
            show paxton unsure talk 
            p "Thanks... it wasn't easy, but you were right. {nw}" 
            show paxton up 
            extend "We couldn’t go on like that."

        "Can I ask the reason you didn't tell him why?":
            show alex up frown 
            show paxton unsure frowntalk 
            p "I, uh, I don't know. I think maybe I just panicked."
            show paxton frown 
            show alex frowntalk 
            a "Panicked?"
            show alex frown 
            show paxton frowntalk 
            p "Yeah, you know. What if he decided that I was just too scared to join them? I'm not sure..."
            show paxton frown 

    show paxton frowntalk down 
    p "But that's not all of it. Zaina messaged me to ask why, and I didn't want to tell her that I was worried. {nw}" 
    show paxton unsure 
    extend "So I just texted back that I didn't feel like it."
    show paxton frown 
    show alex unsure frown 
    an "Oh no, that couldn't have ended well..."
    show paxton frowntalk down 
    ## Paxton frowning/angry
    p "Finn said he wouldn't go, but he and Zaina could maybe try checking it out later. That I could join them next time if I still don't feel up to it by then."
    show paxton frown 
    show alex neutral 
    an "They need to talk about this at one point... this can't go on."
    show alex unsure frowntalk 
    a "Are you going to talk to him about your worries eventually? You know you need to."
    show alex frown 
    p "..."
    show paxton unsure frowntalk 
    p "Maybe later."
    show paxton frown 
    show alex neutral 
    an "He can't keep putting that conversation off."
    show paxton up talk 
    p "Don't worry about it. Finn and I will fix it, we just need some time."
    show paxton smile 
    show alex unsure talk 
    a "If you say so."
    show alex smile 
    show paxton up talk 
    ## Paxton, smiling slightly
    p "I do. Anyway, these sandwiches are really good— thanks for making lunch for me."
    show paxton smile 
    show alex up talk 
    a "Glad you liked them. I wasn't really sure what to make."
    show alex smile 
    show paxton talk 
    p "Well, this was a good choice."
    show paxton blush unsure 
    ## Paxton, blushing
    p "Can I make you dinner tonight in exchange?"
    show paxton smile 
    show alex up shock blush 
    ## Alex, blushing
    an "!!"
    show alex frown
    an "Is he serious? Does he actually want to make me dinner?"
    show alex unsure 
    an "I hope I'm not blushing too much..."
    show alex talk 
    a "Sure, I'd love to."
    show alex smile 
    ## black bg except the words, maybe?? Just a suggestion
    scene black with fade 
    an "Soon, Paxton leaves my apartment to go back to the cafe. I clean up the plates and try to focus on studying until dinner time arrives."
    an "I realize that I have several papers that I haven't finished despite them being given to me a few days ago. I also notice that I'm not worrying over what Mom and Dad would've thought had they learned what I'm doing."
    an "I'm not sure if that's a good thing or not. My future is at stake here, Mom always says so, but..."
    an "I still have time to finish my papers. And my grades haven't suffered as much as I thought they would."
    an "Is it really such a bad thing that I want to continue hanging out with Finn, Zaina and Paxton?"
    an "Soon enough, it's dinner time. I pack up a small bag to carry a textbook with me just in case, but I have a feeling I won't be using it much."
    an "Then, I leave my apartment to walk towards Paxton's place."

    
    ## Scene 9
    ## Paxton's apartment bg
    scene bg paxton_room night
    with fadee 
    
    ## Doorbell ringing
    show alex unsure shock backpack at Transform: 
        xalign 0.25 yalign 2.0 
        linear 1.5 xalign 0.2 
    with dissolve 
    play sound "doorknock.mp3"
    an "I take a deep breath and knock the door. My heart beats wildly against my chest, but I try to ignore it."
    show alex smile 
    show paxton up talk at Transform: 
        xalign 0.75 yalign 1.0 
        linear 1.5 xalign 0.8 
    with dissolve 
    ## door opening sound
    p "Hey, you're right on time."
    show paxton smile 
    show alex talk up
    a "Hi. It smells really good in here."
    show alex smile 
    show paxton talk 
    ## Paxton, smiling
    p "Oh, I know. Why don’t you come in?"
    scene bg paxton_room night with fade 
    show paxton smile at closeleft with dissolve 
    show alex backpack at closeright:
        yalign -0.7 
    with dissolve 
    an "I step inside and walk to the kitchen with Paxton. He serves the dinner right away— instant ramen with an egg on top. {nw}" 
    show alex unsure talk 
    extend "It's a classic college student dinner."
    show alex up shock 
    an "Then, he surprises me with a small, homemade chocolate cake. {nw}"
    show alex smile 
    show paxton talk 
    extend "It tastes delicious, just like his lattes. He brags about his baking skills for a while, and I let him."
    show paxton smile 
    an "We eat and talk at the same time; not about all the drama that's going on in the gang, but rather about our day."
    show alex unsure 
    show paxton talk 
    an "Apparently, one of Paxton's D&D sessions ended up with all players dead since the paladin refused to heal the rogue— he uses all kinds of weird words as he describes the game."
    show alex smile 
    an "I don't ask him. He looks way too excited talking, so I don't want to cut him off."
    show paxton smile 
    show alex shock 
    an "I don't even realize how much time passes as we talk until my plate is empty. When Paxton notices, he offers to give me one more slice of cake."
    show alex up talk  
    
    menu:
        "I thank him, but refuse.":
            show alex unsure smile 
            an "I feel too full to eat more. {nw}" 
            show alex up 
            extend "Instead, I suggest going  to the living room to watch a movie together."

        "I extend my plate to him with a hopeful smile.":
            show alex up smile 
            an "The cake is too delicious to not want one more slice."
            an "Once we're done eating, I suggest going to the living room to watch a movie together."

    show paxton talk up 
    ## Paxton, smiling
    p "Sure, lead the way." 
    
    scene bg paxton_room night
    with fade
    an "I grab his arm to pull him towards the living room—to the couches. He takes his laptop from the table, and we sit down to argue about what we should watch."
    show alex talk down at closeright: 
        yalign -0.9 xalign 0.8 
    with dissolve 
    show paxton at closeleft: 
        yalign -0.3 
    with dissolve 
    a "C'mon, it's just such a cliche-"
    show alex smile 
    show paxton up talk 
    p "Which is {i}exactly{/i} why we should watch it. {nw}" 
    show paxton unsure 
    extend "Please, Alex..."
    show paxton smile 
    show alex neutral frown 
    a "..."
    show paxton down talk 
    p "Please? I'm warning you, I'm not afraid of pulling the puppy look card."
    show paxton smile 
    show alex frowntalk 
    
    menu:
        "But I hate horror movies!":
            ## Paxton, grinning
            show alex frown 
            show paxton down talk 
            p "Well, that just gives me an excuse to cuddle you."
            show paxton smile 
            show alex up frown blush 
            ## Alex, blushing
            a "..."
            show alex unsure talk 
            a "What was it called again?"
            show alex frown 
        "Okay... I like horror movies anyway.":
            show alex down smile 
            show paxton down talk 
            p "Then make sure to be prepared for me hugging you to death."
            show alex up talk 
            ## Alex, laughing/smiling
            a "Alright, scaredy cat. Let's just start it."
            show alex smile 

        "Well, if you really want to...":
            show alex frown 
            show paxton up talk 
            p "Yeah! It'll be really fun."
            show paxton smile 
            show alex down talk 
            a "Whatever helps you sleep at night...."
            show alex smile 
            show paxton down talk 
            p "C'mon, I know you can't wait to watch it with me."
            show paxton smile 
            show alex talk 
            a "You can imagine that if it'll make you feel less scared."
            show alex smile 

    show alex -blush up shock 
    show paxton down frown 
    an "And of course, that's exactly when our time together ends up being interrupted."
    play sound "phonevibrate.mp3"
    show alex frowntalk 
    a "Who is it?"
    show alex frown 
    show paxton frowntalk 
    p "Wait, I think it was sent to our group chat. Check your phone-"
    show paxton frown  
    show alex unsure 
    ## Paxton, worried/frowning
    an "I see Paxton's face bleaching. {nw}" 
    show paxton unsure 
    extend "The warm and playful expression he had the whole night fades into a worried one."
    show alex talk 
    a "Hey, are you okay? Is it important?"
    show alex frown 
    show paxton unsure frowntalk 
    p "It's from Zaina."
    show paxton frown 
    show alex frowntalk 
    a "What does she say?"
    show alex frown 
    show paxton down frowntalk sweat 
    p "Finn went to the old mansion alone without telling anyone."
    show paxton frown -sweat 
    show alex shock sweat 
    an "Oh, no..."
    show alex frowntalk 
    a "Is he okay?"
    show alex frown 
    an "I quickly take out my phone to check the group chat. Like Paxton said, Zaina is the one who sent the message."
    show paxton frowntalk sweat at closeleft: 
        yalign -0.3
        linear 0.2 xalign 0.06 
        linear 0.4 xalign 0.04 
        linear 0.2 xalign 0.05 
    ## Paxton, worried/frowning 
    p "She says he fell and had a nasty landing. He called her when he realized that he couldn't..."
    show paxton frown -sweat 
    an "Paxton's voice dies down, but I can see Zaina's messages too."
    show alex shock 
    a "He couldn't walk. And now Zaina doesn't know what to do either."
    show alex frown 
    show paxton unsure 
    p "..."
    show alex neutral 
    an "He looks so worried about Finn."
    show alex down frowntalk 
    a "What should we do?"
    show alex frown 
    show paxton frowntalk 
    p "I— I don't know. Maybe we should go there to get him? Or tell Zaina to call 911?"
    show paxton frowntalk sweat 
    p "This is the first time one of us had an injury like this. If we call 911, they'd definitely call the cops— {nw}" 
    show paxton at closeleft: 
        yalign -0.3 
        linear 0.2 xalign 0.06 
        linear 0.4 xalign 0.04 
        linear 0.2 xalign 0.05
    extend "Finn is trespassing right now!"
    show paxton frown 
    show alex unsure sweat 
    an "He's right... but what if Finn broke something when he fell? He could have a broken leg or even worse!"
    show paxton unsure frowntalk at closeleft: 
        yalign -0.3 
        linear 0.2 xalign 0.06 
        linear 0.4 xalign 0.04 
        linear 0.2 xalign 0.05
    p "I— I don't know... Alex, what should I do?"
    show paxton frown 
    ## Maybe a close up to Paxton's worried face?
    an "I can try to tell him to do something, but..."
    show alex neutral -sweat 
    an "Should I? It's not really my place to do so, is it?"
    show alex down 
    an "This isn't a choice I should make—it's {i}Paxton's.{/i}"
    show alex frowntalk 
    
    menu:
        "You've been friends with Finn and Zaina since before I came into the picture.":
            show alex unsure 
            a "I'm sorry, but I can't make that choice for you, Paxton. You know better what to do than I do."
            show alex frown 
            
        "Zaina is asking for your help— that's not something I should decide.":
            show alex unsure 
            a "Just do what your heart tells you. I'll be here to help you, no matter what."
            show alex smile 

    show alex up frowntalk sweat 
    a "Tell me... what do {i}you{/i} want to do?"
    show alex frown -sweat 
    show paxton frowntalk sweat at closeleft: 
        yalign -0.3 
        linear 0.2 xalign 0.06 
        linear 0.4 xalign 0.04 
        linear 0.2 xalign 0.05
    p "You— no, I can't..."
    show alex neutral 
    show paxton -sweat frown at closeleft: 
        yalign -0.3
        linear 0.25 xalign 0.08 
    p "..."
    show alex unsure 
    show paxton up at closeleft: 
        yalign -0.3 
        linear 0.25 xalign 0.05 
    p "..."
    show alex smile 
    show paxton down frowntalk at closeleft: 
        yalign -0.3 
        linear 1.5 yalign 0.5 
    p "Let's go. We should hurry."
    show paxton frown 
    
    scene black with fade 
    an "We rush to the old mansion Zaina sent the address of without talking. I know that Finn's all alone and injured, and that Zaina is also on her way to meet up with us there, but all I can see is how worried Paxton is."
    an "He really is a good friend..."
    an "I'm glad I got to know him."
    
    scene bg mansion with fade 
    an "Zaina ends up arriving earlier than us. She helps Finn out of the mansion, and by the time our cab arrives, they're both waiting for us at a safe distance."
    an "Paxton helps Finn settle on the backseats. Zaina has to sit right at the edge of the backseat by Finn's hips, but they make it work."
    
    scene black with fade
    show alex up frown at closeright: 
        yalign -0.7 
    with dissolve 
    show paxton unsure smile at closeleft with dissolve 
    an "Paxton shares the front seat with me. Despite the serious situation, I feel his hand on mine, and he gives me a small, calming smile."
    show alex smile 
    an "We tell the cab to drive to the hospital, but all I can focus on is Paxton's hand on mine."
    show alex blush 
    an "I'm now so gone for him that it's not even funny anymore."
    
    scene black with fade 
    ## Black bg except the texts
    an "The hospital visit ends up being the right choice. We find out that Finn really has a broken leg, and Zaina almost gives him a broken arm with how much she punches for 'how stupid can he be?!'"
    an "We decide to spend the night at the hospital with Finn."
    an "At one point, when Zaina and I leave Finn's side to get some terrible hospital coffee that makes me think Paxton's lattes are a dream, I see Paxton sitting by Finn's bed with a serious expression."
    an "I feel sorry for Finn that he's going to go through another lecture after Zaina's, but at the same time, I'm glad."
    an "It's about time they solved this problem between them."
    an "I'm glad they're okay, now."


    ## Scene 10
    scene bg cafe
    with fadee

    an "Despite yesterday's adventures, today feels very calm and peaceful. I take a look around as I step inside the cafe."
    an "The weather is sunny, Paxton is back at the cafe, and Finn is Zaina's prisoner—she swore that he wouldn't get a chance to get out of the bed for at least 2 more days after that stunt he pulled."
    an "It feels like everything is back to normal. I can see Paxton behind the counter like always, too."
    an "I walk to the counter. I can see that Paxton's back is turned to me."

    show alex up smile at closeright:
        yalign -0.25  
    show paxton up smile apron at closeleft
    with dissolve

    a talk "Any drinks for me to try today?"

    an smile "Paxton turns back so fast that he almost spills the contents of the cup he has in his hands."

    p talk sweat "Alex! Hey! I didn't know you were going to visit."

    show paxton smile

    a talk unsure "You would go on an early lunch break if you knew, wouldn't you?"

    show alex up smile

    p talk -sweat "Stop teasing, I could've made you something to drink."

    show paxton smile

    a talk "Don't worry, I don't have any classes for the next two hours. You can make me any fancy latte you have in mind."

    show alex smile

    p talk "Alright then. Let me give this cup to the customer, then I'll see what I can do for you."

    show paxton smile

    a talk "Go on, Mr. Barista. I'll be waiting."

    show alex smile

    hide paxton with easeoutleft

    an smile "I watch him walk towards a customer waiting by the other end of the counter. His stance doesn't show what kind of stress he went through yesterday."
    an "It feels like nothing can make him abandon his kind smile."

    menu:
        "I admire that about him.":
            an "He's really brave and strong."
            an "Or, well... he has his times."
            ##end choice
        "I think that's what makes him so unique...":
            an "I really hope his smile stays the same."
            an blush "I'd love to keep seeing it tomorrow, the day after, and the day after that... for however long I can."
            ##end choice
    
    show paxton frown sweat apron at closeleft with easeinleft

    an "I watch him as he quickly gets back only to stop and glance around."

    a frowntalk -blush "Is something wrong?"

    show alex frown

    p frowntalk "I think I need to get something from the backroom—I've been making drinks for hours now; we're short on a few things here."

    show paxton frown

    a talk "Want me to come with you? I don't work out much, but I'm sure I can help you carry a box or two."

    show alex smile

    ## Paxton, lifting eyebrows/surprised

    p talk "Sure, if you want to."

    show paxton smile

    pause(0.2)

    hide paxton
    hide alex
    with sideswipe

    an "I get up and follow him as he steps away from the counter and walks to a door that has a 'STAFF ONLY' sign on it."
    an "We step inside. The door quietly clicks shut by itself behind us."

    show alex up smile at closeright:
        yalign -0.25  
    show paxton up smile apron at closeleft
    with dissolve    

    a talk "So... what are you planning to do for me this time?"

    show alex smile

    p talk "Telling you would ruin the surprise."

    show paxton smile

    an "I chuckle a little as he crouches down to check some boxes on the ground."

    a talk "Just don't poison me, please?"

    show alex smile

    p talk "Wouldn't even dream of it."

    show paxton smile

    an "He gets up and looks at me with a smile."
    an blush "My heart flutters in my chest. Paxton's eyes have such a warm look that I can feel my face heating up."
    an "It's amazing how he can have such an effect on me."

    p frowntalk "By the way... I wanted to thank you for helping me with Finn and Zaina."

    show paxton frown

    an -blush frown "Did he finally talk with them about how he feels about Finn's recklessness?"

    a frowntalk "Are you guys good now?"

    show alex frown

    p talk "Yeah. We spoke about a little bit of everything—Finn always had some problems, and I, well, I wasn't really in a good place, either."
    p frowntalk "I was too worried that talking with him would push him away from me that I didn't realize we were already drifting apart."
    p "I should've spoken to him earlier, but I guess better late than never."

    show paxton smile

    a talk "You bet. I'm proud of you for talking to him about your worries."

    show alex smile

    p talk "Thanks."
    p "In the end, Finn apologized to both me and Zaina for worrying us. He also promised that he'd try to be more careful from now on, too."

    show paxton smile

    a talk "That's wonderful news."

    show alex smile

    p talk "Well, yeah. Easy for him to say that when he's stuck in bed with Zaina standing on guard in his room—but I guess we're finally getting somewhere."

    show paxton smile

    a talk "I'm sure you two will figure it out. You're good friends, you wouldn't throw that away."

    show alex smile
    show paxton blush

    an "He blushes and looks down. I distantly realize that I could be touching him if I took two steps forward."
    an "The thought of getting closer to p talk is too tempting, but I manage to refrain myself from doing so."

    show paxton smile

    p talk "I owe it all to you. I couldn't gather my courage if it wasn't for you."

    show paxton smile

    an "But instead of me, p talk is the one who steps closer. His face is still flushed, but he hesitantly reaches to me."

    show paxton smile

    an "It feels like it takes ages for his hand to touch my face. I realize that he's moving slowly to give me the chance to pull away if I want to."
    an "His palm is warm and gentle against my cheek. I lean to it with a small sigh."

    p talk "Thank you, a talk."

    show paxton smile

    ##TODO EVENT IMAGE: SECOND KISS

    an "He tips my head up and presses a gentle kiss to my lips. My eyes slip closed, but it's like the whole world lights up behind my eyelids."
    an "My heart hammers against my chest. I feel Paxton's free hand curling around my forearm, and I cling to his shirt to keep my hands from shaking."
    an "He's warm against me, and all I can think is that this kiss in the dusty backroom of a cafe is the best thing that's happened to me in a while."
    an "Or maybe second-best—getting mixed up in urbexing did end up with me finding two great friends: Finn and Zaina."
    an "And a great person that means a lot more to me than a friend, too..."

    a "Paxton..."


    ## Scene 11
    scene black with fadee

    "..."

    scene bg cafe with fadee

    ##TODO clinking sound effect, coming from the bell on the cafe's door when a talk opens it

    an "I step inside the cafe with a smile on my face."
    an "Paxton's behind the counter like always. There's a small scratch on his face, left over from a small accident he had during our trip to an abandoned mansion with the gang last night."

    show alex up smile at closeright:
        yalign -0.25
    with dissolve

    a talk "Hey!"

    show alex smile

    show paxton up smile apron at closeleft
    with easeinleft

    p talk "Oh, the best girlfriend in the world is here!"

    show paxton smile

    #an "I feel myself blushing."

    a blush talk "Here to visit the best boyfriend in the world."

    an smile "He gives me a sweet smile, then looks back at the cup he has in hand."

    a talk "So what do you have for me this time?"

    show alex smile

    p talk "This one is pretty special—get ready to be blown away by this beauty."

    show paxton smile

    an "I laugh and watch him as he finishes making the latte."

    p talk "Okay, here. Try it and tell me if it tastes good."

    show paxtonend at Pan((0, 0), (0, 850), 12.0)

    an "He extends the cup towards me. The cup looks strange, but I can't put my finger on the reason {i}why.{/i}"

    a "Okay."

    an "I take it from his hands and notice it—{i}there isn't a lid on it.{/i}"

    an "And on the latte is a big heart made with milk foam."

    p "A white chocolate, toasted-marshmallow latte with almond milk—{i}without{/i} whipped cream this time, of course. I hope you like it."

    ##END
    return