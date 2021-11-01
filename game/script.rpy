# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define lib = Character("Liben", who_color="#228b22")
define stu = Character("Student")
define andy = Character("Andrew", who_color="#ff0000")
define jam = Character("James", who_color="#5f9ea0")
define joh = Character("John", who_color="#800080")
define col = Character("Cole", who_color="#ffff00")
define tac = Character("Tacoma", who_color="#0000ff")
define ash = Character("Ash", who_color="#0000ff")
define col2 = Character("Cole Clone", who_color="#ffff00")
define kid = Character("That Kid", who_color="#ffffff")

# Declare character stats.

# Your relationship points with Porf Tacoma before you build it up! :) :) :)
default tac_pts = 0
# You start with energy at 100 each day.
default energy = 100
define maxenergy = 100
default quiznumber = 0
default talknumber = 0
default quiz = True
default research = True
default day = 1
define days = ["day_0", "day_1", "day_2", "day_3", "day_4", "day_5", "day_6", "day_7",
               "day_8", "day_9", "day_10", "day_11", "day_12", "day_13", "day_14", "day_15"]

# Python stuff so minigame is an actual reading from class.
init python:
    import re
define file = open(renpy.loader.transfn("music/reading.txt"), 'r')
define reading_dirty = file.read()
define reading_clean = re.sub('\W', '', reading_dirty)
define reading_list = list(reading_clean)
default letter_counter = 0



# The game starts here.

label start:
    jump day_0

label day_0:

    $energy = min(energy + 70, maxenergy)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show stu_n
    show screen energybar

    # These display lines of dialogue.

    stu "what...which alarm is this"
    stu "...WAIT...WHAT TIME IS IT?"
    stu "IS IT ALREADY 8:30!?"
    stu "Shoot you're already late for the first day of school????"
    stu "This is NOT how you should be starting College."

    play music "music/Grow.mp3"

    show bg main quad with pixellate

    stu "(What a beautiful day to be late!)"
    stu "(It’s your first day at UKokoro, and in true style, you slept in!)"
    stu "(It took you a lot of effort to get into a school as prestigious as
        this one: and you are not going to let your laziness get in the way
        of the start of a new life!)"
    stu "(You’re supposed to be meeting your orientation leader, don’t keep
        him waiting!)"

    andy "HEY!"
    andy "STUDENT! It's ME!"

    stu "(A third-year in a leather jacket and beret calls to you from across the quad.)"

    show andy happy with moveinright
    andy "Student, there you are! Did you sleep in or something?"

    stu "Yeah..."
    stu "...it wasn't my fault though, i just..."
    stu "I was having a weird dream."

    show andy mad
    andy "Yeah, that happens when you drink too much."

    stu "I DIDN'T - "

    show andy happy
    andy "Just kidding!"

    show andy neutral
    stu "(This is Andrew)"
    stu "(a current third-year at UKokoro and my orientation leader)"
    stu "(He runs a fashion blog on campus and even designed for the fashion show last year)"
    stu "(but rather than going in to fashion, he studies economics…which I never understood...)"

    show andy neutral at left
    with move

    show liben happy
    with moveinright

    lib "OH MAN, IS THIS HER!?"
    lib "IS THIS YOUR SPECIAL FRIEND!?"

    show andy sad at left

    andy "Liben! Why would you say that, she’s just a freshman!"

    show liben thinking
    lib "Well is she a SPECIAL freshman?"

    show cole sad at right
    with moveinright

    col "Quit picking on her Liben, you’re just projecting!"

    show liben sad behind andy

    lib "Well...yeah. Yeah I am."

    show liben neutral:
        xalign 0
        yalign 1.0
    with move
    show andy neutral:
        xalign 0.6
        yalign 1.0
    with move

    andy "Sorry about that, these guys asked to tag along to meet you."
    andy "This is Liben."

    show liben happy at left

    lib "Pleasure to meet you! I’m Liben."
    show liben spicy at left

    lib "I’m an econ major and I live with Andy-kun."

    show andy mad

    andy "Unfortunately..."

    show andy neutral

    andy "...and this is Cole!"

    show cole neutral at right
    col "Nice to meet you! I'm Cole and I live everywhere!"

    stu "What does that mean?"

    show cole happy at right
    col "You'll find out!"

    stu "(...)"

    jam "ANDY!"

    show andy neutral
    andy "Oh, it looks like James set up a Juggling booth over there!"

    show andy happy
    andy "Let's go check it out!"

    hide andy neutral with moveoutright
    hide liben neutral with moveoutright
    hide cole neutral with moveoutright

    scene bg juggling
    with Dissolve(.5)

    pause .5

    scene bg juggling
    show andy happy
    with Dissolve(.5)

    andy "JAMES!"

    stu "(You walk over to a young-looking boy juggling plastic clubs.)"
    stu "(Even though you can read the stress on his face, he seems to be
        doing relatively well.)"

    show james neutral at left with moveinright
    andy "JAMES!"

    show james happy
    show andy neutral

    jam "Andy, are you thinking about joining my juggling club?"

    show andy happy

    andy "Ha ha maybe next year..."

    show andy mad
    andy "I've got too much to juggle already..."

    show james happy
    jam "Suit yourself!"

    stu "(The young boy catches all four clubs in his hands and takes a bow.
        Andy and co applaud.)"

    show liben mad at right with moveinright

    lib "THAT WAS SOOO COOL JAMES!!!!"

    jam "You should come to a juggling club meeting some day too."

    show liben spicy

    lib "Nah. I’m too busy tryna finesse my teachers."

    show cole mad:
        xalign 0.6
        yalign 1.0
    with moveinbottom

    col "Aren't we all?"

    show liben thinking:
        xalign 1.3
        yalign 1.0
    with move

    lib "Man, I don’t know what it is, but some of them are so hard to talk
        to."

    show cole sad
    col "...and some of them are just plain creepy..."

    show james neutral
    jam "Yeah, do you guys remember that one teacher who…"

    show andy neutral
    show andy:
        xalign 0.3
        yalign 1.0
    with move

    show andy mad

    andy "Guys..."

    stu "What teacher?"

    show liben thinking
    show cole mad
    show james mad

    show andy neutral

    andy "It’s not unusual for students at this school to try and pursue
        academic research."
    andy "A lot of the money our school makes goes directly into facilities
        for people to work."

    show andy mad with dissolve
    andy "A couple years ago, when I was a first year, this one professor and
        his student..."
    andy "Well... I suppose he wanted more from his student than just research
        assistance..."

    show cole sad
    col "...Creep..."

    show andy neutral
    andy "Since then, a lot of students have been kind of wary about how we
        approach professors."
    andy "We all want the research for our resumés, I guess, but I think
        talking up teachers like that."

    show andy mad
    andy "...It’s tough sometimes. And we’re not sure what to do..."

    show liben sad
    lib "Man, I wouldn’t even know where to start, especially with some of the
        profs here."

    show cole mad
    col "Me neither."

    show james neutral
    jam "Same."

    show john neutral
    show john:
        xalign 1.0
        yalign 1.0
    with moveinbottom

    joh "Me too."

    show james scared:
        xalign 0.0
        yalign 1.0

    show andy sad:
        xalign 0.2
        yalign 1.0

    show cole shook behind andy:
        xalign 0.4
        yalign 1.0

    show liben mad:
        xalign 0.6
        yalign 1.0


    andy "JOHN!? WHERE DID YOU COME FROM!?"
    joh "I’ve been here this whole time."

    show andy sad:
        xalign 0.8
        yalign 1.0
    with move

    show cole sad:
        xalign 0.5
        yalign 1.0
    with move

    show liben mad:
        xalign 0.1
        yalign 1.0
    with move

    show liben mad behind cole

    andy "s-student, this is John..."

    show john happy
    joh "...hey"

    andy "He's also a friend of our's."

    joh "yes"

    show liben neutral
    lib "Say John, have you found research yet?"

    joh "no"

    show liben thinking
    lib "Hm…"
    show liben happy
    lib "I KNOW!"
    show liben neutral
    lib "Let’s all swear now that the five of us will end the semester with a
        research position secured!"
    show liben thinking
    lib "Sure, individually, it might be tough for us to get a position,"
    show liben spicy
    lib "but with our constant support, I know we can do it!"

    show andy happy
    andy "Actually, that sounds like it could be fun, motivation from my
        friends might be exactly what I need to get going."

    show andy neutral
    show cole sad
    col "Couldn't hurt..."

    show james happy
    jam "I'm down!"

    show john happy
    joh "yes"

    show andy happy
    andy "What do you say Student?"
    andy "Are you in?"

    menu:
        "Let's do it!":
            jump choice_research_yes

        "I dunno about this...":
            jump choice_research_no

label choice_research_yes:

    joh "are you sure about that?? aren't we moving kinda fast?"
    jump choice_research_done

label choice_research_no:

    show liben mad
    lib "AW COME ON! IT WAS SUCH A GOOD IDEA!"
    jump choice_research_done

label choice_research_done:
    # ... the game continues here.

    show andy neutral
    show cole neutral
    show james neutral
    show john neutral
    show liben neutral

    joh "Guys, maybe we should give her some time to think."

    stu "I’ll think about it..."
    stu "...but I don’t want to do anything too preemptive, after all, it is
        only my first day of school..."

    show andy neutral
    andy "I guess you're right."

    show james happy
    jam "Hey, it’s almost time for us to get to the orientation party, Andy,
        we gotta go."

    show andy sad
    andy "Oh right!"

    hide andy happy with moveoutright
    andy "It was nice seeing you student, enjoy the rest of the orientation
        fair, but we need to go."

    hide james happy
    with moveoutright

    lib "Later!"
    hide liben spicy
    with moveoutright

    col "See you!"
    hide cole happy
    with moveoutright

    joh "goodbye Student!"
    show john happy
    joh "and good luck."
    hide john happy
    with moveoutright

    scene bg main quad
    with fade
    play music "music/moon shards.mp3"

    show stu_n

    stu "Man, first day of school and I’m already being overloaded with talk
        about research and professors..."
    stu "This school...there’s so much i didn’t know about it before going in."
    stu "I don’t even have a major yet, how am I supposed to figure out what
    kind of research I’m meant to do…?"
    stu "And I don’t know any of my professors and apparently some of them are
        creeps..."
    stu "...and honestly I’m not sure if this is the place for - "

    show stu_n with hpunch
    stu "(THUD)"
    stu "(owwwwwwwww)"

    play music "music/student.mp3"

    show tacoma sad with moveinbottom

    tac "owwwwwww"
    stu "Oh my gosh, I’m sorry, are you alright?"
    show tacoma happy
    tac "Haha yeah I’m fine, that was all on me, I couldn’t see you over my
    papers."
    stu "Here, let me help you out!"
    show tacoma neutral
    tac "OH, it’s no big deal!"
    show tacoma happy
    tac "Are you new here?"
    stu "Yeah. This is my first day...quite a school...so many interesting
    students."
    tac "Haha that is certainly true; I feel the same way!"
    stu "(He must be a new student too; I’ve never seen anyone with blue hair
        like that...)"
    tac "With all those smart kids, I suppose a lot of people must feel like
        small fish, huh?"
    stu "Small...fish?"
    show tacoma neutral
    tac "Like they’re in a big sea and they’re no longer the big fish they once
        were in high school."
    stu "Oh...it’s an interesting way of putting it, though I’m not even sure
    if I ever felt like a big fish…"
    show tacoma happy
    tac "Haha, and here it’s even harder because of all the hype around
        research."
    stu "(Oh, man...he’s feeling it too…)"
    stu "Yeah I know right..."
    stu "I haven’t even decided on a major yet, and I don’t even know if I’d
        consider doing research at a school like this..."
    stu "...Especially considering..."

    show tacoma sad
    tac "...Yeah...well...I’m sure not all the professors are like that here,
        and, well..."
    show tacoma happy
    tac "Having no major is actually kind of liberating when you think about
        it!"

    stu "WHAAAAT?"

    show tacoma neutral
    tac "In the weirdest way, having no path gives you the most freedom to look
        into doing anything and everything!"
    show tacoma happy
    tac "You’re not limited by any single path…"

    stu "Huh...I guess that is true..."

    tac "And y’know, maybe research would help you figure out which path makes
    you the happiest! They say that in helping someone else realize their
    dream, you may realize your own!"

    stu "Realizing..."
    stu "...dreams?"

    tac "Doing research is like helping with a group project where everyone has
        a role" #I really don't like this line.
    tac "and it’s in the combined investment and effort of the group where a
        project is realized!"
    tac "Everyone benefits, but only through the collective work of the team!"

    stu "(Like a group project...That makes it sound a lot more fun!)"

    show tacoma sad
    tac "Well I need to head out now; I need to get these flyers up, but it was
        nice meeting you!"

    stu "Nice to meet you too!"

    show tacoma neutral
    tac "Oh my gosh, and I never got your name."

    stu "Student."

    show tacoma happy
    tac "Nice to meet, you student! I’ll see you around!"

    stu "Bye."

    hide tacoma happy with moveoutleft

    stu "(Come to think of it; I never got his name…)"

    stu "(That kid did have a point though.)"
    stu "(Maybe I’m thinking about this all wrong.)"
    stu "(The whole point of research is to help someone out with their dream)"
    stu "(and maybe)"
    stu "(in helping them out with their dream)"
    stu "(I can figure out what mine is!)"
    stu "(...Maybe...)"
    stu "(Maybe I WILL take up Andy’s challenge.)"
    stu "Finding research to help someone else might end up helping me make up
        my mind about where I’m going at this school!)"
    stu "(...........................)"
    stu "maybe…"

    jump day_1

label day_1:


    $energy = min(energy + 70, maxenergy)

    play music "music/dorm vibe.mp3"
    show bg dorm with pixellate

    show andy neutral with moveinbottom
    show liben neutral at left with moveinbottom
    show james neutral at right with moveinbottom

    show andy happy
    andy "Oh, hey Student!"

    stu "Hey guys, what's up?"
    show liben spicy at left
    lib "Just getting ready to go to our econ class!"

    show andy mad
    andy "Ugh, don't remind me..."

    show liben mad at left
    lib "Hey, you’re the one that signed up for it."
    show liben neutral at left
    show andy neutral
    lib "What classes do you have today, Student?"

    stu "Well...I think I have econ, chemistry, and media studies."

    show james happy at right
    jam "Wow!  A little bit of everything!  That sounds really fun, Student!"

    stu "Thanks!  I may not know what I want to major in, but if I try a lot of
        new things I think I’ll find something I love."
    stu "Actually, I was thinking about what you said about research
        yesterday..."
    stu "If you guys are doing it..."
    stu "I think I’ll go for it too!"

    show andy happy
    andy "That’s great to hear, Student!!!"
    andy "With you, me, James, Liben, John, and Cole all working together and
        supporting each other, I know we’ll succeed!"

    stu "Haha, I don’t even really know where to start looking…"

    show andy neutral
    andy "Well, who are your teachers?  That’s always a good place to start."

    stu "That makes sense.  Here, you can look at my schedule."

    show liben neutral:
        xalign -0.4
        yalign 1.0
    with move

    show andy neutral:
        xalign 0.2
        yalign 1.0
    with move

    andy "Hm...Professor ____ is the economics professor."

    show econ_prof with moveinbottom

    andy "I think she works in the Social Science building."
    andy "She’s really popular right now because she just published a
        best-selling book!"
    andy "She’s very friendly and welcoming, and I heard her research is super
        interesting,"

    show andy sad
    andy "but it might be hard to talk to her because she’s always really busy
        being famous!"

    show liben mad:
        xalign -0.4
        yalign 1.0
    lib "Oh man, I wanna do research with her so bad!"
    show james neutral
    jam "Have you ever even talked to her?"
    show liben thinking:
        xalign -0.4
        yalign 1.0
    lib "Pfft, what? No... But I sent a buuunch of emails!"
    jam "You’ve sent emails to every professor on campus Liben, don’t you think
        you should talk to any of them in person?"
    show liben happy:
        xalign -0.4
        yalign 1.0
    lib "Hmmm, I dunno...That sounds like a lot of work to me…"
    hide econ_prof with moveoutbottom

    show andy mad
    andy "ANYWAY, Student, it looks like your chemistry teacher is
        Professor____."
    show chem_prof with moveinbottom
    show andy neutral
    andy "He runs a great lab in the STEM building; I’ve heard his research
        assistants have a lot of independence to pursue their interests!"
    andy "Professor____ is really sweet, but he’s kind of shy, so you might
        want to get to know him better before you start asking for research."
    show james happy
    jam "I’m pretty sure Cole did research there for a while."
    show liben thinking:
        xalign -0.4
        yalign 1.0
    lib "Really?  I thought he was studying history or psychology or something.
        When did he become a chemistry major?"
    show james neutral
    jam "Uhh, he didn’t.  Cole’s a fourth year, but he somehow hasn’t declared
        a major yet...you’ll always find him in the weirdest classes…"
    hide chem_prof with moveoutbottom
    andy "Okay, so it looks like your last teacher is Professor Tacoma!"
    show tacoma happy with moveinbottom
    andy "Tacoma is really cool!  He values creativity, and all his students
        say he creates a really strong team dynamic in his classes and
        research!"
    show andy happy
    andy"Plus, he’s got the coolest blue hair!"

    stu "(Wait...could it be...)"
    stu "Um, did you say blue hair?"
    andy "Yeah!  Cool, huh?"
    andy "Well, we’d better get going or we’ll be late for our class! Hope you
        have a great first day, Student!"
    show screen instructions
    show tacoma sad
    call screen instructions

    tac "You can't skip class in this demo!"

    ##First day of class!##

    scene bg classroom with fade

    stu "(This is it... the first day of classes!)"
    stu "(After months of waiting this summer...)"
    stu "(...and YEARS of work before that!)"
    stu "(I'll finally be in my first college class.)"
    stu "(Could my professor really be... a chance encounter with a blue haired
        mystery?)"

    show ash cool with moveinright

    stu "(Oh... I guess it isn't him...)"

    hide ash cool with moveoutbottom
    show ash mad with moveinbottom:
        zoom 2.00
        yalign 0.0
    ash "Somebody's late...."
    stu "(!!! But... there's still a couple minutes left...)"
    stu "(... she seems to be waiting expectantly for more people...)"
    stu "(... and I guess my professor isn't mystery boy...)"

    show tacoma sad at right with moveinright

    ash "There you are. Where have you been?"
    stu "(He's in my class!)"
    tac "Oh, sorry... the registrar scheduled my other class right before this
        on the other side of campus. Hopefully, I'll figure out a good system."
    stu "(That's unlucky... I hope the professor understands...)"
    ash "Anyway..."

    hide ash mad with moveoutbottom
    show ash happy with moveinbottom:
        xalign 0.3
        yalign 1.0
    show tacoma happy with moveinright:
        xalign 0.7

    ash "This is Critical Media Studies. I'm Ash, one of your co-instructors."
    stu "(...co-instructor?...)"
    tac "And I'm Tacoma, the professor for the class."
    stu "(!?!?!!?!?!?!)"
    tac "Since we're starting a bit late, I'd like to jump right into it. So
        did everybody do the readings I assigned over break?"
    stu "(Assigned???)"

    show ash happy:
        xalign -0.2
    show tacoma happy:
        xalign 0.3
    with pixellate
    tac "...So what is a game?"
    kid "The Salen and Zimmerman reading defines it: \"A game is a system in
        which players engage in an artificial conflict, defined by rules, that
        results in a quantifiable outcome.\""
    tac "Well, there's many ways to look at it. Some scholars focus on the
        different categories of games. In the Roger Callois depiction of games
        , including non-video games, he describes Competition, Chance,
        Roleplaying, and Vertigo."
    tac "Beyond that, we can look at more traditional genres like platformers
        or first person shooters..."

    show ash happy:
        xalign 0.8
    show tacoma happy:
        xalign 1.2
    with pixellate
    tac "...Hence narratives don't necessarily have to be be explicitly written
        by the game developers. When players construct their own story, it is
        known as an emergent narrative."
    tac "An example is from this GTA player online who became a bus driver..."

    show ash neutral:
        xalign 0.3
    show tacoma neutral:
        xalign 0.7
    with pixellate
    tac "...Remember, the readings are on Tarp, and office hours are on the
        syllabus."
    tac "However, if you drop by whenever I'm in my office and not busy, I'll
        be happy to talk with you about the material!"
    hide ash neutral
    hide tacoma neutral
    with moveoutright

    stu "(That class was so fast! I don't know if I'll be able to keep up...)"
    stu "(Doing my reading for a start will probably help...)"
    stu "(And I still can't believe that guy I ran into was the professor!)"
    stu "(He and Ash seem really passionate! It seems like it'll be tough to
        capture their attention, though without running into them again...)"
    stu "(...especially since I wasn't prepared to answer a single question...)"
    stu "(But they seem really approachable, so it can't be too bad...)"
    stu "(If I dedicate myself, I'll be able to get that research position
        with my friends!)"
    stu "(I hope...)"

    jump overworld_test





label overworld_test:

    call screen overworld

    $ result = _return



    if result == "econ":
        tac "Please only choose media for now :("
        call overworld_test from _call_overworld_test
    if result == "media":
        call tacoma_menu_loop from _call_tacoma_menu_loop
    if result == "dorm":
        scene bg bedroom
        menu:
            "Are you sure you want to go to sleep? (Reset energy)"
            "No":
                jump overworld_test
            "Yes":
                $day += 1
                jump expression days[day]



    if result == "chem":
        tac "Please only choose media for now :("
        call overworld_test from _call_overworld_test_1

    return



label tacoma_menu_loop:



    scene bg

    show tacoma neutral

    menu tacoma:
        "It's Professor Tacoma!"

        "I have no more energy! I should go to sleep!" if energy < 20:
            tac "Hey you look tired! Maybe you should go to sleep?"
            stu "Hmm, maybe I should return to my Dorm"
            call tacoma_menu_loop from _call_tacoma_menu_loop_1

        "Talk" if energy >= 20: #here is where all the talk introductions are
            if talknumber == 0:
                tac "Hey, we’ve met before! What was you name again?"
            elif talknumber == 1:
                tac "So this class focuses on a bunch of different media, but notably on video games! Do you play, Student?"
            elif talknumber == 2:
                tac "Are you ok with your seat, Student?"
            elif talknumber == 3:
                tac "Sorry I’m late guys, I was just setting up for a talk i’m giving!"
            elif talknumber == 4 or (talknumber > 4 and tac_pts < 40) :
                tac "Student, who’s your favorite Mario Kart 8 Player?"
            elif talknumber == 5:
                tac ".."
            elif talknumber == 6:
                tac "Did you get a chance to play today’s game, student?"
            elif talknumber == 7:
                tac "Pop quiz today!"
            elif talknumber == 8:
                tac "Hey I noticed you didn’t submit yesterday’s homework."

            elif talknumber == 9:
                tac "And so Bioshock proves itself as an example of distorted control in a first person game!"
            elif talknumber == 10:
                tac "One way that a lot of game designers implement narrative architecture is through the use of Enacted stories, can you think of any examples?"
            elif talknumber == 11:
                tac "Can anyone think of an instance where real life become game-like?"
            elif talknumber == 12:
                tac "Any comments on Braid?"
            elif talknumber == 13:
                tac "Did you guys know that Jonathan Blow was influenced by Italo Calvino’s Invisible Cities?"
            elif talknumber == 14:
                tac "Roger Caillos proposes four categories of games: Competition, Chance, Roleplaying, Vertigo"
            elif talknumber == 15:
                tac "Can anyone tell me what Media Archaeology is?"
            elif talknumber == 16:
                tac "In what ways do the mechanics of Problem Attic induce emotion?"
            elif talknumber == 17:
                tac "Can anyone tell me in what ways are you disconnected from the avatar in an FPS Game?"
            elif talknumber == 18:
                tac "And so an embedded Story is one that arises from examining the body of information present in the world"
            elif talknumber == 19:
                tac "An Emergent Narratives is kind of like a narrative made by the players"
            menu talk: #here is where all the talk responses are

                "Student! It’s nice to meet you professor." if talknumber == 0:
                    tac "It’s nice to meet you too Student-kun, I hope you enjoy my class!"
                    $energy -= 20
                    $tac_pts += 10
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_2
                "Get away from me creep!" if talknumber == 0:
                    tac "Oh...my bad. (this student is a little strange)"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_3
                "I’ve played some video games, but I didn’t know you could study them" if talknumber == 1:
                    tac "In a lot of ways, I find similarities between video games and literature, they can be close read and analyzed like any text or work of art!"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_4
                "Video Games?? You study video games??" if talknumber == 1:
                    tac "Yeah...so much so that I teach a class on it…"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_5
                "It’s a little bit far from the screen, is it alright if I move up?" if talknumber == 2:
                    tac "Yeah of course, thanks for speaking up"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_6
                "Why would you sort the class alphabetically, I can’t see from back here?" if talknumber == 2:
                    tac "Oh, i’m sorry, here why don’t you move up…?"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_7
                "That’s alright, what’s your lecture on?" if talknumber == 3:
                    tac "I’m giving a talk on gamification! Sorry about being late.."
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_8
                "…" if talknumber == 3:
                    tac "It won't happen again..."
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_9

                "I like wario!" if talknumber == 4:
                    tac "I like him too!"
                    $energy -= 20
                    if tac_pts >= 40:
                        $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_10
                "Baby Mario for LIFE" if talknumber == 4:
                    tac "Get out."
                    $energy -= 20
                    if tac_pts >= 40:
                        $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_11
                "Hey what's lecture on today professor?" if talknumber == 5:
                    tac "Oh. My bad, student-kun, today we’ll be studying control in FPS games, thanks for being so interested in class "
                    $energy -= 20
                    $tac_pts += 10
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_12
                "YO! I'm not paying you to be silent!" if talknumber == 5:
                    tac "MY BAD! Take your seats class!"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_13
                "Yeah but I wasn't quite sure how to read Hair, Nah..." if talknumber == 6:
                    tac "Well, maybe think about it in the context outside the game, it’s a pretty challenging effort to have to fend against people touching you, and it’s a real issue for a lot of people."
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_14
                "I have no idea what you expect me to gain from playing these dumb games." if talknumber == 6:
                    tac "I think there’s a lot more ethical commentary than you give them credit for."
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_15
                "WHAT! I didn't study!" if talknumber == 7:
                    tac "Haha just kidding, just wanted to make sure you paying attention"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_16
                "You can’t make me take a quiz that wasn’t in the syllabus!" if talknumber == 7:
                    tac "Oh... it was just a joke. My bad."
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_17
                "Oh, my bad, I must have just forgotten, but I can get it to you ASAP" if talknumber == 8:
                    tac "No problem, as long as I get it before the end of the day, i’ll be happy.  Can’t wait to read it!"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_18
                "The project was dumb and so are you" if talknumber == 8:
                    tac "Then you can accept your zero"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_19
                "I suppose it’s further exemplified by the narrative elements of the game alongside the use of the subjective view" if talknumber == 9:
                    tac "Wow! Glad to see you’ve been paying attention, Student."
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_20
                "You can be my big Daddy any day ;)" if talknumber == 9:
                    tac "I don't feel comfortable with you saying that Student..."
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_21
                "I’m not quite sure I know too many, but I’d be happy to play any you recommend" if talknumber == 10:
                    tac "Oh, you gotta check out Dear Esther, it’s a really interesting exploration game!"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_22
                "No. Games are dumb and shouldn’t be part of this syllabus " if talknumber == 10:
                    tac "Oh"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_23
                "Oh like on Instagram! Likes and comments on photos become like a point-system among players, who are social media users." if talknumber == 11:
                    tac "Excellent input, Student!"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_24
                "This class feels like a game, and we're all losing" if talknumber == 11:
                    tac "Maybe you’ll lose the game in more than one way, then…"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_25

                "Well, something I was thinking was that maybe the ‘princess’ represents the destruction of mankind, and personifying her as a princess is some strange form of justification for the following through with that destruction" if talknumber == 12:
                    tac "It’s an interesting take, maybe you can write a response post about it!"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_26
                "Well clearly the princess is a bomb" if talknumber == 12:
                    tac "Maybe you should open up the possibilities of the game, it’s an interesting take, but maybe the game isn’t quite as explicit"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_27
                "Sorry I'm not super familliar with Calvino's work, how does it relate to braid?" if talknumber == 13:
                    tac "Oh well, I suppose they both prominently feature worlds which play by different temporal rules."
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_28
                "Wait we had a game to play???" if talknumber == 13:
                    tac "...Oh...maybe you should do your homework then...Remember that they both prominently feature worlds which play by different temporal rules."
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_29
                "I’m a little unclear on that last one, what is Vertigo again?" if talknumber == 14:
                    tac "Oh, Vertigo refers to games that induce altered perception, hallucinations, disorder and dizziness."
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_30
                "Wait, who's Roger Caillos????" if talknumber == 14:
                    tac "Did you do the readings, student?"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_31
                "Oh well it’s when a game makes use of references to make us think about American history or video game history. " if talknumber == 15:
                    tac "Excellent work Student!"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_32
                "I once dug up a computer in my grandma's house" if talknumber == 15:
                    tac "Cool..."
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_33
                "Ah well there are many instances of the player's control of the character being frustratingly limited" if talknumber == 16:
                    tac "Makes you feel preety helpless, eh?"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_34
                "Makes me feel pretty shitty" if talknumber == 16:
                    tac "Right but *why* does it make you feel shitty"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_35
                "Oh well, you can see what he sees, but not what he smells or feels" if talknumber == 17:
                    tac "well for now, technology IS advancing pretty quick"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_36
                "I am the avatar" if talknumber == 17:
                    tac "Ok Aang"
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_37
                "Ah like Tacoma or Obra Dinn" if talknumber == 18:
                    tac "Yes, Precisely!"
                    $energy -= 20
                    $talknumber += 1
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_38
                "What if the world has nothing worth examining" if talknumber == 18:
                    tac "Keep your eyes open..."
                    $energy -= 20
                    $talknumber += 1
                    call tacoma_menu_loop from _call_tacoma_menu_loop_39
                "Ah like Sandbox games" if talknumber == 19:
                    tac "Well studied!"
                    $energy -= 20
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_40
                "Maybe we’re all players in a narrative that we’ve constructed…" if talknumber == 19:
                    tac "Stop being so Meta student, someone might be listening..."
                    $energy -= 20
                    $tac_pts += 10
                    call tacoma_menu_loop from _call_tacoma_menu_loop_41

                    #end of talking













        "Quiz" if tac_pts >= 40 and energy >= 40: #here is where all the quizz questions are
            $energy -= 30
            $quiznumber += 1
            if quiznumber == 1:
                tac "Which game do you think would be a good example of control in first person games?"

            elif quiznumber == 2:
                tac "What is one common type of narrative architecture?"

            elif quiznumber == 3:
                tac  "According to Roger Caillois, what are the four categories of games?"

            elif quiznumber == 4:
                tac "What is one of the works that influenced the development of Braid?"

            elif quiznumber == 5:
                tac "Whic of these mechanics does NOT apply to Emotion in Problem Attic"

            elif quiznumber == 6:
                tac "Which of these narratives are narratives constructed by players?"

            elif quiznumber == 7:
                tac "What am I? A game that  makes use of references to make us think about American history or video game history. "

            elif quiznumber == 8:
                tac "In what ways are you disconnected from the avatar in an FPS Game?"

            elif quiznumber == 9:
                tac "What game type refers to games that induce altered perception, hallucinations, disorder and dizziness "

            elif quiznumber >= 10:
                tac "Which of the following is NOT an instance of gamification."




            menu quiz: #Here is where the quiz responses are


                "Braid" if quiznumber == 1:
                    tac "I don't think that's a first person game Student..."
                    call tacoma_menu_loop from _call_tacoma_menu_loop_42

                "Bioshock" if quiznumber == 1:
                    tac "Oh! Good idea!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_43
                "Loved" if quiznumber == 1:
                    tac "I don't think that's a first person game Student..."
                    call tacoma_menu_loop from _call_tacoma_menu_loop_44
                "Evocative Spaces" if quiznumber == 2:
                    tac "That's correct!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_45
                "Social Contigency" if quiznumber == 2:
                    tac "Have you been coming to class Student?"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_46
                "Eperience design" if quiznumber == 2:
                    tac "Not really..."
                    call tacoma_menu_loop from _call_tacoma_menu_loop_47
                "Competition, Cooperative, Roleplaying, Performance" if quiznumber == 3:
                    tac "Quite close, but not exactly"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_48
                "Competition, Interactive, Strategic, Art" if quiznumber == 3:
                    tac "Quite close, but not exactly"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_49
                " Competition, Chance, Roleplaying, Vertigo" if quiznumber == 3:
                    tac "Exactly!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_50
                "Albert Einstein’s The World as I See It" if quiznumber == 4:
                    tac  "Incorrect, although Braid was influenced by Alan Lightman’s Einstein's Dreams"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_51
                "Italo Calvino's Invisible Cities" if quiznumber == 4:
                    tac "Good Job!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_52
                "Paul McNeive’s The Manhattan Project" if quiznumber == 4:
                    tac "Incorrect!"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_53
                "Stopping and reversing time" if quiznumber ==5:
                    tac "Good job!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_54
                "Being unable  to move sometimes" if quiznumber == 5:
                    tac "No that's incorrect"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_55
                "Having to use enemies as jumping off platforms" if quiznumber == 5:
                    tac "No that's incorrect"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_56
                "Embedded stories" if quiznumber == 6:
                    tac "No"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_57
                "Emergent Narratives" if quiznumber == 6:
                    tac "Nice!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_58
                "Enacted Stories" if quiznumber == 6:
                    tac "No"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_59
                "Media Archaeology" if quiznumber == 7:
                    tac "Level up!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_60
                "Media History" if quiznumber == 7:
                    tac "No..."
                    call tacoma_menu_loop from _call_tacoma_menu_loop_61
                "Media America" if quiznumber == 7:
                    tac "No..."
                    call tacoma_menu_loop from _call_tacoma_menu_loop_62
                "You can see what the avatar sees" if quiznumber == 8:
                    tac "No."
                    call tacoma_menu_loop from _call_tacoma_menu_loop_63
                "You can feel what the avatar feels" if quiznumber == 8:
                    tac "No."
                    call tacoma_menu_loop from _call_tacoma_menu_loop_64
                "You can't feel what the avatar feels" if quiznumber == 8:
                    tac "Nice!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_65
                "Vertigo" if quiznumber == 9:
                    tac "Nice!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_66
                "Competition" if quiznumber == 9:
                    tac "Not nice!"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_67
                "Chance" if quiznumber == 9:
                    tac "Nope"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_68
                "Corporations utilizing life and following systems" if quiznumber >= 10:
                    tac "Nope, that's gamification"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_69
                "Teachers incorporating \"missions\" and \"quests\" as homework" if quiznumber >= 10:
                    tac "Nope, that's very clearly gamification"
                    call tacoma_menu_loop from _call_tacoma_menu_loop_70
                "Multiple choice exams" if quiznumber >= 10:
                    tac "Yes but they can be easily gamified!"
                    $tac_pts += 20
                    call tacoma_menu_loop from _call_tacoma_menu_loop_71

                    #end of quizzes











        "Research" if tac_pts >= 120 and energy >= 60: #qte minigame
            tac "Hey I got some research for you to do!"
            $energy -= 60
            call QTE(renpy.random.randint(1, 4)) from _call_QTE
            call tacoma_menu_loop from _call_tacoma_menu_loop_72
            #end of  minigame
        "Leave (return to overworld map)":
            jump overworld_test

    return




label bedroom:
    scene bg bedroom
    if tac_pts >= 40 and quiz:
        call screen quizzes
        $quiz = False
    if tac_pts >= 120 and research:
        call screen research_screen
        $research = False
    stu "It's the start of a new day!"

    return
label QTE(randomqte):

    # $randomqte = randomqte
    scene bg
    $ counter = 0
    # $ arr_keys = ["a", "s", "d", "w", "K_SPACE"]
    # call qte_setup(0.75, 0.75, 0.01, reading_list[counter],
    #    renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1,
    #    randomqte)
    # call qte_setup(7, 7, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1, randomqte)

    while counter < 20:
        $ countdown = ((20 - counter)*(20 - day))/20
        call qte_setup(countdown, countdown, 0.01, reading_list[letter_counter],
            renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1,
            randomqte) from _call_qte_setup
        # call qte_setup(1.2, 1.2, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1, randomqte)
        $ letter_counter += 1
        $ counter += 1

    if counter == 20:
        play sound "music/victory.mp3"
        "{b}You completed your research on time! Tacoma is very happy!{/b}"
        $tac_pts += 50
    else:
        play sound "music/miss.mp3"
        "{b}You didn't complete your research on time. However, Tacoma understands how hectic college life can be and isn't too bothered.{/b}"


    return



label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align, randqtesetup):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align
    $randqtesetup = randqtesetup

    if randqtesetup == 1 or randqtesetup == 2:
        call screen qte_keyboard
    else:
        call screen qte_button


    $ cont = _return


    return


label day_2:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom



    jump overworld_test








label day_3:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_1

    jump overworld_test



label day_4:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_2

##Football game cutscene##
    scene bg bedroom
    jam "Um, hello, Student?"
    jam "Are you up?"
    stu "Huh?  Who’s there?"
    show liben happy with moveinbottom:
        xalign -0.3
        yalign 1.0
    show james neutral with moveinbottom
    show andy neutral with moveinbottom:
        xalign 0.2
        yalign 1.0
    lib "Only your BEST FRIENDS in the entire world, dummy!"
    stu "Oh, hey guys. Where are you guys all going?"
    show andy happy
    andy "We’re all going to the big UKokoro football game, of course! And
        you’re coming with us!"

    show cole happy with moveinright:
        xalign 0.9
        yalign 1.0
    col "Whether you like it or not…"

    show john mad with moveinright:
        xalign 1.0
        yalign 1.0
    joh "Please do not listen to him."

    stu "(Oh, right...the big game...)"
    stu "(Apparently everybody turns out for it...)"
    stu "(It sounds fun, but I don’t know...only four days in at this school
        and I already feel kind of overwhelmed with everything I have to do.)"
    stu "(On the other hand, it would be nice to take a break and get to know
        everyone better…)"

    menu:
        "Go to Football Game (Lose 30 Energy today)":
            jump choice_football_yes

        "Skip the game and get to work":
            jump choice_football_no

label choice_football_yes:

    $energy -= 30

    stu "Okay, yeah, that sounds pretty fun!"
    show andy happy
    andy "Yaaaaaayyy"
    col "Okay, great, but hurry up! We gotta get there before they run out of
        free popcorn!"

    scene bg football
    show james happy:
        xalign 0
        yalign 1.0
    show andy happy:
        xalign 0.3
        yalign 1.0
    show john neutral:
        xalign 0.5
        yalign 1.0
    show liben neutral:
        xalign 1.2
        yalign 1.0
    show cole neutral:
        xalign 1.3
        yalign 1.0

    "And that’s another touchdown for UKokoro!"
    lib "We’re UNSTOPPABLE!!!!!"
    show john sad
    joh "Drat!"
    show andy sad
    andy "What?! John are you not rooting for UKokoro?!?"
    show john neutral
    joh "What can I say?  I’ve got money on the other team."

    stu "Oh no…how much, John?"
    show john neutral
    joh "Uhhhh, ten–"
    show andy happy
    andy "That’s not so bad…"
    show john sad
    joh "– thousand."
    show andy sad
    andy "Uh oh."
    show john happy
    joh "Eh, wealth is a fleeting thing!"
    show james mad
    jam "I mean, when you bet like that, certainly."
    show liben thinking
    lib "Um, Cole, isn’t that like you’re sixth tub of popcorn??"
    show cole happy
    col "Sure is."
    lib "Don’t you think you’re overdoing it."
    show cole mad
    col "Hmmm, nope.  Pretty sure this is the first thing I’ve eaten all week."
    lib "Uhhh, yeah okay, you go ahead then."
    col "Don’t tell me what to do."

    jump choice_football_done

label choice_football_no:

    stu "I don’t think so guys, I’m already feeling really busy with all my
        new classes.  Thanks, though."
    show andy happy
    andy "Oh, no worries.  I remember it can be really overwhelming at the
        beginning.  Don’t worry you’ll get the hang of it!"
    show liben happy
    lib "Alright, have a groovy time, Student."
    show cole happy
    col "I’ll save you a popcorn."
    jam "Bye, Student!"
    joh "Farewell."

    hide andy happy with moveoutright
    hide liben happy with moveoutright
    hide cole happy with moveoutright
    hide john with moveoutright
    hide james with moveoutright

    jump choice_football_done

label choice_football_done:
    show bg bedroom
    play music "music/dorm vibe.mp3"
    hide andy with moveoutright
    hide liben with moveoutright
    hide cole with moveoutright
    hide john with moveoutright
    hide james with moveoutright
    stu "Okay, time to get to work!"



    jump overworld_test





label day_5:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_3

    jump overworld_test




label day_6:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_4

##James' Cutscene###########
    scene bg juggling
    "(One day while you are walking to the library, you spot James way across
        the quad)"
    stu "Wait a second, what is he doing?"
    "(There’s a small crowd around him)"
    show james happy
    "(Once you get closer, you realize that he is juggling what appear to be
        five rather hefty math textbooks)"
    show stu_n with hpunch
    stu "(Wow, I never noticed how beefy James’s forearms were....)"
    stu "(He tosses those textbooks like they weigh nothing!)"
    show james neutral
    jam "Oh, hey Student!"
    show james happy
    jam "Wow, I’m, uh, so glad you stopped by!"
    stu "Hey, James.  I had no idea you were such a talented juggler."
    show james neutral
    jam "Oh, this?"
    show james happy
    jam "Haha, yeah well it’s nothing much really."
    "(James is positively chucking math textbooks easily twenty-five feet into
    the air and seamlessly catching them while maintaining eye-contact with
    you the entire time)"
    show stu_n with hpunch
    stu "Are you kidding?!  This is super impressive!  I bet it takes a ton of
        concentration not to drop any of those."
    jam "Well, you’d think that, but actually juggling is a great way for me
        to kind of turn my brain off and relax."
    jam "I actually decided to come out here today in order to relieve a
        little bit of stress."
    stu "Is there something going on?"
    show james neutral
    jam "I dunno, nothing really…"
    jam "I’m just looking for a research position like everybody else, but
        sometimes it can be really nerve-wracking to approach professors."
    stu " I totally get that."
    show james mad
    jam "Like, last year I was a TA for Professor Nichols, and it was super
        comfortable."
    jam "She was a little quieter and relaxed, so it didn’t feel stressful to
        communicate about research or grading papers or anything."
    jam "So it would be really easy to go back and TA for her again this year…"
    show james happy
    jam "But I kind of want to branch out and try something new."
    jam "Professor _____, I think maybe Andrew mentioned her before, does
        really cool economics research, and even though I mostly study math, I
        think working with her could be a really exciting way to expand my horizons."
    stu "If it sounds like fun, you should just go for it!"
    show james mad
    jam "The problem is, Professor _____ is really passionate about her work,
        but it also makes her kind of intense."
    show james neutral
    jam "It’s really hard for me to reach out to someone like that when I
        don’t know them…"
    show james happy
    jam "Anyway, that’s what’s got me out here juggling my cares away."
    stu "That sounds like a tough position to be in James.  It seems like you
        have some anxiety about putting yourself out there"
    stu "but I think you might surprise yourself if you give it a shot."
    show james neutral
    jam "Really?"
    "(James shrugs wistfully as he gives the books one last toss and then
    catches all five of them in a stack balanced on top of his head)"
    jam "What makes you think that?"
    stu "Well, while you were talking to me, did you notice how big the crowd
        watching your juggling has gotten."
    jam "Huh?"
    "(There are literally throngs of hundreds of people cheering fanatically
    after James’ thrilling finale)"
    stu "It seems like juggling in public like this really requires you to put
        yourself out there."
    stu "I bet at first it was pretty intimidating but now you seem like a
        natural at it."
    stu "Plus, it seems like you’ve found something you really enjoy and are
        good at."
    jam "That’s true…"
    show james mad
    jam "but what does that have to do with Professor _____"
    stu "Well it may be intimidating to talk to her at first, but if you make
        the effort, it may be super rewarding."
    show james happy
    jam "Haha, that’s true.  I used to be mortified to get on a stage, but now
        it’s actually my go-to to relax."
    jam "I guess maybe I can give it a shot.  What’s the worst that could
        happen, right?"
    stu "That’s awesome, James!  I’m proud of you!"
    jam "Thanks, Student.  It’s always nice to be able to talk through these
        things with someone else.  "
    "(You shake James’ hand, his powerful grasp enclosing your own hand like a
    mighty vicegrip)"
    "(Five math textbooks still balanced flawlessly atop his head.)"
    "(The crowd continues to roar in idolizing devotion, but James, ever
    modest, does not appear to notice.)"
    jam "Haha, well, I’d better run.  Later, Student!"
    hide james happy with moveoutbottom
    stu "(What a remarkable man...)"



    jump overworld_test




label day_7:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_5

    jump overworld_test




label day_8:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_6

##COLE'S CUTSCENE##
##################
    $maxenergy = 100

    scene bg bedroom
    play music "music/dorm vibe.mp3"
    stu "(z-z-z-z)"
    show cole happy with moveinbottom:
        zoom 1.5
        xalign 0.5
        yalign 0.3
    col "GOOD MORNING STUDENT"
    show stu_n with hpunch
    stu "AH COLE!?"
    stu "WHAT ARE YOU DOING HERE!???"
    show cole neutral:
        zoom 1.0
        xalign 0.5
        yalign 0.0
    col "I slept on the roof of your dorm last night"
    show cole happy
    col "I wanted to see the moon."
    stu "The...the moon…?"
    col "ALSO I wanted to drop in and let you know that I’ve solved ALL my
        problems!"
    stu "What…?"
    show cole happy
    col "I killed  two birds with one stone"
    show cole neutral
    col "I found research AND a solution to my major declaration crisis."
    stu "What...?"
    stu "You found research!?"
    stu "That’s great!"
    stu "And I guess that means you’re declaring your major in your research
        field?"
    show cole happy
    col "Not quite!!!!!!"
    stu "W...what?"
    show cole neutral
    col "I got a research position at Professor Dolly’s lab, do you know him?"
    stu "(Wait...professor Dolly is a biology professor…)"
    col "So, I got research for him aaaaaand..."
    show cole neutral at left with move
    show clone cole neutral at right with moveinright
    show cole happy at left
    col "TADA I GOT CLONED"
    show clone cole happy at right
    col2 "Hello, I’m Biology-Cole"
    show stu_n with hpunch
    stu "WHAAAAAT?"
    show cole neutral at left
    col "I cloned myself a few times over so I could have one Cole for all my
        major options!"
    show stu_n with hpunch
    stu "WHAAAAT THE HELL IS GOING ON?"
    col "Pretty clever, eh?"
    col2 "I AGREE!"
    show stu_n with hpunch
    stu "HOW IS THIS POSSIBLE????"
    show cole happy at left
    col "Haha SO COOL EH!?"
    show cole neutral at left
    col "Oh! Andy told me to give you advice today, since I already got my
        position!"
    col " I’ve been thinking long and hard about what I would say to you."
    stu "I’m so confused..."
    col "And here it is:"
    show cole mad at left
    show clone cole neutral at right
    col "Research is an opportunity to experience something that you wouldn’t
        normally experience."
    col "Imagine all the niche things that professors want to look at"
    col "from studying whales in the sea to the stars in space"
    col "research opens you up to so many experiences you might never get the
        chance to face."
    show clone cole happy at right
    col2 "LIKE CLONING!"
    show cole neutral at left
    col "Yes Bio-Cole, like Cloning!"
    show cole mad at left
    col "So let that motivate you to keep looking for something."
    col "Find something that will present you with an experience"
    show cole neutral at left
    col "something that’ll make for a good story when you’re older."
    stu "..."
    stu "(You know what)"
    stu "(for someone as unpredictable and odd as Cole, that advice was kind
        of touching.)"
    stu "(I guess he’s right)"
    stu "(this whole process IS a lot of fun and I really am having a good
        time getting to know these guys and all the professors at this
        school...)"
    stu "It’s so different from high school, but if I do end up getting a
        position, it really would be a great story to share with these guys…)"
    col "Student?"
    stu "Thank you Cole."
    stu "Really! This process has already been so much fun, so I can only
        imagine the actual research part would be even more fun~!"
    show cole happy at left
    col "YEAH! Well, me and my clones are finna go play some 5-man basketball.
        You coming?"
    stu "...maybe later."
    show cole neutral
    col "Suit yourself."
    show cole happy
    col "COLES, WE’RE MOVING OUT!"
    hide cole happy with moveoutright
    hide clone cole happy with moveoutright



    jump overworld_test




label day_9:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_7

    jump overworld_test




label day_10:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_8

##Liben's Cutscene##
####################
    scene bg dorm
    play music "music/dorm vibe.mp3"
    show stu_n
    stu "(Wow it’s been just around a week since I’ve been here, and it
        already seems like more and more people are getting research
        positions...)"
    stu "(I wonder how the rest of them are doing.)"
    "*Knock Knock*"
    stu "Oh, Come in!"

    show liben neutral with moveinbottom
    lib "Hey Student! I Gotta tell you something!"

    stu "Oh Liben! Wow I was just thinking about - "
    show liben spicy
    lib "Okay so..."
    lib "…"
    lib "…"
    lib "…"
    lib "…"
    show liben happy with hpunch
    lib "I GOT A RESEARCH POSITION!!!!!!!"

    stu "WHAT!? CONGRATS LIBEN!"
    lib "I KNOW, I ACTUALLY GOT ONE BOYYYYYY"
    show liben thinking
    lib "or uh girl I guess..."
    stu "Wait didn’t you email every professor in school...and that worked…?"
    show liben happy
    lib "HA"
    show liben sad
    lib "nooooooooo."
    show liben neutral
    stu "Wait...then how did you get research?"
    show liben thinking
    lib "WELL.  I was up in the gym, working on my Inner thighs and - you know
        professor Schwarzenegger???"
    stu "uh...no… I don’t think so"
    show liben spicy
    lib "Well, he’s this SUUUUUPER famous econ professor we have"
    lib "and he’s on leave right now, and I found him at the gym bench pressin’"
    stu "you found him...at the gym?"
    show liben happy
    lib "Yeah and let me just say"
    show liben spicy
    lib "he was trying to lift 300 on each side and I KNEW that was going to
        kill him."
    lib "But he tried to lift it anyway"
    show liben mad
    lib "with NO SPOTTER"
    stu "WHAT???"

    lib "Yeah, he had it pressed like all the way down on his chest"
    show liben spicy
    lib "SO, I slid in and I saved his ass."
    stu "oh my god..."

    show liben happy
    lib "he was so impressed by my fast thinking and GAINS, and I asked him
        right away IRL if he was looking for an assistant in his lab"
    lib "and he gave me the position on the spot."
    stu "Econ professors have labs…? What does he even research."
    show liben thinking
    lib "He founded a subsection of Game theory in weightlifting called GAINS
        THEORY; and his lab is actually in the gym"
    stu "Wait what?????"
    show liben happy
    lib "RIGHT!? I can get a pump in and then go straight to work!"
    stu "well Congrats I guess...though i suppose those emails were for nothing"
    lib "Hahaha maybe. At the end of the day, I guess nothing beats a good old
        fashioned face-to-face."
    show liben spicy
    lib"If you haven’t already started talking to professors, you really should
        hop on that, because it really does make ALL the difference."
    stu "(Liben’s right...Talking to profs is probably the best way to approach
        this)"
    lib "Man. getting the position taught me that you don’t really have to
        compromise too much of yourself for a career; in fact, I think what got
        me the position was the fact that I showed him what I love"
    show liben mad
    lib "RACKING UP GAINS"
    stu "...Uh...yeah..."
    show liben mad with hpunch
    lib "GAAAAAAAAAINS"
    stu "(In a weird way, Liben’s got a point...)"
    stu "(He found research without having to change who he is)"
    stu "(He just found someone who fit him and he retained his personality
        all the way through...)"
    stu "(something to keep in mind, I guess.)"
    show liben spicy
    lib "Anyway, it’s Trap day, so I’m gonna go work out now, Student, but
        good luck on your quest,"
    lib "Like I always say"
    show liben happy
    lib "BELIEVE IN LIBEN!"
    show liben thinking
    lib "Or i guess...Believe in student…"
    stu "hahaha thanks Liben, Good luck on your...traps…"
    show liben happy
    lib "LATA!!!!!"
    hide liben with moveoutbottom

    jump overworld_test






label day_11:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_9

    jump overworld_test




label day_12:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_10

## DAY 12 JOHN'S CUTSCENE#####
##############################
    scene bg dorm
    show john mad with dissolve
    joh "Give me a thousand kisses, and a hundred more, a thousand more again,
        and another hundred, another thousand, and again a hundred more!"
    stu "J...John?"
    joh "As we kiss these passionate thousands let us lose track"
    stu "Hi John, what are you doing?"
    show john neutral
    joh "Give me one second, I am almost done"
    show john happy
    joh "In our oblivion, we will avoid the watchful eyes of stupid..."
    stu "...ok..."
    joh "Evil peasants hungry to figure out how many kisses we have kissed!"
    stu "..."
    joh "oh hi, you are..."
    show john sad
    joh "..."
    joh "May I ask for your name again?"
    stu "Student"
    show john happy
    joh "Hi, Student. Did you enjoy my reading of Catullus’s poem for his lover
        Lesbia?"
    stu "It sure is..."
    stu "...interesting."
    stu "the way he describes kisses. He seems to be quite in love with her."
    joh "Yes, he was"
    show john sad
    joh "if only he knew of all the misery in the years to come..."
    stu "uh John..."
    stu  "aren’t you worried about finding a research opportunity?"
    stu "Everybody is already on their way to ask professors for potential
        research positions."
    stu "How come you even have time here to read an ancient Roman love poem?"
    show john neutral
    joh "“Wanting to be faster only slows you down.”"
    stu "What?"
    show john happy
    joh "That’s a quote by Confucius."
    stu "But what does it mean?"
    show john neutral
    joh "Everybody is so rushed to build connections with professors as early
        as possible."
    joh "But they often ignore that knowledge takes time to accumulate."
    show john happy
    joh "A true scholar takes a hundred years to foster!"
    stu "Now who is that from?"
    show john sad
    joh "Me."
    stu "Oh…."
    joh "I want to be a poet in the future so now I do my homework."
    joh "Word by word I indulge myself in the lines evocative of the purest
        human emotions in history."
    show john mad
    joh "The irony is--time doesn’t seem to exist when I read. Sometimes, I
        even forget to sleep."
    stu "Wow..."
    stu "(I wouldn't expect such a quiet guy to be so...)"
    stu "(...deep.)"
    stu "(John's a lot more profound than I thought and I suppose his thinking
        is pretty sound...)"
    show john happy
    joh "Rather than stressing over how to ask your professor about research
        positions"
    joh "why not sit down and spend some time studying for theeir quizzes."
    show john neutral
    joh "Once you can memorize all the key points that a professor talked about
        in class, then you are ready to approach him."
    stu "(I guess I should really be paying attention to the conversations I
        have with profs)"
    stu "You're right John"
    stu "Maybe I should catch up on all the reading that I skipped first…"
    stu "Thanks John"
    show john happy
    joh "You are welcome."
    show john mad
    joh "“Once upon a time, I dreamt I was a butterfly…”"
    stu "later John..."

    jump overworld_test




label day_13:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_11

## ANDREW's CUTSCENE ###
########################
    play music "music/dorm vibe.mp3"
    scene bg main quad
    show andy neutral with moveinbottom
    andy "Good Morning Student, how has the research quest been going?"
    stu "Fine, I guess."
    stu "How are you doing?"
    show andy happy
    andy "I’m really excited!"
    andy "I’m conducting a shoot this week for our campus fashion magazine!"
    andy "And I think I’m going to go fabric shopping tonight for my spring
        collection!"

    stu "WOAH THAT’S SO COOL,"
    stu "I’m so impressed you manage to pull that together AND try to find
        research!"

    andy "Oh yeah..."
    show andy sad
    andy "the research."

    stu "Is...is everything going alright?"
    stu "Have you secured a position already?"

    andy "It’s been going well..."
    show andy sad:
      zoom 1.25
      yalign 0.0
    andy "And I love Econ"
    show andy sad:
        zoom 1.5
        yalign -0.25
    andy "And it makes me so fulfilled"
    show andy sad:
        zoom 1.6
        yalign -0.3
    andy "And valued"
    show andy sad:
        zoom 1.7
        yalign -0.3
    andy "And loved"
    show andy sad:
        zoom 1.8
        yalign 0
    andy "and even though it’s stressful"
    show andy sad:
        zoom 2.0
        yalign 0
    andy "I know"
    show andy sad:
        zoom 2.25
    andy "I’ll"
    show andy sad:
        zoom 2.5
    andy "Make"
    show andy sad:
        zoom 3.0
        yalign 0.1
    andy "It"
    stop music
    show andy sad with hpunch:
        zoom 4.0
        yalign 0.2

    andy "Through."

    stu "Andy..."

    play music "music/dorm vibe.mp3"
    hide andy sad
    show pink andrew neutral
    andy "You know what, I actually think I’m going to take a minute to maybe
        reconsider my options."
    andy  "I’m really not sure if pursuing serious work in economics is for me."
    andy "I love the courses I take and the teachers are swell, but if we’re
        being perfectly honest, pursuing something more creative seems better
        for me."
    stu "...is your hair pink…?"
    show pink andrew happy
    andy "I actually applied for a few fashion internships and even some
        English Research."
    show pink andrew neutral
    stu "Actually, that sounds like a better fit for you, Andy."
    show pink andrew happy
    andy "I think so too!"

    stu "Um...are you going to be ok?"
    show pink andrew neutral
    andy "Yeah..."
    show pink andrew happy
    andy "Yeah I think so."

    stu "Good."
    show pink andrew neutral
    andy "Not that I should be giving you any advice, you seem more certain of
        things than I do,"
    andy "but I suppose my advice would be not to fall into the trap of
        surrendering yourself to something that hurts you so much."
    andy "Leave some space for you to pursue things you love and maybe you can
        build a career off of that."
    show pink andrew happy
    andy "Who says that work can’t be really fun too?"
    stu "(Woah...It’s as if Andy is totally different from when we met on the
        first day)"
    stu "(I’m glad that he’s keeping his options open…)"
    show pink andrew neutral
    andy "Y’Know STUDENT, even though I’m supposed to mentor you"
    show pink andrew happy
    andy "I’m really grateful that you agreed to do this research quest with
        all of us"
    andy "I really do think it’s helping all of us really think about our time
        at this school,"
    andy "but also, I think it’s bringing the six of us much closer."
    show pink andrew neutral
    andy "We’ve invested so much into our dreams, but we still manage to hang
        out with each other, and I dunno"
    andy "it’s just really nice watching all of us grow."
    stu "(Andy...)"
    stu "(...what a mentor...)"
    stu "(Even though he’s older than I am, he still feels like he’s just like
        me...)"
    stu "(and I’m glad he can be so honest with me about his struggles...)"
    stu "(I guess I really did get lucky to have a friend like him…)"
    show pink andrew happy
    andy "Anyway, I need to head to class, but I’ll see you around, good luck
        with everything, STUDENT!"
    stu "Thanks Andy, Good luck to you too~!"

    jump overworld_test




label day_14:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_12

##FRAT PARTY CUTSCENE##

    scene bg bedroom
    play music "music/dorm vibe.mp3"
    "(Knock Knock)"
    lib "HELLOOOOOO STUDENT???"
    show liben neutral with moveinright
    stu "Liben, what are you doing here???"
    show liben neutral with move:
        xalign -0.5
    show pink andrew happy with moveinright:
        xalign 0.25
        yalign 1.0
    andy "Surprise Student!"
    stu "Andy!?"
    stu "What’s going on!?"
    show james happy with moveinright:
        xalign 0.5
        yalign 1.0
    jam "We all go invited to a party tonight and were wondering if you’d be
        interested in going."
    show john happy with moveinright:
        xalign 0.7
        yalign 1.0
    joh "It’s at Alpha Kappa Kappa, and we wanted to celebrate our quest"

    show cole neutral with moveinbottom:
        xalign 1.2
        yalign 1.0

    col "We’ve made it pretty far in such a short amount of time here"
    hide cole neutral
    show cole happy:
        xalign 1.2
        yalign 1.0
    col "so we figured we’d go out tonight!"
    stu "Alpha Kappa Kappa??"

    show pink andrew mad
    andy "Yeah, turns out that even a school of research centric nerds still
        love frat parties"

    show liben mad:
        xalign -0.3
    lib "I CAN’T WAIT FOR THEM TO PLAY MO BAMBA"

    show james neutral:
        xalign 0.5
    jam "I’m not normally one to go..."
    show james happy:
        xalign 0.5
    jam "but with all of you, it sounds like it could be fun"
    show pink andrew neutral
    andy "What do you say, STUDENT? Are you in?"

    menu:
        "Go to AKK. (lose 30 energy for the next day)":
            jump choice_frat_yes

        "Stay in and go to bed":
            jump choice_frat_no

label choice_frat_yes:

    $energy -= 30

    stu "You know what, let’s do it~!"

    show pink andrew happy:
        xalign 0.25
        yalign 1.0
    andy "YAAAAAAAAAAS!!!!!"
    show liben happy:
        xalign -0.5
        yalign 1.0
    lib "WOOOHOOOO"

    scene bg frat
    play music "music/groovy.mp3"
    show pink andrew happy:
        xalign -0.1
        yalign 1.0
    show james neutral:
        xalign 0.2
        yalign 1.0
    show john sad:
        xalign 0.5
        yalign 1.0
    andy "JAMES, ARE YOU HAVING A GOOD TIME?"
    show james happy:
    jam "NO I’M NOT ON PRIME, I DON’T REALLY USE AMAZON"
    stu "MAN DO ALL THESE PARTIES LOOK LIKE THIS????"
    show john neutral:
    joh "SOMETIMES PEOPLE STAGE DIVE"
    show cole happy with moveintop:
        yzoom -1.0
        yalign 0.0
        xalign 1.0
    col "WOOOOOHOOOOOOO!!!! I LOVE IT HERE"

    show liben mad with moveinbottom
    lib "MO BAMBA BABYYYYYY"
    hide liben mad with moveoutbottom
    stu "(man, frat parties sure are weird)"
    show pink andrew sad
    andy "THIS SONG MAKES ME FEEL SO ALIIIIIVE"
    col "YO I THINK I RECOGNIZE THAT GUY FROM MY ART CLASS"
    col "YO XAVIER!"
    hide cole happy with moveoutright
    show james scared
    jam "I LOVE YOU GUYS"
    show john mad
    joh "why are we screaming"
    show liben mad with moveinbottom
    lib "YO I HATE THIS SONG NOW"

    jump choice_frat_done

label choice_frat_no:

    stu "Interview day is pretty soon, I think I’m gonna take it easy and stay
        in tonight, sorry guys."
    show andy happy
    andy "oh, okay, suit yourself, best of luck, we’ll let you know what
        happens~!"
    show liben happy
    lib "LATER!"
    show cole mad
    col "We’ll pour one out for you!"
    show james happy
    jam "Have a good night, Student!"
    show john neutral
    joh "bye."

    hide liben happy with moveoutright
    hide andy happy with moveoutright
    hide james happy with moveoutright
    hide john neutral with moveoutright
    hide cole mad with moveoutbottom

    stu "Bye guys."

    jump choice_frat_done

label choice_frat_done:

     jump overworld_test




label day_15:

    $energy = min(energy + 70, maxenergy)

    call bedroom from _call_bedroom_13

#INTERVIEW#

    if tac_pts >= 500:
        jump best_ending
    else:
        jump worst_ending

label best_ending:
    #beginning of good ending
    scene bg
    show tacoma happy
    tac "Well, Student, thank you so much for coming in to talk!"
    stu "Of course, Professor!  I know I’m still pretty new here"
    stu "but I’ve really appreciated getting to know you over the course of the quarter."
    show tacoma neutral
    tac "I have too, Student!  You’ve put in a lot of work and seem to have really shown an interest in what we’re doing here.  That’s great to see!"
    stu "Um, does that mean I got the job?"
    show tacoma happy with dissolve
    tac "Haha, Student"
    tac "...well."
    show stu_n with hpunch
    tac "yes, I would like to offer you a position as a research assistant!"
    play music "music/success.mp3"
    tac "...if you are interested of course..."
    tac"  I think you can be a valuable addition to the team and hopefully get a lot out of working with us!"
    tac "Congratulations!"

    scene bg main quad
    show liben neutral with moveinbottom:
        xalign -0.3
        yalign 1.0
    show james neutral with moveinbottom
    show pink andrew neutral with moveinbottom:
        xalign 0.2
        yalign 1.0
    show cole neutral with moveinright:
        xalign 0.9
        yalign 1.0
    show john neutral with moveinright:
        xalign 1.0
        yalign 1.0

    lib "sooooo...?"
    lib "how'd it go...?"
    stu "...you guys...I...I..."
    joh "Student..."
    andy "It's okay..."
    stu "I GOT IT! I GOT RESEARCH WITH TACOMA!"
    show liben mad with hpunch
    lib "YAAAAAAAAAAH STUDENT HYAAAAAAH"
    show pink andrew happy
    andy "You did it!! I'm so proud of you, Student"
    show john happy
    joh "A job well done"
    show james happy
    jam "We knew you could do it"
    show cole sad
    col "nice, Student..."
    show cole happy
    col "nice"
    stu "I really couldn't have done it without all of you guys"
    stu "I really couldn't..."
    jam "We need to celebrate now!"
    lib "WITH DRANKS!!!!"
    show pink andrew mad
    andy "liben..."
    show liben happy
    lib "haha just kidding"
    show liben spicy
    lib "not really."

    scene jagoda finale
    show stu_n with dissolve

    stu "Wow!  To finish off a great first quarter at UKokoro, I found a research position!"
    stu "It’s really exciting to see hard work rewarded, especially when it’s hard work I have enjoyed so much!"
    stu "I really am thankful for the relationship I have been able to develop with Professor Tacoma."
    stu "It’s important to work with people that you really feel you can trust!"
    stu "and those boys...I'm so happy that I got to meet them, They’re the ones that inspired me to go after this in the first place!"
    stu "We may all be a little busy next quarter with our various research positions,"
    stu "but I won’t let myself get so caught up I don’t have time to spend with them."
    stu "Who could ask for a better crew?"


    jump game_done

    #end of good ending

label worst_ending:
#begining of bad ending
    scene bg
    show tacoma neutral
    tac " Well, Student, thank you so much for coming in to talk."
    stu "Of course, professor!  I really appreciate you inviting me when I’m still pretty new."
    tac "Hey, if I wasn’t willing to reach out, I’d never meet anybody new, would I?"
    stu "I guess that’s true."
    tac "So, like I said, I really appreciate you coming in and think you have shown a lot of potential…"
    tac "Right now, though, I don’t think I’d be ready to offer you a research position here."
    tac "I know this can be hard to hear, but I really encourage you to keep in touch.  It seems like you just need a little bit more time to familiarize yourself with what we do and how we work here, so I’d love to see you apply again next quarter."
    stu "Oh, okay, professor...thank you…"

    scene bg main quad
    show liben happy with moveinbottom:
        xalign -0.3
        yalign 1.0
    show james happy with moveinbottom
    show pink andrew happy with moveinbottom:
        xalign 0.2
        yalign 1.0
    show cole happy with moveinright:
        xalign 0.9
        yalign 1.0
    show john happy with moveinright:
        xalign 1.0
        yalign 1.0

    lib "Student!"
    joh "Hello."
    stu "Guys!  What are all you doing here?"
    jam "We wanted to see you after your interview!"
    stu "You guys...You’re so sweet."
    col "We know you worked so hard for all of this, and we thought it was the least we could do."
    show pink andrew neutral
    andy "so…? How’d it go?"

    stu "...I didn’t get it."
    show liben mad with hpunch
    lib "WHAT!? YOU DIDN’T GET IT!???? BUT YOU’RE SMARTER THAN ALL OF US"
    show cole mad
    col "Liben!"
    show liben mad with hpunch
    lib "Am i wrong????"
    show pink andrew mad
    andy "I must say, I’m a little bit surprised too..."
    show pink andrew neutral
    andy "Are you doing alright?"
    stu "Actually...I feel totally fine."
    show james scared
    jam "Hey you worked really hard… and I’m sure that you put up a good fight and…"
    show john neutral
    joh "Student...you’re not sad?"
    stu "not really."
    andy "what…?"
    stu "Obviously, it doesn’t feel great to get declined, but I don’t really feel all that defeated…"
    show liben thinking
    lib "wait but you don’t have any work for the summer, no idea of where you could possibly go in life and no money for christmas presents!!!!"
    show cole sad
    col "LIBEN"
    stu "Hahahaha"
    show james neutral
    jam "She’s....laughing?"
    show cole neutral
    col "must have completely lost her mind"
    andy "Student, what’s so funny?"
    stu "You guys are the best!  I really am fine. I’m just happy that I got
        this opportunity in the first place."
    stu "Finding research is super
        difficult, especially alongside having to balance so many things;  so
        I’m happy that I had all of you here to guide me all the way through…"
    andy "Student…"
    hide andy
    hide col
    hide lib
    hide jam
    hide joh

    stu "So, to conclude my first quarter at UKokoro, I didn’t get a position
        right away. And honestly, at the end of the day, I don’t feel too
        bad about that."
    stu "I’m just happy that I got the opportunity to meet so
        many colorful and exciting people here at university and I have faith
        that the relationships I develop right now are gonna help me out later."
    stu "I can always pursue research next quarter!"

    jump game_done

    #end of bad ending

label game_done:
"GAME OVER"
