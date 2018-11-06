import os
import subprocess
import requests
import time
import datetime


script_dir = os.path.dirname(os.path.abspath(__file__))
game_count = 14 ### The number of total games expected in one day
current_date = datetime.date.today()
date_string = "%s%s%s" % (current_date.strftime('%Y'), current_date.strftime('%m'), current_date.strftime('%d'))
# date_string = "20180930" ### Used for testing


################################################################################
# Classes
################################################################################


class Team:
    def __init__(self, abbr):
        self.abbr = abbr
        self.score = 0
        self.json_id = -1

    # Find the correct JSON ID from nfl.com by checking for the provided team.abbr
    def find_json_id(self):
        while self.json_id == -1:
            for count in range(game_count):
                try:
                    request = requests.get(url='http://www.nfl.com/liveupdate/game-center/' + date_string + "%02d" % count + '/' + date_string + "%02d" % count + '_gtd.json')

                    # If the team we're looking for is found in the returned JSON,
                    # set the team.json_id
                    if '"' + self.abbr + '"' in request.text:
                        self.json_id = count
                        return
                except requests.exceptions.RequestException as e:
                    print("CONNECTION ERROR: " + str(e))

            # Sleep for a bit to be nice to the NFL servers if the JSON files
            # havent been posted yet
            time.sleep(60.0)


################################################################################
# Functions
################################################################################

# Check for an available connection to nfl.com by sending a single ping and
# returning True and playing a notification sound if it returns
def check_connection():
    if subprocess.call(['ping', 'nfl.com', '-c', '1']) == 0:
        subprocess.call(['aplay', script_dir + '/whistle.wav'])
        return True


# Check both "home" and "away" fields in the provided JSON for the desired team
# and return its total overall game score
def get_score(team):
    # fetch the JSON file from nfl.com then parse out the score
    request = requests.get(url='http://www.nfl.com/liveupdate/game-center/' + date_string + "%02d" % team.json_id + '/' + date_string + "%02d" % team.json_id + '_gtd.json')

    if request:
        if request.json()[date_string + "%02d" % team.json_id]['home']['abbr'] == team.abbr:
            return int(request.json()[date_string + "%02d" % team.json_id]['home']['score']['T'])
        else:
            return int(request.json()[date_string + "%02d" % team.json_id]['away']['score']['T'])


# Simple score check to determine if the score has increased. Return True
# if it has
def cheer_check(current_score, team):
    if current_score > team.score:
        return True


# Has the cheerbot.conf file for user configurable settings
def config_file_hash():
    config_hash = {}

    with open(script_dir + '/cheerbot.conf') as config_file:
        for line in config_file:
            line_key = line.split("=")[0]
            line_value = line.split("=")[1].rstrip()
            config_hash[line_key] = line_value

        return config_hash
