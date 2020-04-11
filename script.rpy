# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Alex", color="#ffff66", image="alex")
define an = Character("Alex", color="#ffff66", image="alex")
define question = Character("???", color="#ffffff")
define Police = Character("Police", color="#ffffff")
define f = Character("Finn", color="##bd8be7", image="finn")
define Bio = Character(" ", color="#ffffff")
define c1 = Character("Classmate1", color="#ffffff")
define c2 = Character("Classmate2", color="#ffffff")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene alex apartment

    $ persistent.CG1_unlocked = True
    $ persistent.CG2_unlocked = True
    $ persistent.CG3_unlocked = True
    $ persistent.CG4_unlocked = True
    $ persistent.CG5_unlocked = True

    $ persistent.PA1_unlocked = True
    $ persistent.PA2_unlocked = True
    $ persistent.PA3_unlocked = True
    $ persistent.PA4_unlocked = True
    $ persistent.PA5_unlocked = True
    $ persistent.PA6_unlocked = True
    $ persistent.PA7_unlocked = True

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    show Alex:
        xalign 0.5

    #play sound phonebuzz.ogg

    a "Nn…"

    an "Phone… phone… where’d I stick it…"

    an "I sit up, rubbing the sleep from my eyes. It’s too early for this."

    a "Where did you go… aha!"

    an "Grabbing my phone from the floor, I pull it off the charger and punch in my passcode. I don’t even have to unlock it to know what these texts are, no one texts me in the first place, but even if they did it would never be {i}this{/i} early."

    an "Another text pops up across the top of my screen as my phone vibrates in my hand, and I tap it, opening streams of texts from both of my parents."

    an "It’s the usual things that I don’t want to answer. What are my grades, how many classes am I taking… There’s only one right answer, and it isn’t the truth."

    an "Though even the right answer isn’t the answer they want. Not that I’ve ever managed to figure out what exactly that is."

    an "But I can’t keep dodging their questions like I have been… I mean, I can, but it’s going to get me in trouble."

    an "... which feels a little pathetic."

    an "I’m an adult now, aren’t I? Or I’m supposed to be, though I don’t feel like one."

    an "But it’s not like I’ve ever been treated like one either."

    an "I send back a quick ‘good morning,’ hoping that gets them to stop for just a minute so I can backread and make sure I’m not missing anything that they’ll complain about later."

    an "I don’t see anything new, so I start tapping out a reply to them. Twelve measly credit hours, and no, I don’t know my grades. I won’t know them until midterms and finals."

    an "I’m not sure if it’s a blessing or a curse that my professors won’t update grades on a more frequent basis. On one hand, I’m not obsessing from week to week. On the other, I have no idea from week to week."

    an "I add in a final note that I’m going to be in classes all day, and that I love them, before muting my text notifications."

    an "I put my phone face down on the bed for the moment, getting up for the day. It’s before my alarm would’ve gone off, but I might as well get out of bed."

    an "I can get some more studying in, maybe."

    an "Something so I don’t feel like twelve hours of classes isn’t enough."

    scene classroom
    show Alex:
        xalign 0.5

    c1 "Oh, oh! They posted a new story to their Instagram!"

    an "There are way, way too many terms for all the things in the human body…"

    an "I’m pretty good at memorization, but this is too much. I can feel my eyes glazing over... "

    c2 "Where is this?"

    c1 "Looks like an old house, maybe?"

    c2 "Yeah, but {i}where{/i}?"

    an "Why do they have to talk about this now? It’s so distracting…"

    an "I guess it’s my fault for finding it interesting enough to {i}be{/i} distracted."

    c1 "Hmm… well, it’s not on campus..."

    c2 "No shit, Sherlock. If we had any abandoned churches on campus, people would’ve had a drunken party in it by now."

    an "It’s not something I could do—exploring abandoned buildings like these people do. If my parents didn’t kill me, I think I would probably get myself hurt, and {i}then{/i} my parents would kill me."

    an "So the same end result. It’s reckless and stupid."

    c1 "Do you want to see if we can find it after class?"

    c2 "I feel like it’s bad to talk about that right this minute..."

    an "I don’t have time, anyway. These muscle terms aren’t gonna memorize themselves."

    an "Class starts in about ten minutes… I’ll focus on this until then."

    an "..."

    an "..."

    an "..."

    an "The stool squeaks across the floor, snapping me out of my concentration."

    ##Finn appears! Should have a relaxed smile.

    show Alex:
        xalign 0.8

    show Finn smile:
        xalign 0.2

    question "Hey."

    a talk "You’re early."

    an smile "Usually he slides in right before the professor shuts the door."

    f talk "Oh, I haven’t been to sleep yet."

    show Finn smile:
        xalign 0.2

    an "I look at my watch."

    a talk "... how long have you been awake?"

    f talk "Uhh, about twenty-two hours now, maybe? I’ll sleep after this. I didn’t wanna miss."

    show Finn smile:
        xalign 0.2

    an smile "I don’t really know what to do with this information… is he telling me he usually oversleeps, and that’s why he’s almost late to class? Why was he up all night?"

    an "I don’t have a chance to inquire before the professor shows up, though, so I decide I’ll take notes for him—he’s pretty nice. I like him."

    an "Usually, having to have a partner or do any kind of group work is my least favorite thing. {i}Usually{/i}, my partners never do their part, or they do it so badly I end up redoing it anyway."

    an "Finn isn’t bad, though. He keeps up on the material for the most part, and he’s easy to get along with."

    an "He’s only a little strange… I can’t imagine having a wardrobe full of nothing but black clothes, but I’ve never seen him wear a {i}color{/i}."

    an "Honestly, I wouldn’t have paid him much attention if we hadn’t ended up accidental lab partners, but I can’t say I have any complaints."

    an "I steal a glance at him as the professor begins his lecture and Finn looks like he’s already fading."

    an "I think he might’ve been better off skipping class."

    an "Not that I’ve never come to class on too little sleep—I don’t think I have the capacity to skip class."

    an "I hate that my stomach drops at the thought alone…"

    an "I hate the thought of looking at my phone later."

    an "..."

    an "..."

    an "..."

    an "Like I expected, Finn fell asleep a few minutes into class, and is still asleep, actually."

    an "I’m not sure if it’s that the professor didn’t notice or that he didn’t care… or maybe he did, and Finn’s going to get docked for it later."

    an "All the more reason I’m glad I took some extra-thorough notes."

    an "Though…"

    ##if we have it as an option, a cut in of a piece of notebook paper and some VERY sloppy handwriting/scribbles would be cute!

    an "This isn’t quite legible yet."

    an "I give him a careful shake, hoping that isn’t rude. I feel like it would be worse to not wake him up, though—he said he was sleeping after this, but he should do that in a bed."

    f talk "Mm…?"

    show Finn smile:
        xalign 0.2

    an "He vaguely stirs, and I find myself thinking that he’s kinda cute… long eyelashes, and what looks like some smudged eyeliner."

    an "I don’t think it occured to me before college that guys would wear makeup willingly, but he does, and it looks nice."

    an "... I shouldn’t be staring."

    an "I give him another shake and his eyes finally open. He sits up, blinking blearily and rubbing his face."

    f talk "That wasn’t supposed to happen. Ugh."

    show Finn smile:
        xalign 0.2

    a talk "Well, I took notes for you, so it could be worse."

    a "Though I’ll probably need to rewrite them for you."

    an smile "I show him my notes, and he looks over them, blinking the sleep from his eyes before he starts laughing."

    f talk "I really appreciate the thought, but I think you’re right—is this even English?"

    show Finn smile:
        xalign 0.2

    a talk "It should be—it’s the only language I know."

    show Alex smile:
        xalign 0.8

    f talk "I’m not sure—maybe you unlocked something in your subconscious."

    show Finn smile:
        xalign 0.2

    an "I can’t help but laugh a little bit at that, tucking my notebook away."

    a talk "That’s absurd."

    a "I can type these up and email them to you, if that works."

    f talk "It does."

    f "I appreciate it."

    show Finn smile:
        xalign 0.2

    a talk "It’s not a problem! I was going to type them anyway."

    a "Anyway, I have another class to get to."

    a "See you!"

    hide finn with dissolve

    show Alex smile with move:
        xalign 0.5

    an "Checking my watch, I probably shouldn’t have dawdled."

    an "But more than that, I think I shouldn’t have scheduled my classes quite so close together…"

    scene alex apartment

    show Alex:
        xalign 0.5

    an "By the time I get back to my apartment, my phone has too many texts again. I really don’t want to read them."

    an "But I do, because what else am I gonna do? Ignore them? That’ll go over well, I’m sure."

    an "Reading over them properly, I feel pretty bad…"

    an "I should’ve kept up my course load and powered through it."

    an "Though it’s bold of them to think that I’m doing anything extracurricular or romantic."

    an "The last time I had a boyfriend, I think I was fourteen."

    an "I really don’t like it when they’re mad at me, though…"

    an "I take a breath and then type out an apology. I’ll make it up to them next term. They’re paying for my classes, so it’s the least I can do…"

    an "I don’t want to disappoint them."

    scene classroom

    show Alex smile:
        xalign 0.8

    show Finn smile:
        xalign 0.2


    an "Tonight, Finn looks much more awake than he did in class before."

    an "Which is good, because we need to get this lab report done, and I could do it myself, but I don’t particularly… want to…"

    an "Aside from that, this is one of my few chances to socialize at all! I like Finn well enough, and I’d like to get to know him better."

    an "He’s pretty reserved, though. Hmm… I don’t think I’ve ever heard him mention a hobby or anything that he’s into."

    an "We really only talk about stuff for class, which doesn’t say much about anyone."

    an "I feel like I’ve forgotten how to talk to people, though… how {i}do{/i} you talk to someone about something that isn’t schoolwork? Uhm…"

    a talk "Do you have any plans after this?"

    an smile "That’s a start, I guess."

    an "Finn stops what he’s doing for a moment and shrugs."

    f talk "Nothing in particular. Do you? I thought all you did was study."

    show Finn smile:
        xalign 0.2

    a talk "Not all the time!"

    an smile "Just most of the time…"

    an "Part of me feels a little offended that he’s making fun of me, but he’s smiling, and I think maybe he doesn’t mean it in a mean way."

    an "Besides, it’s not like he’s wrong."

    an "Can’t get mad at the truth."

    a talk "I do other things…"

    show Alex smile:
        xalign 0.8

    f talk "Like?"

    show Finn smile:
        xalign 0.2

    a talk "I like to try my hand at music composition sometimes, on the computer… reading, too."

    a "Walks are nice if the weather’s good—I like walking around the part of town with all the old houses. They’re so much more interesting than anything built nowadays—they have a lot more personality to them."

    a "What about you?"

    an smile "He’s quiet for a long moment, finishing up the question we were working on before answering."

    f talk "I do a lot of outdoor stuff, I guess. I used to do rock wall climbing."

    show Finn smile:
        xalign 0.2

    an "... this is not what I expected from someone that looks like…"

## if we can just get a focus or a pan on Finn or something to emphasize her looking at him that would be great!
    show Finn with move:
        xalign 0.5

    show Alex with move:
        xalign 1.5

    an "This…"

    f talk "Is there a reason you’re staring?"

    show Finn smile with move:
        xalign 0.2

    show Alex with move:
        xalign 0.8

    a talk "Oh! Oh, I just… I didn’t take you as the type to do a lot of physical stuff."

## I need a smirk or something playful here on Finn’s face
    show Finn smile:
        xalign 0.2

    f talk "What did you expect? That I haunted campus, looking for my next victim?"

    show Finn smile:
        xalign 0.2

    a talk "No!"

    an smile "... not quite that dramatic, but that’s closer to what I was imagining…"

    a talk "I don’t know, maybe you like, stayed in more."

    an smile "He laughs and shakes his head."

    f talk "Nah, I like being outside."

    show Finn smile:
        xalign 0.2

    a talk "During the day?"

    show Alex smile:
        xalign 0.8

    f talk "Sure, but not without SPF-100 sunscreen."

    show Finn smile:
        xalign 0.2

    a talk "Oh."

    an smile "That explains how he can be an outdoorsy person and still be this pale."

    f talk "Do you know how to answer the next question?"

    show Finn smile:
        xalign 0.2

    a talk "Um… let’s see…"

    an smile "He doesn’t seem interested in telling me anything else, so we focus on getting the lab report done."

    an "It’s not the most exciting thing in the world, but it’s nice."

    an "... there’s something sad about how much stimulation I get out of doing this lab report with him."

    scene alex apartment

    show Alex:
        xalign 0.5

    #play sound phonebuzz.ogg

    an "It takes me a moment to realize what I’m hearing beyond the music from my headphones, my studying focus broken now."

    an "The screen on my phone says it’s Mom… I wonder what she wants."

    an "... it’s the same as always."

    an "Any time they ask me what I’m doing, it’s never because they want to know what I’m up to."

    an "I lean back in my chair and tap out a reply to them, letting them know I’m studying."

    an "Another text comes through and this one is a little different from usual…"

    an "What am I doing on the weekend… I don’t know yet."

    an "Is she worried about me?"

    an "Both my parents are always worried about me, technically, but… not in a way that feels particularly loving."

    an "I’ll tell her I don’t have plans… see where that gets me."

    an frown "The typing notification appears on my phone screen after I send it—"

    ##Alex annoyed/mad/exasperated/something

    a talk "‘I hope you blocked in time for studying.’"

    a "Really?"

    an frown "My hand hurts—"

    an "Shaking my head, I stop squeezing my phone in a death grip and turn it off."

    an "I don’t ever do enough, do I?"

    an "If it’s not studying, then there’s no point to anything that I do."

    an "They haven’t asked me about friends since I told them I didn’t have any, months ago."

    an "I don’t know what to do."

    an "I know they love me, but what does that even mean?"

    an "Do they care about {i}me{/i}, or do they just care about my success?"

    an "I can’t tell."

    an "I’ve never been able to."

    an "Turning off my phone, I drop it on the floor."

    an "They’re never going to be happy with me."

    scene classroom

    show Alex:
        xalign 0.5

    an "Shocking no one, least of all myself, I spent my weekend sleeping and studying."

    an "Not that I have anyone {i}to{/i} shock."

    an "But it’s fine! I’m going to do great on this test."

    an "And then… study some more?"

    an "..."

    an "It never ends…"

    c1 "Look! {i}Look!{/i}"

    an "In front of me, a couple of my classmates are excited about something."

    c2 "How did they get so high up?!"

    c1 "I don’t know! I think this is the old cathedral… you know, the one you pass on the highway if you’re coming in from the north side of campus?"

    c2 "No, that can’t be it. Roof’s the wrong color."

    c1 "Hrm…"

    c2 "I wonder who runs it… they’d have to be pretty fearless to get up on the roof, right?"

    c1 "Or stupid."

    c2 "Both?"

    c1 "Both."

    c2 "Probably someone on the football team or something like that… I watch these videos on YouTube, and it takes a ton of work to get up to some of these places."

    c1 "May—"

    a talk "Um, excuse me?"

    show Alex smile:
        xalign 0.5

    c1 "Huh? What is it?"

    an "This is the most impulsive thing I’ve done in who knows how long."

    an "I can feel myself losing my resolve already… but no. I won’t."

    a talk "What are, uh, you talking about exactly? With the old cathedral?"

    show Alex smile:
        xalign 0.5

    c2 "Oh, there’s some urbex group that goes to school here. They post a lot of photos and videos to their Instagram account."

    c1 "Yeah, see—like this."

    an "They show me a photo of a steeply inclined roof with dark shingles, barely visible in the darkness."

    an "The sky is a sea of stars…"

    an "Even just looking at a picture of it, I feel breathless."

    c1 "See? You get it! It’s cool, right? Super cool! Look at these..."

    an "They show me more of the photos, some of them in buildings that really don’t look safe, one that has a vague, partial shape of a person in it with a mask of some sort on."

    an "The caption on that one says ‘What’s with the spooky mask? For those of you watching at home, we’re in an old place with a potential asbestos problem, and I’d like to escape here with some cool pictures, not lung cancer, thanks."

    an "So this place was built… in the 1900s, probably? It was used in construction for a long time…"

    an "Each photo they show me feels like a frozen piece of time. Places with old medical files, places where nature has taken over again."

    an "It’s amazing."

    a talk "Yeah, wow. I’m definitely going to follow them..."

    an smile "The professor walks in then, so I quickly thank my classmates and go back to my desk, quickly searching up the account."

    an "I hit the follow button without thinking too hard about it, before reading their bio."

    ##Some kind of special formatting here?

    Bio "{i}Feeling adventurous? Come find us.{/i}"

    an "I feel jittery—excited?"

    an "My nerves are flooded with excited energy."

    an "For the first time, I barely focus on my notes, and I barely hear the homework assigned."

    an "I’m going to find these places."

    scene alex apartment

    show Alex:
        xalign 0.5

    an "I was good—I did some studying over the weekend. A little."

    an "Not much, though."

    an "Usually, that would stress me out."

    an "But right now? I can’t bring myself to care."

    an "I spent most of my time digging through the Instagram account of these urbex people, going all the way back to the first post to see if I could figure out where these pictures are from."

    an "There’s factories, an abandoned mall."

    an "An old theme park, a lot of old houses."

    an "Abandoned hospitals…"

    an "Some of the hospitals have old patient files, which I can’t help but wonder: is that a HIPAA violation?"

    an "I can’t stop thinking about this."

    an "I can’t think of a single time in my life that I’ve been this fixated on something."

    show Finn with dissolve:
        xalign 0.2

    show Alex with move:
        xalign 0.8

    f talk "Alex? Are you there?"

    an "I jump, startled back to my senses. Studying. I’m studying with Finn. Or I’m supposed to be, anyway…"

    a talk "S-Sorry! I spaced out."

    show Alex smile:
        xalign 0.8

    f talk "I think you went to another planet, maybe."

    show Finn smile:
        xalign 0.2

    a talk "Hahaha…"

    an smile "Crap. That’s embarrassing."

    an "I pull out my phone and pull up the account—I feel the need to justify myself. Maybe he’ll understand?"

    an "How can you see all this stuff and not be interested?"

    a talk "I was thinking about this—I have been all weekend."

    an smile "I show him the account, and he immediately stiffens."

    f frowntalk "That kind of thing seems pretty dangerous."

    a talk "Oh?"

    show Alex smile:
        xalign 0.8

    f frowntalk "I haven’t done it—some of the guys at the gym where I used to do wall climbing did. It’s fine to look, but… it’s dangerous."

    f "You shouldn’t try to do this kind of thing."

    show Finn frown:
        xalign 0.2

    an "Somehow, I feel like a deflated balloon."

    an "But only for a minute."

    a talk "I’m not going to do anything stupid. I like having a mystery to solve, so I want to find out what at least one of these places {i}is{/i} exactly."

    show Alex smile:
        xalign 0.8

    f frowntalk "You’ll get yourself killed."

    show Finn frown:
        xalign 0.2

    a talk "I will not—why do you care, anyway?"

    show Alex smile:
        xalign 0.8

    f frowntalk "I don’t know, logic tells me I should stop someone from running into abandoned buildings? Seems like a questionable life choice."

    f frowntalk "You’d be stupid to dig into it."

    show Finn frown:
        xalign 0.2

    an "I feel so tense—so agitated."

    an "I can take care of myself."

    an "I’m not a child, and I’m not stupid."

    an "But… we’re here to study. And I have been slacking on that."

    an "Taking a deep breath, I force myself to calm down."

    a talk "Sorry for bringing it up. We should get back to this, right?"

    show Alex smile:
        xalign 0.8

    f frowntalk "Uh… yeah."

    show Finn frown:
        xalign 0.2    

    an "The rest of the evening feels stiff—off and tense—but we get through it."

    an "Back home, there’s a nagging thought in the back of my head that I should study some more before I go to bed."

    an "But I don’t want to do that."

    an "I pull up the Instagram account, looking over the photos again."

    an "This one set they did is a hospital—I think, anyway. It looks like it’s only one floor, though… usually, they explore the whole building, so this must be the only level to this place…"

    an "Hrrm…"

    an "I grab my laptop and open up my browser. There can’t be that many abandoned hospitals, right?"

    an "In the end, there’s a couple of small psych wards nearish to here that were closed but not torn down."

    an "I’m feeling excited again—I want to go see these places…"

    scene black

    an "Ugh."

    an "Sitting in my car, the first location was a bust. There was a gate that was open, but the windows and the doors were all locked."

    an "This is risky, but I’m not gonna be {i}more{/i} reckless by trying to break and enter."

    an "This is illegal as is, but that would be {i}really{/i} illegal, and I really don’t want to get arrested."

    an "My parents would flip, but I might also get kicked out of school."

    an "If I get kicked out of school, then I have to go home."

    an "..."

    an "I’m not getting arrested."

    an "Because I’m not going to do anything stupid."

    an "..."

    an "Anything… stupid...er…"

    an "..."

    an "I’ll be fine."

    an "I punch in the next address on my phone. First location’s a bust, but I’m not giving up!"

    an "Not yet, anyway."

    an "The drive to the next site is pretty painless, boring."

    Phone "Your destination is on the left."

    an "I look to my left as I drive past, noticing the ‘NO TRESPASSING’ signs first."

    an "Maybe this {i}is{/i} a bad idea…"

    an "I change lanes, ready to get back on the highway and turn around. I feel kind of sad about it, though."

    an "I see a supermarket parking lot and flip on my turn signal, turning way too hard into the lot and earning myself an annoyed honk for braking out of nowhere."

    an "But really, whose fault is it that they were tailgating?"

    an "I pull into a parking spot and turn off my car. Pulling up the map on my phone, it’s only about a ten minute walk back to the site."

    an "I came all the way out here; I’m going to at least {i}look{/i}."

    an "I get out, grab my backpack and lock up my car."

    an "... and then I make double sure I locked it. It beeps at me, and I start my trek."

    an "..."

    an "..."

    an "..."

    an "Approaching the site, I notice the barbed wire wrapped around the top of this six foot tall fence."

    an "Maybe I won’t be able to get in?"

    an "Circling around, there’s no gate I can get through, but there {i}is{/i} a patch in the top of the fence where the wire is broken."

    an "Looking up at it, I try to remember the last time I climbed a fence. Maybe when I was a little kid?"

    an "But I never even really did anything adventurous then, either."

    an "I grab the chainlink, stick my foot in, and carefully pull myself up and on top of the fence."

    an "Take it slow… don’t get scratched…"

    an "If I have to get a tetanus shot and it runs through my parent's insurance, they’re going to know I was up to {i}something.{/i}"

    an "Very carefully, I get my feet under me and hop down."

    a "Ouch!"

    an "Note to self, don’t do that again. Ow."

    an "I wait for the pain in my feet to dissipate and then carefully stand up, walking over to the building."

    scene hospital
    ##I think the music should be really quiet here?
    an "I enter through the door at the back, wincing as it creaks."

    an "I step inside, letting the door close behind me. The floors are covered in dust and dirt, and I’ve never been somewhere so quiet."

    an "Even if I’m the only one here, it feels criminal to let my footsteps make noise."

    an "I approach the front of the building, spotting old, water-damaged posters on the wall for group activities."

    an "On the front desk, there’s files, old pens. A keyboard was left behind."

    an "You could almost believe this was ready for another day of work, another day of treating patients…"

    an "I take some pictures as I walk, careful not to disturb anything."

    an "I feel like time stopped here long ago, and I don’t belong as someone from the present."

    an "I walk down the next hallway, peeking into the rooms. There’s still beds in them, some made, some stripped. Stubby wooden pencils lay on top of ancient pads of paper."

    an "I wonder, when I become a nurse, if I’ll ever end up working somewhere like this."

    an "What I read online said this was a psych ward for adults."

    an "But so much of it feels childproofed."

    an "I understand why, but it’s strange nonetheless."

    an "... I don’t know if I {i}could{/i} work somewhere like this, actually."

    an "No one goes to a hospital because they want to, but {i}especially{/i} no one comes to a place like this because they want t—"

    question "Hey! Is someone here? This is the police!"

    an "Crap."

    an "Think think think—the rooms—the doors don’t have locks…"

    an "I quickly slip inside the closest room and carefully close the door as quietly as possible."

    an "Pulling off my backpack, I crawl under the bed and pull my backpack in, hugging it close to my body."

    an "I squeeze my eyes shut, heart thudding in my chest."

    an "I can’t get caught I can’t get caught I can’t get caught—"

    #play sound footsteps.ogg
    an "Footsteps…"

    Police "Hello? Is anyone here?"

    an "I feel like all the air has left my lungs."

    an "I’ve never been this scared in my life…"

    an "But I focus on listening as the footsteps continue and then fade into the distance."

    an "They get louder again, passing the room I’m in, until I hear the sound of the door at the front open and close."

    an "It’s quiet again."

    an "I crawl out from under the bed, standing and putting my backpack back on. I dust myself off, and this time, I’m much more careful about getting back out of here."

    scene hospital bg
    ##out of town bg? I feel like that was mentioned.

    an "Back in my car, I take a minute to just sit there and catch my breath before pulling out my phone and opening a DM to the account."

    an "There’s some texts from my parents waiting, but I’m not going to try to reply to those right now."

    an "Selecting the pictures, I send them all before locking my phone, tossing it on the passenger’s seat."

    an "It’s easy enough to get back home from here."



    # This ends the game.

    return
