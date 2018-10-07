import time
import lib
from lib import Team
import animation

lib.check_connection() ### Check for active internet connection
config_hash = lib.config_file_hash()

initial_score_check = False
team = Team(config_hash['team'])
team.find_json_id()

# Main execution loop
while True:
    current_score = lib.get_score(team)
    print("####Current score: " + str(current_score))

    # Call cheer_check and equalize the previous and cureent scores then cheer
    if lib.cheer_check(current_score, team):
        team.score = current_score

        #If we start in the middle of a game don't cheer on the initial score check
        if initial_score_check == False:
            time.sleep(int(config_hash['broadcast_delay']))
            animation.play_animation()
            time.sleep(1.0)

    initial_score_check = False

    time.sleep(int(config_hash['score_check_delay']))
