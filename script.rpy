# The script of the game goes in this file.

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
define question = Character("???", color="#ffffff")
define Police = Character("POLICE", color="#ffffff")
define Phone = Character("PHONE", color="#ffffff")
define Bio = Character(" ", color="#ffffff")
define c1 = Character("CLASSMATE 1", color="#ffffff")
define c2 = Character("CLASSMATE 2", color="#ffffff")

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

default finn_stat = 0
default zaina_stat = 0
default paxton_stat = 0

label start:    ## start of the game!

    stop music fadeout 1

    scene bg alex_room with fadee

    play sound "phonevibrate.mp3"

    a "Nn..."


    an "Phone... phone... where'd I stick it..."


    an "I sit up, rubbing the sleep from my eyes. It's too early for this."


    a "Where did you go... aha!"


    an "Grabbing my phone from the floor, I pull it off the charger and punch in my passcode. I don't even have to unlock it to know what these texts are, no one texts me in the first place, but even if they did it would never be {i}this{/i} early."

    play sound "phonevibrate.mp3"

    an "Another text pops up across the top of my screen as my phone vibrates in my hand, and I tap it, opening streams of texts from both of my parents."

    an "It's the usual things that I don't want to answer. What are my grades, how many classes am I taking... There's only one right answer, and it isn't the truth."

    an "Though even the right answer isn't the answer they want. Not that I've ever managed to figure out what exactly that is."

    an "But I can't keep dodging their questions like I have been... I mean, I can, but it's going to get me in trouble."

    an "... which feels a little pathetic."

    an "I'm an adult now, aren't I? Or I'm supposed to be, though I don't feel like one."

    an "But it's not like I've ever been treated like one either."

    an "I send back a quick ‘good morning,' hoping that gets them to stop for just a minute so I can backread and make sure I'm not missing anything that they'll complain about later."

    an "I don't see anything new, so I start tapping out a reply to them. Twelve measly credit hours, and no, I don't know my grades. I won't know them until midterms and finals."

    an "I'm not sure if it's a blessing or a curse that my professors won't update grades on a more frequent basis. On one hand, I'm not obsessing from week to week. On the other, I have no idea from week to week."

    an "I add in a final note that I'm going to be in classes all day, and that I love them, before muting my text notifications."

    an "I put my phone face down on the bed for the moment, getting up for the day. It's before my alarm would've gone off, but I might as well get out of bed."

    an "I can get some more studying in, maybe."

    an "Something so I don't feel like twelve hours of classes isn't enough."

    scene bg classroom with fadee

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    show alex up frown backpack at center with dissolve

    c1 "Oh, oh! They posted a new story to their Instagram!"

    an "There are way, way too many terms for all the things in the human body..."

    an "I'm pretty good at memorization, but this is too much. I can feel my eyes glazing over... "

    c2 "Where is this?"

    c1 "Looks like an old house, maybe?"

    c2 "Yeah, but {i}where{/i}?"

    an unsure "Why do they have to talk about this now? It's so distracting..."

    an "I guess it's my fault for finding it interesting enough to {i}be{/i} distracted."

    c1 "Hmm... well, it's not on campus..."

    c2 "No shit, Sherlock. If we had any abandoned churches on campus, people would've had a drunken party in it by now."

    an "It's not something I could do—exploring abandoned buildings like these people do. If my parents didn't kill me, I think I would probably get myself hurt, and {i}then{/i} my parents would kill me."

    an "So the same end result. It's reckless and stupid."

    c1 "Do you want to see if we can find it after class?"

    c2 "I feel like it's bad to talk about that right this minute..."

    an "I don't have time, anyway. These muscle terms aren't gonna memorize themselves."

    an "Class starts in about ten minutes... I'll focus on this until then."

    an "..."

    an "..."

    an "..."

    an "The stool squeaks across the floor, snapping me out of my concentration."


    ##Finn appears! Should have a relaxed smile.
    show alex unsure frown backpack at closeright:
        yalign -0.4                 
    show finn up frown at closeleft
    with dissolve

    show finn talk

    question "Hey."

    show finn smile

    a talk "You're early."

    an smile "Usually Finn slides in right before the professor shuts the door."

    f frowntalk "Oh, I haven't been to sleep yet."

    show finn frown

    an "I look at my watch."

    a frowntalk "...how long have you been awake?"

    show alex frown

    f frowntalk "Uhh, about twenty-two hours now, maybe? I'll sleep after this. I didn't wanna miss."

    show finn frown

    an smile "I don't really know what to do with this information... is he telling me he usually oversleeps, and that's why he's almost late to class? Why was he up all night?"

    hide finn
    hide alex
    with dissolve

    an "I don't have a chance to inquire before the professor shows up, though, so I decide I'll take notes for him—he's pretty nice. I like him."

    an "Usually, having to have a partner or do any kind of group work is my least favorite thing. {i}Usually{/i}, my partners never do their part, or they do it so badly I end up redoing it anyway."

    an "Finn isn't bad, though. He keeps up on the material for the most part, and he's easy to get along with."

    an "He's only a little strange... I can't imagine having a wardrobe full of nothing but black clothes, but I've never seen him wear a {i}color{/i}."

    an "Honestly, I wouldn't have paid him much attention if we hadn't ended up accidental lab partners, but I can't say I have any complaints."

    an "I steal a glance at him as the professor begins his lecture and Finn looks like he's already fading."

    an "I think he might've been better off skipping class."

    an "Not that I've never come to class on too little sleep—I don't think I have the capacity to skip class."

    an "I hate that my stomach drops at the thought alone..."

    an "I hate the thought of looking at my phone later."

    an "..."

    an "..."

    an "..."

    an "Like I expected, Finn fell asleep a few minutes into class, and is still asleep, actually."

    an "I'm not sure if it's that the professor didn't notice or that he didn't care... or maybe he did, and Finn's going to get docked for it later."

    an "All the more reason I'm glad I took some extra-thorough notes."

    an "Though..."

    ##if we have it as an option, a cut in of a piece of notebook paper and some VERY sloppy handwriting/scribbles would be cute!

    an "This isn't quite legible yet."

    an "I give him a careful shake, hoping that isn't rude. I feel like it would be worse to not wake him up, though—he said he was sleeping after this, but he should do that in a bed."

    show alex unsure frown backpack at closeright:
        yalign -0.4                 
    show finn up frown at closeleft
    with dissolve

    f "Mm...?"

    an "He vaguely stirs, and I find myself thinking that he's kinda cute... long eyelashes, and what looks like some smudged eyeliner."

    an "I don't think it occurred to me before college that guys would wear makeup willingly, but he does, and it looks nice."

    an "... I shouldn't be staring."

    an "I give him another shake and his eyes finally open. He sits up, blinking blearily and rubbing his face."

    f frowntalk "That wasn't supposed to happen. Ugh."

    show finn frown

    a talk "Well, I took notes for you, so it could be worse."

    a "Though I'll probably need to rewrite them for you."

    an smile "I show him my notes, and he looks over them, blinking the sleep from his eyes before he starts laughing."

    f talk "I really appreciate the thought, but I think you're right—is this even English?"

    show finn smile

    a talk "It should be—it's the only language I know."

    show alex smile

    f talk "I'm not sure—maybe you unlocked something in your subconscious."

    show finn smile

    an "I can't help but laugh a little bit at that, tucking my notebook away."

    a talk "That's absurd."

    a "I can type these up and email them to you, if that works."

    show alex smile

    f talk "It does."

    f "I appreciate it."

    show finn smile

    a talk "It's not a problem! I was going to type them anyway."

    a "Anyway, I have another class to get to."

    a "See you!"

    hide finn
    hide alex
    with dissolve

    an "Checking my watch, I probably shouldn't have dawdled."

    an "But more than that, I think I shouldn't have scheduled my classes quite so close together..."

    stop music fadeout 3

    scene bg alex_room with fade

    play sound "phonevibrate.mp3"

    an "By the time I get back to my apartment, my phone has too many texts again. I really don't want to read them."

    an "But I do, because what else am I gonna do? Ignore them? That'll go over well, I'm sure."

    an "Reading over them properly, I feel pretty bad..."

    an "I should've kept up my course load and powered through it."

    an "Though it's bold of them to think that I'm doing anything extracurricular or romantic."

    an "The last time I had a boyfriend, I think I was fourteen."

    an "I really don't like it when they're mad at me, though..."

    an "I take a breath and then type out an apology. I'll make it up to them next term. They're paying for my classes, so it's the least I can do..."

    an "I don't want to disappoint them."

    scene bg lab with fade

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    an "Tonight, Finn looks much more awake than he did in class before."

    an "Which is good, because we need to get this lab report done, and I could do it myself, but I don't particularly... want to..."

    an "Aside from that, this is one of my few chances to socialize at all! I like Finn well enough, and I'd like to get to know him better."

    an "He's pretty reserved, though. Hmm... I don't think I've ever heard him mention a hobby or anything that he's into."

    an "We really only talk about stuff for class, which doesn't say much about anyone."

    an "I feel like I've forgotten how to talk to people, though... how {i}do{/i} you talk to someone about something that isn't schoolwork? Uhm..."

    show alex unsure frown backpack at closeright:
        yalign -0.4                 
    show finn up frown at closeleft
    with dissolve

    a talk "Do you have any plans after this?"

    an smile "That's a start, I guess."

    an "Finn stops what he's doing for a moment and shrugs."

    f talk "Nothing in particular. Do you? I thought all you did was study."

    show finn smile

    a talk "Not all the time!"

    an smile "Just most of the time..."

    an "Part of me feels a little offended that he's making fun of me, but he's smiling, and I think maybe he doesn't mean it in a mean way."

    an "Besides, it's not like he's wrong."

    an "Can't get mad at the truth."

    a talk "I do other things..."
    
    show alex smile

    f talk "Like?"

    show finn frown

    a talk "I like to try my hand at music composition sometimes, on the computer... reading, too."

    a "Walks are nice if the weather's good—I like walking around the part of town with all the old houses. They're so much more interesting than anything built nowadays—they have a lot more personality to them."

    a "What about you?"

    an smile "He's quiet for a long moment, finishing up the question we were working on before answering."

    f talk "I do a lot of outdoor stuff, I guess. I used to do rock wall climbing."

    show finn frown

    an "... this is not what I expected from someone that looks like..."

## if we can just get a focus or a pan on Finn or something to emphasize her looking at him that would be great!

    an unsure "This..."

    f talk "Is there a reason you're staring?"

    show finn frown

    a talk "Oh! Oh, I just... I didn't take you as the type to do a lot of physical stuff."

    show alex smile

    f frowntalk "What did you expect? That I haunted campus, looking for my next victim?"

    show finn frown

    a shock "No!"

    an smile "... not quite that dramatic, but that's closer to what I was imagining..."

    a talk "I don't know, maybe you like, stayed in more."

    an up smile "He laughs and shakes his head."

    f talk "Nah, I like being outside."

    show finn smile

    a talk "During the day?"

    show alex smile

    f frowntalk "Sure, but not without SPF-100 sunscreen."

    show finn frown

    a talk "Oh."


    an smile "That explains how he can be an outdoorsy person and still be this pale."


    f talk "Do you know how to answer the next question?"

    show finn frown

    a talk "Um... let's see..."

    an smile "He doesn't seem interested in telling me anything else, so we focus on getting the lab report done."


    an "It's not the most exciting thing in the world, but it's nice."


    an "... there's something sad about how much stimulation I get out of doing this lab report with him."

    stop music fadeout 5

    scene bg alex_room with fade

    play sound "phonevibrate.mp3"

    an "It takes me a moment to realize what I'm hearing beyond the music from my headphones, my studying focus broken now."

    an "The screen on my phone says it's Mom... I wonder what she wants."

    an "... it's the same as always."

    an "Any time they ask me what I'm doing, it's never because they want to know what I'm up to."

    an "I lean back in my chair and tap out a reply to them, letting them know I'm studying."

    an "Another text comes through and this one is a little different from usual..."

    an "What am I doing on the weekend... I don't know yet."

    an "Is she worried about me?"

    an "Both my parents are always worried about me, technically, but... not in a way that feels particularly loving."

    an "I'll tell her I don't have plans... see where that gets me."

    an "The typing notification appears on my phone screen after I send it—"

    a "‘I hope you blocked in time for studying.'"

    a "Really?"


    an "My hand hurts—"


    an "Shaking my head, I stop squeezing my phone in a death grip and turn it off."


    an "I don't ever do enough, do I?"


    an "If it's not studying, then there's no point to anything that I do."


    an "They haven't asked me about friends since I told them I didn't have any, months ago."


    an "I don't know what to do."


    an "I know they love me, but what does that even mean?"


    an "Do they care about {i}me{/i}, or do they just care about my success?"


    an "I can't tell."


    an "I've never been able to."


    an "Turning off my phone, I drop it on the floor."

    an "They're never going to be happy with me."

    scene bg classroom with fade

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    an "Shocking no one, least of all myself, I spent my weekend sleeping and studying."

    an "Not that I have anyone {i}to{/i} shock."

    an "But it's fine! I'm going to do great on this test."

    an "And then... study some more?"

    an "..."

    an "It never ends..."

    c1 "Look! {i}Look!{/i}"

    show alex up frown backpack at center with dissolve

    an "In front of me, a couple of my classmates are excited about something."

    c2 "How did they get so high up?!"

    c1 "I don't know! I think this is the old cathedral... you know, the one you pass on the highway if you're coming in from the north side of campus?"

    c2 "No, that can't be it. Roof's the wrong color."

    c1 "Hrm..."

    c2 "I wonder who runs it... they'd have to be pretty fearless to get up on the roof, right?"

    c1 "Or stupid."

    c2 "Both?"

    c1 "Both."

    c2 "Probably someone on the football team or something like that... I watch these videos on YouTube, and it takes a ton of work to get up to some of these places."

    c1 "May—"

    a talk "Um, excuse me?"

    show alex smile

    c1 "Huh? What is it?"

    an "This is the most impulsive thing I've done in who knows how long."


    an "I can feel myself losing my resolve already... but no. I won't."


    a talk "What are, uh, you talking about exactly? With the old cathedral?"

    show alex smile

    c2 "Oh, there's some urbex group that goes to school here. They post a lot of photos and videos to their Instagram account."

    c1 "Yeah, see—like this."

    an frown "They show me a photo of a steeply inclined roof with dark shingles, barely visible in the darkness."

    an "The sky is a sea of stars..."

    an "Even just looking at a picture of it, I feel breathless."

    c1 "See? You get it! It's cool, right? Super cool! Look at these..."

    an "They show me more of the photos, some of them in buildings that really don't look safe, one that has a vague, partial shape of a person in it with a mask of some sort on."

    an "The caption on that one says ‘What's with the spooky mask? For those of you watching at home, we're in an old place with a potential asbestos problem, and I'd like to escape here with some cool pictures, not lung cancer, thanks."

    an "So this place was built... in the 1900s, probably? It was used in construction for a long time..."

    an "Each photo they show me feels like a frozen piece of time. Places with old medical files, places where nature has taken over again."

    an "It's amazing."


    a talk "Yeah, wow. I'm definitely going to follow them..."


    an smile "The professor walks in then, so I quickly thank my classmates and go back to my desk, quickly searching up the account."

    an "I hit the follow button without thinking too hard about it, before reading their bio."


    Bio "{i}Feeling adventurous? Come find us.{/i}"

    an "I feel jittery—excited?"

    an "My nerves are flooded with excited energy."

    an "For the first time, I barely focus on my notes, and I barely hear the homework assigned."

    an "I'm going to find these places."

    stop music fadeout 3

    scene bg alex_room with fade

    an "I was good—I did some studying over the weekend. A little."
    an "Not much, though."
    an "Usually, that would stress me out."
    an "But right now? I can't bring myself to care."
    an "I spent most of my time digging through the Instagram account of these urbex people, going all the way back to the first post to see if I could figure out where these pictures are from."
    an "There's factories, an abandoned mall."
    an "An old theme park, a lot of old houses."
    an "Abandoned hospitals..."
    an "Some of the hospitals have old patient files, which I can't help but wonder: is that a HIPAA violation?"
    an "I can't stop thinking about this."
    an "I can't think of a single time in my life that I've been this fixated on something."

    show alex up frown at closeright:
        yalign -0.4             
    show finn up frown at closeleft
    with dissolve

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    f frowntalk "Alex? Are you there?"

    show finn frown

    an "I jump, startled back to my senses. Studying. I'm studying with Finn. Or I'm supposed to be, anyway..."

    a talk "S-Sorry! I spaced out."

    show alex smile

    f talk "I think you went to another planet, maybe."

    show finn smile

    a talk "Hahaha..."


    an smile "Crap. That's embarrassing."
    an "I pull out my phone and pull up the account—I feel the need to justify myself. Maybe he'll understand?"

    an "How can you see all this stuff and not be interested?"

    a talk "I was thinking about this—I have been all weekend."
    show finn down frown
    an smile "I show him the account, and he immediately stiffens."

    f frowntalk "That kind of thing seems pretty dangerous."

    a unsure talk "Oh?"

    show alex frown

    f frowntalk "I haven't done it—some of the guys at the gym where I used to do wall climbing did. It's fine to look, but... it's dangerous."
    f "You shouldn't try to do this kind of thing."

    show finn frown

    an frown "Somehow, I feel like a deflated balloon."
    an "But only for a minute."

    a talk "I'm not going to do anything stupid. I like having a mystery to solve, so I want to find out what at least one of these places {i}is{/i} exactly."

    show alex smile

    f frowntalk "You'll get yourself killed."

    show finn frown

    a talk "I will not—why do you care, anyway?"

    show alex smile

    f frowntalk "I don't know, logic tells me I should stop someone from running into abandoned buildings? Seems like a questionable life choice."
    f frowntalk "You'd be stupid to dig into it."

    show finn frown

    an "I feel so tense—so agitated."
    an "I can take care of myself."
    an "I'm not a child, and I'm not stupid."
    an "But... we're here to study. And I have been slacking on that."
    an "Taking a deep breath, I force myself to calm down."

    a talk "Sorry for bringing it up. We should get back to this, right?"

    show alex smile

    f frowntalk "Uh... yeah."

    show finn frown

    an "The rest of the evening feels stiff—off and tense—but we get through it."
    an "Back home, there's a nagging thought in the back of my head that I should study some more before I go to bed."
    an "But I don't want to do that."
    an "I pull up the Instagram account, looking over the photos again."
    an "This one set they did is a hospital—I think, anyway. It looks like it's only one floor, though... usually, they explore the whole building, so this must be the only level to this place..."
    an "Hrrm..."
    an "I grab my laptop and open up my browser. There can't be that many abandoned hospitals, right?"
    an "In the end, there's a couple of small psych wards nearish to here that were closed but not torn down."
    an "I'm feeling excited again—I want to go see these places..."

    stop music fadeout 3

    scene black with fade

    an "Ugh."

    an "Sitting in my car, the first location was a bust. There was a gate that was open, but the windows and the doors were all locked."

    an "This is risky, but I'm not gonna be {i}more{/i} reckless by trying to break and enter."

    an "This is illegal as is, but that would be {i}really{/i} illegal, and I really don't want to get arrested."

    an "My parents would flip, but I might also get kicked out of school."

    an "If I get kicked out of school, then I have to go home."

    an "..."

    an "I'm not getting arrested."

    an "Because I'm not going to do anything stupid."

    an "..."

    an "Anything... stupid...er..."

    an "..."

    an "I'll be fine."

    an "I punch in the next address on my phone. First location's a bust, but I'm not giving up!"

    an "Not yet, anyway."

    an "The drive to the next site is pretty painless, boring."

    Phone "Your destination is on the left."

    an "I look to my left as I drive past, noticing the ‘NO TRESPASSING' signs first."

    an "Maybe this {i}is{/i} a bad idea..."

    an "I change lanes, ready to get back on the highway and turn around. I feel kind of sad about it, though."

    an "I see a supermarket parking lot and flip on my turn signal, turning way too hard into the lot and earning myself an annoyed honk for braking out of nowhere."

    an "But really, whose fault is it that they were tailgating?"

    an "I pull into a parking spot and turn off my car. Pulling up the map on my phone, it's only about a ten minute walk back to the site."

    an "I came all the way out here; I'm going to at least {i}look{/i}."

    an "I get out, grab my backpack and lock up my car."

    an "... and then I make double sure I locked it. It beeps at me, and I start my trek."

    scene bg outside_campus night with fade

    play sound "crickets.mp3"

    an "..."

    an "..."

    an "..."

    an "Approaching the site, I notice the barbed wire wrapped around the top of this six foot tall fence."

    an "Maybe I won't be able to get in?"

    an "Circling around, there's no gate I can get through, but there {i}is{/i} a patch in the top of the fence where the wire is broken."

    an "Looking up at it, I try to remember the last time I climbed a fence. Maybe when I was a little kid?"

    an "But I never even really did anything adventurous then, either."

    an "I grab the chainlink, stick my foot in, and carefully pull myself up and on top of the fence."

    an "Take it slow... don't get scratched..."

    an "If I have to get a tetanus shot and it runs through my parent's insurance, they're going to know I was up to {i}something.{/i}"

    an "Very carefully, I get my feet under me and hop down."

    a "Ouch!"

    an "Note to self, don't do that again. Ow."

    an "I wait for the pain in my feet to dissipate and then carefully stand up, walking over to the building."

    stop sound fadeout 1

    scene bg hospital with fade

    play music "Be_piano12.ogg" fadein 1
    queue music "Be_piano12.ogg"

    ##I think the music should be really quiet here?
    an "I enter through the door at the back, wincing as it creaks."

    an "I step inside, letting the door close behind me. The floors are covered in dust and dirt, and I've never been somewhere so quiet."

    an "Even if I'm the only one here, it feels criminal to let my footsteps make noise."

    an "I approach the front of the building, spotting old, water-damaged posters on the wall for group activities."

    an "On the front desk, there's files, old pens. A keyboard was left behind."

    an "You could almost believe this was ready for another day of work, another day of treating patients..."

    an "I take some pictures as I walk, careful not to disturb anything."

    an "I feel like time stopped here long ago, and I don't belong as someone from the present."

    an "I walk down the next hallway, peeking into the rooms. There's still beds in them, some made, some stripped. Stubby wooden pencils lay on top of ancient pads of paper."

    an "I wonder, when I become a nurse, if I'll ever end up working somewhere like this."

    an "What I read online said this was a psych ward for adults."

    an "But so much of it feels childproofed."

    an "I understand why, but it's strange nonetheless."

    an "... I don't know if I {i}could{/i} work somewhere like this, actually."

    an "No one goes to a hospital because they want to, but {i}especially{/i} no one comes to a place like this because they want t—"

    stop music fadeout 1

    question "Hey! Is someone here? This is the police!"

    an "Crap."

    an "Think think think—the rooms—the doors don't have locks..."

    an "I quickly slip inside the closest room and carefully close the door as quietly as possible."

    an "Pulling off my backpack, I crawl under the bed and pull my backpack in, hugging it close to my body."

    an "I squeeze my eyes shut, heart thudding in my chest."

    an "I can't get caught I can't get caught I can't get caught—"

    play sound "footsteps.mp3"
    an "Footsteps..."

    Police "Hello? Is anyone here?"

    an "I feel like all the air has left my lungs."

    an "I've never been this scared in my life..."

    an "But I focus on listening as the footsteps continue and then fade into the distance."

    an "They get louder again, passing the room I'm in, until I hear the sound of the door at the front open and close."

    an "It's quiet again."

    an "I crawl out from under the bed, standing and putting my backpack back on. I dust myself off, and this time, I'm much more careful about getting back out of here."

    scene bg outside_campus night with fade

    play sound "crickets.mp3"

    an "Back in my car, I take a minute to just sit there and catch my breath before pulling out my phone and opening a DM to the account."

    an "There's some texts from my parents waiting, but I'm not going to try to reply to those right now."

    an "Selecting the pictures, I send them all before locking my phone, tossing it on the passenger's seat."

    an "It's easy enough to get back home from here."

    ## Scene 9
    ##classroom/lab bg/whatever

    scene bg lab
    with fadee

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    show alex unsure smile backpack at closeright:
        yalign -0.4
    with dissolve

    an "For the first time ever, Finn is there before me."

    an up "I wave to him, and then stop."

    ##Finn annoyed/mad
    show finn down frown at closeleft
    with dissolve

    an unsure frown "I don't think I've ever seen him look like this either..."

    an "As I take my seat, he doesn't acknowledge me. Instead he's just messing with his phone."

    an "I wonder what's eating him..."

    hide alex
    hide finn
    with dissolve

    an "Class is hard to focus on, and it doesn't seem like Finn's focusing much either. I don't think he's looked away from his phone for more than a minute."

    an "..."

    an "..."

    an "..."

    an "Okay, putting away my notebook, my pen—"

    ##finn serious
    show alex neutral smile backpack at closeright:
        yalign -0.4
    show finn down frown at closeleft
    with dissolve

    stop music fadeout 3

    f unsure frowntalk "I need to talk to you."
    show finn frown

    ##Alex startled
    an up "What?"

    a unsure frowntalk "Um, okay?"

    an frown "He doesn't budge as the classroom empties out, and neither do I."

    an "This is... intimidating."

    f down frowntalk "What the hell were you doing?"
    show finn frown

    a down frowntalk sweat "Excuse me?"
    show alex frown

    f frowntalk "I saw the photos. What were you {i}doing{/i}?"
    show finn frown

    an up "Photos—"

    an "Oh my god."

    an "He's the one that runs the account?"

    a unsure shock "It's your account?! Is {i}this{/i} what you meant about doing outdoor stuff?!"
    show alex frown

    f unsure frowntalk "Look, yes, but that doesn't matter. Did you go by yourself? Have you done this before?"
    show finn frown

    a down frowntalk "I did—"
    show alex frown

    f down frowntalk "Are you stupid?"
    show finn frown

    a up frowntalk -sweat "I am not. I was {i}fine{/i}."
    show alex frown

    f unsure frowntalk "Do you realize how dangerous it is to mess around in abandoned buildings?"
    f frowntalk "You could've gotten yourself killed."
    show finn frown

    a unsure frowntalk "Well, {i}you're{/i} the one with the account that says 'come find us!'"

    an frown "That gets him to stop talking long enough for me to keep going."

    a up frowntalk "I didn't get hurt, because I'm {i}not{/i} stupid."

    a unsure frowntalk "I was careful, I didn't disturb anything, I didn't get hurt."

    an frown "We'll just leave out... the part about almost getting caught by the police."

    a down frowntalk "Do {i}you{/i} go by yourself?"

    an frown "If he's being a hypocrite..."

    f down frowntalk "Dammit—no, I don't."
    f unsure frowntalk "I go with a couple of friends."
    show finn frown

    a unsure frowntalk "Then if you're so concerned about what I'm doing—"

    an frown "I take a breath."

    a down talk "You should let me come with you."
    an smile "The way he's staring at me... I can't tell if he's mad, shocked, or just thinks I'm crazy..."

    an "Maybe I am."

    an "Maybe not having real conversations with anyone for months made me crazy."

    an "But after a moment, he sighs and rubs his face."

    f down frowntalk close "Fine. I'll ask if they're okay with it."
    f unsure side "I'd rather you come with us than go off by yourself again."
    show finn frown -side

    play music "happy.ogg" fadein 5
    queue music "happy.ogg"

    an up "Oh."

    an "I think I didn't expect him to agree to this."

    an "I don't even know what to say..."

    f up talk "I'll text you."
    show finn smile

    a unsure talk "Um—yeah, that's fine."
    show alex smile

    f unsure frowntalk "Cool."
    f down "Don't go off exploring anything else in the meantime."
    show finn smile

    a up talk "I-I won't."
    show alex smile

    hide alex
    hide finn
    with dissolve

    scene black
    with dissolve

    an "My heart is thundering in my chest."

    an "I didn't know I could be this kind of person."

## Scene 10
    ##Alex apartment bg

    scene bg alex_room
    with fadee

    an "I've been feeling weirdly anxious the past couple of days."

    an "I really, really didn't expect Finn to be involved with the account."

    an "I know I shouldn't judge a book by its cover, but..."

    an "Well, I did."

    an "Not that I know {i}what{/i} I expected from him, but it wasn't this."

    an "But he probably didn't expect this from me either."

    play sound "phonevibrate.mp3"
    "Bzz..." with vpunch

    an "I look at the notification on my screen, and for once, I don't feel stressed—I feel excited."

    an "It's not a number I have in my phone, but it says it's Finn."

    an "He's texted me a couple times before, but since it was just for study meetups, I never really bothered to add him to my contacts..."

    an "I open the message, excitement bubbling within me as I read over it."

    an "He wants to meet at a coffee shop today."

    an "Do I have time?"

    an "I close the textbook that's open on my desk."

    an "I have time."

    an "I text back that I can meet them and then add Finn's number to my phone."

    an "I wonder what his friends are like..."

    stop music fadeout 2

    ##Cafe bg
    scene bg cafe
    with fadee

    play music "Bm_Cafe04.ogg" fadein 2
    queue music "Bm_Cafe04.ogg"

    show alex up smile at closeright:
        yalign -0.4
    with dissolve

    an "I'm a little early, I think."

    an "This place is cute... and it smells nice."

    an "I walk up to the counter, looking over everything on the menu."

    an "Seems like mostly normal things that you can get at any coffee shop."

    an unsure "The raspberry mocha sounds nice though..."

    an up shock "And they have milk alternatives!"

    ##Paxton sprite! Friendly smile!
    show paxton up smile apron at closeleft
    with dissolve

    show paxton up talk
    question "Can I get something started for you?"
    show paxton smile

    a unsure talk "Oh, um, can I get the raspberry mocha with almond milk?"
    show alex smile

    an "He writes in a flurry across the cup."

    show paxton unsure talk
    question "Do you want whipped cream on that?"
    show paxton smile

    a down talk "No, thank you."
    show alex smile

    show paxton up talk
    question "You got it. Can I get a name?"
    show paxton smile

    a up talk "Alex."
    show alex smile

    ##surprised Paxton
    show paxton up frown
    an "He stops and blinks at me."

    show paxton unsure talk
    question "Are you here to meet Finn by any chance?"
    show paxton frown

    a down talk "I am..."
    an up smile "Is this one of his friends?"

    show paxton up talk
    question "Nice to meet you! I'm Paxton. I'm on the clock right now, but I'll be over to join you guys soon."
    show paxton smile

    p down talk "While I make your drink, you can go meet Zaina over there."
    show paxton smile

    an "He gestures to a pretty girl sitting at a table in the corner with her headphones on."

    a unsure talk "Okay—um, what do I owe you?"
    show alex smile

    p up talk "Don't worry about it! It's on the house."

    p unsure talk "I'll bring it over in a few minutes."
    show paxton smile

    a up talk "Oh! Thank you!"
    show alex smile

    hide paxton
    with dissolve

    an "I stuff the cash I had in my hand into the tip jar and walk over to the table he gestured to."

    an "The pretty girl—Zaina?—notices me and looks up."

    show zaina up frown at closeleft:
        xalign 0.15
        yalign -0.20
    with dissolve

    z unsure frowntalk "Can I help you?"
    show zaina frown

    ##Alex awkward/nervous/something
    an sweat "Er..."

    a unsure talk "I'm here to meet Finn? And, um, Paxton said I should just come over here..."
    show alex smile

    ##Zaina smile?
    z up talk "Oh! Hey. Alex, right? Is it short for something?"
    show zaina smile

    an "She softens immediately, pulling her headphones off and patting the seat next to her."

    a up talk -sweat "Oh, no, it's just Alex." 
    a unsure "My parents thought they were getting a boy... and they got me instead."
    a down "But they didn't like any of the feminine variations, so... it's just Alex."
    show alex smile

    z unsure talk "Huh. Cute."
    show zaina smile

    show alex up
    an blush "I can feel my cheeks get hot—usually, people just think it's weird."

    an unsure "She thinks it's cute? Is it cute?"

    z down talk "Anyway, Finn will show up eventually. He probably overslept. Or he got distracted doing his eyeliner. You know how that goes."
    show zaina smile

    an -blush up "The way Zaina just moves on with the conversation snaps me out of my embarrassment."

    an "I think about how the most I've ever done is sloppily apply a little with a pencil, so no, I don't know."

    an "But the day I saw him sleeping... it did look pretty good."

    a up talk "Oh, yeah!"

    a unsure talk "It's nice to meet you by the way."
    show alex smile

    z up talk "Likewise." 

    ##Zaina scowling/frowning
    show zaina up frown
    an "Her attention shifts to her phone and she scowls."

    z down frowntalk "Don't leave me on read when you're {i}late{/i}, asshole."
    show zaina up frown

    an "She rolls her eyes and puts her phone on the table."

    z unsure talk "So you went out to that old hospital by yourself?"
    show zaina smile

    a up talk "Yeah. I went to another one too but it was locked up."
    show alex smile

    a unsure talk "I don't know how to pick locks."
    show alex smile sweat

    z down frowntalk "I'm glad you don't. If you got caught, you could've gotten charged with breaking and entering on top of trespassing."

    z unsure "Can't play dumb like you didn't {i}know{/i} you were trespassing when you also {i}broke in{/i}, after all."
    show zaina frown

    a down frowntalk "O-Oh."
    a unsure "That makes sense..."
    show alex frown

    z down frowntalk "I think Finn knows how to pick locks, but like, seriously, don't do it."
    z unsure "Though..." 
    show zaina frown

    an "She's burning holes into her phone now..."

    z up talk "Sometimes I can't help but think it might be a useful skill to have..."

    z down frowntalk "For when your idiot friend is incapable of being on time for {i}anything.{/i}"
    show zaina frown

    an "...I have decided that I am never ever going to piss off Zaina."

    an "Ever."

    hide alex
    hide zaina
    with dissolve

    show finn up smile:
        xalign -0.05
        yalign 1.0
    show zaina up smile:
        xalign 0.9
        yalign -2.2
    show alex up smile:
        xalign 0.45
        yalign 2.3
    with dissolve

    f unsure talk "Hey."
    show finn smile

    an "I jump a bit as he takes the seat next to me, across from Zaina."

    an "Where did he come from?!"

    z unsure talk "So what's your excuse?"
    show zaina smile

    f down talk "I was too comfortable to get up."
    show finn smile

    ##Zaina staring
    z frown "..."

    ##Zaina glaring
    z down frown "..."

    z frowntalk "You're an ass sometimes, you know that?"
    show zaina frown

    f unsure talk "You never miss a chance to remind me." 
    show finn smile

    an "I would be worried, except Finn doesn't seem at all put off by Zaina's irritation."

    an "He might even enjoy needling her?"

    an "Zaina looks ready to say something else when Paxton sets down a mug in front of her."

    an "And a mug in front of me."

    show alex:
        xalign 0.35
    show zaina close:
        xalign 0.7
    show paxton up smile apron behind zaina:
        xalign 1.05
        yalign 1.0
    with easeinright

    p unsure talk "Sorry about the wait!"
    show paxton smile

    a unsure talk "It's fine! Thank you!"
    show alex smile

    an "Zaina doesn't say anything, but she's holding the mug up, close to her face, and she looks like she's in heaven..."

    hide paxton
    with easeoutright

    an "Paxton walks away again before returning a moment later with two more mugs."

    show paxton up smile apron behind zaina:
        xalign 1.05
        yalign 1.0
    with easeinright

    p down talk "I knew it was a good move not to go on break until you showed up."
    show paxton smile

    f down frowntalk "I wasn't {i}that{/i} late."
    f unsure talk side "Anyway—me being late isn't what the topic is."
    show finn smile -side

    z unsure frowntalk -close "Maybe it should be."
    show zaina frown

    f up talk "Nah, telling Alex about what we do is way more exciting."
    show finn smile

    an "I keep my mouth shut, not wanting to get on Zaina's nerves by agreeing with Finn, and not wanting to be a third person on Finn's back about being late—even though he {i}was{/i} pretty late."

    f unsure talk "Besides, I don't want her running off to do this stuff on her own again."
    show finn smile

    a down talk "I wasn't going to..."
    show alex smile

    z down talk "Good."
    show zaina smile

    p down talk "So where do we wanna start?"
    show paxton smile

    f down talk "Hmmm... the basic rules would be good, I guess."
    show finn smile

    an "He drums his fingers on the table for a moment before continuing."

    f unsure talk "So generally, you don't actually break into places. The hospital you went to was unlocked, right? That's fine, but breaking and entering is a bad idea."
    show finn smile

    z up talk "I told her that already."
    show zaina smile

    f down talk "It's never a bad reminder. What else... oh, you know how at parks they always tell you 'take nothing but photos, leave nothing but footprints?' Same rule applies here."
    f up talk "You want it to look like you were never there."
    f unsure talk "You'll find cool stuff sometimes, but you leave it for the next explorers to find."
    show finn smile

    a unsure talk "That makes sense..."
    show alex smile

    z unsure talk "I think taking photos is the best part, personally."
    show zaina smile

    z up talk "There's something cool about capturing the process of urban decay on film..."
    show zaina smile

    f down talk "Or memory card."
    show finn smile

    an "Zaina laughs a bit at that."

    z unsure talk "These days, yeah."
    show zaina smile

    a up talk "I did really like seeing all the photos on your account—that's what really inspired me to go and try it for myself."
    show alex smile

    f unsure talk "By yourself."
    show finn smile

    a down talk "And I won't do it again! Lesson learned!"
    show alex smile

    f up talk "Good. I'll stop bringing it up. Maybe."
    f down talk "Really, though, the idea is that if you get hurt, or something goes wrong, someone can go get help or call 911 for you."
    f unsure talk "Which, speaking of 911, sometimes we run into people when we're exploring."
    show finn smile

    p unsure talk "Sometimes they're cops."
    show paxton smile

    z down talk "They've been cops more than once..."
    show zaina smile

    f up talk "Even so, don't run. Sometimes we've hidden, sometimes we're just up front that we're exploring and taking pictures."
    show finn smile

    p down talk "But if you run, there's a good chance you're going to get hurt, or they're going to think you're doing something like vandalism."
    show paxton smile

    z unsure talk "But we're only taking pictures of that."
    show zaina smile

    f unsure talk "Are you prepared for that kind of thing?"
    show finn smile

    an "Considering I already almost got in trouble once..."

    a up talk "Sure."

    an smile "Might as well."

    an "I'd rather not get arrested, but... we'll just have to be careful."

    f up talk "Cool. Let's see..."
    show finn smile

    z down talk "We're not taking her anywhere with asbestos, right?"
    show zaina smile

    f up talk "Not now, anyway."
    show finn smile

    a unsure talk "I would need a mask for that, right?"
    show alex smile

    f unsure talk "Yup. Unless you want cancer in 40 years."
    show finn smile

    a down talk "I can't say I do."
    show alex smile

    f down talk "Didn't think so. Anyway, that's most common in places that were built between the thirties and fifties."
    show finn smile

    a unsure talk "Right. Even though it wasn't banned until the late seventies?"
    show alex smile

    f unsure talk "Yeah. We're gonna be taking you to more... contemporary places, probably. Though it would be good to have gloves for that."
    show finn smile

    an "I nod along. So far everything they're telling me makes sense, and it's making my heart race."

    an "The same kind of giddy excitement I felt exploring the hospital I went to before."

    an "This is so unlike me, but..."

    an "I don't want to let this feeling go."

    z unsure talk "You look awfully excited."
    show zaina smile

    show alex at Transform:
        easein 0.15 yoffset 10
        pause .10
        easein 0.15 yoffset -10
        pause .10
        easein 0.15 yoffset 0

    an up "I jump a little bit."

    a unsure talk "W-Well... I've always wanted to see this kind of old architecture up close..."

    a down talk "Old buildings have always kind of fascinated me..."

    a up talk "And seeing the psych ward was also pretty cool—really cool, honestly."

    a unsure talk "It felt so timeless? Like aside from the dust everywhere, you could imagine people coming in again..."

    a down talk "The old files were there, the beds were still there..."

    a up talk "I've never seen anything like it before—never experienced anything like that before—and, um—"

    a unsure talk sweat "Um..."

    an smile "Oh no. They're staring."

    an "I got way too excited..."

    a down talk "... yeah."

    an smile "I don't make eye contact with them until I hear Finn chuckle beside me."

    f down talk "It {i}is{/i} cool, isn't it?"
    f up talk "I think you'll make a good addition to our little team."
    show finn smile

    an blush -sweat "I feel my face flush from the compliment, my heart pounding in my chest."

    f unsure talk "Meet us back here, say... this Thursday, around 10:30 PM? We'll leave after Paxton's off work."
    show finn smile

    a -blush up talk "I can do that!"
    show alex smile

    f up talk "Cool. Anyone wanna tell her anything else?"
    show finn smile

    z up talk "I'm curious to see what our newbie is made of."
    show zaina smile

    a blush unsure talk "N-Newbie?"
    an smile "Okay, {i}now{/i} I'm embarrassed." 

    p unsure talk "Don't tease her too much, Zaina."
    show paxton smile

    z unsure talk "If she's put off by {i}this{/i}, she's gonna have a bad time."
    show zaina smile

    a down talk "I-I'm not! I'm fine!"

    an smile "I can handle a little teasing!"

    z up talk "Good. We'll see you Thursday then."
    show zaina smile

    p talk "It was good meeting you, by the way."
    show paxton smile

    a -blush unsure talk "It was good meeting you too—all of you."
    a up "I'll see you Thursday!"

    hide alex
    hide finn
    hide paxton
    hide zaina
    with dissolve

    an "I can't think of the last time I was this excited about anything..."

    ## Scene 11
    ##black screen
    stop music fadeout 2

    scene black
    with fadee

    an "Finn texted me this morning to let me know that I just need a good pair of shoes for this."

    an "No respirator required for this particular place, which is good, given that I haven't had a chance to get one yet." 

    an "It seems to be their regular thing to meet up with Paxton once he's done with his shift at the cafe."

    an "I'm filled with nervous energy, but something else too."

    an "But once the front door of the mansion opens, all that nervousness melts away into pure, unadulterated excitement."

    ##mansion BG
    scene bg mansion
    with fadee

    play music "Be_piano12.ogg" fadein 1
    queue music "Be_piano12.ogg"

    an "We head inside, and I'm met with that same feeling as before, but also something new."

    show finn up smile:
        xalign 0.0
        yalign 1.0
    show zaina up smile:
        xalign 0.67
        yalign -2.2
    show alex neutral smile:
        xalign 0.37
        yalign 2.3
    show paxton up smile hat:
        xalign 1.05
        yalign 1.0
    with dissolve

    f unsure talk "Let's take a look around, shall we?"
    show finn smile

    an "I'm not lonely."

    a up talk "Y-Yeah."

    an smile "It feels nice to really {i}be{/i} with people again, outside of class, outside of schoolwork."

    an "This is just something fun."

    an "Or hopefully, it will be."

    p unsure talk "Do we want to split off into pairs?"
    show paxton smile

    f up frowntalk "That sounds good to me."
    f down talk "Personally, whoever comes with me is getting dragged into looking for any secret pathways."
    f unsure talk "What about you two?"
    show finn smile

    z unsure talk "Dunno yet, we'll see where inspiration and my camera take me. "
    show zaina smile

    p down talk "I mostly just want to explore the house."
    show paxton smile

    an down frown "Hmm..." 

    an unsure "This would be a good chance to get to know them all a little better..."

    f up talk "Anywhere you wanna go in particular, Alex?"
    show finn smile

    ##Basically there are four sets of choices, each one giving a point to one of the love interests.

    ##choice
    menu:
        "I'd like to explore the place with Paxton.":
            a up talk "If that's not any trouble!"
            an smile "He seems pretty easy going..."
            p up talk "Sounds great!"
            an "But I'm relieved nonetheless."
            ##end choice (+1 to Paxton Go to Scene 11A)
            $ paxton_stat += 1
            f down talk "With that settled, we'll meet back here in half an hour or so."
            show finn smile
            hide alex
            hide finn
            hide paxton
            hide zaina
            with dissolve
            jump Scene11A
        "Maybe I could help you, Finn?":
            f unsure talk "Oh? You have more of an appetite for excitement than I expected."
            show finn smile
            a up talk "I could say the same to you."
            an smile "Finn laughs easily at that."
            an "He has a point, though—I didn't think I had this in me either."
            ##end choice (+1 to Finn Go to Scene 11B)
            $ finn_stat += 1
            f down talk "With that settled, we'll meet back here in half an hour or so."
            show finn smile
            hide alex
            hide finn
            hide paxton
            hide zaina
            with dissolve
            jump Scene11B
        "You take the photos for the Instagram page, Zaina?":
            z up talk "Usually, yeah."
            show zaina smile
            an "I'm really curious about how she takes the photos. They all look so amazing..."
            an "Is there a trick to it?"
            ##Zaina smile
            z down talk "I'll let you come along if you don't get in my way."
            show zaina smile
            a up talk "I won't."
            an smile "Something about her playful tone relaxes something in me."
            a down talk "Probably."
            show alex smile
            ##end choice (+1 to Zaina Go to Scene 11C)
            $ zaina_stat += 1
            f down talk "With that settled, we'll meet back here in half an hour or so."
            show finn smile
            hide alex
            hide finn
            hide paxton
            hide zaina
            with dissolve
            jump Scene11C

label Scene11A:
    ## Scene 11A
    show alex neutral smile at closeright:
        yalign -0.4
    show paxton down smile hat at closeleft
    with dissolve

    p unsure talk "Ready, Alex?"
    show paxton smile

    a up talk "Y-Yeah!"
    show alex smile

    hide paxton
    hide alex
    with dissolve

    an "Zaina goes to follow Finn while Paxton and I make our way through the downstairs area."

    an "I can't help but fall a bit quiet as I take in the sights around me."

    an "Everything's covered in a thick layer of dust, furniture left in place."

    an "But still, I can imagine this was once a beautiful place to live..."

    show alex up smile at closeright:
        yalign -0.4
    show paxton up smile hat at closeleft
    with dissolve

    p unsure talk "Enjoying yourself?"
    show paxton smile

    a unsure talk "Oh—um, yes."

    a down talk "I wonder a bit what it might've been like to live here..."

    a unsure talk "And who might've."
    show alex smile

    p up talk "Finn might know."

    p unsure talk "He usually researches these places pretty thoroughly."

    p up talk "It's fun to hear about, but sometimes I like having it stay a mystery."
    show paxton smile

    a up talk "Oh?"
    show alex smile

    ##paxton flustered/blushing/whatever
    show paxton unsure talk sweat
    p blush "Well, uh, I like writing a lot." with Dissolve(1.0)

    p up talk "I write RPG campaigns..."

    show paxton unsure -sweat
    p -blush "And while this is totally different from that, it's still a fun way to flex that muscle." with Dissolve(1.0)
    show paxton smile

    a unsure talk "Like coming up with stories for the people who may have lived here?"
    show alex smile

    p up talk "Yeah!"
    show paxton smile

    an "We wander down a hallway, stopping at a double set of doors."

    p unsure talk "Wanna see what's in here?"
    show paxton smile

    a up talk "Sure!"
    show alex smile

    an "The door opens with a creak and we step inside, discovering a grand and dusty ballroom."

    an "It must have been beautiful when it was in use..."

    a unsure talk "So would you come up with a story about the people who might dance here?"
    show alex smile

    p up talk "Hmm, yeah."

    p down talk "I think maybe not a lot of dancing happened here. Maybe more of a focus on socializing..."

    p unsure talk "Maybe a wealthy, middle aged couple lived here, retired early."

    p up talk "And were just living out their days throwing parties for no good reason."

    p unsure talk "Or, well, any reason at all."
    show paxton smile

    an "It's a simple idea, but it's fun to think about."

    a down talk "Do you think they were important?"
    show alex smile

    p down talk "Hmm... yeah, but not {i}too{/i} important."

    p unsure talk "This isn't a former governor's house or anything as far as I know."
    show paxton smile

    a unsure talk "Makes sense..."
    show alex smile

    an "It's fascinating to think about this room being filled with people chatting and drinking champagne."

    a down talk "Maybe the couple did dance here though, when the room wasn't being used for a party."
    show alex smile

    p up talk "Haha, maybe."
    show paxton smile

    play sound "upbeat.mp3" fadein 1 fadeout 3

    an "I watch as he pulls out his phone and a song starts to play."
    
    ## if you prefer something else you can swap it it just needs to be upbeat

    p unsure talk "Would you like to dance?"

    p up talk "Just for fun."
    show paxton smile

    an unsure "Part of me feels embarrassed in an instant."

    an "It's not as though I know how to dance at all."

    an "But there's no one here but him to judge my lack of skills."

    an "And he really doesn't seem like the type."

    a up talk "Sounds fun!"

    an smile "I don't know what I'm doing at all, but neither does he."

    an "And in the end we're both laughing." 

    an "I feel lighter than I have in months and months..."

    an "Impulsively, I try to spin around—"

    a up shock "Eep!"

    an "I feel myself falling, but before I can hit the ground, I feel something—someone—grab me."

    p down talk "You okay?"
    show paxton smile

    an frown blush "Breathless, I look up at Paxton. I can feel my cheeks burn."

    a unsure talk "Y-Yeah."

    a down talk "I'm fine. Sorry."
    show alex smile

    stop sound fadeout 1

    an "He helps me steady myself, and otherwise seems unbothered as he turns off the music."

    p unsure talk "Should we head back?"
    show paxton smile

    a unsure talk "Yeah, maybe."

    an smile "Before I can make a fool of myself any further."

    an "We're a little quiet on the walk back, and I wonder if I've fumbled this already."

    p down talk "You know, I didn't think dancing would be the most dangerous part of today's venture."
    show paxton smile

    a down talk "W-Well, maybe that's for the best."
    show alex smile

    p up talk "Ha! Probably. Better than any broken bones or scratches."
    show paxton smile

    an unsure "He doesn't sound like he's making fun of me or laughing at me, and some anxiety in my stomach eases."

    an "Maybe I didn't ruin this."

    hide alex
    hide paxton
    with dissolve
    jump Scene11D

label Scene11B:
    ## Scene 11B

    an "We split into two groups, Paxton following after Zaina while I go with Finn."

    an "Our pace is slow and he periodically stops to examine the walls, his touch light and careful."

    show alex up smile backpack at closeright:
        yalign -0.4
    show finn up smile at closeleft
    with dissolve

    a unsure talk "Do you often find secret passages?"
    show alex smile

    f unsure talk "Not often, but sometimes."

    ##Finn smile
    f up talk "Just often enough that it's worth looking every time."

    f unsure talk "There's maintenance tunnels under the school, you know."
    show finn smile

    a down talk "Have you been in them?"
    show alex smile

    f up talk "Yeah, with Zaina and Paxton."

    f down talk "We've only done it the one time, though. Pretty sure we'd get in more trouble with the school that we {i}couldn't{/i} talk our way out of than with police, you know?"
    show finn smile

    a unsure talk "Hm... yeah..."
    show alex smile

    f unsure talk "Wanna go sometime?"
    show finn smile

    a up frowntalk "I don't want to get kicked out of school!"

    an frown "My parents would have my head!"

    f down talk "You're not the only one. We'd just be extra careful."
    show finn smile

    an unsure smile "I'm not convinced now, but maybe I'll be more interested another time."

    an "Especially given that I didn't think I'd be doing any of this in the first place."

    an "As we wander through the mansion, we end up in a storage room."

    an "While Finn looks around, my eyes fall on a gold frame with a sheet over it."

    an frown "What's this?"

    an "I lift up the sheet carefully, revealing a painting of a man and a woman kissing. It has an unexpectedly calming atmosphere despite the darkness of the storage room."

    f up talk "Nice find." 
    show finn smile

    a up talk "Oh—thank you..."

    a down talk "It's pretty..." 
    show alex smile

    f unsure talk "It is." 
    show finn smile

    an "I watch as he carefully leans the frame forward, examining the back of it."

    a unsure talk "What are you doing?"
    show alex smile

    f up talk "Seeing if there's a potential title for this thing anywhere."
    show finn smile

    a down talk "Are they usually on the back?"
    show alex smile

    f down talk "No, I've found old paintings that aren't titled at all."

    f up talk "But it's worth looking."
    show finn smile

    f unsure talk "Hmm... 'Le Confort,' maybe."
    show finn smile

    an "He sets the frame back in place and we take a look at it again."

    a unsure talk "I wonder who painted it..."

    a up talk "And who the subjects are."
    show alex smile

    f down frowntalk "Hmm... well, it's down in this dusty storage area, so maybe one of them got dumped after they painted this."
    show finn frown

    a down frowntalk "That's depressing..." 
    show alex frown

    f unsure frowntalk "Or maybe one of them died, hmm..."
    show finn frown

    a unsure talk "Do you think this way because you're a goth or is this just who you are?"
    show alex smile

    f up talk "Why not both?"
    show finn smile

    an "I can't help but laugh a little at that."

    an "I like his sense of humor."

    a up talk "What if it wasn't so miserable? Maybe the couple lived a long, happy life together and this ended up down here after they passed."
    show alex smile

    f unsure talk "Since that still involves dying, you're not really making this all that better."
    show finn smile

    a down talk "It's less sad than one of them being alone."
    show alex smile

    f down talk "Hmm... you have a point."
    show finn smile

    a up talk "I {i}do{/i}."

    an smile "I drop the sheet back over the painting."

    a unsure talk "Should we start heading back?"
    show alex smile

    f up talk "Sounds good."
    show finn smile

    hide finn
    hide alex
    with dissolve

    jump Scene11D

label Scene11C:
    ## Scene 11C

    show alex up smile backpack at closeright:
        yalign -0.4
    show zaina up smile at closeleft:
        xalign 0.15
        yalign -0.15
    with dissolve

    z up talk "Come on if you're coming."
    show zaina smile

    an "I quickly follow after her, wondering where exactly we're going."

    an "Does she already have an idea in mind?"

    a unsure talk "How do you usually choose what to take pictures of?"
    show alex smile

    z unsure talk "Eh, it's whatever strikes my mood."
    show zaina smile

    an down frown "That's pretty vague..." 

    a unsure frowntalk "Is there something specific you do to get good shots?"
    show alex frown

    z down talk "Who knows."
    show zaina smile

    ##Alex frowning/scowling/pouting/w/e
    z unsure talk "Do you have an interest in this kind of thing?"
    show zaina smile

    a up talk "I do now."

    a unsure talk "What kind of camera is that?"
    show alex smile

    z down talk "A mirrorless."
    show zaina smile

    an frown "I realize that I have no idea what that means."

    z up talk "Sometimes I just use my phone, though—phone cameras have improved a lot these days."

    z unsure talk "But this is my nicer camera."
    show zaina smile

    an "Looking around as we walk, I try to see what she might see."

    an up smile "In all the photos she posted to the account, there's something striking about them."

    an "And though the inside of this mansion is fascinating, I don't quite get how she manages to make them look {i}so{/i} enticing."

    a unsure talk "How does it pick up the light when it's so dark?"
    show alex smile

    z down talk "I don't know, I know how to use it, not how it {i}works{/i}. Those are two different things."
    show zaina smile

    a down smile "Hmm..."

    an "We stop in what seems to be a foyer."

    an "I don't think I'll ever understand how anyone can need {i}this{/i} many rooms with couches and stuff."

    an "Zaina starts taking pictures, multiple ones that all seem to be of the same thing."

    an "I watch as she squats down for a few shots before standing up again."

    a up talk "Is there something interesting about that couch?"
    show alex smile

    z unsure talk "Hmmm I liked the angle I guess."
    show zaina smile

    a unsure frowntalk "The... angle?"
    show alex frown

    z down talk "The way all the stuff is laid out, from where I'm standing."

    z up talk "I thought it'd make a good shot."
    show zaina smile

    a up talk "Oh!"

    an smile "I wonder how she sees things that way."

    an "Maybe I'm too logical of a person for this kind of thing?"

    a unsure talk "Do you take pictures of people or just things?"
    show alex smile

    z unsure talk "Usually just things. Why, do you want me to take a picture of you?"
    show zaina smile

    ##Alex blushing/flustered
    show alex down talk sweat
    a blush "No! Not in particular..." with Dissolve(1.0)

    an smile "Did that sound like I wanted her to take a picture of me?"

    a unsure talk "I just—I think all the photos you take are cool an—"

    ## First ten seconds of this? If there's something better I'm all for it, I'm going for something skittering over the roof and this sounds close enough https://freesound.org/people/Darius%20Kedros/sounds/276857/
    show alex up frown -blush -sweat
    show zaina up frown
    "Skitterr..."

    an down shock "What—What was—"

    an unsure frown "An animal, probably. It was probably definitely an animal."

    an down "Given that we are, in fact, in an old building."

    an up "That has been partially overtaken by nature."

    an down "Just an animal."

    an unsure "It's just an animal—"

    ##Zaina smile
    z unsure talk "You okay there?"
    show zaina smile

    a up frowntalk sweat "I'm fine—"

    an smile "She looks... really happy for some reason."

    an "I'm immediately suspicious."

    z up talk "Well that's good."

    z down talk "Can't have my new favorite model {i}too{/i} spooked."
    show zaina smile

    a unsure shock "M-Model?"

    a up frowntalk "Did you take a picture of me?!"
    show alex frown

    z up talk "Sure did. It was too good to pass up."
    show zaina smile

    a down frowntalk "You're gonna delete it, right?"
    show alex frown

    z down talk "Nah."
    show zaina smile

    a unsure frowntalk "Zaina!"

    hide zaina
    with dissolve

    an frown "She isn't listening to me though, already heading back the way we came."

    an "I'm so embarrassed..."

    an smile "But I have no choice but to follow after her."

    hide alex
    with dissolve

    jump Scene11D

label Scene11D:
    ## Scene 11D
    stop music fadeout 4

    scene black
    with fadee

    an "We meet back in the main area of the house and talk a little bit about what we found in our explorations before heading our separate ways."

    an "Back in my apartment, I fall into bed. I'm tired, but for the first time in months my eyes aren't burning."

    an "My back doesn't hurt."

    an "I don't close my eyes and see walls of text."

    an "For the first time in months, I feel really, really happy."

## Scene 12
    ##classroom bg
    scene bg classroom
    with fadee 

    play music "happy.ogg" fadein 1
    queue music "happy.ogg"

    play sound "phonevibrate.mp3"

    an "I got a text from Finn during class, inviting me to another site."

    #"Classmate1" "You look happy—text from your boyfriend?"

    #an "I jump, looking at the person beside me."

    #a "N-No. Just some good news."

    an "I feel my face burn and tap out a quick reply that I'd like to come before putting my phone away."

    an "By this point, our professor is back to teaching, and I throw myself back into taking notes."

    an "It's hard to focus, though, as I wonder about where we're gonna go tonight."

    stop music fadeout 2
    ##hospital bg
    scene bg hospital
    with fadee

    play music "Be_piano12.ogg" fadein 1
    queue music "Be_piano12.ogg"

    an "Finn texted me the address this time, and we meet at the site."

    an "The inside of this old hospital isn't exciting in and of itself, but it's bigger than the other two places we've been."

    an "This time, I'm a little more prepared too, with a first aid kit tucked into my backpack."

    an "No one got hurt last time, but better safe than sorry, right?"

    show finn up smile:
        xalign -0.05
        yalign 1.0
    show zaina up smile:
        xalign 0.67
        yalign -2.2
    show alex up smile backpack behind zaina:
        xalign 0.37
        yalign 2.3
    show paxton up smile hat:
        xalign 1.05
        yalign 1.0
    with dissolve

    f unsure talk "Do we want to split up again?"
    show finn smile

    z down talk "Sounds good to me. I like having the newbie around—we don't have to stick together quite so much."
    show zaina smile

    f up talk "What, do you not like hanging out with me, Zaina?"
    show finn smile

    z up talk "You're unbearable and you know it."
    show zaina smile

    an "Finn laughs. It's a little difficult to parse their relationship, but they seem to be okay? They're kind of like how some of my old friends are with their siblings, I guess."

    z unsure talk "Anyone in particular you want to come with, Alex?"
    show zaina smile

    a unsure talk "Oh! Um..."
    show alex smile

    ##choice
    menu:
        "Would you mind if I tagged along, Paxton?":
            p unsure talk "Not at all!"
            show paxton smile
            an up "He's so easy going, it's really relaxing to me..."
            ##end choice (+1 to Paxton Go to Scene 12A)
            $ paxton_stat += 1
            hide alex
            hide finn
            hide zaina
            hide paxton
            with dissolve
            jump Scene12A
        "Um... Finn? If that's okay with you.":
            f down talk "Fine by me."
            show finn smile
            ##end choice (+1 to Finn Go to Scene 12B)
            $ finn_stat += 1
            hide alex
            hide finn
            hide zaina
            hide paxton
            with dissolve
            jump Scene12B
        "If you're going to call me a newbie...":
            a down talk "... then you should help keep an eye on me, right?"
            show alex smile
            z up talk "Oh? Am I your babysitter now?"
            show zaina smile
            an "There's something fun about her..."
            an "I want to get to know her a little better."
            a up talk "If you want to call it that, sure."
            show alex smile
            z unsure talk "Well, as long as you can keep up, it's fine."
            show zaina smile
            ##end choice (+1 to Zaina Go to Scene 12C)
            $ zaina_stat += 1
            hide alex
            hide finn
            hide zaina
            hide paxton
            with dissolve
            jump Scene12C

label Scene12A:
    ## Scene 12A
    show alex neutral smile backpack at closeright:
        yalign -0.4
    show paxton up smile hat at closeleft
    with dissolve

    a unsure talk "So where are we heading?"
    show alex smile

    p unsure talk "Hmm, we'll see. I don't have anything particular in mind."
    show paxton smile

    an "There's a pleasant quiet between us as we walk down the empty corridors."

    an "But I can't help but want to fill the silence a little more."

    an "I want to get to know him a little better."

    a up talk "So, um, what got you interested in working as a barista anyway?"
    show alex smile

    p down talk "Oh, nothing special."

    p unsure talk "I've always liked coffee, and I needed a job."

    p up talk "So when I heard the cafe was hiring, I went ahead and applied!" 

    p unsure talk "I figured it couldn't be too hard—it's minimum wage."

    p up talk "And it wasn't."

    p down talk "The trickiest part you {i}have{/i} to learn is steaming the milk right."

    p unsure talk "It has to be a certain texture for latte art in particular, but even in general there's a big difference in how much foam there should be for a latte versus a cappuccino." 

    p up talk "And getting a handle on that, and how far what milks go is the main thing to learn."
    show paxton smile

    a unsure talk "What about the flavored lattes? And the things you make up?"
    show alex smile

    p unsure talk "Oh, those just follow proportion rules."

    p down talk "Just a lot of memorizing measurements."
    show paxton smile

    a down talk "Oh."

    an smile "Somehow I always thought it was more complicated than that."

    a unsure talk "So it's pretty hard to mess up?"
    show alex smile

    p unsure talk "Yeah. Unless you're not paying attention to how many pumps of something you're putting in."

    p down talk "Or you put too much milk in the pitcher so it overflows all over your hand."

    p up talk "After a while it's all automatic, though."
    show paxton smile

    a down talk "That doesn't seem so bad—aside from the overflowing milk..."

    an smile "He makes it sound way more interesting than I expected."

    p unsure talk "Haha, it's not that bad."

    p down talk "This is going to sound {i}way{/i} worse than I mean it, but after a while of working with hot drinks all day, your reaction to spilling hot liquids on yourself is pretty muted."

    p unsure talk "Aside from when I've gotten {i}really{/i} hot water on myself, my reaction is usually just 'ow' after the first few times..."
    show paxton smile

    a unsure talk "As long as you run your hand under cold water after..."
    show alex smile

    p up talk "Oh yeah, usually."

    p unsure talk "Unless I have a line of drinks."

    p down talk "Then I usually forget I burned myself by the time I address it."
    show paxton smile

    a up frowntalk "That isn't good!"
    show alex frown

    p unsure talk "It's fine, it's fine! Really, I don't make a habit of it."

    p up talk "I'm not a masochist or anything."
    show paxton smile

    a unsure talk "Well... good."

    an smile "I'm trying to think of what else to say when I spy a room with the door slightly ajar."

    an "Curious, I stop and push the door open."

    an "It's nothing particularly exciting, just a room full of filing cabinets."

    an "A couple of knickknacks are left on this old desk."

    p unsure talk "Something catch your eye?"
    show paxton smile

    a down talk "I just wanted to see what was in here."

    an smile "I remember what Finn said about not taking anything."

    an "But I wonder what's stored away here..."

    an "Nothing too important if it's still here, but..."

    an "I experimentally tug on one of the filing cabinet drawers, only to find that it doesn't open."

    p down talk "Is it locked? I can open it."
    show paxton smile

    an "He pulls out a knife—"

    a unsure frowntalk "Aren't we not supposed to damage anything?"
    show alex frown

    p up talk "This won't break it."
    show paxton smile

    an frown "I watch as he puts it into the keyhole, and carefully jiggles it around for a moment."

    an "I never thought of picking a lock with a knife, but he seems to know what he's doing..."

    play sound "break.mp3"

    an "After a moment, the lock pops open, the mechanism sliding out, and the knife falls from Paxton's hands."

    an "Before I can react, I see him reflexively reach for the knife—"

    p down frowntalk "Ouch! Shit..."
    show paxton frown

    an "Blood wells on the surface of his skin and the knife lays on the floor."

    an "It takes it a second to hit me what just happened."

    a down frowntalk "Paxton!"
    show alex frown

    p unsure frowntalk "I'm fine, I'm fine!"
    show paxton frown

    a up frowntalk "You're bleeding!"
    show alex frown

    p down frowntalk "... okay, maybe I'm not fine."
    show paxton frown

    a down frowntalk "Um—hold on."

    an frown "I take off my backpack and quickly pull out my first aid kit. I'm glad I brought it—I didn't think I'd need it, but here we are."

    a unsure frowntalk "Let me see?"

    an frown "He holds out his hand for me so I can see the cut across the side of his finger."

    an "Carefully holding his hand in mine, I grab a piece of gauze from my first aid kit to wipe up the blood as best I can."

    an "His hand is steady in mine as I grab the antiseptic and spray it on."

    an "... maybe a little too much, given that it's dripping, but..."

    a down frowntalk "Sorry if that stung."
    show alex frown

    p unsure talk "It's fine. Barely felt it."
    show paxton smile

    an "The way he smiles loosens something in me I didn't realize was tense..."

    a unsure frowntalk "Hrm... this is an awkward cut..."

    an frown "Bandages won't cut it."

    an "Or well, they might, for five minutes at best."

    an "I pull out the gauze again, wrapping it around the wound before getting the medical tape and using that to secure it in place."

    an "It's not the prettiest bandaging job, but..."

    p up talk "Thank you."

    p unsure frowntalk "Do you still want to see what's in there?"
    show paxton frown

    a down talk "Oh, um, sure, if it's already open."
    show alex smile

    p down frowntalk "I had to pay the price in blood..." 

    ##Paxton smile
    show paxton smile
    p unsure talk "So the treasure within {i}must{/i} be worth it."
    show paxton smile

    an "I start giggling before I can even try to catch myself."

    a unsure talk "Is that your inner creative writing major coming out?"
    show alex smile

    p up talk "More like my inner dungeon master."
    show paxton smile

    an "He pulls open the drawer, looking quite pleased with himself."

    p unsure talk "You're welcome to sit in on one of my campaigns sometime if you'd like."
    show paxton smile

    an "I've never done something like that before either..."

    a up talk "I might take you up on that."

    an smile "But first..."

    an "I peek into the drawer, seeing a couple of medical books and an old yellow notepad with a bunch of medical terms on it. Medication notes, I think, but the author's handwriting is worse than mine."

    an "Paxton picks up an envelope, carefully pulling out the contents."

    a unsure talk "What's that?"
    show alex smile

    p up talk "A letter, it seems..."
    show paxton smile

    an "We read over it together, and it's short but sweet."

    an "One doctor asking another on a date."

    a down talk "Aww..."
    show alex smile

    p unsure talk "Yeah... this is pretty sweet."
    show paxton smile

    ##paxton blushing
    show paxton up talk
    p blush "I think we should probably get back to the others though."
    show paxton smile

    a up talk "Oh! Yeah, probably. It's been awhile now, hasn't it..."

    an smile "I watch as he carefully puts the letter back in the envelope, and the envelope back in the drawer, before he shuts it."

    hide alex
    hide paxton
    with dissolve

    scene black
    with fadee

    an "As we make our way back to the main entrance, I wonder what became of the doctor who wrote the letter."

    an "And I wonder what whoever finds it next will think of it."

    jump Scene13

label Scene12B:
    ## Scene 12B

    an "He doesn't wait long before he's already trekking down the hall, away from the others."

    show alex up smile backpack at closeright:
        yalign -0.4
    with dissolve

    a up talk "Oh—wait up!"
    show alex smile

    show finn up smile at closeleft
    with dissolve

    f unsure talk "Hm? Oh, right, sorry."
    show finn smile

    an "He slows his steps until I'm at his side and we continue our walk together."

    f up talk "This place feels bigger on the inside."
    show finn smile

    a down talk "Yeah, it does."
    show alex smile

    f down talk "More than usual, anyway."
    show finn smile

    a unsure talk "More than usual?"
    show alex smile

    f unsure talk "Well, a lot of these abandoned places look big on the inside 'cause so much of the clutter is gone. But this place... is different."
    show finn smile

    an "I don't really know what Finn is seeing. It's a standard, albeit dusty, hospital to me. But I wonder what the world is like in Finn's eyes?"

    a up talk "Anything in particular you're searching for?"
    show alex smile

    f down talk "If you're asking about what I'm searching for in life, the answer is no. If you're asking about the hospital, then the answer is..."

    f up talk "... also no."
    show finn smile

    a unsure talk "Haha. Fair enough."

    an smile "It's mostly quiet between us after that, but I'm still pretty entertained by Finn's eyes sweeping the entire place meticulously."

    an "He's serious about it in his own way. It's nice. Hehe, I feel like we're undercover investigating or something."

    f unsure frowntalk "Do I have something on my face?"
    show finn frown

    a up talk "Oh! Sorry, I didn't mean to stare."
    show alex smile

    ##Finn smile
    f up talk "So you {i}were{/i} staring."
    show finn smile

    a unsure talk "It's n-not like that!"
    show alex smile

    f unsure talk "Like what? I didn't say anything."
    show finn smile

    a down talk "I was just noticing how you seemed very focused. That's all."
    show alex smile

    f down frowntalk "Hm. I guess it might seem that way."
    show finn frown

    an "He trails off, his focus returning to the numerous doors we pass. I wonder what he's looking out for?"

    f unsure frowntalk "This time..."
    show finn frown

    a unsure frowntalk "Huh? This time, what?"
    show alex frown

    f up talk "We didn't find anything last time. This time I know we will."
    show finn smile

    ##Alex smile
    a up talk "Wow, you really are excited today. And optimistic, too?"
    show alex smile

    f unsure talk "What are you going on about now?"
    show finn smile

    a unsure talk "You seem determined, that's all. It's getting me excited, too."
    show alex smile

    f up talk "You're the one who wanted to come. I'd hope you are."
    show finn smile

    a down talk "You know what I meant, Finn."

    #Finn smile
    show finn up smile
    an smile "He chuckles and rolls his eyes at me before focusing on the next door we come across. I can't pinpoint why, but it's built differently than the others."

    a unsure talk "This one looks like it might have something interesting for you."
    show alex smile

    f unsure talk "Hm. Nice eye, I think you're right."
    show finn smile

    ##Vibration
    "..." with vpunch

    f down frowntalk "Huh?"
    show finn frown

    a down frowntalk "Oh, is it locked?"
    show alex frown

    f unsure frowntalk "No way. I think it's just stuck."
    show finn frown

    an "He uses both hands this time, straining against the door that's not budging."
    
    ##Vibration
    "..." with vpunch

    a up frowntalk "Are you sure it's stuck? Should I help?"
    show alex frown

    f up frowntalk "No, it's fine. I can open a stuck door. No reason for you to hurt yourself."
    show finn frown

    an smile "Ha, can't tell if he's trying to be nice or patronizing me..."

    a unsure frowntalk "Well, if you think someone might get hurt, maybe we should just move on."

    an smile "He shakes his head way too fast."

    f down frowntalk "Nuh uh. Hold on, one more try."
    show finn frown

    a down frowntalk "Umm..."
    show alex frown

    ##Vibration
    "..." with vpunch

    play sound "break.mp3"

    ##Surprised Finn face
    f up frowntalk sweat "Ah!"
    show finn frown

    hide finn
    with easeoutbottom

    a unsure shock "Finn?!"

    an frown "Whether the door was stuck or locked doesn't matter anymore. It falls with a crash to the floor and Finn along with it."

    an "I rush over to him, past the snapped-off door hinges that roll under the kicked up dust and debris."

    a down frowntalk "Finn. {i}Cough, cough.{/i} Are you okay?"
    show alex frown

    show finn down close frown -sweat at Transform:
        linear 0.0 zoom 1.3 xalign 0.05 yalign -5.0
        linear 1.5 zoom 1.3 xalign 0.05 yalign 0.2
    with dissolve

    f unsure frowntalk "Ugh..."
    show finn frown

    an "I move to help him sit up before I gasp and see red, tinged on both his shoulder and the broken door."

    a unsure frowntalk "Oh my God. Finn! You're hurt!"

    an frown "He looks over to his shoulder and winces."

    f down frowntalk -close "Aw man, I liked this shirt..."
    show finn frown

    a down frowntalk "Focus, Finn. H-hold on, I brought my first aid kit. I'll bandage you up."
    show alex frown

    f unsure frowntalk "It's fine... I think the door got worse than me."
    show finn frown

    a up frowntalk "It's not fine! Who cares about a door when you're bleeding?!"

    an frown "I'm definitely panicking more than Finn is. Isn't he worried about getting an infection?"

    an "Finn sighs and shakes his head when I start pulling out the kit."

    f down frowntalk "Alex, I promise I'm okay. Jeez... a little pain doesn't matter. I'm more annoyed about the damaged property than anything."
    show finn frown

    a unsure frowntalk "Well, sure, but shouldn't we make sure you don't get infected or something?"
    show alex frown

    f up frowntalk "Don't want to be bandaged. I'd rather keep going."
    show finn frown

    a up frowntalk "But your {i}shoulder{/i}, Finn. I really insist."

    an frown "He chuckles and reaches for my head before pausing."

    ##Finn frowning
    show finn down
    a unsure frowntalk "Huh? What is it?"
    show alex frown

    f unsure frown "..."

    an "He moves away from my head and instead takes my hand in his."

    ##Alex blushing
    show alex up frowntalk
    a blush "U-um—"
    show alex frown

    f up frowntalk "Blood."
    show finn frown

    an "I follow his gaze to see him turn my hand palm-up. He's right. I got some of his blood on my hand when I helped him sit up."

    show alex unsure frowntalk
    a -blush "Oh. I didn't notice..."

    an smile "Finn sighs and gently lets me go, a brief flash of guilt crossing his face."

    f down frowntalk "... fine."
    show finn frown

    a down frowntalk "What? So you want me to bandage you?"
    show alex frown

    f up frowntalk "... sure."
    show finn frown

    an smile "I don't really know why he changed his mind, but I'm grateful for it. It's one less thing to worry about."

    a unsure talk "Good. Thank you."
    show alex smile

    f unsure frown "Mm."

    an "I carefully blot away the blood and then spray the antiseptic. It's not as bad as it initially looked, thank goodness."

    an "Finn says nothing, gazing off into the distance and only flinching when I finally tighten the end of the gauze. It's not perfect, but it'll hold."

    a up frowntalk "Oops, sorry! Did that hurt? I'm done, by the way."
    show alex frown

    f down frown "..."

    show finn smile
    an "He looks down at his shoulder and flexes it before smiling back at me."

    f up talk "Didn't hurt. Thanks."
    show finn smile

    a up talk "Oh. You're welcome."

    an smile "He carefully takes my hand again, opening a wet tissue packet from the kit before cleaning away the small spot of blood there."

    an "For a moment, he really does look like a vampire with the way he's so focused on it."

    a unsure talk "Oh. Uh, thanks..."
    show alex smile

    f unsure talk "Mhmm. Let's go back."
    show finn smile

    a down talk "Right... I guess it is getting late. I'm sorry we didn't find something cool."

    an smile "Finn doesn't look disappointed in the slightest, much to my surprise. In fact, he just grins at me again."

    f up talk "Nah. I think I saw plenty."
    show finn smile

    a unsure frowntalk "Huh...?"

    hide finn
    with dissolve

    an frown "He doesn't elaborate, but I'm too exasperated to question him further. We leave the broken door behind and I wonder what about it was so cool."

    ##Alex smile
    an up smile "What a weirdo."

    hide alex
    with dissolve

    jump Scene13

label Scene12C:
    ## Scene 12C

    an "As soon as we split up from the boys, it becomes very apparent that Zaina has something on her mind."

    an "She's restless, constantly holding up her camera at something, then lowering it."

    an "We haven't spent very long exploring these halls, but even so, I don't think I've seen her take a single picture at all."

    show alex up frown backpack at closeright:
        yalign -0.4
    show zaina up frown at closeleft:
        xalign 0.15
        yalign -0.15
    with dissolve

    a unsure frowntalk "Something wrong?"
    show alex frown

    an "Zaina drops her camera again, this time letting it hang by the strap around her neck."

    z down frowntalk "That obvious, huh?"
    show zaina frown

    an "It's clear she's frustrated, and I'm not exactly sure what kind of answer she wants to hear."

    a up frowntalk "Um. Sort of?"
    show alex frown

    an "{i}Smooth{/i}, Alex."

    an "But my non-answer doesn't seem to irritate Zaina, in fact, it seems she's more annoyed at {i}herself{/i}."

    z unsure frowntalk "I guess you could say it's kind of like writer's block?"
    show zaina frown

    an "Her lips twist into a scowl, as if it hurt her to admit that something like writer's block could ever happen to her."

    z down frowntalk "Nothing's standing out to me."
    show zaina frown

    an "I look around. Well, apart from the cobwebs and the paint peeling from the walls, there isn't much to see in these hallways."

    a unsure frowntalk "We could go somewhere else? See if you get inspired elsewhere?"
    show alex frown

    z unsure frowntalk "... like?"
    show zaina frown

    an "She's looking at me expectantly, apparently waiting for my suggestion now, since I was the one to bring it up."

    an "I squirm under her gaze."

    an "Come on, Alex. This is a hospital, it's practically your backyard!" 

    an "What could be a place someone can take a lot of pictures of in here?"

    an "The ICU, maybe? There's bound to be abandoned beds and machines laying around in that department."

    an "No... I don't know where that'd be in here."

    an "Any maps left on the walls have pretty much degraded, rendering them useless."

    an "So then..."

    a unsure talk "Um, how about the roof?"
    show alex smile

    z down frown "..."

    an frown "I cringe when all I get is silence. That was a stupid idea, wasn't it? Oh, I knew I should've—"

    z unsure talk "The roof, huh? That's not bad, Newbie."

    z up talk "We can probably make out the stars clear as day up there."
    show zaina smile

    a down talk "Well, it's {i}night{/i}, actually."

    an smile "I blurt that out without thinking."

    a smile "..."

    z down frown "..."
    show zaina smile

    an "If I thought the silence before was bad, then this is even {i}worse{/i}."

    ##alex blush
    show alex unsure
    an blush "Oh God. Please, Earth, swallow me whole." with Dissolve(1.0)

    ##zaina laugh

    z up talk "So she can make jokes, too."

    z down talk "{i}Shitty{/i} ones, but..."

    z unsure talk "You're pretty entertaining to have around, aren't you?"
    show zaina smile

    an "She's mostly laughing {i}at{/i} me, but I've never seen her look so animated. It's hard to feel too bad about it when her laugh lights up her entire face."

    an "I stare, transfixed."

    an "By the time her laughter dies down, the heat in my cheeks is there for an entirely different reason."

    show alex down talk
    a -blush "So, um, the roof, then?" with Dissolve(1.0)

    an smile "I'm eager to get moving before I embarrass myself again."

    z up talk "Sure, I think it's this way..."
    show zaina smile

    an "It turns out to be a good thing that we didn't get far thanks to Zaina's dawdling. The stairs to the roof happen to be nearby, just a short walk from where we currently are."

    an "Still, we're in no particular hurry."

    a unsure talk "You don't normally get stuck like this, then?"
    show alex smile

    an "Zaina frowns, but I get the feeling it isn't directed at me."

    z down talk "Nah."

    z up talk "But I wanna get good shots now, since last time was a bust."
    show zaina smile

    an "Last time..."

    an "I wince. I'd spent so much of our time asking her questions she didn't get the chance to take any photos."

    an "It was all my fault."

    an "I frown, lips parting to offer an apology, but before I can do so, Zaina pinches my nose."

    a down shock "Ow!"
    show alex frown

    z down frowntalk "Doom and gloom doesn't suit you, Newbie."

    z unsure frowntalk "Besides..."

    ##zaina smirk
    z up talk "I didn't leave the mansion completely empty-handed."
    show zaina smile

    a unsure frowntalk "Huh?"

    an frown "I have no idea what she's talking about. Did she take pictures when I wasn't looking?"

    z unsure talk "Don't remember?"

    ##zaina shocked/scared
    z up sweat "..."

    an "Zaina pulls a face that can only be straight out of a horror movie. She looks like the first victim meeting the killer for the—{i}wait{/i}."

    an "Was that supposed to be {i}me{/i}? From the other day?"

    show zaina smile
    an "Her shaking shoulders ruin the effect she's going for and it isn't long before she dissolves into chuckles."

    ##zaina laugh, alex pout
    a up frowntalk "Hey!"

    a down frowntalk "That's not—"
    show alex frown

    z unsure talk "Funny? Oh, I think so."

    z up talk "Might've even made my day when it happened."

    z down talk "So don't worry about it."

    z unsure talk "Okay?"
    show zaina smile
    
    an "Any protests are swiftly met by a look that manages to be both sharp and playful."

    an smile "It's hard to say anything to that."

    an "We reach the stairs to the roof moments later, but upon trying the door at the top, we find it locked."

    an "Zaina looks more displeased than I thought she would be. Had she actually been looking forward to it?"

    z down frowntalk "I think there was a window somewhere..."
    show zaina frown

    an unsure frown "Wait. A {i}window{/i}?"

    an "Zaina descends the stairs before I can question her, only to confirm that I had indeed heard her correctly when I see her eyeing an open window."

    an "She inches her head out and looks up, probably gauging how much she'd have to climb to get to the roof."

    a down frowntalk "I don't think that's a—"

    an frown "If Zaina hears me, she gives no indication. Instead, she thrusts an arm out, hand settling on the windowsill to help balance her as she attempts to climb out of the window."

    an "But she doesn't get very far."

    an "The hand that's on the windowsill retracts immediately and when she pulls it toward her, I see red coating her palm."

    an "{i}Blood{/i}."

    z unsure frowntalk "Shit, that hurt..." 
    show zaina frown

    a up shock "Zaina!" 
    show alex frown

    an "I rush toward her, hands reaching for hers. I stop just short of her fingers, though, as I'm careful to avoid the cut."

    an "We glance at the window at the same time. It's then that we both realize that the window wasn't open, it was {i}broken{/i}. The windowsill still had remnants of the glass left, which is what she probably put her hand on. It shines red with her blood."

    z down frowntalk "Damn, and I gave my first-aid kit to Paxton, too..."
    show zaina frown

    a unsure frowntalk "It's okay! I brought one with me!"
    show alex frown

    an "The kit is out of my backpack in a flash, as I hurry to get the disinfectant and gauze out."

    an "When I turn to her, she's already holding her hand out. For some reason, I'd expected her to put up more of a fight."

    z unsure frowntalk "I'm usually the one who's doing this."

    z up frowntalk "So I know what it's like to have uncooperative patients."
    show zaina frown

    an frown "I blink. Am I really {i}that{/i} easy to read?"
    an "... but that's right. She mentioned that she gave her first-aid kit to Paxton."

    a down frowntalk "Finn?"
    show alex frown

    z down frowntalk "Finn."
    show zaina frown

    an "Suddenly she groans, as if Finn's name reminded her of something. She covers her face with her uninjured hand."

    z up frowntalk "I can't believe I actually pulled a {i}Finn{/i}."
    show zaina frown

    an "Zaina lamenting her decision specifically because it was something Finn would do was not what I expected when I saw her cut herself. I fight a smile as I apply disinfectant to the wound."

    a unsure frowntalk "It happens to the best of us."
    show alex smile

    z down frowntalk "Oh, acting like an idiot happens to the best of us? What does that make Finn? A dumbass?"
    show zaina frown

    a up frowntalk "You're the one that said it, not me."
    show alex frown

    z up frowntalk "I did. And I'll say it to his face, too. Only a dumbass would do something as stupid as get himself hurt every week."
    show zaina frown

    an "Her words are harsh, but I see the way her eyes grow fond at talk of him. Her harshness clearly comes from a place of worry."

    z down frowntalk "Anyway, sorry to make you do this. One Finn is enough." 
    show zaina frown

    an "I shake my head as I finish wrapping the gauze around her hand."

    a unsure frowntalk "If you've done this before, then you know it's not a big deal." 

    a down frowntalk "Sorry you couldn't take photos today either."
    show alex frown

    z unsure frowntalk "Nah. It's for the best. I probably would've fallen to my death if I tried that stunt." 

    z up frowntalk "Let's keep this between you and me, though. Finn would never let me live it down if he found out."
    show zaina frown

    an "She's done her best to hide it, but Zaina's actually {i}embarrassed{/i}. I didn't think that was possible for her."

    ##alex playful grin
    a talk "Or maybe it could bring you two closer. You guys can compare battle scars." 
    show alex smile

    z down talk "I take it back. I'm not sorry at all."
    show zaina smile

    hide alex
    hide zaina
    with dissolve

    an "Zaina takes off in a brisk step to meet up with the others, forcing me to chase after her with laughter on my lips."

    jump Scene13



label Scene13:
    ## Scene 13

    ##probably you're gonna wanna black bg each scene once they get to the roof
    scene bg hospital
    with fadee
    
    an "So we're at a hospital again."
    an "As much as I'm enjoying exploring these places, I think I'll be satisfied if I never see another hospital."
    an "The first one I went to was exciting because I'd never done anything like it before."
    an "The last one was fun because I was exploring it with everyone else."
    an "This one..."

    show finn up smile:
        xalign -0.05
        yalign 1.0
    show zaina up smile:
        xalign 0.67
        yalign -2.2
    show alex unsure smile backpack behind zaina:
        xalign 0.37
        yalign 2.3
    show paxton up smile hat:
        xalign 1.05
        yalign 1.0
    with dissolve

    an "Well, I already know what I want to do."
    an "I don't need to see the inside of this one again, but since it's such a tall building..."

    ##choice
    menu:
        "Hey, Paxton...":
            a unsure talk "Do you want to go up to the roof with me?"
            show alex smile
            p unsure talk "The roof? I'd love to."
            show paxton smile
            ##end choice (+1 to Paxton Go to Scene 13A)
            $ paxton_stat += 1
            hide alex
            hide paxton
            hide finn
            hide zaina
            with dissolve
            jump Scene13A
        "Hey, Finn.":
            f unsure frowntalk "What's on your mind?"
            show finn frown
            a unsure talk "Want to go up to the roof with me?"
            show alex smile
            ##end choice (+1 to Finn Go to Scene 13B)
            $ finn_stat += 1
            jump Scene13B
        "Hey Zaina.":
            a unsure talk "Have you been to the roof here before?"
            show alex smile
            z unsure talk "I have. Do you wanna go see it?"
            show zaina smile
            a up talk "Yeah!"
            show alex smile
            ##end choice (+1 to Zaina Go to Scene 13C)
            $ zaina_stat += 1
            hide alex
            hide paxton
            hide finn
            hide zaina
            with dissolve
            jump Scene13C

label Scene13A:
    ##Scene 13A
    scene black
    with fade

    scene bg hospital
    with sidefade

    an "Before I can suggest we find the stairs to the roof together, Paxton is ahead of me. He seems to know right where he's going, and honestly, his excitement is pretty cute..."

    an "I follow after him, picking up the pace a bit."

    an "But regardless, he arrives first."

    show paxton up smile hat at closeleft
    with dissolve

    p up talk "After you."
    show paxton smile

    an "He holds the door open for me, bowing a bit in the process."

    show alex up smile backpack at closeright:
        yalign -0.4
    with dissolve

    a up talk "Why thank you!"
    show alex smile

    an "He's cute—I keep being surprised by it, but he's really charming..." 

    an "The air is cool and crisp, but not too cold."

    p unsure talk "You want a good view, right?"
    show paxton smile

    a unsure talk "Yeah—that's why I wanted to come up here."

    a down talk "The photos that get posted are so pretty..." 

    a up talk "I wanted to see what it was like in person."
    show alex smile

    p down talk "Let's see, then..." 
    show paxton smile

    an "He looks around a bit and seems to settle on a spot near the edge."

    an "Curiously, I watch as he takes off his backpack..."

    an "... and dumps everything on the ground?!"

    a unsure talk "Uhm... Paxton?"
    show alex smile

    p up talk "Here! The roof is pretty dirty."
    show paxton smile

    an "He lays his backpack on the roof and gestures for me to take a seat."

    a down talk "Oh, um, thank you."

    an smile "He's so sweet..."

    an unsure "Sitting next to him, I gaze out over the city and its sea of lights..."

    an "It's {i}incredible{/i}."

    p unsure talk "Enjoying yourself?"
    show paxton smile

    a up talk "Yeah! It's so pretty... everything looks like ants from up here."
    show alex smile

    an "Paxton laughs easily before falling quiet again, his eyes passing over the city."

    p down talk "Do you recognize anything from up here?"
    show paxton smile

    a unsure talk "Um... not really. I'm not really all that familiar with the city, honestly."
    show alex smile

    a up talk "I'm just here for college."
    show alex smile

    a unsure talk "Did you grow up here?"
    show alex smile

    p up talk "I did, yeah."
    show paxton smile

    p unsure talk "Do you see that over there?"
    show paxton smile

    an down frown "I squint into the distance."

    p up talk "The baseball field."
    show paxton smile

    a unsure talk "I think so, yeah."

    a up talk "What about it?"
    show alex smile

    p unsure talk "I went there a lot when I was a kid."

    p up talk "My dad was {i}super{/i} into baseball. He did sports journalism."

    p unsure talk "So I saw a lot of games as a kid."

    p down talk "When this stadium opened up, there was a press conference about it."

    p unsure talk "I was just a kid, but my dad took me, since he was there to write an article about it."
    show paxton smile

    an "He pauses, a smile on his lips."

    a unsure talk "Yeah?"
    show alex smile

    an "I'm curious about where he's going with this..."

    p down talk "The owner was a bit of an older dude, and it was a windy day."
    show paxton smile

    p unsure frowntalk "And... well..."

    p up frowntalk "Turns out he had a toupee."
    show paxton frown

    a down frowntalk "Oh no."
    show alex frown

    p unsure frowntalk "And it wasn't very well secured."
    show paxton frown

    an up shock "I put my hands over my mouth. I can see where this is going..."

    p down talk "So it blew off and, well."
    show paxton smile

    an smile "He's stifling laughter now, with mixed success."

    p up talk "It hit my dad in the face."
    show paxton smile

    a unsure talk "No! Oh my God..."
    show alex smile

    p unsure talk "So every time I see the stadium, I remember that."

    p down talk "I don't think I'll ever witness something as funny or embarrassing for the rest of my life."
    show paxton smile

    an "I'm trying to stifle my own laughter now at the visual of all this."

    a down talk "That-That {i}is{/i} a really high bar, isn't it."
    show alex smile

    show paxton up talk
    p blush "It sure is..."
    show paxton smile

    an up "We both laugh a little more about it before managing to catch our breath."

    an "His cheeks are flushed, and I can't tell if it's from the wind or from laughing so much."

    an "But it's a cute look on him."

    hide alex
    hide paxton
    with dissolve
    jump Scene14

label Scene13B:
    ## Scene 13B
    f up frowntalk "H-huh? Me?"
    show finn frown

    a talk "Yeah! You don't want to?"
    show alex smile

    ##Finn blush
    show finn unsure frowntalk
    f blush side "... I didn't say that."
    f -blush -side up "But sure."
    show finn smile

    hide alex
    hide paxton
    hide finn
    hide zaina
    with dissolve

    scene black
    with fade

    scene bg hospital
    with sidefade

    an "Finn lets me take the lead to the roof, which is a nice change of pace. I feel a bit giddy about the whole situation."

    an "Though it doesn't escape my notice that he keeps looking past me."

    show alex up smile backpack at closeright:
        yalign -0.4
    show finn up smile at closeleft
    with dissolve

    a unsure talk "Hey, Finn. What are you looking at?"
    show alex smile

    f down talk "Nothing."
    show finn smile

    an "Yeah, right. The staircase to the roof is pretty sturdy and it boosts my confidence when I see the door knob approaching."

    f up talk "Watch the last step."
    show finn smile

    an down "I squint and see it—the last step has a slightly different color. I gingerly step on it but it doesn't budge."

    a unsure talk "It's safe. Haha, is that what you were watching for? You were worried?"
    show alex smile

    f unsure talk "{i}Definitely{/i} didn't say that."
    show finn smile

    an "Finn pouts and snaps his head away from my gaze. What's he so embarrassed about anyway?"

    an "I don't let it distract me for too long before I carefully push the door and step onto the roof."

    a up shock "Wow..."

    an smile "It's better than I thought it'd be. The stars are brilliant above, but so is the city below. It glitters beautifully, just like the sky, in a sea of swirling navies and golds."

    an "If one is merely reflecting the other, part of me wonders which is the original."

    an "Finn comes up behind me, but he looks far less impressed."

    f down talk "No danger whatsoever."
    show finn smile

    a unsure talk "Finn... {i}that's{/i} what you're looking for?"

    an smile "I don't know whether to laugh or cry, and Finn chuckles when he sees my expression."

    f unsure frowntalk "The view is... just okay."
    show finn frown

    ##Alex frown
    a unsure frowntalk "Just okay?"

    an frown "I don't know why I'm so desperate to show him, but I wave my hand enthusiastically toward the sea to get him to look again."

    a up talk "It's beautiful, Finn. We can see everything from here!"

    an smile "I hesitate and pull my hand back, feeling as if the 'sea' was real and I caused a ripple across it. It must've been the wind."

    f down frowntalk "It's just a bunch of lights."
    show finn frown

    a down frowntalk "It is {i}not.{/i} L-look! Over there."

    an frown "I point to the left of the roof."

    a unsure talk "See? If you really look you can see there's so many different colors, there's even a range of the whites and yellows. Some are big and some are small. Isn't it beautiful?"

    a up talk "So many different lives at home, so many families having dinner, or maybe they're stuck late at work, or maybe they're on dates..."

    ##Finn smile
    ##I think the flow of the scene works best if this expression isn't accompanied by his own dialogue
    f unsure smile "..."

    a unsure talk "And there? See straight head?"

    an smile "Maybe he's not convinced yet, but I can show him!"

    a down talk "There's a giant light right in the center. But it's probably just an apartment or something, you know? Or maybe it's a party or a gathering... And we can see it all from here, it's incredible."
    show alex smile

    f down talk "Could be a fire."
    show finn smile

    a up talk "O-or a {i}bonfire{/i}!"

    show finn up
    an smile "Finn laughs at my counter suggestion, which just fires me up even more."

    a unsure talk "And—um—it's all relaxing. You can sit back and realize you're not alone in the world, you know? The sky looks so beautiful and vast..."

    ##Alex smile
    a up talk "...and so does the city. Except these lights are lives, so while the stars sometimes feel too far away, we know these city ones are right here with us."
    show alex smile

    f unsure talk "...so optimistic. You're just like him."
    show finn smile

    a unsure frowntalk "Er, what? Sorry, I'm not sure I caught that."
    show alex frown

    an "'You're just like him?' Did I hear that right? What does he mean by that?"
    
    ##Vibration
    a up shock "Ah!" with vpunch

    f down frowntalk "Hey, now..."
    show finn frown

    an "Finn rushes to my side, helping steady me with a strong grip around my waist."

    a unsure frowntalk sweat "I'm alright, I just tripped a little."
    show alex frown

    f unsure frowntalk "You need to be careful up here. You could fall."
    show finn frown

    a down talk "Y-yeah, noted."
    show alex smile -sweat

    show finn smile
    an "He stares at me a little longer before nodding and gently letting me go."

    an "He's not touching me anymore, but the warmth of Finn's hands still makes me feel..."

    ##Alex blush
    show alex unsure talk
    a blush "Um. So what were you saying?"
    show alex smile

    f up talk "... that you've convinced me."
    show finn smile

    a up talk "Really?"
    show alex smile

    f unsure talk "Sure. The roof is fine, so... will you sit with me?"
    show finn smile

    ##Alex smile
    show alex unsure talk
    a -blush "You want to stay?"
    show alex smile

    an "I knew he'd see how beautiful this view was!"

    an "Finn plops down and pats the spot next to him."

    f up talk "We can stay a little longer if you want as long as you stay away from the edge."
    show finn smile

    a up talk "Haha. That won't be a problem."

    an smile "I carefully sit down and stare at the gorgeous sight."

    a down talk "It's so great that we can see the sky clearly at all with pollution these days. It's a great night."
    show alex smile

    f unsure smile "..."

    a unsure talk "Finn?"
    show alex smile

    f up talk "Yeah. It's a beautiful night."
    show finn smile

    an "I peek over to see him smiling, the stars—or perhaps the city lights—reflecting in his eyes."

    an "It takes my breath away."

    f unsure talk "You know... if you like the stars so much, there are plenty of other rooftops to see them from."
    show finn smile

    a down talk "Are you offering to take me?"

    an smile "He turns his head to look at me, still smiling."

    f up talk "I am."
    show finn smile

    a unsure talk "Perhaps I'll take you up on that."

    a up talk "I'm glad I've convinced you to enjoy the view."
    show alex smile

    f unsure talk "The view is still just average."
    show finn smile

    a down frowntalk "Hey!"

    an smile "He laughs and lays back on the roof, using his arms as a headrest."

    f up talk "In comparison to the others I could show you, I mean."
    show finn smile

    a unsure talk "Oh... you could've said that in the first place, you know."
    show alex smile

    f unsure talk "But what would be the fun in that?"
    show finn smile

    an "I sigh and find myself deciding to lay down next to him. If the occasional gust of wind didn't pass by, I feel like I'd be able to sleep here."

    a down talk "This is comfortable. A bit chilly, though, after a while."
    show alex smile

    f down talk "Mhmm. Here."
    show finn smile

    an "He scoots himself next to me until our bodies touch. I'm instantly warmer, both from his body heat and his kindness."

    show alex up talk 
    a blush "Oh. T-Thank you."
    show alex smile

    f up smile "Mhmm."

    hide finn
    hide alex
    with dissolve

    scene black
    with dissolve

    an "Maybe Finn means what he said about better views because he's no longer looking, just staring at the same spot in the sky as if it holds a secret."

    an "He looks so peaceful..."

    an "I try not to laugh, seeing how his hair seems to blend in with the dark of the night and his jewelry glistens like stars of their own."

    an "I keep my musings to myself, wondering how any view could be better than this one right now."

    jump Scene14

label Scene13C:
    ## Scene 13C
    scene black
    with fadee

    scene bg hospital
    with sidefade

    show alex up smile backpack at closeright:
        yalign -0.4
    show zaina up smile at closeleft:
        xalign 0.15
        yalign -0.15
    with dissolve

    z unsure talk "Before you get any ideas, I was already planning on heading up to the roof. With or without you."
    show zaina smile

    ##alex smile
    a down talk "I wouldn't think of it."

    an smile "So she wants to go to the roof just as much as I do. Guess we were both left wanting after our last trip."

    an "Zaina waits for me to fall into step with her and then we set off—in no rush, just like last time. I think we both want for that to be the only thing that's the same, as we're careful not to jinx it by hurrying over there too soon."

    an "I glance at her right hand. It's covered by the sleeve of her jacket."

    a unsure talk "How's your hand?"
    show alex smile

    z unsure talk "Better."
    show zaina smile

    an "She lifts her hand up and pulls down her sleeve."

    z up talk "It was hard to wrap it with my left hand, but I managed."
    show zaina smile

    an "Sure enough, the bandaging looks like it was done more than once, like she couldn't quite get it the first time."

    an "But otherwise, it looks pretty good."

    z down talk "Washing my hands is a bitch, though."
    show zaina smile

    ##alex laugh
    a up talk "If it wasn't, I'd suspect you'd have super healing powers."
    show alex smile

    ##zaina playful smile
    z unsure talk "How'd you know I wasn't just trying not to blow my cover?"
    show zaina smile

    a unsure talk "Is that what you get up to in your spare time?"
    show alex smile

    z up talk "Maybe."
    show zaina smile

    an "Her smile turns coy as she bumps my shoulders."

    z down talk "Well, since you figured it out, I guess I can let you know I'm looking for a sidekick."
    show zaina smile

    an "I hem and haw, putting on the airs of somebody who's not quite convinced by her offer."

    a down talk "I don't know... spandex isn't really my thing."

    an smile "Something in my words gives her pause and I glance at Zaina to find her studying me with a hand stroking her chin."

    an "Her examination of me is clearly exaggerated, but nonetheless, I feel my mouth grow dry at the way she looks me up and down, not once, not twice, but {i}three{/i} times."

    an "I might've felt self-conscious if not for the lazy smile quirking her lips."

    z unsure talk "No, I think you can pull it off."
    show zaina smile

    an "I try not to think about the way her gaze lingers and clear my throat, jumping at the lifeline offered to me by the door to the roof."

    an "Our hands both hover at the handle, neither of us quite ready to attempt to try the door just yet."

    a unsure talk "What will you do if it's locked this time too?"
    show alex smile

    z up talk "What will {i}we{/i} do."
    show zaina smile

    an "Somehow, that distinction warms my heart more than I ever thought it could."

    z unsure talk "And I dunno."

    z down talk "Definitely won't be climbing out of any windows any time soon."
    show zaina smile

    a down talk "It's too bad you don't have laser vision as your superpower."
    show alex smile

    ##zaina laugh
    z unsure talk "Right? Healing is so useless."
    show zaina smile

    an "The two of us share a laugh and content that we'll at least have each other's company, we grasp the handle together and turn it."

    an "I hear the mechanism click."

    an "The door opens."

    an "We grin triumphantly at each other. We're probably way too happy over a door opening, but I can't bring myself to care."

    an "The cold doesn't have its usual bite when we exit to the roof, though maybe that's the joy talking. Instead, the wind that whips past is comforting, much like a mother's embrace."

    an "It caresses my cheeks, turning them apple red, and when I turn to Zaina, I marvel at the way the wind lightly tousles her hair."

    a unsure talk "Good?"
    show alex smile

    z up talk "{i}Better{/i}."

    z unsure talk "Injuring myself and waiting a couple days might've been worth it for this view."
    show zaina smile

    an "It's an embellishment, of course, but I sort of see what she means. The twinkling lights of the city below are ordinarily no match for the stars when they're visible, but tonight it appears as though they're working in tandem."

    an "The shine of one matches the other, enveloping the city in a blanket of lights."

    an "And it's not just the city, either."

    an "I turn to Zaina, where the stars reflect in her eyes and the city lights illuminate her face."

    an "It's a sight that will surely stick with me, even without the use of a camera."

    an "But Zaina can't quite resist the pull, not that I blame her. I'm tempted to sneak a quick candid picture of her myself, but she's already moving before I have the chance to make up my mind, pulling a tripod out of her bag."

    an "She sets it up so fast that I blink and miss it."

    ##zaina smile
    z down talk "Yup."

    z up talk "Definitely worth it."
    show zaina smile

    a up talk "Yeah."

    an smile "Though I'm talking about a different view altogether..."

    an "For a few minutes, I'm content to just watch, settling down on the ground while Zaina does her thing."

    an "'Does her thing' doesn't quite do it justice though, because the smile that lingers on her lips as she takes pictures lights her face up in a way that no city light or star in the sky can."

    an "It's honestly... {i}breathtaking{/i}."

    an "Eventually though, my legs begin to cramp and I'm suddenly reminded of the fact that we {i}are{/i} outside, and I didn't exactly dress in anticipation for it. My jacket is light and does little to prevent the chill that rises now that it's later in the evening."

    an "The adrenaline from discovering that the door to the roof was unlocked also subsides."

    an "None of this seems to deter Zaina, though, who isn't dressed much better than I am."

    an "But I'd be surprised if she feels the cold at all."

    a unsure frowntalk "Zaina?"
    show alex frown

    z unsure frown "Hm...?"

    an "She clearly hears me, but everything else apart from her camera and the view is secondary."

    a down talk "Could you maybe, um, put down the camera?"

    an smile "Now {i}this{/i} gets her attention."

    an "She steps from behind the tripod and fixes me with a look that I'm not quite sure what to make of. Annoyed? Curious? Contemplative, maybe?"

    z down frowntalk "I can't exactly 'put it down.' It's attached to my tripod." 
    show zaina frown

    an "That settles my nerves a little. If she's making jokes, she must not be mad like I thought she was."

    an "Evidently, she's receptive enough to the idea to consider it."

    a unsure frowntalk "I just meant, um..."

    a down frowntalk "I don't know..."

    an smile "I'm suddenly finding everywhere and everything absolutely interesting, except, that is, her eyes."

    z unsure frowntalk "Hey."

    z up frowntalk "Look at me when you're making a request like that."
    show zaina frown

    an "I force myself to do so, cringing when our eyes finally meet."

    show zaina smile
    an "But to my surprise, the smile that's quirking her lips is an amused one." 

    ##zaina smile

    an "Or it would be, if it didn't turn into a smirk immediately after."

    ##zaina smirk

    z unsure talk "You were saying?"
    show zaina smile

    an "I pout, which only gets me a laugh for my troubles."

    an "She's really making me say it again..."

    a unsure talk "I was just saying that, um, it would be nice if we, you know, were just present in the moment."

    a down talk "With no cameras or anything."

    an smile "I'm aware of how much that makes me sound like a sixty year old, but I can't take it back now. All I can do now is own it."

    an "It's difficult to, what with Zaina's gaze penetrating through my soul, but I steel myself to not look away from her anyway." 

    an "I'm mostly successful."

    z unsure frowntalk "It's not like I'm on my phone or anything."

    z down frowntalk "It's completely different."
    show zaina frown

    an "My stomach churns and I feel a little silly for bringing it up now. I immediately backtrack."

    a down frowntalk "Sorry—"

    an frown "She clicks her tongue."

    z unsure frowntalk "You didn't let me finish."
    show zaina frown

    an "I open my mouth to apologize again, but I shut it at the look Zaina shoots me."

    z down frowntalk "It's completely different, but..."
    show zaina frown

    an "{i}But{/i}?"

    z up talk "But I guess I can be 'present in the moment.'"

    z unsure talk "Can't be too different from hanging out with my grandma, right?"
    show zaina smile

    an "She grins while unattaching her camera and folding up her tripod, and I groan, convinced she'll never let me live it down."

    an "But, well..."

    an smile "With her grinning like that, a life spent getting teased by Zaina couldn't be {i}too{/i} bad."

    an "In fact, as she settles down beside me, arm around my shoulder to keep us both warm, I'd say I'd be lucky to have her in my life for nearly half as long."

    a unsure talk "What were you taking pictures of?"

    an smile "I can't say I wasn't curious as to what could've kept her attention for so long."

    z down talk "A little of this, a little of that."
    show zaina smile

    an frown "I pout, again, and she must feel sorry for me because she decides to throw me a bone."

    an "Not before laughing first, though."

    z up talk "Mostly constellations."

    z down talk "They're really clear tonight." 
    show zaina smile

    an smile "I look up. I don't know much about constellations except the Big Dipper and I don't see that one now."

    an "I squint to see if it'd help any, but it doesn't."

    an "The stars, while visible and very pretty, are all indistinguishable to me."

    an "I was never one to stargaze anyway. My parents made sure I put my time to better use."

    an "So while I could probably name a lot of them, I was as good as lost trying to find them in the sky."

    z unsure talk "You can't see them, can you?"
    show zaina smile

    an "I shake my head."

    z down talk "Probably 'cause we don't have a telescope or binoculars."

    z up talk "I could see them through my camera, at least."

    z down talk "But, see, that one there..."
    show zaina smile

    an "Zaina traces a pattern in the sky and I follow it with my eyes."

    z unsure talk "Doesn't it look like Finn's ass?"
    show zaina smile

    ##alex laugh

    a unsure talk "What—what does that even look like?"
    show alex smile

    z down talk "{i}Flat{/i}."
    show zaina smile

    an up "Any hope I have of stifling my laughter goes out the window. My shoulders shake despite my best attempts and when I reach out to point out something in the sky, it's difficult to keep my finger still."

    a unsure talk "That one there looks like Paxton's hat."

    an smile "She tilts her head and traces the pattern I pointed out with a finger."

    z up talk "{i}Nice{/i}."

    z unsure talk "Oh, look at that one—"
    show zaina smile

    hide alex
    hide zaina
    with dissolve

    scene black
    with fadee

    an "We continue on like that for a while."
    an "It's hard to keep track of all the constellations we make up, but by the end of it, Zaina's in a good enough mood that when I ask her if she'll teach me how to take photos, she says maybe instead of refusing outright."

    an "That possibility means more than I could ever say, especially when it comes from someone like Zaina, who says no like it's a hobby."

    an "I go home that day with promises of maybes in my heart and go to sleep with dreams of girls with stars in their eyes."


    jump Scene14

label Scene14:

    stop music fadeout 2

    if finn_stat >= 2:
        jump finnroute
    elif paxton_stat >= 2:
        jump paxtonroute
    elif zaina_stat >= 2:
        jump zainaroute
    else:
        jump finnroute


    return