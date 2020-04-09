####################################################################################################################
#######################                                                                  ###########################
#######################                         Zaina's Route                            ###########################
#######################                                                                  ###########################
####################################################################################################################
init python:

    def mumble_tag(tag, argument, contents):

        """
        Useful for when a character is either mumbling or whispering.
        """

        size = gui.text_size / 1.5

        return [(renpy.TEXT_TAG, u"size={}".format(size)),] + contents + [(renpy.TEXT_TAG, u"/size"),]


    def shout_tag(tag, argument, contents):

        """
        Useful for when a character is shouting.
        """

        size = gui.text_size * 1.5

        return [(renpy.TEXT_TAG, u"size={}".format(size)),] + contents + [(renpy.TEXT_TAG, u"/size"),]

    config.custom_text_tags["mumble"] = mumble_tag
    config.custom_text_tags["shout"] = shout_tag


label zainaroute:

    ## This is just a failsafe ;)

    jump zainaroute_scene_1

label zainaroute_scene_1:

    ## Scene One
    scene bg alex_room with fade
    show alex with dissolve

    an "These days I find myself restless during classes. My eyes wander to my watch too often for my liking, and when it’s not on my wrist, it’s on the door."
    an "My mind, on the other hand, wanders to starry night skies on rooftops and crumbled buildings."
    an "I got home one day and opened my notebook to find doodles in the margins. And even {i}I{/i} had a hard time deciphering the notes that I {i}did{/i} take."
    an "And yet... I can’t bring myself to feel too bad about it."
    an "Going out with Finn, Paxton, and Zaina has been the most fun I’ve had in years."
    an "Worries of my overbearing parents hovering over my shoulders, watching my every move, they all simply melt away when I’m with them."

    ##phone buzz sound effect
    # play sound phone_buzz_sound

    an "Speak of the devil."
    an "I suppose it was too good to be true. I haven’t heard from them in a while after all."
    an "My stomach no longer drops at the thought of my parents texting me for updates, but still I brace myself as I pick up my phone."

    ##alex surprised 

    an shock "It’s not my parents."
    an "Instead, it’s a text from Zaina and—-oh."
    an "She wants to go on a date."
    an "With me. On a date."

    ##alex blush

    an smile blush "The room suddenly feels a whole lot warmer."
    an "I stare at my phone, my mind scrambling for a response."
    an "Should I say yes? No? I haven’t dated anyone since I was fourteen."
    an "And it wasn’t another woman. I’ve never been with another woman."
    an "But Zaina..."

    ##alex soft smile

    an -blush "Sure, she’s pretty rough around the edges, and sure, she really likes picking on me, but I do find myself wanting to see her smile lately. Not just her usual smirk, either, but her smile."
    an "I text her back in the affirmative, ignoring the warmth in my cheeks and the way the phone feels clammy in my hands."
    an "Maybe two seconds pass before Zaina replies, with a bunch of heart emojis."
    an "I laugh at that. Zaina didn’t seem the type to use emojis, much less heart ones."
    an "Another text follows that, with a time and a heads up that she’ll be picking me up tomorrow."
    an "Tomorrow... I have a test tomorrow."
    an "My eyes drift to the textbooks on my desk, but I think of Zaina, her smile, and the way she called me ‘cute’ last time we met."

    a @talk "I’ll be fine."

    an "I pass by my desk for my closet instead, intent on living up to Zaina’s compliment. At least I hope it was a compliment. You never quite know with Zaina. She can make an insult out of anything."
    an "I clutch a shirt in my palm, though I’m careful not to wrinkle it. I can’t believe I actually have a date tomorrow!"


label zainaroute_scene_2:
    ## Scene Two

    ##outside alex’s apartment
    scene alex_apartment with fade
    show alex with dissolve

    an "Zaina had said to be ready by seven, but I’ve been ready since six."
    an "Nervous? Who’s nervous?"
    an "Not me."
    an "I stare at my phone, open to a tab of puppy pictures, hoping the cuteness would settle the butterflies in my stomach."
    an "It works for a bit, until I come across a husky with Zaina’s likeness."
    an shock "The picture psyches me out. Does it really look like her or am I just seeing Zaina everywhere? Am I actually insane?"
    an @sweat "I frantically exit the tab to my texts. Do I still have enough time to back out? Should I tell her the truth or make up some excuse? Would an emoji be rude in this situation?"

    ##engine (bike) sound effect
    show alex at rightt with move
    show zaina at leftt with easeinleft

    an "The sound of an engine revving snaps me out of my panic and I look up, my mouth going dry at the sight of Zaina on a motorcycle."

    menu:

        "Nice car.": 
            a smile sweat "Nice... car."
            ##zaina smirk
            ##exchange is teasing on both sides
            z unsure talk "Did I say I was gonna pick you up in a car?"
            a talk "Well... no."
            a -sweat "But if you were going for the cool factor, couldn’t you have gone for a sports car instead?"
            an "It’s almost much safer."
            z -unsure "I’ll keep that in mind in my next life when I’m richer."
            z "You’ll be there, most definitely missing my bike."
            an -smile "I protest playfully, but it does funny things to my stomach knowing that she’s imagined another life, with me still in it."

        "Nope.":
            a talk "There’s no way I’m getting on that."
            z unsure neutral "Fine by me. You can walk to the restaurant."
            an "She looks me up and down."
            z -neutral "You’ll ruin your cute outfit with sweat stains, though."
            an "I sigh, though secretly I’m quite pleased she noticed the effort I put into dressing for our date."
            a "Fine."

        "That’s hot.":
            ##zaina smirk
            z "What was that?"
            ##alex blush
            an blush "I freeze. I hadn’t meant to say that out loud."
            a talk "Nothing! I said nothing!"
            z unsure "No, I’m pretty sure I heard a whole lot of something."

            an -talk sweat "Zaina leans as close to me as she can while on her motorcycle. Her grin turns predatory."
            z "Me or the bike?"
            a shock blush "...What?"
            z "Did you mean me or the bike when you said that?"
            an -talk "Zaina was somehow kind enough to not repeat what I had said."
            z up "I can wait all day, you know."
            an "But not kind enough to let it go."
            an "I force the words out of my mouth, as quickly as possible."
            ##alex is pretty much mumbling here, maybe make the text a little smaller at this part?
            a "{mumble}Both... I meant both.{/mumble}"
            an -shock "My eyes stay stubbornly fixed to the ground for some time, but at Zaina’s chuckle, I peek at her hesitantly."
            z talk "You’re cute."
            an shock "She pinches my nose and though I protest, her comment warms me down to my toes."
            an smile -sweat "Alright, maybe all that embarrassment was worth it."
            ##endchoice 

    z up smile "Anyway, here."
    an "She tosses me a helmet and gestures behind her."
    z talk "Hop on."
    an "I put on the helmet and scramble behind her, looping my arms around her waist."
    z "You’ll wanna hold on tighter than that." 
    an sweat "Oh propriety be damned. I hug her as tight as I can without squishing her ribs."
    an "I mutter against her shoulder."
    a shock -sweat "This was all a ploy for me to hug you, isn’t it? You actually have a perfectly working car back at your place." 
    an "I feel Zaina’s laugh, rather than see it."
    z -talk sweat "Damn, you caught me."
    an "I laugh too and the nerves dissipate."
    z @talk "Ready?"
    an "I nod, before realizing she can’t see me. Oops."
    a @talk "Yes."
    an "Zaina sets off for the restaurant and I’m suddenly very glad for her warning. I hold on even tighter." 
    an "Yet even as the wind whips past, I feel only the warmth of Zaina’s back. It soothes me, comforts me, and when I smile at the view through my helmet, it’s without any fear."


label zainaroute_scene_3:

    ##scene three
    scene bg cafe with fade

    an "The restaurant Zaina chose is a hole in the wall and family-owned, making our date for the evening a very private affair."
    an "It’s cozy. I like it." 

    show alex at rightt
    show zaina at leftt
    with dissolve

    a @talk "How’d you find this place?"

    an "The waiter knew Zaina by name, so I assume she’s a regular." 

    z talk "It was after an urbex trip with the guys."

    z "We split ways and I was hungry. This place was the only thing open at 3 AM. That’s about it."

    a @talk "Have you ever taken Finn and Paxton here?"

    z "Nope."

    an "That’s surprising. I feel like they’re always together."

    an "Though I guess I’ve only seen them in the company of each other. This is the first time I’ve hung out with one of them just one-on-one."

    a @talk "So does that mean you only take girls here?"

    ##a playful smile from alex here

    an "I couldn’t resist."

    ##zaina smirk

    z smile "Wouldn’t you like to know?"

    an "I give her my best puppy dog eyes, but the woman is made of steel apparently."

    an "She props her chin up with one hand and swirls pasta onto her fork with the other."

    z @talk "Is that it? I think you can get cuter than that."

    an "The next few minutes, I try to muster up puppy dog eyes up to Zaina’s standards and fail. Even after using the puppy pictures I browsed through before our date for reference."

    a talk "Do you actually have no heart?"

    z frowntalk "Nah, I’ve just had a lot of practice."

    a "Paxton?"

    z talk "Paxton."

    an -talk "We return to our meals, before it gets cold. It would be a shame not to, after all I’m pretty sure Zaina took me here to share one of her favorite spots with me."

    an "Tasting the food, I can honestly say that I see why she’s a regular."

    an "Once we’ve gotten through a portion of our dishes, Zaina slides me her phone. I take it and glance down to see a photo of the most recent site we went to. She motions for me to continue swiping."

    z "I exported the photos from my camera. Those are the ones not up on Insta yet." 

    z smile "Pick your favorites and we’ll post ‘em up later."

    an "Zaina’s eye for detail continues to amaze me. The shots look amazing. Even someone like me, who doesn’t know much about photography, can tell she has a talent for it."

    an "I’m honestly surprised she isn’t already going into photography. She seems to like it well enough to take the pictures for their Instagram."

    z "I don’t do well in classroom settings."

    an @shock "Huh? Did I say that out loud?"

    z talk "Majoring in it would take the fun out of it and I don’t want to {i}hate{/i} photography."

    z "Things are fine as they are."

    a talk "Do you know what you do want to do?"

    z neutral "Nope."

    an neutral "She crosses her arms, not unhappy with the current subject of our conversation, but clearly not happy either."

    an "I figure she gets that question a lot."

    z "My dad’s this big shot marketer and my mom’s a housewife. Like {i}hell{/i} am I doing either."

    a @talk -neutral "I don’t know... I think you’d make a pretty good housewife."

    an "She cracks a grin and so do I, glad that at least she’s not taking this too seriously. This was never meant to be an interrogation."

    z talk "I guess cleaning up after you wouldn’t be the worst thing in the world."

    ##alex blush

    an blush "She’s only saying that to tease me. She must be."

    z "Anyway, nothing else interested me either."

    z smile "So here I am."

    z talk "What about you? Why’d you go into nursing?"

    an "It probably shouldn’t be my answer to such a question, but I do it anyway. I shrug."

    a @talk "I don’t know. Memorization comes easy to me and I like science. Nursing just seemed to be the natural step to take."

    ##serious zaina

    z down neutral "Was it really? Or was it ‘the natural step to take’ because your parents pressured you into picking nursing?"

    an shock "I open my mouth, but no words come out. I’ve never thought about it that way before."

    ##choice
    menu:
        "I don’t know.":
            a talk "I don’t know."
            a "I know it’s stupid, but I honestly don’t."
            an neutral "My distress must show on my face because Zaina reaches over and places her hand on top of mine, squeezing."
            an smile "I lose myself in the sensation and focus only on the feeling of her hand over mine. It’s warm. Comforting."
            z talk "It’s fine to not know. I mean look at me."
            an -talk "I do look at her. She’s grinning, but it’s softer somehow. More reassuring."
            an "I squeeze her hand back."
            ##end choice

        "I really do like nursing.":
            a @talk "Maybe they did, maybe they didn’t. I still like what I’m doing right now."
            an "Zaina doesn’t look the least bit convinced, but it doesn’t matter. I know I’m happy where I stand right now."
            a frowntalk "Should you really be dissuading me from nursing? You’re going to get awfully sick one day and then you’ll have no one to take care of you."
            z "A personal nurse does sound nice... {i}okay{/i}, I guess you can stay in your major. Will you wear a nurse’s outfit?"
            a smile "I’ll be wearing scrubs when I take care of you."
            an "Zaina laughs."
            ##end choice

        "I guess they did...":
            an "It doesn’t sit well in my stomach."
            an "My parents have dictated so much of my life already. How many classes I take, how much I should study... but it makes sense. There was always that feeling of guilt whenever I texted them back. It makes sense I was guilted into this too."
            a @talk "I might’ve been a little pressured..." 
            an "That was the understatement of the century."
            z talk "I thought so. My parents tried to do the same with me."
            an "Someone pressuring Zaina? I can’t imagine it."
            a talk "But you’re so—"
            z @neutral "Yeah. It’s why me and my parents don’t talk that much anymore."
            z "You don’t have to do the same with your parents, but maybe don’t let them kick you around as much."
            an -talk @neutral "That’s easier said than done..."
            an @shock "It must’ve been written on my face because Zaina reaches over and pokes me in the forehead."
            z smile "Hey, how about this? If you ever decide to stick it to ‘em, I can come with you to offer support. How’s that sound?"
            a @talk "...Really?"
            z @talk "Sure, screw parents."
            an smile "Something about the way she said that makes me laugh. I feel much lighter for the rest of the meal."
            ##end choice

    an smile up "She takes a sip of her soda and regards me with a look I’m unused to from her. Zaina looks... thoughtful? Curious? I can’t quite tell."

    z @talk "When was the last time you took a class outside of your major?"

    an neutral "I pause. I haven’t."

    an "My silence seems to tell Zaina all she needs to know because she continues."

    z talk "You should try other classes. See what you like, what you don’t like."

    z "If all you’ve taken are nursing courses, you’re just screwing yourself over." 

    an "My parents don’t seem to think so. They’d actually prefer it that way."
        
    an "But that’s the point, isn’t it? Not letting my parents tell me what to do."

    z frowntalk -neutral "I’m not trying to force you into finding something else you’re in love with, here. Just think about taking a class for fun."

    an shock "For... fun?"

    z talk "Maybe we can even take a class together."

    an "A class... with Zaina?"

    z frowntalk "The class will probably be trash, but at least we’ll get to shit talk it together." 

    an smile "Laughter blooms from my chest in spite of my best effort to swallow it. It’s unreal. The thought of taking a class with Zaina actually sounds, to borrow her words, {i}fun{/i}."

    an "Spending more time with Zaina is undoubtedly something I’m interested in and for once, the thought of taking another class isn’t stressful."

    show zaina smile
    a talk "Sure, that sounds good."

    a "Great, actually."

    an -talk "Zaina looks like the cat that got the cream. I should feel wary, but it’s excitement that bubbles in my stomach, not fear."

    z @talk "I’ll be the one picking the class, though."

    an "I make a big show of groaning, as though I don’t trust her. Zaina feeds off of it as her grin, somehow, gets even wider."

    a @talk "I just signed my death warrant, didn’t I?"

    z @talk "You sure did."

    an "Could the next semester come any faster?"



