######################################################################################################################
########################                                                                  ############################
########################                         z talk's Route                            ###########################
########################                                                                  ############################
######################################################################################################################
init python:


    def mumble_tag(tag, argument, contents):

        """
        Useful for when a character is either mumbling or whispering.

        Usage: a "{mumble}Hey.{/mumble}"
        """

        size = int(gui.text_size / 1.5)

        return [(renpy.TEXT_TAG, u"size={}".format(size)),] + contents + [(renpy.TEXT_TAG, u"/size"),]


    def shout_tag(tag, argument, contents):

        """
        Useful for when a character is shouting.

        Usage: a "{shout}HEEEYY!{/shout}"
        """

        size = int(gui.text_size * 1.5)

        return [(renpy.TEXT_TAG, u"size={}".format(size)),] + contents + [(renpy.TEXT_TAG, u"/size"),]

    config.custom_text_tags["mumble"] = mumble_tag
    config.custom_text_tags["shout"] = shout_tag


define flash = Fade(0.1, 0.0, 0.5, color='#FFF')


label zainaroute:

    ## Scene One
    scene bg alex_room with fadee

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    an "These days I find myself restless during classes. My eyes wander to my watch too often for my liking, and when it's not on my wrist, it's on the door."
    
    an "My mind, on the other hand, wanders to starry night skies on rooftops and crumbled buildings."
    
    an "I got home one day and opened my notebook to find doodles in the margins. And even {i}I{/i} had a hard time deciphering the notes that I {i}did{/i} take."
    
    an "And yet... I can't bring myself to feel too bad about it."
    
    an "Going out with Finn, Paxton, and Zaina has been the most fun I've had in years."
    
    an "Worries of my overbearing parents hovering over my shoulders, watching my every move, they all simply melt away when I'm with them."

    play sound "phonevibrate.mp3"

    "Bzzzzzz..." with vpunch
    
    an "Speak of the devil."
    
    an "I suppose it was too good to be true. I haven't heard from them in a while after all."
    
    an "My stomach no longer drops at the thought of my parents texting me for updates, but still I brace myself as I pick up my phone."

    an "It's not my parents."
    
    an "Instead, it's a text from Zaina and—-oh."
    
    an "She wants to go on a date."
    
    an "With me. On a date."

    ##alex blush
    
    an "The room suddenly feels a whole lot warmer."
    
    an "I stare at my phone, my mind scrambling for a response."
    
    an "Should I say yes? No? I haven't dated anyone since I was fourteen."
    
    an "And it wasn't another woman. I've never been with another woman."
    
    an "But Zaina..."

    ##alex soft smile

    an "Sure, she's pretty rough around the edges, and sure, she really likes picking on me, but I do find myself wanting to see her smile lately. Not just her usual smirk, either, but her smile."
    
    an "I text her back in the affirmative, ignoring the warmth in my cheeks and the way the phone feels clammy in my hands."
    
    an "Maybe two seconds pass before Zaina replies, with a bunch of heart emojis."
    
    an "I laugh at that. Zaina didn't seem the type to use emojis, much less heart ones."
    
    an "Another text follows that, with a time and a heads up that she'll be picking me up tomorrow."
    
    an "Tomorrow... I have a test tomorrow."
    
    an "My eyes drift to the textbooks on my desk, but I think of Zaina, her smile, and the way she called me ‘cute' last time we met."

    a "I'll be fine."

    an "I pass by my desk for my closet instead, intent on living up to Zaina's compliment. At least I hope it was a compliment. You never quite know with Zaina. She can make an insult out of anything."
    
    an "I clutch a shirt in my palm, though I'm careful not to wrinkle it. I can't believe I actually have a date tomorrow!"

label zainaroute_scene_2:
    ## Scene Two

    ##outside alex's apartment
    scene bg outside_campus night with fadee
    show alex at center with dissolve:
        yoffset 50
    
    an "Zaina had said to be ready by seven, but I've been ready since six."
    
    an "Nervous? Who's nervous?"
    
    an "Not me."
    
    an "I stare at my phone, open to a tab of puppy pictures, hoping the cuteness would settle the butterflies in my stomach."
    
    an "It works for a bit, until I come across a husky with Zaina's likeness."
    
    an shock "The picture psyches me out. Does it really look like her or am I just seeing Zaina everywhere? Am I actually insane?"
    
    an sweat "I frantically exit the tab to my texts. Do I still have enough time to back out? Should I tell her the truth or make up some excuse? Would an emoji be rude in this situation?"

    play sound "motorcycle.mp3"
    "Vrroooom..." with vpunch

    show alex at rightt with move
    show zaina behind alex at leftt with easeinleft:
        yoffset 50

    an "The sound of an engine revving snaps me out of my panic and I look up, my mouth going dry at the sight of Zaina on a motorcycle."

    menu:

        "Nice car.":
            
            a talk "Nice... car."
            
            ##zaina smirk
            ##exchange is teasing on both sides

            show zaina smile
            show alex smile

            pause 1.5
            
            z unsure talk "Did I say I was gonna pick you up in a car?"
            
            show zaina smile
            
            a talk sweat "Well... no."
            
            a -sweat "But if you were going for the cool factor, couldn't you have gone for a sports car instead?"
            
            an smile "It's almost much safer."
            
            z -unsure talk "I'll keep that in mind in my next life when I'm richer."
            
            z "You'll be there, most definitely missing my bike."
            
            show zaina smile
            
            an "I protest playfully, but it does funny things to my stomach knowing that she's imagined another life, with me still in it."

        "Nope.":
            
            a talk "There's no way I'm getting on that."

            show alex smile
            
            z unsure frowntalk "Fine by me. You can walk to the restaurant."

            show zaina frown
            
            an "She looks me up and down."
            
            z up frowntalk "You'll ruin your cute outfit with sweat stains, though."

            show zaina frown
            
            an "I sigh, though secretly I'm quite pleased she noticed the effort I put into dressing for our date."
            
            a talk "Fine."

        "That's hot.":
            ##zaina smirk
            
            z talk "What was that?"

            show zaina smile
            
            ##alex blush
            
            an blush "I freeze. I hadn't meant to say that out loud."
            
            a talk "Nothing! I said nothing!"

            show alex smile
            
            z unsure talk "No, I'm pretty sure I heard a whole lot of something."

            show zaina smile:
                ease 0.5 xalign 0.45
            
            an shock sweat "Zaina leans as close to me as she can while on her motorcycle. Her grin turns predatory."
            
            z talk "Me or the bike?"

            show zaina smile
            
            a shock blush "...What?"
            
            z unsure talk "Did you mean me or the bike when you said that?"

            show zaina smile
            
            an smile "Zaina was somehow kind enough to not repeat what I had said."
            
            z up talk "I can wait all day, you know."

            show alex:
                xalign 0.57
            show zaina smile behind alex:
                xalign 0.32
            with move
            
            an "But not kind enough to let it go."
            
            an "I force the words out of my mouth, as quickly as possible."
            
            ##alex is pretty much mumbling here, maybe make the text a little smaller at this part?
            
            a talk "{mumble}Both... I meant both.{/mumble}"
            
            an smile "My eyes stay stubbornly fixed to the ground for some time, but at Zaina's chuckle, I peek at her hesitantly."
            
            z talk "You're cute."

            show zaina smile
            
            an shock "She pinches my nose and though I protest, her comment warms me down to my toes."
            
            an smile -sweat "Alright, maybe all that embarrassment was worth it."
            ##endchoice 
    
    z up talk "Anyway, here."
    
    an "She tosses me a helmet and gestures behind her."
    
    z talk "Hop on."
    
    show zaina smile

    an "I put on the helmet and scramble behind her, looping my arms around her waist."
    
    z talk "You'll wanna hold on tighter than that." 

    show zaina smile
    
    an sweat "Oh propriety be damned. I hug her as tight as I can without squishing her ribs."
    
    an "I mutter against her shoulder."
    
    a shock -sweat "This was all a ploy for me to hug you, isn't it? You actually have a perfectly working car back at your place." 
    
    an smile "I feel Zaina's laugh, rather than see it."
    
    z talk sweat "Damn, you caught me."

    show zaina smile
    
    an "I laugh too and the nerves dissipate."
    
    z talk -sweat "Ready?"

    show zaina smile
    
    an "I nod, before realizing she can't see me. Oops."
    
    a talk "Yes."
    
    an smile "Zaina sets off for the restaurant and I'm suddenly very glad for her warning. I hold on even tighter." 
    
    an "Yet even as the wind whips past, I feel only the warmth of Zaina's back. It soothes me, comforts me, and when I smile at the view through my helmet, it's without any fear."

label zainaroute_scene_3:

    ##scene three
    scene bg cafe:
        xzoom -1
    with fade

    play music "Bm_Cafe04.ogg" fadein 1
    queue music "Bm_Cafe04.ogg"

    an "The restaurant Zaina chose is a hole in the wall and family-owned, making our date for the evening a very private affair."
    an "It's cozy. I like it." 

    show alex at rightt:
        yoffset 50
    show zaina at leftt:
        yoffset 50
    with dissolve

    a talk "How'd you find this place?"

    an smile "The waiter knew Zaina by name, so I assume she's a regular." 

    z talk "It was after an urbex trip with the guys."

    z "We split ways and I was hungry. This place was the only thing open at 3 AM. That's about it."

    show zaina smile

    a talk "Have you ever taken Finn and Paxton here?"

    show alex smile

    z talk "Nope."

    show zaina smile

    an "That's surprising. I feel like they're always together."

    an "Though I guess I've only seen them in the company of each other. This is the first time I've hung out with one of them just one-on-one."

    a talk blush "So does that mean you only take girls here?"

    ##a playful smile from alex here
    show alex smile
    pause 1.5

    an sweat "I couldn't resist."

    ##zaina smirk

    show zaina smile
    pause 1.5

    z talk "Wouldn't you like to know?"

    show zaina smile

    an -sweat "I give her my best puppy dog eyes, but the woman is made of steel apparently."

    an "She props her chin up with one hand and swirls pasta onto her fork with the other."

    z talk "Is that it? I think you can get cuter than that."

    show zaina smile

    an blush "The next few minutes, I try to muster up puppy dog eyes up to Zaina's standards and fail. Even after using the puppy pictures I browsed through before our date for reference."

    a talk "Do you actually have no heart?"

    show alex smile

    z talk "Nah, I've just had a lot of practice."

    show zaina smile

    a -blush talk "Paxton?"

    show alex smile

    z talk "Paxton."

    show zaina smile

    an smile "We return to our meals, before it gets cold. It would be a shame not to, after all I'm pretty sure Zaina took me here to share one of her favorite spots with me."

    an "Tasting the food, I can honestly say that I see why she's a regular."

    an "Once we've gotten through a portion of our dishes, Zaina slides me her phone. I take it and glance down to see a photo of the most recent site we went to. She motions for me to continue swiping."

    z talk "I exported the photos from my camera. Those are the ones not up on Insta yet." 

    z "Pick your favorites and we'll post ‘em up later."

    show zaina smile

    an "Zaina's eye for detail continues to amaze me. The shots look amazing. Even someone like me, who doesn't know much about photography, can tell she has a talent for it."

    an "I'm honestly surprised she isn't already going into photography. She seems to like it well enough to take the pictures for their Instagram."

    z talk "I don't do well in classroom settings."

    show zaina smile

    an shock "Huh? Did I say that out loud?"

    z talk "Majoring in it would take the fun out of it and I don't want to {i}hate{/i} photography."

    z "Things are fine as they are."

    show zaina smile

    a talk "Do you know what you do want to do?"

    show alex smile

    z talk "Nope."

    show zaina smile

    an neutral "She crosses her arms, not unhappy with the current subject of our conversation, but clearly not happy either."

    an "I figure she gets that question a lot."

    z talk "My dad's this big shot marketer and my mom's a housewife. Like {i}hell{/i} am I doing either."

    show zaina smile

    a talk up "I don't know... I think you'd make a pretty good housewife."

    an smile "She cracks a grin and so do I, glad that at least she's not taking this too seriously. This was never meant to be an interrogation."

    z talk "I guess cleaning up after you wouldn't be the worst thing in the world."

    show zaina smile

    ##alex blush

    an blush "She's only saying that to tease me. She must be."

    z talk "Anyway, nothing else interested me either."

    z "So here I am."

    z "What about you? Why'd you go into nursing?"

    show zaina smile

    an -blush "It probably shouldn't be my answer to such a question, but I do it anyway. I shrug."

    a talk "I don't know. Memorization comes easy to me and I like science. Nursing just seemed to be the natural step to take."

    ##serious zaina

    z down neutral "Was it really? Or was it ‘the natural step to take' because your parents pressured you into picking nursing?"

    an shock "I open my mouth, but no words come out. I've never thought about it that way before."

    ##choice
    menu:
        "I don't know.":
            
            a talk "I don't know."
            
            a "I know it's stupid, but I honestly don't."
            
            an neutral frown "My distress must show on my face because Zaina reaches over and places her hand on top of mine, squeezing."
            
            an up smile "I lose myself in the sensation and focus only on the feeling of her hand over mine. It's warm. Comforting."
            
            z talk "It's fine to not know. I mean look at me."

            show zaina smile
            
            an "I do look at her. She's grinning, but it's softer somehow. More reassuring."
            
            an "I squeeze her hand back."
            ##end choice

        "I really do like nursing.":
            
            a talk "Maybe they did, maybe they didn't. I still like what I'm doing right now."
            
            an smile "Zaina doesn't look the least bit convinced, but it doesn't matter. I know I'm happy where I stand right now."
            
            a frowntalk "Should you really be dissuading me from nursing? You're going to get awfully sick one day and then you'll have no one to take care of you."
            
            z talk "A personal nurse does sound nice... {i}okay{/i}, I guess you can stay in your major. Will you wear a nurse's outfit?"

            show zaina smile
            
            a talk "I'll be wearing scrubs when I take care of you."

            show zaina smile
            
            an smile "Zaina laughs."
            ##end choice

        "I guess they did...":
            
            an "It doesn't sit well in my stomach."
            
            an "My parents have dictated so much of my life already. How many classes I take, how much I should study... but it makes sense. There was always that feeling of guilt whenever I texted them back. It makes sense I was guilted into this too."
            
            a talk "I might've been a little pressured..." 
            
            an smile "That was the understatement of the century."
            
            z talk "I thought so. My parents tried to do the same with me."

            show zaina smile
            
            an "Someone pressuring Zaina? I can't imagine it."
            
            a talk "But you're so—"

            show alex smile
            
            z frowntalk "Yeah. It's why me and my parents don't talk that much anymore."
            
            z "You don't have to do the same with your parents, but maybe don't let them kick you around as much."

            show zaina smile
            
            an neutral "That's easier said than done..."
            
            an shock up "It must've been written on my face because Zaina reaches over and pokes me in the forehead."
            
            z talk  "Hey, how about this? If you ever decide to stick it to ‘em, I can come with you to offer support. How's that sound?"

            show zaina smile
            
            a talk "...Really?"

            show alex neutral
            
            z talk "Sure, screw parents."

            show zaina smile
            
            an smile "Something about the way she said that makes me laugh. I feel much lighter for the rest of the meal."
            ##end choice

    an smile up "She takes a sip of her soda and regards me with a look I'm unused to from her. Zaina looks... thoughtful? Curious? I can't quite tell."

    z talk "When was the last time you took a class outside of your major?"

    show zaina smile

    an unsure shock "I pause. I haven't."

    an sweat "My silence seems to tell Zaina all she needs to know because she continues."

    z talk "You should try other classes. See what you like, what you don't like."

    z "If all you've taken are nursing courses, you're just screwing yourself over."

    show zaina smile

    an frown -unsure "My parents don't seem to think so. They'd actually prefer it that way."
        
    an shock "But that's the point, isn't it? Not letting my parents tell me what to do."

    z talk "I'm not trying to force you into finding something else you're in love with, here. Just think about taking a class for fun."

    show zaina smile

    an shock "For... fun?"

    z talk "Maybe we can even take a class together."

    show zaina smile

    an "A class... with Zaina?"

    z frowntalk "The class will probably be trash, but at least we'll get to shit talk it together." 

    show zaina smile

    an smile "Laughter blooms from my chest in spite of my best effort to swallow it. It's unreal. The thought of taking a class with Zaina actually sounds, to borrow her words, {i}fun{/i}."

    an "Spending more time with Zaina is undoubtedly something I'm interested in and for once, the thought of taking another class isn't stressful."

    show zaina -frowntalk

    a talk "Sure, that sounds good."

    a "Great, actually."

    an smile "Zaina looks like the cat that got the cream. I should feel wary, but it's excitement that bubbles in my stomach, not fear."

    z talk "I'll be the one picking the class, though."

    show zaina smile

    an neutral shock "I make a big show of groaning, as though I don't trust her. Zaina feeds off of it as her grin, somehow, gets even wider."

    a up talk sweat -blush "I just signed my death warrant, didn't I?"

    show alex smile

    z talk "You sure did."

    show zaina smile

    an shock "Could the next semester come any faster?"

label zainaroute_scene_4:
    ##scene four

    scene bg amusementpark with fadee

    play music "Be_piano12.ogg" fadein 1
    queue music "Be_piano12.ogg"

    an "A couple days later, we all agree to meet up. It's supposed to be a nice time at an abandoned amusement park. For me, it's a break from all the assignments I've been drowning in lately."

    an "But things are tense."

    show zaina down frown at leftt:
        yoffset 100 xoffset 95
    show alex unsure frown at right:
        yoffset 100
    show paxton down frown hat behind alex  at rightt:
        xoffset -95
    with dissolve

    an "Zaina, Paxton, and I watch Finn with bated breath as he climbs up the tracks of one of the rollercoasters. I should be worried about how natural he makes it look. How many times has he done stuff like this?" 

    an "Sure enough, fear grips me the same time Zaina shouts at him. He's getting awfully high up..." 

    z frowntalk "I've got enough of you being a dumbass! If you fall, I'm leaving! I'm not scooping up your brains off the ground!"

    show zaina frown

    #an "I can tell she doesn't mean that, though. Zaina's a woman of action. If she wanted to leave, she would've done so already."

    f "I'll be fine! This isn't the worst thing I've done!" 

    an "Should Finn even be talking right now? I'd rather he focus on climbing!"

    an "How he manages to see Zaina's unconvinced face that high up, I don't know, but it spurs him to do something completely insane."

    an frown "Finn leans back and takes one hand off the tracks."

    an down "My stomach drops. I feel like throwing up."

    an "But I'm more worried about Zaina's reaction. There's no way this is sitting well with her."

    hide zaina with easeoutleft

    an "I glance at her nervously, just in time to see the furious look on her face before she whips around and stalks off in the opposite direction."

    p frowntalk "Zaina, wai—!"

    show paxton frown

    hide alex with easeoutleft

    an "I don't stay long enough to hear Paxton's objections. I hurry after Zaina, as fast as my feet can take me."

    hide paxton with dissolve

    an "{cps=5}...{/cps}"

    an "My legs are almost no match for the fury that fuels Zaina. She's fast. {i}Incredibly fast{/i}."

    an "I'm grateful that she occasionally feels the need to release her anger by kicking various pieces of debris, because it slows her down some."

    an "When she pauses to punt a cone across the park, I catch up to her. Her pace slows down to something more leisurely."

    an "All that walking and kicking must've tired her out."

    show alex frown at rightt:
        yalign 2.0
    with dissolve

    a frowntalk "Was it a good idea to leave him?"

    show alex frown

    an "Finn must be the last thing she wants to talk about, but it doesn't change the fact that I'm worried about him. What if he does fall?"

    a frowntalk "He might hurt himself."

    show alex frown
    show zaina down frown:
        xoffset 200 yoffset 50
    with dissolve

    z frowntalk "{i}Tch.{/i} He'll be fine."

    # show zaina frown
    
    # an "She doesn't look like she believes that."
    
    z frowntalk "Paxton's still there to watch over his bony ass, so he'll be {i}fine{/i}."

    show zaina frown
    
    an "Is she trying to convince me or herself?"
    
    an "We slow to a stop in front of the Ferris wheel. Zaina still looks agitated and seems short of yelling out her frustrations in the empty park."
    
    an "It's probably very effective, but big as the park is, we shouldn't do something that'll draw attention towards us. Just in case anyone happens to be nearby." 
    
    an "So what to do?"
    
    show zaina neutral
    
    an "Zaina's starting to look restless in front of the Ferris wheel and—wait, that's it! The {i}Ferris wheel{/i}!"
    
    a talk "Zaina."

    show alex smile
    
    z frowntalk "What?"

    show zaina neutral

    ##alex grin

    a talk "What do you say to an impromptu photoshoot?"
    
    an smile "The proposal has Zaina looking up, from where she'd been glaring at earlier. Her mouth twitches and I let myself hope for a moment."
    
    an "But instead of smiling, she scoffs."
    
    an "My heart sinks."
    
    z frowntalk down "No thanks. I don't like taking pictures when I'm pissed off. They always turn out shitty."

    show zaina neutral
    
    an "That may be the case, but I won't let that deter me!"
    
    an "I pull out my phone."
    
    a unsure "Who said you were taking the pictures?"

    ##zaina surprised
    
    z frowntalk unsure "... What?"

    show zaina neutral
    
    a talk "I'm the one taking the pictures, not you."
    
    an smile "I hold my phone in one hand and gesture for her to move in front of the Ferris wheel with the other."
    
    a talk "Go on. You can survive being the model just this once."

    show alex smile

    ##happy zaina
    show zaina up smile

    an "A surprised Zaina is already rare enough, but the laugh that erupts from her lips is something else. It's full-bodied, not like her usual chuckles, which are brief and often gives the impression that she's laughing at you, not with you."
    
    an "But this laugh is warm, pleasant in the way a cozy blanket might feel during the winter. It fills the space, displacing the quiet, and all I know is that I'd give anything to hear it again."
    
    an "I settle for the smile that lingers on her lips instead as a smile of my own shyly shows itself at the sight."
    
    an "As instructed, Zaina positions herself closer to the Ferris wheel while I move myself further back, mindful of the debris that litter the ground."
    
    z unsure talk  "You sure you can tell the difference between photo and video mode?"

    show zaina smile
    
    a talk "Just for that, I'll make you blurry in all these photos!"

    show alex smile
    
    z talk "Oh, I don't think you'll need to {i}try{/i} for them to turn out blurry."

    show zaina smile
    
    a talk "Are your models always so insufferable?"

    show alex smile
    
    z talk "Dunno. You've never modelled for me."

    show zaina smile

    an "Neither of us want to back down and our cheeky grins show it. In the end, I'm the one to move things along, if only because Finn and Paxton will probably be done exploring soon."

    z talk unsure "So how do you wanna do this, {i}Ms. Photographer{/i}?"

    show zaina smile up

    ##choice
    menu:
        "Starfish pose.":
            
            a talk "Do the starfish pose!"
            
            a "In the air!"

            show alex smile
            
            z talk "Are you actually five years old?"

            show zaina smile
            
            a talk "Nope."
            
            an smile "I grin."
            
            a talk blush "You are. Since you're the one doing the pose."
            
            ##end choice

        "Smize.":
            
            a talk "Do your best smize!"

            an smile "I zoom in, intending to catch Zaina in an unflattering angle, but I'm unprepared for the intensity of her gaze and nearly drop my phone."
            
            ##alex blush
            
            an blush "This is... fine! Zaina looks at me all the time! No need to get flustered!"
            
            ##zaina smirk
            
            show zaina smile -unsure
            
            an "Unfortunately, Zaina seems to realize the effect she has on me because she smirks, despite my earlier instructions to do any smiling with her eyes."
            
            z talk "You're looking a little red. Too hot?"

            show zaina smile
            
            a unsure talk "Nobody said anything about you being hot!"
            
            an up shock "Her smirk widens."
            
            z talk "I meant the weather, but thanks, I'm flattered."

            show zaina smile
            
            an shock sweat "I... want to die."
            
            ##end choice

    an smile -sweat "Though the photoshoot couldn't have been more than ten minutes, it felt much longer. We had gone through so many poses after all, though most of them were ridiculous."

    an "And to think that I have photo evidence of everything!"

    an "Sure, none of it embarrasses Zaina, but it's still nice to see her in a different light, outside of just being badass and cool. Honestly, I didn't actually expect her to go through with all of them."

    an "But my next proposal might be my hardest sell yet..." 

    a talk "Zaina..."

    an smile "I can see her suspicion from a mile away. I carry on, anyway."

    z frowntalk "What?"

    show zaina frown

    a talk "Let's take a picture together!"

    show alex frown neutral

    show zaina -frown unsure

    an "She just stares at me, and I try not to squirm under her scrutiny."

    z talk up "A selfie. You want a selfie, don't you?"

    show zaina smile

    a talk "Yes..."

    a "I know it must be some kind of cardinal sin for photographers, but please? Won't you indulge me?"

    an smile "I try the puppy dog eyes that weren't so effective on her before. It's my only play."

    an "A few agonizing seconds pass."

    an "And to my surprise, Zaina finally motions for me to join her side."

    ##alex happy

    an smile "I can't help it. I can't keep the grin off my face. It stays even as Zaina pinches my cheek when I join her side."

    z talk "Alright. I'll do only one take, so you better be ready."

    show zaina smile

    an "I can't mess this up!"

    an "Slowly, I angle the phone so that the Ferris wheel is in the shot. Then I make sure Zaina and I aren't too cramped. I'm no Zaina, but I do my best to account for everything before taking the photo."

    an "When everything looks good, I ready the shot."

    a talk "Ready."

    an smile "At Zaina's nod, I move to press the button."

    an "Just before I finish pressing it, a flash of movement blindsides me and so does the featherlight touch on my cheek. It takes a second to sink in, but just as the phone flashes, I can only stare dumbly at the screen."

    ##EVENT IMAGE: FIRST KISS
    #Scene 4 - Line 919; Event Image - I assume it's ZAINA + ALEX kissing (?)
    scene ZainaCG1 with dissolve

    $ persistent.CG3_unlocked = True

    an blush "Me, my lips parted and my cheeks flushed. Zaina, eyes closed and her lips brushing my cheek."

    a "Wha—"

    an smile "The hand holding my phone hangs limply at my side while the other reaches up to touch my cheek. Though lasting for only a moment, the feeling of her lips on my cheek is one that'll surely stay with me forever."

    an "But, God, did that really just happen?"

    an "I turn to Zaina, expecting her to smirk at my shock, but it's a soft smile I barely get a glimpse of before she turns as well, in the direction of where we came from."

    z talk "C'mon. The boys are probably waiting for us."

    scene bg amusementpark with fade

    an -blush up "I follow her in a daze and before I know it, we're back at the entrance. Finn and Paxton stand up as we approach."

    show alex at rightt:
        yoffset 80 xoffset -100
    show zaina at leftt:
        yoffset 80 xoffset 125
    show finn behind zaina at left
    show paxton hat behind alex at right
    with dissolve

    an "The sight of the boys happens to be just what I needed to snap out of my stupor, as I look over Finn, relieved he's unharmed."

    an "That must be thanks to Paxton."

    an "When my eyes finally reach his face, though, I find Finn surveying us with similar intensity."

    f talk "You're in a good mood, Zaina."

    show finn smile

    an "Instead of denying it like she usually would, she just hums under her breath and turns to me."

    z talk "Want a ride back to your place?"

    show zaina smile

    a talk "Oh, um, sure."

    an smile "The boys wave goodbye and we go our separate ways."

    hide finn
    hide paxton
    with dissolve

    an "The ride back is much easier on my heart this time, which I'm grateful for. Plenty of other things involving girls, lips, and cheeks have done their own number on it."

    an "Still, who am I to deny an opportunity to hold Zaina as close to me as possible?"

    ##outside of apartment
    scene bg outside_campus night with fadee

    show alex at rightt:
        yoffset 50 xoffset -100
    show zaina at leftt:
        yoffset 50 xoffset 100
    with dissolve

    an "The loss of contact is that much more disappointing, though, when we finally arrive at my apartment. I try to find an excuse to dawdle as much as possible."

    z talk "Send me the pictures when you have time."

    show zaina smile

    an "I'm not sure where I find the confidence, but I take it. Anything is better than being a flustered mess. I push memories of the kiss to the back of my head, where I can linger on them later."

    ##alex smirk or playful smile

    a talk "Do you plan on grading my work?"

    ##zaina smirk

    an smile "Instead of rising to my bait, Zaina just shoots me her trademark smirk and pokes my forehead, before setting off in her motorcycle." 

    an shock sweat "{i}Oh boy{/i}. What have I gotten myself into?"

label zainaroute_scene_5:
    ##scene five
    ##alex apartment

    scene bg alex_room with fadee

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    show alex with dissolve

    an "I had sent Zaina the pictures last night just before I slept and in the morning, I wake up to texts from her."

    an "Over breakfast, I look them over."

    an "It's difficult to keep the smile off my face."

    a talk "‘B+ nice effort.'" 

    a "‘Will accept kisses for extra credit.'"

    an smile "It brings forth memories of the kiss and my hands subconsciously wander to my cheek. Her touch somehow still lingers."

    an "If I could make Zaina flustered for even the slightest bit, I'd give her as many kisses as she wants."

    an "But really, I'm just relieved she didn't brush off the kiss as just a one time thing, even if it was only on the cheek."

    an "I go to school today with the feeling that I can conquer the world."

    an "The texts my parents send me later don't bother me in the slightest."

label zainaroute_scene_6:
    ##scene six
    ##mansion bg

    scene bg outside_campus night with fadee

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    show zaina at leftt:
        yoffset 50
    show alex at rightt:
        yoffset 50
    with dissolve

    an "Ever since we've agreed to start seeing each other, Zaina's taken to giving me rides whenever we go out as a group. It's crazy how quickly she's endeared me to riding motorcycles."

    an "{i}Well{/i}. I suppose getting the chance to hug Zaina with each ride had some part in it."

    an "Tonight is no different."

    an "I scroll through our group chat to the latest texts. Finn is already on his way and Paxton is just finishing up at the cafe. It shouldn't be too long now."

    an neutral "In the meantime, I ask Zaina the question that's been nagging at me ever since she picked me up."

    a frowntalk unsure "So why didn't you bring your camera equipment tonight?"

    an frown "It might be because I've been spending a lot of time with her lately, but I can tell she's not pleased with the current arrangement. She must feel like a fish out of water."

    show zaina frown

    an neutral "She's quiet for much longer than I expected, though, and I blink, unused to silence from Zaina."

    z frowntalk "... There's a police station not too far out from here."

    show zaina frown

    an "She points north, the way we came from, and I briefly recall passing by one on the way to the mansion."

    z frowntalk  "So there's a lot of patrols in this area."

    show zaina frown

    an neutral "That checks out, but it still doesn't explain why she didn't bring her camera."

    an "Zaina must see the confusion on my face because she continues."

    z talk "It was a while back. We were still pretty new to urbex. New and stupid."

    show zaina smile

    an "At that, I straighten up, curious. They didn't talk about their past explorations that often."

    z frowntalk "I think it was at an old hospital that was going to be demolished soon. So we were eager to check it out before they tore down the building."

    z unsure "We didn't account for security though."

    z "They catch Pax first, then Finn, and when one of them sees me, well, that's when shit breaks loose."

    z -unsure "Apparently, one of the officers saw me with my camera—"

    show zaina frown

    an shock "Oh no. I see where this is going."

    z frowntalk "—yeah, exactly. It was dark out and none of us could really see very well. The officer without the flashlight just saw something in my hands and assumed it was a gun."

    z unsure "So they decide to pull {i}their{/i} guns on us."

    show zaina neutral

    an shock sweat "I shudder."

    an "I can't imagine what that must've been like. My palms are already sweaty just from the thought of it."

    show alex frown -sweat

    z frowntalk "There's a lot of shouting and it's dramatic as hell, but things settle down when they realize it was just a camera."

    z talk up "We got off with warnings, if you can believe it."

    show zaina smile

    an "Despite how scary it must've been, Zaina is smiling as she finishes recalling the incident. My guess is it's because it brought the three of them closer."

    an "That and it was the sort of far-fetched tale you tell others for entertainment."

    z talk "But we didn't want to take chances this time."

    show zaina smile

    an "She nods at the phone in my hand."

    z talk "That's why we're doing the pictures on the phone for this one."

    show zaina smile

    an "Their reasons for doing that makes sense. I wouldn't want to risk it either."

    an "But what sticks with me from Zaina's story is that they were caught."

    a frowntalk up "I thought you guys always evaded the authorities when you go out."

    show alex frown up

    z talk "Nah. It happens all the time within the community. Especially if you're just starting out."

    show zaina smile

    an "That... Doesn't sound reassuring."

    an "I'd never considered the possibility of getting caught in all the times I've gone out with the group before. Their Instagram made them appear untouchable."

    an "And apart from that moment with Zaina and the glass, our adventures had always gone through without a hitch."

    an "Now? I don't know."

    an "I enjoy my time with everyone, but I'd also enjoy a secure job. Whenever that might be."

    an "Having an arrest on my record for trespassing doesn't exactly make me prime hiring material."

    an "At some point, I'm going to need to establish boundaries. What I will and won't do."

    an "But for now..."

    z frowntalk "Hey, spacey head. You doin' okay?"

    show zaina smile

    an "Zaina places a hand on my shoulder and I touch it, playing with her fingertips."

    a talk "I'm fine."

    ##alex playful smile

    an smile "I hold up my phone and shake it."

    an "It was supposed to be Zaina taking the pictures on her phone, but she said something earlier about accidentally breaking hers. She didn't exactly elaborate."

    a talk "I'm just thinking about what I can do to improve my grade. I'll be aiming for higher than a B+ this time!"

    show alex smile

    an neutral "..."

    ##zaina neutral
    show zaina neutral

    an "Normally, I would've gotten a chuckle or a smirk from Zaina by now. Instead, her face looks inscrutable. The part that I'm able to see at least, because she's dropped the hand on my shoulder and turned away from me."

    an "Her gaze, meanwhile, is fixed resolutely on the ground and I wonder what could be so interesting about a couple rocks."

    an "For such a warm night, the air is rather frosty."

    a frowntalk "Um."

    an frown "I scramble for something—anything to say."

    a frowntalk "Should I use any filters when I'm taking the pictures?"

    a "Or, um, is that something I should do after?"

    an frown "Does Zaina even use filters?"

    an "Zaina shrugs and picks a piece of lint off her jacket in the silence."

    an unsure shock "Did I do something wrong?"

    hide zaina
    hide alex
    with dissolve

    an frown "My brain is buzzing with possibilities of what had possibly turned things sour, but before I could pick any of the theories apart, Finn appears."

    # show zaina at leftt:
    #     yoffset 100 xoffset 100
    # show alex at rightt:
    #     yoffset 100 xoffset -100
    # show finn behind zaina at left
    # show paxton behind alex at right
    # with dissolve

    an "He distracts me long enough with talk of exams that Zaina's odd behavior is the least of my concerns."

    an "Paxton arrives shortly after."

label zainaroute_scene_7:
    ##scene seven 
    ##mansion bg (inside)

    scene bg mansion with fadee

    play music "Be_piano12.ogg" fadein 1
    queue music "Be_piano12.ogg"

    show zaina at right:
        yoffset 100
    show alex at rightt:
        xoffset -100 yoffset 100
    show paxton hat at left
    show finn at leftt:
        xoffset 100
    with dissolve

    an "When I was asked to take the pictures for tonight, I had been excited. I thought it was something Zaina and I could do together."

    an "I imagined her teaching me, in that roundabout way of hers. Never giving me tips outright, but dangling them in front of me, and then taking them away when I reached for them."

    an "I thought it was something that could bring us closer. I yearned for something like that experience she told me about with Finn, Paxton, and the police officers." 

    an "... Though preferably something much safer."

    an "But Zaina sticks to the corners of the building, hands in her pockets as she meticulously peers out of every window. Away from me. The boys too."

    an "What could have gotten her attention that deeply?"

    an "Curiosity getting the better of me, I follow her example after she leaves for another window, but only find the night sky, not a single star in sight."

    an "It gives me no insight into Zaina's strange actions, but I snap a picture anyway, so that we'll leave the mansion with at least one photo."

    an "However, the first picture emboldens me and I take a few more after, slowly getting into the groove of things."

    an "Most of them are useless, though, since my first instinct is to take pictures of the boys and Zaina. I take a couple shots of them navigating the weak floorboards and ducking under fallen ceiling beams."

    an "It's not until I'm several shots in that I realize we can't use the ones with their faces in them. I fix that in the next ones, but even so, I'm particularly proud of the one of Zaina by the grand piano."

    an "She's the perfect picture of contemplation in that one, eyebrows furrowed while her fingers absentmindedly trace the keys." 

    an "The light from the moon enhances her features and grants her an otherworldly vibe amongst all the rubble, but she's always looked ethereal to me. Especially when she's smiling."

    an "I heart the photo to make sure I wouldn't accidentally delete it later."

    an "I've taken all the pictures I can when I hear a crash coming from where I last saw Finn."

    ##make the text smaller as this is said very quietly

    f "{mumble}Damn...{/mumble}" 

    ##everyone shocked
    show alex shock up
    show zaina frown up  ## From the file I have Zaina doesn't have a 'shock' attribute. - Angel
    show finn frown up  ## From the file I have Finn doesn't have a 'shock' attribute. - Angel
    show paxton frown up  ## From the file I have Paxton doesn't have a 'shock' attribute. - Angel

    an "I catch Zaina's eye for the first time since we entered the mansion and I'm sure the alarm on her face mirrors mine."

    an "Paxton, likewise, looks like he's seen a ghost."

    an "We all hurry to Finn, mindful of the weak spots in the floor."

    a talk "Finn! Are you okay?"

    show alex frown

    f frowntalk "I'm fine..." 

    show finn frown

    z frowntalk "You don't look {i}fine{/i}, dumbass."

    show zaina frown

    p unsure frowntalk "I agree with Zaina, here..." 

    show paxton frown

    an "Sure enough, Finn is bleeding. A lot."

    an "Not enough to warrant a hospital visit, but he's definitely ruined his shirt, even if you can't see it through all the black."

    p frowntalk "What happened?"

    show paxton frown

    an "Finn motions to behind him, where the door lies on the ground. That must've been the crash we heard."

    f frowntalk "The door wasn't budging and—"

    show finn frown

    z frowntalk "You thought you'd do something stupid?"

    show zaina frown

    an "Finn goes quiet and presses a hand on his wound. His hand comes away red."

    an "That's when I notice the blood on the hinges. The door didn't snap cleanly and he must've cut his shoulder on the splintered wood."

    an "Ouch."

    z frowntalk unsure "Sorry, I can—"

    show zaina frown

    an "At Zaina taking out the first-aid kit from her bag, Finn turns to me."

    f talk "Alex, do you mind?"

    f "You have better bedside manner." 

    f "And you're the nursing major, anyway."

    show finn smile

    an "Did he really mean that or is he just upset at Zaina's earlier comment?"

    an "I look between them, unsure. Finn looks expectant, while Zaina looks..." 

    z frown unsure "..." 

    a talk unsure "Oh, um, I don't know..." 

    show alex frown up

    z frowntalk "... It's fine. Here."

    show zaina frown

    an "She hands me the first-aid kit and leaves without another word." 

    ##zaina exit

    hide zaina with dissolve

    p talk "Are you guys okay here?"

    show paxton smile

    a talk "Yeah."

    show alex smile

    p talk "Okay, be careful heading back out. We'll be waiting for you guys."

    ##paxton exit

    hide paxton with dissolve

    an "And then Paxton goes too, leaving me with Finn."

    an "I treat him in silence, and he, too, is quiet. Not even a wince when I apply the disinfectant, just the light twitching of his fingers."

    an "How many times has this happened for Finn to be so desensitized to the pain?"

    a frowntalk "Are you sure you're okay?"

    show alex frown

    f frowntalk "Yeah. I've had worse."

    f "So don't worry."

    show finn frown

    an "I'm reminded of that time at the amusement park. He had said something similar while hanging on the rollercoaster tracks with one hand."

    an "That wasn't exactly something I wanted to relive."

    menu:
        ##choice
        "Push":
            
            a frowntalk "By worse, you mean..."

            show alex frown
            
            an "I'm not sure what he means. I have ideas, but none of them are... good."
            
            an "Do I even want to know the answer?"
            
            f frowntalk "Just that."

            show finn smile
            
            an "He offers me a smile that doesn't reach his eyes. Yet another thing he seems used to doing."
            
            f frowntalk "Maybe I'll tell you later."
            
            ##endchoice

        "Don't push":
            
            an "He says not to worry, but how can I not when he's said he had worse?"
            
            an frown "How can anybody?"
            
            an shock "Worser injuries or worse... what?"
            
            an frown "I don't know, but Finn seems awfully determined not to divulge anything."
            
            an "Well, I won't force him. I can only hope he feels comfortable to share eventually. If not with me, then with Zaina or Paxton."
            
            ##endchoice

    f frowntalk "You're done, right?"

    show finn frown

    an "I give his shoulder another once over and he's right. I've finished wrapping up his wound. Must've done it while I was thinking."

    f talk "Thanks."

    show finn smile

    an "We exit the mansion together, though I insist on taking up the rear in case something happens on the way."

    scene bg outside_campus night with sidefade

    show alex at right:
        yoffset 100
    show paxton hat at center
    show finn at left
    with dissolve

    an "But nothing happens."

    an "Except Paxton is the only one waiting for us outside."

    a frowntalk "Where's Zaina?"

    show alex frown

    p talk "She said there was something she had to do that she forgot about. So she had to leave."

    show paxton frown

    an "Zaina never struck me as the forgetful type, though."

    an "... Or maybe she was just tired. I'm overthinking things too much."

    f talk "Zaina was your ride here, wasn't she?"

    f "I can take you back to your place. Since you patched me up and all."

    show finn smile

    ##alex playful smile

    show alex smile

    a talk "Oh, so you wouldn't have given me a ride if I hadn't taken care of you?"

    show alex frown

    ##finn smile

    show finn smile

    pause 1.5

    f talk "Are you saying you don't like Paxton's company? Hey, Pax—"

    show finn smile

    an "Paxton waves off Finn's attempt to antagonize him, however playful, and fixes me with a concerned look."

    p talk "I wouldn't trust Finn's driving if I were you."

    show paxton smile

    an "It's nice talking to the other two. Still, as Finn and I say our goodbyes to Paxton, and Finn drives me home, I can't help but notice that Finn's sense of humor is pretty similar to Zaina's."

    an "Was that actually the case or do my thoughts just naturally wander to her?"

label zainaroute_scene_8:

    ##scene eight 
    ##alex apartment
    scene bg alex_room with fadee

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    show alex frown with dissolve

    an "The next day comes and I'm once again stuck in the whirlwind of assignments and exams."

    an "Finn reminded me of our upcoming exam last night, but it feels more real today now that the course is actually gearing up for it." 

    an "I go back to my place with a half-completed study guide and when my parents ask me what I'm up to, I'm not just using exam season as an excuse not to respond."

    an "Lately, though, they've been badgering me less and less, taking my silence as proof that I've been busy studying."

    an "That they came to that conclusion themselves is on them, not me."

    an "It hasn't stopped them by any means, but the occasional reprieve from their helicoptering is more than welcome." 

    an "Texting doesn't leave as much of a bad taste in my mouth anymore and I've even reached out to old friends, asking how they've been."

    an "And commiserating over exams."

    an "It's a nice feeling and for once, the stress isn't getting to me as much as it used to."

    an "The joys of actually having a social life, I guess. Who knew?"

    ##phone buzz
    play sound "phonevibrate.mp3"

    an shock "I reach for my phone, expecting a text from one of the friends I had just reconnected with."

    an "The contact name has too many heart emojis for it to be one of them, though."

    ##happy alex

    an smile "I open the texts."

    an "It's probably just Zaina apologizing for taking off yesterday, but I'm happy to hear from her nonetheless. I didn't expect her phone to get fixed so soon."

    an "I could use the opportunity to ask her if she wants to go on a date!"

    an "Before school gets too hectic."

    an "My eyes skim the texts and as I thought, she's saying sorry—"

    ##confused alex
    stop music fadeout 5

    a frowntalk unsure "Wait... What?"

    an smile "I reread the texts."

    a shock up "‘I'm sorry, but I don't want to see you anymore.'"

    a "‘It's over.'"

    an frown unsure "What do I even say to that?"

    menu:
        ##choice
        "Can't we talk about this in person?":
            
            an "It feels sudden. Too sudden."
            
            an "And I like to think I've known Zaina long enough to know she wouldn't just break up with someone over text."
            
            an "... Right?"
            
            an "There has to be more to this than meets the eye."
            
            an "And well, if she really wants to call it quits, then she should tell me face-to-face."
            
            ##end choice
        
        "Haha. You're joking, right?":
            
            an up "This has to be a joke."
            
            an "Even if she's serious, she wouldn't do it over text."
            
            an neutral "You would think someone like Zaina would find it cowardly to break up with someone over the phone."
            
            an "It's something fourteen year old Alex would do, not her."
            
            an unsure "Or did I just not know her as well as I thought I did?"
            
            ##endchoice
        
        "Call her":
            
            an "There's no point in texting her back a paragraph."
            
            an "I'll just call her and set things straight."
            
            a unsure frowntalk "Okay, you can do this..."
            
            an frown "I go to her contact info and press call."
            
            an "The dial tone rings twice and in my anticipation, I lose my nerve, ending the call abruptly."
            
            a frowntalk "No, you can do this!"
            
            an frown "I steel myself and call her one more time."
            
            ##end choice

    an up frown "I wait five minutes. Then ten."

    an "No response."

    an unsure "Maybe she just turned her phone off after texting me?"

    an "... Or, the likelier option, she's avoiding me."

    an "I certainly would. After dropping a bomb like that on somebody."

    an "I sigh and collapse onto my bed, taking my phone with me. I don't know how long I spend staring at the texts, hoping it's just one of those exam stress hallucinations."

    an "I know better, though. This is the first time I haven't stress cleaned my apartment with exams looming. If there's anything that's stressing me out, it's this."

    an unsure frown "Stressed. Confused. Baffled. I'm certainly all of those things and more."

    an up "But I'm not upset."

    an "Maybe I would be if it made sense, but I can think of no possible reason she would want to stop seeing me."

    an "Okay, that might be egotistical of me, but she's fought with Finn over worse and they're still friends."

    an unsure "Would Zaina really give up so quickly?"

    an "My hands reach for my phone once more."

    an "I need a second opinion on this. Before I can second guess myself, I text my old friend from high school. This would be more interesting to them than exams, at least."

label zainaroute_scene_9:
    ##scene nine
    ##cafe bg

    scene bg cafe:
        xzoom -1
    with fadee

    play music "Bm_Cafe04.ogg" fadein 1
    queue music "Bm_Cafe04.ogg"

    show alex frown at right:
        yoffset 100
    show paxton hat
    show finn at left
    with dissolve

    an "More days pass and still no word from Zaina."

    an "I'd think I was blocked, but the messages I send Zaina still go through."

    an "So she's still getting them."

    an "She's just not responding."

    an "It's honestly hard to be mad at Zaina for ghosting when I'm mostly just worried. If she could just show some sign of life I'd stop spamming her with messages."

    an "But even my messages telling her that go unanswered."

    an "At least Finn and Paxton still answer my texts, though."

    an "I'm supposed to be meeting Finn for a study session, but I deliberately planned it at the cafe so I could pick both his and Paxton's brains for a second."

    an "That was what my friend suggested, and it wasn't difficult at all to get Paxton's break time out of him."

    an "I just had to agree to be his guinea pig and taste some of his drink experiments."

    p talk "Here you are."

    show paxton smile

    an "Paxton hands me a cup with a smile and settles into the chair next to Finn."

    p talk "It's a white chocolate matcha latte."

    p "Oh, and with almond milk! Just like you asked!"

    show paxton smile

    a talk "Thank you!"

    a "...You didn't make Finn one?"

    an smile "Finn snorts and loudly sips his drink. The one he bought himself."

    f talk "I don't trust his creations."

    show finn smile

    an "He gives me a once over and smiles at me with what I think is pity."

    f talk "Good luck."

    show finn smile

    an "I can't tell if he's kidding, but what's more worrying is that Paxton doesn't refute Finn's statement. Oh god, what did I get myself into?"

    an "I slowly bring the cup to my lips and hesitate. Finn just looks amused and Paxton is like an expectant golden retriever."

    an "Well, here goes..."

    an "..."

    a frowntalk "It's—"

    show alex frown

    p talk unsure "It's...?"

    show paxton smile

    a talk "—pretty good, wow!"

    an smile "And it is. I can hardly tell he used almond milk instead."

    an "I never thought white chocolate and matcha would go so well together, too."

    p talk "I'm glad! It took a couple tries to get it right!"

    show paxton smile

    an "Finn whistles a low tune at the result. I'm not sure if he's impressed by me or Paxton."

    f talk "Congrats. You survived Pax's latte roulette."

    show finn smile

    a talk "Um... thanks."

    a "But that's not actually why I called you both here."

    an smile "Paxton and Finn share a look."

    f talk "{i}Really{/i}? Why, I thought you called me here to study."

    show finn smile

    an "I pout. For some reason, I didn't think Finn knew how to be sarcastic. Yet he seems right at home with his dry drawl."

    an "I stand corrected."

    a up talk "Well... Since you both seem to know already..."

    a frowntalk "I've been texting Zaina."

    a unsure "Or I guess, {i}trying{/i} would be more accurate."

    a "She hasn't replied to any of my messages and I haven't heard from her in days."

    a up "Has she been texting either of you?"

    show alex up frown

    ##boys speak at the same time
    ## Sorry, didn't have time to create a multi-dialogue for this.
    ## They'll have to speak one at a time here. :(
    
    f frowntalk "Nope."
    
    show finn frown
    
    p frowntalk "No, sorry."
    
    show paxton frown

    an neutral "I try not to get disheartened. At least it meant she wasn't just ignoring me, right?"

    an "But if no one has gotten a hold of her... Then..." ## Correction: 'a hold' and not 'ahold'. I assume that was a typo. - Angel

    an "Is Zaina okay?"

    an up "Finn and Paxton look unperturbed by the news, though. Shouldn't they be concerned? Their—{i}our{/i} friend has practically gone missing!"

    an "My worry must show on my face because Paxton reaches over to soothe me."

    p talk "Hey, it's okay."

    p "Zaina does this all the time. It's kind of... Her thing?"

    show paxton smile

    f talk "Yeah. There's not much you can do but just give her some space."

    f "She comes back, she always does."

    show finn smile

    a frowntalk "But we were—"

    an frown "I bite my lip. It wasn't like we were only just friends! Didn't that mean something?"

    p talk "Seeing each other?"

    show paxton smile

    f talk "Yeah, we know."

    show finn smile

    #finn and paxton smug, alex shocked/maybe blushing??
    show alex unsure blush

    show finn smile
    show paxton smile

    an blush shock "They {i}knew{/i}?!"

    f talk "You guys were pretty obvious."

    show finn smile

    p talk "Finn and I were talking about it after you guys left. At the amusement park."

    show paxton smile

    an "They're talking like they're trying to comfort me, but I don't feel very comforted when they're both grinning like that!"

    ##finn and paxton smile

    show paxton smile
    show finn smile
    pause 1

    f talk "Look, it's nothing personal."

    f "If she likes you, and {i}she does{/i}, then she'll come back."

    show finn smile

    p talk "There's no doubt about that."

    show paxton smile

    a frowntalk -blush "That she likes me or that she'll come back?"

    an frown "Paxton and Finn share another look over their drinks. Paxton smiles."

    p talk "Isn't it obvious?"

    show paxton smile

    an unsure frown "I mask my frown under the guise of sipping my latte. No, it really isn't."

    an down "And I wonder if they'd still say the same thing if they saw Zaina's texts. They sounded pretty final to me."

label zainaroute_scene_10:
    ##scene ten
    ##alex apartment bg

    scene bg alex_room with fadee

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    an "Finn and Paxton suggest an expedition the next day to take my mind off the Zaina situation."

    an "I'm already halfway out of my apartment when I spot the first-aid kit on my kitchen counter."

    an "It's Zaina's from the other night. I have my own, but it's decidedly less beat up. The trio has clearly seen a lot of use out of it."

    an "I stare at it, contemplating my options."

    an "I could go with the boys. Give Zaina her space and let her decide the terms of our reunion."

    an "That is, if she wants to see me again."

    an "Or I could go to Zaina's under the pretense of returning the first-aid kit."

    an "It's a little desperate, but I do want to find out what's wrong. And if I don't go now, when will I find a better excuse? Better yet, when else will I find the nerve?"

    an "If I don't go now, nothing will change. Zaina will continue doing this even if we do make up. I'd just be dooming our relationship before it got to fully start."

    an "And do I want a relationship with Zaina?"

    an "{i}Yes{/i}. So much."

    an "I grab the first-aid kit and fire off a text to Finn. I've never been to Zaina's place, so I don't actually know where it is. If anyone knows, it's Finn."

    ##phone buzz
    play sound "phonevibrate.mp3"

    an "He replies rather quickly and I wonder if he'd expected this all along."

    a "‘You're whipped' he says, as he gives me the address anyway."

    an "I send a quick thank you and a bunch of heart emojis. Finn responds with three of the vomiting ones."

    an "And then two minutes later—"

    play sound "phonevibrate.mp3"

    an "A ‘good luck' from Pax." 

    an "I smile and pocket my phone."

    ##black screen
    scene black with dissolve

    an "Though I shouldn't be surprised, Zaina's apartment turns out to be pretty close to the restaurant she's a regular at."

    an "It's in a nice enough neighborhood, but I'm not here to gawk. I hurry up the complex, clenching the first-aid kit in an iron grip."

    play sound "doorknock.mp3"

    an "The minute I spend waiting is agonizing."

    an "It's all it takes for me to second guess everything."

    an "Should I have come? She's going to slam the door in my face, isn't she? I should go, now, before she opens the door. Oh god, feet move—"

    ##door opening sfx, shocked alex

    scene bg zaina_room with fade

    play music "Be_Longing04.ogg" fadein 1
    queue music "Be_Longing04.ogg"

    an shock "I'm not sure what I expected, but it's certainly not this."

    ##tired zaina
    show alex at closeright:
        yoffset 100 xoffset -100
    show zaina unsure neutral at closeleft:
        yoffset 80 xoffset 100
    with dissolve

    an "The light normally does her plenty of favors, but now all it does is highlight the bags under her eyes. And her hair, usually full of volume and effortlessly tousled, hangs limply below her shoulders."

    an "Her clothes look slept in and her voice, when she finally speaks, is hoarse with disuse."

    z frowntalk "How'd you—{i}Finn{/i}."

    show zaina neutral

    an neutral "She doesn't look as angry as I thought she would be, though even that observation doesn't fill me with relief."

    an "I take my chances."

    a talk "... Can I come in? I have your first-aid kit."

    an smile "Zaina shrinks behind her door and it strikes me that she's the one who wants to escape."

    an sweat "I slowly reach out a hand, careful not to startle her into closing the door. I place it on her wrist, just the slightest of touches, before I respectfully retreat."

    a frowntalk -sweat "Please?"

    an frown -sweat "She looks behind her, hesitant, and I reel back in horror."

    an "I hadn't considered the possibility that she might have someone over."

    an "But Zaina opens the door after much deliberation, quelling my fears."

    an "I step inside only to realize she must've been worried about the mess."

    an "It's nothing I haven't seen, though, and I tell her so myself."

    z frowntalk "That's not—"

    show zaina frown

    an "She stops herself, as if she was about to say something incredibly incriminating. To Zaina, that could be absolutely anything."

    an "Her eyes then flit to mine and she must see something that she likes in them because she picks up where she left off."

    z frowntalk "This wasn't how I imagined your first time here."

    show zaina neutral

    a frowntalk "{i}Oh{/i}."

    a "Me neither."

    an frown up "I imagined us huddled together, laptops out as we make the painstaking effort to go through the entire course directory for next semester."

    an "She'd propose something out of left field like woodworking and I'd try to coerce her into an architecture class."

    a talk "But I'm happy I'm here now. Thanks for letting me in."

    show alex smile

    z frowntalk "I just wanted my first-aid kit back."

    show zaina frown

    an "Her lips twitch, just barely, but a warmth blooms in my chest all the same. It relieves me to find she hasn't lost her sense of humor, even through all of this."

    a talk "Well, here it is."

    an smile "I set it down on her coffee table."

    ##music change to something more somber maybe?

    an "But the mood then shifts to something awkward and stifling now that neither of us no longer have an excuse to dance around with."

    an "..."

    an "Without anything else to do, she gestures for me to take a seat as she does the same."

    an "I do so."

    a frowntalk sweat "So, um..."

    an frown "‘What happened?' doesn't sound quite right. We both know what happened. ‘Why?' is a loaded question and I'm not sure I can keep my tone neutral if I asked it. If she didn't want to kick me out before, she would then."

    an -sweat "That only leaves..."

    a frowntalk "What's wrong?"

    an frown "At the end of the day, that's all I want to know. Is she alright? We might move past this day as only friends, if even that, but I'd rather do so knowing what's been bothering her."

    ##surprised zaina

    show zaina up neutral

    an "Zaina seems a little surprised. There's a moment where she starts to reply, only to abruptly stop, as though she'd prepared for me to say something other than what I did."

    an "The silence stretches for an unbearably long amount, but I steel myself to be patient."

    an "Zaina's probably just unused to talking about her feelings. After all, look at the company she keeps."

    an "Finally, I hear a sharp intake of breath and follow it across to the room to find Zaina, looking the most unsure I've ever seen her."

    z talk "This stays between us, okay?"

    z "For now, at least."

    show zaina smile

    a talk blush "I promise." 

    an smile -blush "I mime the motion of zipping my lips and this seems to give her the confidence she needs. She takes another deep breath."

    z frowntalk blush unsure "I... I was jealous."

    z "Of you."

    show zaina frown

    an up shock "My eyebrows shoot up in surprise, though I bite my lip to keep myself from saying something."

    an "Zaina, jealous of {i}me{/i}? What could she possibly be jealous about? Zaina is... {i}Zaina{/i}."

    an neutral "Cool, badass, and beautiful, there's very little that Zaina doesn't already have in spades. For her to be jealous..."

    z talk "I've known Finn and Pax for a while but when Finn brought you along, I thought I was ready to welcome somebody new into the group."

    ##zaina smile

    show zaina smile

    pause 1.5

    z talk "And I really was. You were cute... Fun to tease..."

    ##alex blush

    an blush "My cheeks warm, both at the sincerity behind her words and at the soft smile that crosses her lips. Her smile, perhaps because of its rarity, is stunning." 

    show alex smile

    z talk "The more I spent time with you, the more I realized I didn't mind the thought of my life being uprooted by some newbie."

    z frowntalk "As long as it was {i}my{/i} life."

    ##alex confused, zaina serious

    show zaina unsure frown

    an unsure "That was... an interesting distinction."

    z frowntalk "But you've wormed your way in, didn't you? Pax and Finn like you too and..." 

    z up "You've become a part of their lives as well."

    z "I should be happy, right? {i}I{/i} like you, {i}my friends{/i} like you... It's all fine... Until they decide they like you better than me."

    show zaina frown

    an "Zaina speaks slowly now, forcing each word out through gritted teeth as though it physically pains her to say."

    z frowntalk unsure "And why shouldn't they? I'm... not the most agreeable person to be around."

    show zaina frown

    an shock -blush "I open my mouth, ready to protest."

    z frowntalk "Don't deny it. It's true."

    show alex frown up

    z "I have a bad habit of always saying what I mean and a lot of the time, it hurts people's feelings."

    show zaina frown

    an "Sure, there's a speck of truth to that. But she's truly not as terrible as she's making herself seem. It isn't like she's out purposely putting people down."

    z frowntalk down "I'm the worst to Finn."

    z unsure "I like to pretend we're close, but I make him feel awful, on top of him {i}already{/i} feeling shitty."

    z down "It's no wonder he prefers you."

    show zaina frown

    an "She must mean that other night, when he asked me to tend to his wounds after Zaina offered to do it herself."

    z "The boys were asking you to do things I normally do and... I just—"

    an "This time I can't just keep quiet."

    a frowntalk unsure "You felt like I was replacing you?"

    an frown "Zaina's silence is answer enough. Suddenly, her moody behavior from a couple days ago make so much more sense now."

    an "She's known Finn and Paxton longer than I have. And even though she liked me, she also felt threatened by me joining the group."

    an "It's not without reason, either. I was encroaching on all her roles. To her, it just seemed like I was stealing her friends away."

    menu:
        ##choice
        "Hug her":
            
            an "Actions do speak louder than words, don't they?"
            
            an "I peel myself off the couch and cross the room like a woman on a mission, right to where Zaina's sitting."

            show alex at closeright:
                # yoffset 100
                easein 1 xoffset -100
            
            a talk neutral "Up."

            show alex smile
            
            z up frowntalk "...What?"

            show zaina frown
            
            a talk up "Up."
            
            an smile "I gesture for her to stand up."
            
            an "She gets up, her confusion making her movements slow and uncertain."
            
            an "But I don't pay any of that any mind."

            show alex at closeright:
                # yoffset 100
                easein 1.5 xoffset -250

            show zaina at closeleft:
                # yoffset 80
                easein 1.5 xoffset 150
            
            an "The moment she's fully up I don't waste any time and immediately envelop her into a hug."
            
            an "I wrap my arms around her, locking my hands around the dip of her back."
            
            an "For a moment I'm not exactly sure what Zaina makes of this, but then her arms settle around me, too, and I can feel her consciously relax, in time with the soft, slow breath that ghosts past my temple."
            
            an "Her hair tickles my nose and I hum, rocking on my feet. I simply bask in the feeling of her in my arms and I can only hope she finds this just as comforting as I do."
            
            an "I hold her even closer to me."
            ##end choice

        "I'm sorry.":
            
            an "For some reason, my first instinct is to apologize."
            
            an "This somehow alarms Zaina because she shakes her head vehemently once the apology leaves my lips."
            
            z frowntalk down "No."
            
            z "Why are you apologizing?"

            show zaina neutral
            
            a unsure frowntalk sweat "I didn't mean to make you feel inadequate."

            show alex frown -sweat
            
            z frowntalk "That's not—"
            
            z unsure "It's not your fault. If anything it was {i}mine{/i}."
            
            z "I felt shitty and insecure and I took it out on you."

            show zaina frown
            
            a unsure frowntalk "I'm sorry you feel this way, then. You're anything but inadequate."
            
            a "Especially to me."
            
            an frown "Zaina stills, and for a moment, I think I've gotten through to her. But when I move in for a closer look, her frown remains."
            
            z frowntalk unsure "I'm not sure I believe that..."

            show zaina frown
            
            an "I reach for her hand and squeeze."
            
            a frowntalk "Then let me spend the rest of our time together trying to convince you."
            
            a "If you'll have me."
            ##end choice

        "I could never replace you.":
            
            an "The thought of me replacing Zaina in any universe is laughable."
            
            an "But this is clearly no laughing matter."
            
            a frowntalk unsure "Even if I wanted to replace you, I couldn't."

            show alex frown
            
            z frowntalk "... But you'd thought about it?"

            show zaina neutral
            
            a frowntalk "Never."
            
            an frown "And yet... maybe what Zaina needs is a laugh."
            
            a frowntalk "For one thing, I can't fill out your pants as well as you do. And two, I'd crash your motorcycle the moment I'd try to drive it."
            
            a "Would you dare subject the public to such a menace on the streets?"
            
            a "Could you live with yourself if you let people see me try to pull off drop crotch pants?" 
            
            show alex smile
            ##zaina laugh
            show zaina smile

            pause 1.5
            
            z talk up "I don't know."
            
            z "Seeing you make a fool of yourself might be worth the risk."
            
            z unsure "If I die, at least I'll die happy."

            show zaina smile up
            
            an "Well, I know I could certainly die happy from just hearing that laugh of hers..."
            ##end choice

    ##screen fadee to black, then fadee in back to zaina's apartment

    scene bg zaina_room with fadee

    show alex at closeright:
        yoffset 100 xoffset -100
    show zaina at closeleft:
        yoffset 80 xoffset 100
    with dissolve

    an "I'm not sure exactly how much time passes, but I end up in the same bean bag chair as Zaina, sitting comfortably in her lap."

    an "Her fingers comb through my hair in gentle strokes and all I know is that I never want to leave."

    z talk "Stay with me?"

    show zaina smile

    an "I hum in the affirmative."

    a talk "Honestly, I was going to stay here, even if you didn't ask."

    an shock blush "She removes the hand in my hair and uses the same one to pinch my nose."

    z talk "Moocher."

label zainaroute_scene_11:

    ##scene eleven
    ##sanitorium bg

    scene bg hospital with fadee

    play music "Be_piano12.ogg" fadein 1
    queue music "Be_piano12.ogg"

    show zaina at leftt:
        xoffset 100 yoffset 100
    show alex at rightt:
        xoffset -100 yoffset 100
    # show paxton at leftt:
    #     xoffset 100
    # show finn at left
    with dissolve

    an "Following my make-up with Zaina, she reconnects with the boys and we resume our expeditions. Finn complains that we're turning the sites into date spots, while Paxton is ever so supportive."

    an "Secretly, though, I believe Finn is the happiest out of all of us that Zaina's back."

    an "I bring this up to Zaina one day, but she dismisses the thought and figures he just missed having someone to look after him." 

    an "I say nothing of the fact that he could very easily have gotten that through Paxton."

    an frown unsure "Although things have pretty much gone back to normal, it seems Zaina's insecurities still fester. I wonder every day what I could do to possibly get her to see that the boys do value her."

    an smile up "But that is the furthest thing from my mind right now when she's holding my hand."

    an "Zaina leads me through the sanatorium with the ease of a seasoned veteran, confident and sure of herself, but she holds my hand as if it were a lifeline."  ## I think you meant 'sanAtorium' and not 'sanItorium'. Corrected it. - Angel

    an "She lets go only to take pictures and before I can even blink, her palm is already sliding back into mine."

    an "It's when we're apart for longer than just a moment that my eyes wander and when I finally look back, I find myself immediately enraptured by Zaina in her element. I allow myself to just take her in."

    an "She's still got that scowl of hers even as she takes pictures of something just over my shoulder, like the wall isn't cooperating with her."

    an "It only makes the pleased set of her mouth later when she gets her shot that much more captivating."

    an "I may not have Zaina's eye, but even {i}I{/i} can appreciate beauty."

    a talk "You got it?"

    show alex smile

    z talk "Yup."

    show zaina smile

    a talk "Can I see?"

    show alex smile

    ##zaina smirk
    show zaina smile

    pause 1.5

    an "She angles the camera away from me and purposefully lines up another shot."

    z talk "Nope."

    show zaina smile

    an "However, something must not have been to her liking because Zaina lowers the camera almost immediately."

    ##zaina neutral
    show zaina neutral

    z talk "Can you hold the flashlight up a little higher? The light is a bit..." 

    show zaina neutral

    an "I position the flashlight just under my chin and do my best evil smile. I model it after Paxton's, the exact one he makes when he's planning a difficult boss encounter for his campaigns."

    a talk "Like this?"

    show alex smile

    ##camera sfx, zaina smirk
    play sound "camera.mp3"
    "Click..." with flash

    an "The sound of the camera shutter going off is almost swallowed by Zaina's laugh."

    ##alex blush

    an blush "Okay, so that backfired. For a moment, even with her in front of me, I'd forgotten she had a camera on her."

    an "... But getting Zaina to laugh was worth it."

    an "I definitely don't have to feign embarrassment, though I exaggerate for Zaina's amusement anyway."

    a talk "Hey! You weren't supposed to take a picture of that!"

    show alex smile

    z talk "{i}Really{/i}? And what law says I can't do that?"

    show zaina neutral

    a talk down -blush "The don't-make-fun-of-Alex law!"

    show alex smile up

    z talk "I think I'm well past breaking that law, don't you think?"

    show zaina smile

    a talk up "Oh, believe me, I know."

    ##zaina and alex smile

    an smile "We share a smile from across the room and I lower the flashlight from my face."

    a talk "Is this good?"

    show alex smile

    z talk "A bit higher still."

    z "... Mhm. Yeah, that's better."

    show zaina smile

    an "I'm careful to stay still, lest I ruin the lighting, and in the quiet, my eyes are drawn to Zaina once again."

    an "I've always been curious..."

    a talk "How'd you get into photography?"

    an smile "If Zaina hears my question, she gives no indication. She resumes her work behind the camera and the shutters fill the silence."

    an "I consider repeating myself when at last, she lowers her camera."

    z talk "I got in trouble a lot when I was younger."

    show zaina smile

    a talk "Really? I never would have guessed."

    ##zaina smirk

    an smile "Even with a camera blocking half her face, it's hard to miss her smirk."

    an "It's clear she takes no offense at all from my sarcasm, like she's proud of having such a reputation."

    z talk "Yeah, well..."

    z "My parents thought that if I had a hobby, I wouldn't have the time or energy to stir up shit."

    show zaina smile

    an "She lifts her camera again and I assume that's the entirety of her answer, but she continues."

    z talk "They signed me up for a bunch of lessons for all kinds of shit, but I'd never get past the second day."

    z "Buying me a bunch of disposables was probably their twentieth attempt...? Something like that."

    show zaina smile

    a talk "And you liked it straight away?"

    an smile "She barks out a laugh so hard she's forced to put down her camera."

    z talk "Hell no."

    z "I thought it was stupid."

    z "I wasted so much film just taking pictures of me flipping the camera off."

    show zaina smile
    ##alex laugh

    an smile "That definitely sounded like something Zaina would do. Past or present."

    z talk "But my parents printed ‘em all out anyway and let me put ‘em up my walls."

    z "That was probably how it started."

    show zaina smile

    an "So she liked having something she made up on display..."

    an "She takes a few more pictures before I catch her looking at me over the lens."  ## Did you mean 'lenS' and not 'lenSE'? Corrected it. - Angel

    an "Perhaps sensing I still had more to ask her, Zaina lowers her camera and gestures for me to come over."

    an "I join her side and she angles the camera away from me for a moment, flipping through the pictures she's taken. When it appears as though she finds ones she likes, she angles the screen back into my view."

    an "Only to flip through more of them, though I feel it's for my benefit this time. Unlike before, she goes through them slowly, pausing just long enough for me to take in each picture."

    an "This set of pictures seems to be of the same thing: a row of abandoned beds we found earlier."

    z talk "I don't really have much of a technique. I like to feel things out as they come."

    z "But one thing I always do is take a bunch."

    show zaina smile

    an "True to her words, there's at least fifteen pictures of just the beds."

    z unsure talk "Chances are you won't get your shot on the first try."

    z "Or even the second or third one."

    z -unsure "I'll change the angle on some of ‘em. Or shoot from the ground. Play with the lighting a little."

    z "You don't always know what works at the start, and sometimes going with the flow does the job."

    show zaina smile

    an "Zaina stops at the picture she must deem the best."

    an "I honestly can't tell the difference. Most of them look the same to my amateur eyes."

    z talk "Look at this one. Because I opened the aperture up and increased the ISO, I get a shallower depth of field. There's more focus on the shadows here."

    show zaina smile

    an "Aperture? ISO? Depth of field?"

    an "These terms mean absolutely nothing to me."

    a unsure talk "Uh..."

    show alex shock

    ##zaina laugh

    z talk up "I'm just messing with you. That was all bullshit, I have no idea what I actually said."

    z "I just picked a random photo, too."

    show zaina smile

    an up smile blush "My cheeks puff up before I know it and Zaina takes great pleasure in poking one to release the air that's gathered. When she's done, she pinches my nose."

    z sweat talk "Sorry, I was starting to feel like some pretentious ass professor and just leaned into it."

    z -sweat "The part about taking a lot of shots was real, though."

    z "Anyway..."

    z "I'm done here."

    show zaina smile

    an -blush "Zaina loops the camera strap from under her head and hands me her camera."

    ##surprised alex

    an shock "I take it and my lips part to say something—{i}anything{/i}, but I'm stunned into silence."

    z talk "You once asked me if I could teach you how to take photos, remember?"

    an smile "I do. I never actually expected her to take me up on it, though."

    z talk "Well? That was it."

    z "There's not much to it, really."

    ##zaina smirk 

    show zaina smile

    pause 1.5

    z talk "But, hey, if you're good, I'll even let you use my tripod."

    show zaina smile

    an shock "There's a teasing lilt to her voice I'm definitely not a stranger to, but even that doesn't distract me from the weight of the camera in my hands."

    an smile "It's heavier than I expected, and still warm from when Zaina was holding it. I trace the buttons with a finger, utterly mystified."

    an "Finally it sinks in, and there's nothing I can do to stop the joy that blooms in my chest. It spreads, to my toes, my fingers, and finally to my mouth, where it splits to the widest it's ever been."

    ##happy alex, shocked zaina

    show zaina neutral up

    an smile "The strain on my cheeks would probably hurt if I didn't feel so warm all over."

    an "Zaina actually trusts me with her camera. I'd never even seen her allow Finn and Paxton touch it. She'd always batted their hands away when they—mostly Finn—tried or dissuaded them with her most intense glare."

    an "I see none of that here. Only faith."

    an "Though Zaina, when I chance a look at her, looks dazed. Like something heavy struck her in the chest."

    an "After a few moments like that, she recovers, a wistful smile crossing her lips."

    z talk "That's no fair."

    z "Making a face like that... When I no longer have the camera..."

    show zaina smile

    an "She moves as if to take the camera from me, but seems to think better of it, patting it from where I hold it in my hands and then crossing the room for the door."

    z "C'mon. Let's get something new for your debut."

    show zaina smile

    an "I follow her into the next room, cheeks warm."

    ##they're moving to a different room so maybe a fadee in and fadee out?

    show zaina at closeleft:
        xoffset 130 yoffset 80
    show alex at closeright:
        xoffset -130 yoffset 120
    with sidefade

    an "The floor has seen better days in this one, but I follow Zaina's example and mostly stick to the corners."

    an "Zaina sees my conundrum right away. She walks me through the zoom feature since I'm unable to get any closer and my first picture is of a rusting wheelchair just across the room."

    an "She peeks over my shoulder when I check the photo."

    z talk "Not bad for a newbie."

    show zaina smile

    an "Zaina nudges me with an elbow and the corners of my lips tug into a bashful smile."

    an "I'm reminded of her nickname for me when I was just starting out with the group. She still calls me that, occasionally, when she wants to tease me, and I can't deny I've gone from disliking it to honestly being a little attached to it."

    an "With it comes memories of our time together."

    z talk "Like I said, don't be afraid to take more pictures."

    z "And you might want to try shooting low for one of them. The light will hit it differently."

    show zaina smile

    an "I lift the camera and try again."

    an "Honestly, I still don't quite know what I'm doing, but Zaina's guidance is easy to follow. I come away with pictures I wouldn't exactly mind posting on my Instagram."

    an "And yet though the pictures are nice, it's sharing this with Zaina that I can't get enough of." 

    an "When I start to get the hang of it, I continue to ask questions anyway, just to see that passion flicker in her eyes when she explains it to me."

    an "It turns thick, prowling clouds into a storm I wouldn't mind getting caught in the middle of."

    an "I proceed to lose myself in that very storm for a moment and it's the sound of a bird chirping a little song that brings me back to Earth."

    ##chirping bird sfx
    play sound "birds.mp3"

    a talk "Oh!"

    an smile "I turn to the source of the noise. A bird—a sparrow perhaps—perches on the open windowsill."

    an "The bird cocks its head at my exclamation, but otherwise stays in place, tittering."

    an "It's a small thing, not much bigger than my fist."
        
    an "I definitely have to take a picture!"

    an "This is my only chance!"

    an "My hands grip the camera while my feet go on autopilot, slow and careful so as to not scare the bird. Zaina follows just as discreetly."

    an "I lift the camera, but I'm all tensed muscle."

    ##smaller font from this point on as they're talking quietly

    z talk "{mumble}Relax...{/mumble}"

    z "{mumble}And breathe...{/mumble}"

    show zaina smile

    an "Zaina squeezes my shoulders and when they finally relax under her ministrations, she wraps her arms around me, hands over mine as she directs the camera to a better angle."

    ##alex blush

    an blush "Her breath tickles my ear and I'm feeling warm for completely different reasons than earlier. I try not to focus on how nice it feels to be in her arms."

    z talk "{mumble}Let's do it together in three...{/mumble}"

    z "{mumble}One...{/mumble}"

    show zaina smile

    a talk "{mumble}Two...{/mumble}"

    show zaina talk
    "{color=#ffff66}ALEX{/color} & {color=#62baf0}ZAINA{/color}" "{mumble}Three.{/mumble}"

    show zaina smile
    show alex smile

    an "I press the button."

    play sound "camera.mp3"
    "Click" with flash

    an "I glance at Zaina in the corner of my eye, triumphant, but when I do so, I take my attention off the bird."

    play sound "birds.mp3"

    an "I hear the bird's alarm at the flash rather than see it."

    an "When I turn back it's to the bird just inches from my face as it flies past."

    ##screen shake

    play sound "break.mp3"
    with vpunch

    a shock sweat "...!"

    show zaina sweat frown unsure

    an "I can't help it. I flail."
    an "Through the haze, I can make out the sound of a crash, or something like that, but it's the least of my concerns when I jolt backwards, falling and taking Zaina, whose arms are still on mine, with me."

    an "It's maybe halfway through the fall that I remember the weakened floor, but by some stroke of luck or maybe just Zaina's reflexes, we stop short of falling on the ground."

    an "She rights her footing just in time and stabilizes the both of us."

    an "My heart is racing."

    ##back to normal size font for dialogue

    a frowntalk -sweat "That was clo—"

    an shock unsure "I can't help but feel like I'm missing something important and sure enough, my eyes are drawn to the sad heap of something black."

    an frown "Something most definitely broken."

    ##shocked alex

    an shock "If my heart was racing before, now it just stops."

    an "That must've been the noise I heard earlier."

    an "Zaina's camera lies at our feet, in pieces."

    a blush sweat frowntalk "I-I'm so sorry, I—"

    an frown "I can't bring myself to look at Zaina. Not when I've ruined what was probably one of her most prized possessions. Not when I've ruined everything."

    ##upset alex

    a frowntalk "I didn't mean to drop it, I'm sorry—"

    a "I-I just got scared by the—"

    a "That's no excuse. I'm... So so sorry, it's all my fault—"

    show zaina -sweat up neutral

    an -sweat frown "Zaina shushes me. And takes my hands."

    z frowntalk "Hey... Look at me."

    show zaina frown

    an "It takes everything within me not to just bolt straight out of there and drive back home."

    an "But I owe it to Zaina to do what she asks, even if it's the last thing I want to do. Even if I can't bear to see her look at me with disgust."

    an "My discomfort is second to Zaina's loss."

    a sweat "..."

    an "With great trepidation, I finally meet her eyes. I steel myself for the fall out."

    ##shocked alex

    an shock "Only to reel back at the genuine relief that floods her face. It's in the way her eyes roam all over me, checking for injuries. It's in the way her lips quiver just the tiniest bit with a sigh before stretching into a small, muted smile."

    an "And her hands—they've let go of mine to gently cup my face, thumbs swiping under my eyes."

    z frowntalk "Forget the camera. I can always buy a new one."

    show alex frown

    z talk "There's only one of you."

    show zaina neutral

    an unsure "The tears that have gathered in my eyes fall freely now and when she wipes each one, it's not with any urgency or pressure. She takes her time, just as she wants me to."

    an "It's a level of gentleness I've only seen her use with Finn, when she thinks no one is looking."

    an "The thought that I've become someone important in her life like Finn and Paxton brings more tears to my eyes."

    an -sweat "Eventually, I take over for Zaina, wiping at my eyes myself while she presses a kiss to my temple, and by the time that Finn and Paxton arrive, I'm all cried out."

    an up "Still, I appreciate her standing in front of me anyway, blocking the boys' view of me."

    hide zaina
    hide alex
    with dissolve

    ##worried finn and paxton
    show zaina frown unsure at leftt:
        xoffset 130 yoffset 100
    show alex frown unsure at rightt:
        xoffset -130 yoffset 100
    show finn up frown behind zaina at left
    show paxton up frown behind alex at right
    with dissolve

    f frowntalk "We heard something."

    show finn frown

    p frowntalk "What happened? Are you guys okay?"

    show paxton frown

    an "My eyes accidentally lock with Finn's, just above Zaina's head, but he averts his gaze after a beat and says nothing."

    z frowntalk "It's nothing. The sound made it worse than it actually was."

    show zaina frown

    f frowntalk "Which was...?"

    show finn frown

    an "Zaina bends down and picks up what's left of her camera. I try not to linger on the disfigurement this up close, as Zaina would want me not to."

    z frowntalk "I dropped it. That's all."

    show zaina frown

    an "Paxton's face softens in what I think is sympathy and he squeezes Zaina's shoulder."

    p frowntalk unsure "How unlucky."

    show paxton frown up

    z frowntalk "It's fine."

    show zaina frown

    an "They seem to be taking cues from Zaina, who, by all accounts, looks utterly unfazed rather than upset."

    ##neutral finn and paxton
    show paxton unsure frown
    show finn unsure frown

    z frowntalk "We can take pictures on your phone from now on."

    z "No big deal."

    show zaina frown

    p talk "Let's call it a night for now. That's too much excitement for one day."

    show paxton frown

    z frowntalk down "Don't say that. The idiot's gonna get himself hurt just for the hell of it."

    show zaina frown

    f talk "Huh. My pinky looks mighty breakable to me..."

    show finn smile

    p frowntalk "Finn!"

    show paxton frown
    show finn frown

    pause 1.5

    hide zaina
    hide finn
    hide paxton
    hide alex
    with dissolve

    stop music fadeout 5

    scene black with fade

    an "The boys lead the way out while Zaina stays by my side, lingering behind them a few steps and holding my hand." 
    an "Her hand always feels like coming home after a long day and there's nothing I would like more than to hold her hand forever, now especially."

    an "When I go to sleep that night, I dream of soft hands and gentle caresses."

    ##scene twelve 
    ##alex apartment
    scene bg alex_room
    with fadee

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    an "The guilt, though it subsided after Zaina consoled me, returns with a vengeance when I don't see her for a couple of days."

    an "It eats at me over breakfast, on the drive to school, and even during my classes."

    an "I relive the moment over and over in flashes, and the sound of the camera hitting the ground haunts my dreams after that night. I don't sleep very well for a while."

    an "So long the memories of Zaina's soft touch..."

    an "However, a free day finds me in my apartment, at my desk, laptop open."

    an "I Google ‘best camera for pictures' and intend to spend hours skimming through lists and narrowing down the camera with the best specs."

    an "If I were to really buy her a replacement, only the best would suffice for Zaina!"

    an "Also, I had absolutely no idea what kind of camera the one she owned was..."

    an "One look at the prices, however, has my stomach dropping. I didn't realize they were so expensive."

    an "I revise my search to \"best {i}cheap{/i} camera for pictures\" but even those were outside my budget. Way outside my budget."

    an "On the cusp of giving up, I wonder out loud to myself if the cafe Paxton works at is hiring and for a few moments, I actually entertain the thought of working there."

    an "But I shake the thought, tempting as it is. Not only would it take me forever to gather enough money, if my parents heard that I was wasting ‘precious study time' on a job, they'd have my head for it."

    an "Still, it doesn't stop me from asking Paxton how much he makes per hour."

    an "Just y'know... In case."

    an "It's when I eagerly await Paxton's response that I get texts from Zaina."

    play sound "phonevibrate.mp3"
    "Bzz..." with vpunch

    an "They're texts telling me not to worry about the camera—"

    an "I spare a glance at my laptop screen, where a list details the pros and cons for each of the twenty cameras catalogued. A little too late for that."

    an "—and that it's all fine."

    an "She even sends me heart emojis, which I suspect is her way of cheering me up."

    an "It works. A little."

    an "It doesn't dispel any of the doubt I feel about Zaina's true feelings on the incident, but it does ease some of the weight on my shoulders."

    an "Zaina's not ignoring me, at least, so that's a marked improvement from last time."

    an "That she even bothered to text me when she could've very easily blocked or ghosted me again means that she hasn't given up on our relationship."

    an "And that she's still thinking of me, even after what I did."

    an "I expel a shaky breath and once again return to my laptop."

    an "Forgiveness isn't going to come easy, from myself at least, but even if she's angry, I'd rather have her angry and in my life than not at all."

    ##scene thirteen
    ##alex apartment
    scene bg alex_room
    with fadee

    an "Paxton gets back to me later, though I don't apply for a job at the cafe. It does motivate me to be more proactive about saving, however."

    an "The next two days, I budget out every purchase. If I don't need it, I don't buy it."

    an "It gives me some peace of mind—knowing that while I certainly can't cash out the money for a camera right now, I can chip in and help Zaina out."

    an "Maybe it's selfish, doing so to alleviate my guilt, but in the end it's all for one thing: to get Zaina to smile."

    an "And not with pity for me like before, either, but a genuinely happy smile."

    an "I allow myself to imagine it while I pour over my textbook."

    an "The words on the paper blend together into nothingness and I prop my chin up with a hand, thinking of crooked smiles and hints of teeth more blinding than her camera's flash."

    an "The images have me in such a vice-grip that I almost don't notice the sound of an incoming call."

    play sound "phonevibrate.mp3"
    "Rinng..." with vpunch

    an "I mark my place in my textbook, shake my head free of my fantasies, and then reach for my phone. I look at the contact information."

    an "It's Zaina."

    an "I pick up immediately."

    a "Hello?"

    stop music fadeout 2

    an "A sharp intake of breath answers me and I straighten in my chair, tempted to take one of my own. That's not a good sign."

    an "Zaina's no fan of phone calls as it is, but the few I've had with her have been lighthearted, usually when she's just across the room and wanting to whisper a joke, often at the expense of someone in that room."

    an "This is clearly something else altogether."

    z "It's Finn... he's—"

    an "Her voice breaks, though whether it's because she's overwhelmed or just doesn't know what to say, I can't say for certain. Probably both."

    an "She gathers herself together quickly, though, and I can {i}feel{/i} the urgency of the situation bleeding through the phone."

    z "He's gone off by himself somewhere—"

    z "And he's hurt. Real bad."

    an "The fact that Zaina doesn't spare any time berating Finn for his actions tells me all that I need to know about the situation. There must be no time at all."

    a "Do you have the address to the place?"

    z "Ye—yeah, I'll send it to you right now."

    a "Alright, I'll meet you there. Is there anything you need me to bring?"

    z "Your first-aid kit, just in case."

    z "Cardboard, if you have any."

    z "Belts would be useful, too."

    an "Cardboard? {i}Belts{/i}? My lips pull into a grimace as I put it together."

    an "There's really no time to lose, then. If Finn's really broken something, then we'd have to hurry or else he might go into shock, waiting all by himself like that."

    a "I'll see you in a bit."

    z "Okay..."

    an "There's silence on the line and I almost think she's hung up, but then—"

    z "... Alex?"

    a "Yeah?"

    z "Thank you."

    an "The call ends this time and I allow myself a moment to just breathe, knowing I won't have the chance to do so again once I leave my place."

    an "No time to lose!"

    an "I proceed to turn my apartment upside down looking for the materials Finn needs for his splint."

    an "Any remaining thoughts of broken cameras and broken trust begin to slip from my mind as I focus only on Finn and getting to him as fast as possible."

    an "When I push against the speed limit as far as I can without getting pulled over, fear is the prevailing emotion that courses through my veins, not guilt."

    ##scene fourteen
    ##mansion bg
    scene bg mansion
    with fadee

    play music "Be_piano12.ogg" fadein 1
    queue music "Be_piano12.ogg"

    an "Normally, I would be parking a couple blocks away from the site for insurance, but considering Finn's situation, I park as close as I can to the mansion."

    an "I pull up just in front of it and hurry out my car, splint materials in my arms."

    an "It's awkward carrying everything together and I'm a lot slower because of it, but I don't want to risk a second trip when I don't know how long Finn's been waiting."

    play sound "motorcycle.mp3"
    "Vrumm..." with vpunch

    an "I've just about reached the door when Zaina arrives. I hear her, rather than see her—the motorcycle's engine giving her away."

    an "I don't look over to confirm it's her, preoccupied with getting the door open, but she's by my side in a flash, moving with a speed and urgency I've never seen from her before."

    an "She takes the cardboard from me, freeing up my hands as we enter together."

    an "The sound of my heart thudding loudly in my ears fills the eerie silence."

    a "Finn?"

    an "I'm careful not to yell as the last thing we need is the police here. I speak in what I think is a good volume, for anyone inside to hear me."

    an "But only silence answers me and Zaina and I look at each other, worried."

    an "Had Finn passed out?" 

    an "My lips part to try again, only louder this time, but a voice, sounding more bashful than weak, reaches us from upstairs."

    ##small text, as he's probably wheezing this out
    f "{size=16}Up here...{/size}"

    an "Zaina wastes no time climbing up the stairs, two at a time, and I follow her, though a little more carefully."

    an "I trust Zaina, given how long she's been doing this, but it wouldn't do anyone any good if I got myself hurt too."

    an "There's no telling what else could be weak and rotting."

    an "I keep an eye on the floors and any holes in them, and after calling for him a few more times, we locate Finn, in a pile of what probably used to be part of the third floor."

    an "Zaina is on him in an instant."

    show finn down frown:
        xalign 0.75
        yalign 1.0
    show zaina unsure frown:
        xalign 0.05
        yalign -2.2
    show alex unsure frown:
        xalign 0.33
        yalign 2.3
    with dissolve

    z down frowntalk "You... you {i}idiot{/i}."
    show zaina frown

    ##finn smile
    show finn smile
    an "Finn's eyes shut in what I think must be relief, while a wry smile turns one side of his mouth."

    f unsure frowntalk "Tell me something I don't know."
    show finn smile

    an "If he's making comments like that, he mustn't be feeling too bad."

    an "Still, the way his right leg is bent like that doesn't look good, even if he is lucky to only come away with that after a fall from the third floor."

    ##neutral alex
    an neutral "Closing my eyes, I try to recall what I've learned in class."

    an "Shock... What are the symptoms of shock...?"

    an "I press a hand against his forehead, while the other checks for his pulse."

    an "His skin doesn't feel clammy... and his pulse is a little fast, but not alarmingly so. It's not weak either."

    a unsure frowntalk "He doesn't seem to be experiencing shock."
    show alex frown

    an "Zaina, from where she's crouching by Finn's leg, looks relieved."

    z up frowntalk "That's good."
    show zaina frown

    z unsure frowntalk "He's not hurt from anywhere else?"
    show zaina frown

    a up frowntalk "No, just scratches, but I'll take care of those right now."
    show alex frown

    an "Zaina then resumes her inspection of Finn's leg, who hisses when her fingers brush upon a certain spot. I take the opportunity to apply disinfectant to his cuts and scratches while he's distracted."

    z down frowntalk "Yeah, that's definitely broken..."
    show zaina frown

    a unsure frowntalk "At least the bone didn't break the skin."
    show alex frown

    an "That would've been bad news for everybody. There wouldn't be much we could do except call 911 and wait."

    z up frowntalk "Alright, come help me with splint."
    show zaina frown

    an "I take the opposite side of Finn's leg and assist Zaina with the cardboard, which we cut into two smaller, rectangular pieces for splinting."

    an "..."
    an "..."
    an "..."

    an "While we're positioning the cardboard into place, I catch Finn's eye."

    a down talk "This has to be the worst, right?"
    show alex frown

    an "Finn blinks slowly at me, and I'm not sure if it's delirium from the broken leg or just confusion."

    f unsure talk "What?"
    show finn smile

    an "I grab my shoulder to jog his memory of the night he hurt himself with the door."

    a up frowntalk "Back then, you said you've gone through worse."
    show alex frown

    f up talk "Ah."

    f down talk "I did."
    show finn smile

    an "The smile that quirks his lips is a curious mix of something sly yet melancholic. Like there's a sad secret he's keeping."

    f unsure talk "This is pretty bad, but..."
    show finn smile

    an "But?"

    an "What could be worse than this?" 

    z down frowntalk "Quit it. She doesn't understand your sense of humor."
    show zaina frown

    f down frowntalk "But I wasn't joking?"
    show finn frown

    z up frowntalk "Yeah, right."
    show zaina frown

    ##finn soft smile/laugh
    show finn smile
    an "I look at Finn again, and almost miss the way his shoulders lightly shake with mirth."

    an "He's clearly subdued, as if there was something that still had a tight grip on him, but it seems he's able to joke about it, at least."

    an "This discovery eases my mind some, and I'm able to devote the rest of my attention to securing the splint with the belts without much worry for Finn's safety."

    an "It's when we're putting the last belt on that he speaks again."

    f unsure talk "Thank you."
    show finn smile

    an "He's looking at both of us, but I feel this is more for Zaina's benefit than mine."

    f up talk "I'm glad I called you."
    show finn smile

    z down talk "Sh-shut up."
    show zaina smile

    an "Zaina just avoids his eyes and finishes securing on the belt. When she's done, she clears her throat."

    an "She does this a couple of times."

    z unsure talk "Alright. We're done here."

    z up frowntalk "We've done all we can with the leg, but we have to get you to a hospital."
    show zaina frown

    f down talk "Okay."
    show finn frown

    an "Good. Finn is smart enough not to argue."

    z unsure frowntalk "I can't take you there on my bike, though. I don't want to, but it looks like we'll have to call an ambulance..." 
    show zaina frown

    ##shocked alex
    an "I blanch at the suggestion. Who would be paying for the ambulance bill?"

    an "I doubt any of our insurance covers it."

    a up shock "W-Wait! We can take my car."

    a unsure frowntalk "We'll have to carry him down, but..."
    show alex frown

    an "That was a better idea than calling for one and having the police show up too. Finn was technically trespassing."

    an "Finn looks between us and shrugs, appearing as if he accepted his fate either way."

    f unsure talk "I'm fine with whatever Zaina decides."
    show finn smile

    an "With the decision up to her now, Zaina falls silent. I don't have to know her very well to see the uncertainty on her face."

    an "It's in her furrowed brows and her frown. She's usually not this serious if she can help it."

    an "But finally, she makes up her mind."

    an "Zaina bends down to sling one of Finn's arms around her shoulder. She gestures for me to do the same."

    z down frowntalk "Help me get him to your car."
    show zaina frown

    z down frowntalk "And you—"
    show zaina frown

    an "Up this close, Finn can't avoid Zaina's glare even if he tried."

    z down frowntalk "—don't put any weight on your leg, if you can help it. If you need us to carry you higher, {i}tell us{/i}."
    show zaina frown

    f up talk "Yes, ma'am."
    show finn smile

    z unsure frowntalk "Ready?"
    show zaina frown

    #both finn and alex talking
    show alex frowntalk
    show finn talk
    "{color=#ffff66}Alex{/color} {color=#FFF}&{/color} {color=#bd8be7}Finn{/color}" "Ready."
    show alex frown
    show finn smile

    hide alex
    hide finn
    hide zaina
    with dissolve

    ##black screen
    scene black
    with dissolve

    an "The tough part was getting Finn to the car. But now that we were confident Finn wasn't in any imminent danger, we could afford to move slower and more carefully."

    an "Finn served as our eyes as Zaina and I carefully moved downstairs and out the mansion as one unit."

    an "Once he was in my car, it was all smooth sailing."

    an "..."

    an "..."

    an "..."

    an "The hospital staff take him away to the emergency room when we arrive. I reassure Finn we'll be staying, through the night if necessary, but he declines vehemently, and says he can call a cab home, so we shouldn't bother."

    an "One look at Zaina after he's gone tells me she doesn't like the idea, though."

    an "I don't either. I want to make sure he's okay, just as much as Zaina."

    an "But as a compromise, I call Paxton during a lull, to tell him what happened."

    an "He's as shocked as anyone would be. Fortunately, he's nearing the end of his shift, so he can head over soon. Paxton promises to call when he arrives and that he'll keep us updated on Finn's status."

    an "This frees me and Zaina up to go home, and I feel a little less guilty than if we'd just left Finn there alone."

    an "Zaina and I gather our things, and I drive back to the mansion, where Zaina left her motorcycle."

    ##not sure if mansion bg still works here if they're outside
    scene bg mansion
    with sidefade

    an "But Zaina lingers by my car, even as she's out of it."

    an "Though I shoot her an inquisitive look, I'm patient, allowing her to take the time to get her bearings straight."

    an "It's not often that Zaina's at a loss for words, after all."

    show alex down frown at closeright:
        yalign -0.25
    show zaina down frown at closeleft:
        yalign -0.25
    with dissolve

    z unsure talk "Do you... want to spend the night at my place?"
    show zaina smile

    ##alex smile
    a up talk "Yeah, of course."
    show alex smile

    ##black screen
    scene black
    with dissolve

    an "I follow Zaina's motorcycle back to her place and when we're there, it's a struggle up the stairs."

    an "We lean on each other the whole way up, not unlike a gaggle of drunk college students heading back home after a night out."

    ##zaina's apartment
    scene bg zaina_room night
    with fadee

    play music "Be_Longing04.ogg" fadein 1
    queue music "Be_Longing04.ogg"

    an "As it is, I all but collapse on the couch when Zaina opens the door to her apartment."

    an "Zaina joins me."

    an "Our time on the couch is spent mostly in silence. I think we both needed some time to relax after all the craziness."

    an "Eventually, Zaina gets up to go get snacks and drinks and when she returns, food in both of our bellies, it's then that I gather enough energy to finally say what's been on my mind since this all started."

    show alex up frown at closeright:
        yalign -0.5
        xalign 0.8
    show zaina up frown at closeleft:
        yalign -0.25
        xalign 0.2
    with dissolve

    a down frowntalk "So, Finn..."
    show alex frown

    ##choice
    menu:
        "He doesn't hate you.":
            a unsure frowntalk "I know you think he does, but..."
            show alex frown
            z unsure frowntalk "Where is this coming from all of a sudden?"
            show zaina frown
            an "Her lips are tight-lipped behind the cup of coffee she's drinking."
            an "It's clear Zaina doesn't want to revisit this topic, though it's likely more because she doesn't like being vulnerable than her disliking the subject itself."
            a up talk "Today."
            a unsure talk "After today, I have no doubt."
            show alex smile
            z down talk "You sound... confident."
            show zaina frown
            an "She says confident like she means to say something else."
            a up talk "I am."
            show alex smile
            ##end choice
        "He really trusts you.":
            z down frowntalk "No, he doesn't."
            show zaina frown
            an "She says that without any hesitation at all. I don't think I saw her even blink."
            an "I tilt my chin at her."
            a up talk "I think you're wrong."
            show alex smile
            z down talk "And I think you're wrong."
            z unsure talk "You're cute when you get like this, but I'm not budging."
            show zaina smile
            ##alex blush
            an blush "I try to physically will my blood to not go to my cheeks." with Dissolve(1.0)
            ##alex serious
            a unsure talk "I know what you're doing!"
            a down talk "You're calling me cute just so I'll drop this!"
            show alex smile
            ##zaina smirk
            z down talk "Smart, too."
            z up talk "Just my type."
            show zaina smile
            an -blush "I fix her my most serious look, though it's effectiveness is probably dampened by the smile that's threatening to break through." with Dissolve(1.0)
            a down talk "Just—just listen to me."
            show alex frown
            ##end choice

    a unsure talk "Who did Finn call?"

    a up talk "You."

    a unsure talk "Who did he let decide on how we were going to get here?"

    a up talk "You."
    show alex smile

    z unsure talk "I don't see what that has to do with anything."
    show zaina frown

    an down frown "I level her with the closest thing to a glare I can manage with her."

    an "When she quiets down, I reach over to grasp her hands in mine."

    an "I squeeze."

    a up talk "Finn got himself into a bind and you were the first person he called."

    a down talk "Because he trusts you to be there for him."

    a unsure talk "I know you guys fight a lot and maybe sometimes it doesn't feel like you're friends, but..."

    a up talk "He obviously recognizes the effort you put into the relationship and thinks highly of you."

    a unsure talk "Finn wouldn't have turned to you if he didn't."

    a down talk "Look, you've known him longer than I have. Would he really keep the company of someone whose guts he hated?"
    show alex smile

    an "I exhale a shaky breath."

    an "My chest is practically heaving with how worked up I am."

    an "If nothing else, I want Zaina to know just how much her friends value her in their lives."

    an "When I finally catch my breath, I nervously chance a look at Zaina, unsure exactly how she's going to take my spiel."

    ##zaina shocked or neutral i'm not sure which fits better

    an "For as long as I've known her, Zaina doesn't tend to show emotions on her face very deeply, except when she's angry, but looking at her now—"

    an "Her lips are parted and for once, she's speechless."

    an "I don't know if it's surprise or incredulity, but at least I've said my mind."

    play sound "phonevibrate.mp3"
    "Rinng..." with vpunch

    an "A call, most likely from Paxton, saves her from having to respond, though."

    an "I reluctantly let go of Zaina's hands so she can reach for her phone."

    an "She answers, but the phone call doesn't last long, just under a few minutes."

    a unsure talk "So?"
    show alex smile

    z unsure talk "The break isn't too bad."
    show zaina smile

    an "I let out a sigh of relief. It feels like a huge weight is off my shoulders."

    a down talk "That's good."
    show alex smile

    z up talk "They're keeping him overnight, though, just to monitor his condition."
    show zaina smile

    z unsure talk "It looks like Pax might stay the night, too."
    show zaina smile

    ##surprised alex
    a up shock "How'd he convince Finn of that?"
    show alex smile

    an "He was pretty adamant about us not staying longer than necessary."

    z up talk "Pax has his moments."
    show zaina smile

    an "The smile that crosses her lips is one of pride. I can see why, it's usually Zaina who objects when Finn's being unreasonable, not Paxton."

    an "I admit, I would've loved to see that."

    an "But now, with the drama of tonight mostly behind us, I'm content to let the couch do its job. I sink into the cushions with a sigh, energy all sapped out."

    an "Zaina's intent on separating me from the comforting embrace of her couch, however. She loops an arm around me and tugs me up, practically dragging me into her bedroom."

    an "In my exhaustion, I don't have the energy to overthink about the implications of sleeping in the same room."

    z unsure talk "We can share the bed. I'm not letting you sleep on the couch after all that."
    show zaina smile

    a unsure talk "No, I guess that would be cruel and unusual punishment, wouldn't it?"
    show alex smile

    ##zaina laugh

    an "Zaina's laugh, even tinged with fatigue, is music to my ears. I snuggle into the covers with a contented smile on my face."

    z up talk "Alex?"
    show zaina smile

    a up smile "Mhmm...?"

    z down talk "I said it before, but... Thank you."

    z up talk "For everything."
    show zaina smile

    hide zaina
    hide alex
    with dissolve

############# Scene 15
    
    scene bg zaina_room with fadee

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    an "I wake the next morning to empty sheets and the sunlight filtering in through the window."
    an "My fingers trace the empty space beside me. They're still warm."
    an "Zaina must've woken up not too long ago."
    an "Sighing, I savor the feeling of a warm, cozy bed, much needed after the events of last night. I inadvertently inhale Zaina's scent when I do so, the lingering smell of her perfume light and pleasant."

    an "Surprisingly at odds with her personality perhaps, but now I know better."

    an "It suits her and her capacity for gentleness well."

    an "I allow myself a few minutes in bed just letting the smell lull me into a sense of tranquility, thinking of her soft hands and the care behind them."

    an "When I feel at peace, I finally bring myself to get out of bed."

    an "I trudge into the living room, steps still heavy with sleep."

    an "I'm met with the sight of Zaina setting out plates of toast with eggs, along with a bowl of fruit in the middle."

    show alex up frown at closeright:
        yalign -0.5
        xalign 0.8
    show zaina up frown at closeleft:
        yalign -0.25
        xalign 0.2
    with dissolve

    an "She smiles, in a sheepish manner that doesn't quite befit someone of her temperament."

    z talk "I'm better at taking pictures of food than actually cooking, but..."

    z talk "I tried."

    z talk "I thought you'd be hungry."

    show zaina smile

    a talk "I am."

    an smile "I don't say much more than that as my stomach does the rest of the talking for me."

    ##stomach growl sfx
    ##alex blush, zaina smirk

    z talk "You might want to stick to the fruit. I can't promise that the rest isn't shit."

    show zaina smile

    ##alex laugh

    a talk "How do you mess up toast?"

    show alex smile

    z talk "Very badly."

    show zaina smile

    an "Despite Zaina's best attempts to dissuade me from the toast and eggs, they're not bad at all. The toast isn't burnt and the eggs, though a little runnier than what I usually like, are pretty good."

    ##zaina, alex neutral

    an "I'm spreading jam on my last piece of toast when Zaina gets up from the table."

    z talk "I have something for you."

    show zaina smile

    an frown "That catches my attention."

    a shock "What is it?"

    show alex frown

    z talk "You'll see."

    z talk "Though I can give you a hint..."

    z talk "For something in return."

    show zaina smile

    an smile "It doesn't take a rocket scientist to figure out what Zaina has in mind."

    an "I indulge her, beckoning her closer with a finger. She puts on the airs of someone who's clueless on what's about to happen, but the telltale twitching of her lips gives her away."

    an "Not that it matters much when I brush my lips against hers, swallowing her smile."

    ##EVENT IMAGE HERE
    scene ZainaCG2 with dissolve

    $ persistent.CG4_unlocked = True

    an "The kiss itself is soft and warm, and tastes of daydreams made underneath the shadow of a tree and strawberries."

    an "My hand slides up to cradle her cheek, tangling my fingers gently into her hair. I use it to bring her closer and I feel as much as hear the way Zaina sighs into the kiss."

    an "When we break apart, Zaina leans her forehead against mine, not wanting to leave just quite yet. We relish each other's company for a moment."

    ##zaina, alex smile
    scene bg zaina_room with fade

    show alex up frown at closeright:
        yalign -0.5
        xalign 0.8
    show zaina up frown close at closeleft:
        yalign -0.25
        xalign 0.2
    with dissolve

    z talk "I guess that was probably worth a hint or two."

    z talk -close "Well."

    z talk "I was busy getting it together after our time at the sanitorium."

    show zaina smile

    an frown "'It'?"

    z talk "It's why I didn't come see you right away afterwards."

    show zaina smile

    an "Withdrawing, but not without a parting kiss on the cheek first, Zaina leaves for her bedroom and returns with a box shortly after."

    an "She ushers me to the couch before handing over the box."

    z talk "Go ahead."

    show zaina smile

    z talk "It's not a bomb, I promise."

    show zaina smile

    an "Somehow, the image of Zaina holing herself up in her apartment and building a bomb from scratch isn't all that farfetched."

    a talk "Oh? What if what I wanted was a bomb?"

    show alex smile

    z talk "Then I'll keep it in mind for next time."

    show zaina smile

    an "The promises of next times and a future together warms me more than I could possibly say."

    an "With one last look at Zaina, I pry open the box. The lid slides off rather easily."

    an "In it are two sleeves. Of what exactly I can't tell."

    an "I reach for the one on the..."

    ##choice
    menu:
        "Left":
            z talk "Not that—"

            show zaina smile
            an "I pause and Zaina peers over at my selection."
            z talk "Nevermind, that's the right one."

            show zaina smile
            an "I school my expression into a deadpan one."
            a talk "No, this is the left one."
            an smile "She reaches over to pinch my nose."
            z talk "Cute."

            show zaina smile
            ##end choice
        "Right":
            z talk "Not that—"

            show zaina smile
            an "I pause and Zaina peers over at my selection."
            z talk "Look at the left one first."

            show zaina smile
            an "I give her a questioning look, but she shakes her head."
            z talk "There's a method to my madness."

            show zaina smile
            an "I school my expression into a deadpan one."
            a talk "Oh, so you admit you're mad? Finn and Paxton were getting worried."
            an smile "She reaches over to pinch my nose."
            z talk "Cute."

            show zaina smile
            ##end choice

    an "There's no discernible difference between the two, but I pick up the left sleeve. The inside feels pretty... hard? That was the closest word I could think of."

    an "At Zaina's encouragement, I turn the sleeve upside down and empty out the contents."

    an "Inside are... Pictures? The first one, a photo of a wheelchair, looks familiar—"

    ##surprised alex

    a shock unsure "Oh!"

    an "Zaina smiles at me the exact moment it sinks in."

    z talk "I thought you might want to have them."

    show zaina smile

    z talk "Since they're the first pictures you took with my camera."

    show zaina smile

    a talk "But I thought—"

    show alex smile

    z talk "The camera was as good as dead, but the storage card wasn't damaged. I was able to retrieve all my photos."

    show zaina smile

    z talk "Took a {i}hell{/i} of a long time to export, but I didn't lose anything."

    show zaina smile

    an "She regards me with a look that's almost—chiding, maybe?"

    z talk "So don't you dare feel bad, you hear me? I'll say it every hour if I have to to get it through your skull."

    show zaina smile

    a talk "Okay, okay!"

    show alex smile

    an "It was difficult to argue against someone as persistent as Zaina..."

    an "Zaina grins, satisfied. She gestures for me to continue."

    an "There aren't very many photos, despite me following Zaina's advice to take a bunch of them. She must've sorted through all of them and picked the best ones."

    an "That might've been for the best. I don't think I could've been able to tell the difference between take one and take thirteen unless it was really obvious."

    an "Still..."

    z talk "What is it?"

    show zaina smile

    a talk "I don't know... I just—"

    show alex smile

    a talk "They're not very good... you edited these, didn't you?"

    show alex smile

    an "I feel like I've been caught with a pre-school drawing. I'm obviously very touched by Zaina's efforts, but..."

    z talk "Hey!"

    show zaina smile

    an "Zaina pokes me in the forehead and my hands fly out to the spot, rubbing it. She did that pretty hard..."

    z talk "You're a professional now. You should flaunt it!"

    show zaina smile

    an "My eyes flit back to the pictures and I stare at them, unconvinced."

    z talk "I mean it."

    show zaina smile

    an "She takes the pictures from me and spreads them out on the table, probably so I can better look at all of them."

    z talk "And no..."

    show zaina smile

    z talk "I didn't edit them."

    show zaina smile

    ##shocked alex

    a shock "Really?"

    z talk "That's right. I didn't touch a single one."

    show zaina smile

    an "My eyes find the picture of the sparrow and I take it from the pile to closer inspect it."

    an "The photo is clear; a little dark, but the light from the moon shining through the window as it catches on the bird's feathers lends it a mystifying vibe."

    an "Now that I'm looking at it closer, it's... Not a bad picture. It's probably more Zaina's influence than mine, but collaborating on something together is a concept I can get behind."

    an "I decide right then to keep the photos. Not that Zaina would even let me throw them away, but... I wouldn't mind having them up on my wall as a reminder of something we did together."

    an "Something Zaina let me be a part of."

    an "Her confidence in me bolsters my own and when I look at the pictures again, it's in a new light."

    z talk "You can check out the other one now."

    show zaina smile

    an "I toy with the other sleeve."

    an "They're pictures, they must be, but of what, I'm drawing a blank."

    an "It's possible Zaina just printed out highlights from our expeditions, though the reason why she insisted on having me look at them last escapes me."

    an "My mind swims with possible explanations and the number of them only intensify when I finally empty out the contents of this sleeve too."

    an "It couldn't have prepared me for this, though."

    ##alex shocked

    a shock "It's pictures... of me."

    an frown "Sure enough, they're all photos of me, also from our time at the sanitorium."

    ##zaina smile

    an "My eyes seek out Zaina, whose smile is unusually soft."

    a talk "When did you—?"

    show alex smile

    z talk "I pretended to take pictures of stuff behind you."

    show zaina smile

    z talk "It's also why they're mostly close-ups."

    show zaina smile

    z talk "But I think you get the point."

    show zaina smile

    an "I don't. Not entirely at least."

    an "I've snuck pictures of Zaina before, but they're for my eyes only. I certainly don't ever mean to show them to Zaina."

    an "That would be... Embarrassing!"

    an "Zaina must see the confusion plain as day on my face, though, because she throws me a bone."

    z talk "When I met you, you were—"

    show zaina smile

    an "She pauses, mouth moving silently like she's fishing for the right word to say."

    an "When she finds it, she meets my eye and grins."

    ##zaina smirk

    z talk "—a newbie."

    show zaina smile

    z talk "You were kind of like a bumbling fawn."

    show zaina smile

    an "I... Can't disagree with that."

    z talk "But you picked things up quick."

    show zaina smile

    z talk "Faster than the three of us thought you would."

    show zaina smile

    an "Zaina picks up the pile of photos and slowly goes through them in front of me."

    z talk "Can't you tell the difference?"

    show zaina smile

    an "She stops at one of them and places it on the table in front of me."

    z talk "What's different?"

    show zaina smile

    a talk "Um..."

    show alex smile

    a talk "My hair...?"

    show alex smile

    an "My response must not have been what Zaina wanted because she clicks her tongue and lightly hits me with the stack of photos. The twitching of her lips tells me she's fighting a laugh, though."

    z talk "You're joking."

    show zaina smile

    an "I am."

    an "I can see the difference."

    an "I'm smiling in most of them. Probably Zaina's doing, but the boys too."

    an "When I'm with them, it's not about how high or how fast I can go. I can just be me and whatever that entails."

    an "Sometimes it's worrying about Finn. Sometimes it's groaning at Paxton's coffee puns and then turning around and making some myself. Sometimes it's spending the day in Zaina's arms."

    z talk "You look more sure of yourself now."

    show zaina smile

    z talk "You definitely wouldn't have made that same joke when we first met."

    show zaina smile

    an "Zaina's right. I wouldn't have."

    an "Skirting the law does wonders for your confidence, I guess."

    a talk "You didn't have to do this, though."

    show alex smile

    an "The scoff that leaves Zaina's lips is reprimanding, but not unkind."

    z talk "I did."

    show zaina smile

    z talk "You wouldn't have believed the growth you've made if I'd just said it. You need to have tangible proof in front of you."

    show zaina smile

    z talk "You're a science girl, Finn's the same way."

    show zaina smile

    an "Finn's a... ‘science girl'?"

    z talk "And besides—"

    show zaina smile

    ##zaina smile

    an "Uh-oh. That smile doesn't bid well for my heart."

    z talk "How could I pass up such a photographic opportunity?"

    show zaina smile

    z talk "There's nothing more striking than a subject that evolves in front of you."

    show zaina smile

    ##alex blush

    a talk "I—"

    show alex smile

    a talk "That's—"

    show alex smile

    an "I clear my throat."

    a talk "So I'm a Pokemon, now?"

    show alex smile

    an "..."

    an "What. Was. That."

    an "Pokemon? What is wrong with me? That's the least romantic response ever."

    ##zaina smirk or laugh

    an "Zaina seems to find it amusing, though. Not that that makes me feel any better."

    z talk "Sure."

    show zaina smile

    z talk "Have to say, my favorite is probably your unevolved form."

    show zaina smile

    z talk "Look at little Newbie."

    show zaina smile

    hide zaina
    hide alex
    with dissolve

    an "I pick up my face from behind my hands and look at the photo she's holding out."

    an "It's the very first photo she ever took of me on our first outing as a group. When a noise spooked me and I screamed—just a little."

    an "I drop my face back into my hands, groaning. I can't believe she immortalized it!"

    an "Zaina's laughter fills the room, fueling my neverending shame, and yet when I take a peek to see her head thrown back with abandon, I find it hard not smile."


    return