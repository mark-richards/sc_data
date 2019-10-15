import csv
import glob
import time


column_header_names = [
    'Fanfooty Match ID',
    'Round',
    'Year',
    'Player ID',
    'First Name',
    'Surname',
    'Team',
    'null',
    'DT',
    'SC',
    'null2',
    'null3',
    'null4',
    'Kicks',
    'Handballs',
    'Marks',
    'Tackles',
    'Hitouts',
    'Frees for',
    'Frees against',
    'Goals',
    'Behinds',
    'Not sure',
    'Tag',
    'Tag Notes',
    'Tag 2',
    'Tag 2 Notes',
    'null5',
    'null6',
    'null7',
    'null8',
    'Position',
    'Jumper Number',
    'null9',
    'null10',
    'null11',
    'DT own %',
    'SC own %',
    'AF own %',
    'null12',
    'AF Breakeven',
    'null13',
    'Contested Possessions',
    'Clearances',
    'Clangers',
    'Disposal efficiency',
    'Time on ground',
]


def get_number_of_lines_in_file(data):
    return len(data.split('\n'))


def get_url_of_match(data):
    name = data.split('\n', 1)[0]
    url = "http://live.fanfooty.com.au/game/matchcentre.html?id=" + name[-8:-4]
    return url


def get_round(data):
    line = data.split('\n', 1)[1]
    stripped_line = [x.strip() for x in line.split(',')]
    afl_round = stripped_line[4]
    return afl_round


def get_year(data):
    second_line = data.splitlines()[2]
    stripped_second_line = [x.strip() for x in second_line.split(',')]
    afl_year = stripped_second_line[1]
    return afl_year


def get_match_data_list():
    data_list = []
    path = "C:\\Users\Richa\Dropbox\Supercoach\All Match Data\*.txt"
    # path = "C:\\Users\Richa\Dropbox\Supercoach\2019\2019 match files after rd 15\*.txt"


    for item in glob.glob(path):
        file = open(item, 'r')
        name = file.name
        data = file.read()
        data_list.append(name + '\n' + data)
    return data_list


def return_player_match_data(data_list):
    player_data_for_match = []

    for match in data_list:
        number_of_lines = get_number_of_lines_in_file(match)
        afl_round = get_round(match)
        afl_year = get_year(match)
        name = get_url_of_match(match)

        for line in range(5, number_of_lines - 1):
            line_data = match.splitlines()[line]
            line_data = [x.strip() for x in line_data.split(',')]
            line_data = [name] + [afl_round] + [afl_year] + line_data
            player_data_for_match.append(line_data)
    return player_data_for_match


def write_to_csv(data):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    with open("outputs/match_data_{}.csv".format(timestr), "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(column_header_names)
        for item in data:
            writer.writerow(item)
            print(item)


match_data_list = get_match_data_list()
player_data = return_player_match_data(match_data_list)
write_to_csv(player_data)
