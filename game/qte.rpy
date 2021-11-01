screen qte_keyboard:
    #key input qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_keyboard')])

    key trigger_key action (Play("sound", "music/hit.mp3"), Return(1) )
    #Add Play("sound", "sounds/hit.mp3") when i can add sound

    vbox:
        xalign x_align
        yalign y_align
        spacing 25


        text trigger_key:
            xalign 0.5
            color "#0000ff"
            size 45


        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"



screen qte_button:


    button:
        action Return(0)
        align 0.5, 0.5
        background "images/transparent.png"



    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start', time_start - interval), false=[Return(0), Hide('qte_button')])


    vbox:
        xalign x_align yalign y_align spacing 25

        button:
            action Return(1)
            xalign 0.5
            xysize 125, 125
            background Animation("#000", 1, "images/jagoda_reacts.jpg", 1, "#fff", 1, "images/jagoda_reacts.jpg", 1)
            activate_sound "music/hit.mp3"



        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
