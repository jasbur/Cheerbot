This is the main Cheerbot program to check the NFL.com Gamecenter JSON for the
desired team and trigger a "Cheer" if they score. You can simply run the `cheerbot.py`
script, but I recommend running the `cheerbot_bootstrapper.py` which will recover
the main script from any crashes that might be caused by a malformed response from NFL.com.

Cheerbot will cheer for whichever team you have specified in the cheerbot.conf
file in this directory.

When a cheer is triggered the play_animation function will be called from 
animation.py You can have anything occur here really (play sounds, blink lights, etc.)
The servo_animation_example/servo_animation_example.py file demonstrates the use
of servos synchronized with .wav audio files. This is the setup I use on my Cheerbot.

cheerbot.conf file:

    "team=": The NFL abbreviation for the team you want Cheerbot to cheer for.
    (e.g. GB is the Green Bay Packers)

    "score_check_delay=": The delay in seconds between each score check against
    the NFL's Gamecenter JSON feed.

    "broadcast_delay=": The number of seconds to delay before cheering after a
    new score is detected. This can help account for a broadcast delay. The NFL
    JSON is updated almost instantly after a score is made official, but the
    video feed you're watching may be delayed by several seconds. This can
    sometimes result in CHeerbot predicting the future by cheering for a score
    before you see it on your video feed.
