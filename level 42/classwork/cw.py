def points(games):
    score = 0
    for game in games:
        if game[0] > game[2]:
            score += 3
        if game[0] == game[2]:
            score += 1
        if game[0] < game[2]:
            score += 0
        return score
    

def fake_bin(number_string):
    binary_string = ''
    for number in number_string:
        if int(number) < 5:
            binary_string += '0'
        else:
            binary_string += '1'

def goals(laLiga, copaDelRey, championsLeague):
    return  laLiga + copaDelRey + championsLeague