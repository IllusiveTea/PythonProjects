import random
'''
ELO CALULCATION



ScoreToGive = Qa / (Qa+Qb)

Qa = 10 ^ Ra/400
Qb = 10  Rb/400

Ra = Player 1 rating
Rb = Player 2 rating

'''

players = { "p":2400, "p2":2000}
games = { "p":0, "p2":0 }

#http://en.wikipedia.org/wiki/Elo_rating_system#Most_accurate_K-factor
def calculateKFactor(playername):
    if (games[playername] < 2100):
        return 32
    elif(games[playername] >= 2100 and games[playername] <= 2400):
        return 24
    elif(games[playername] > 2400):
        return 16
    return 32 #Default value


def addPlayer ( name, score=1445 ):
    players[name] = score
    games[name] = 0
    print("Added {n} to players with score {s}".format(n=name, s=score))

def play( player1, player2 ):
    win = random.randint(0,2)
    #Increase games played (comes in handy later)    

    games[player1] = games[player1]+1
    games[player2] = games[player2]+1
    
    transformed_rating_1 = 10**(players[player1]/400) # 10^(currentRating/400)
    transformed_rating_2 = 10**(players[player2]/400)

    expected_1 = round(transformed_rating_1 / (transformed_rating_1 + transformed_rating_2),2)
    expected_2 = round(transformed_rating_2 / (transformed_rating_1 + transformed_rating_2),2)

    s1 = 0
    s2 = 0
    if (win == 0): #Player 1 wins
        s1 = 1
        s2 = 0
        print("Player 1 ({p}) won!".format(p=player1))
    elif (win == 1): #Draw
        s1 = 0.5
        s2 = 0.5
        print("Draw!")
    elif (win == 2): #Player 2
        s2 = 1
        s1 = 0
        print("Player 2 ({p}) won!".format(p=player2))
    print("Win ", win)
    new_1 = round(players[player1] + calculateKFactor(player1) * (s1 - expected_1), 1)
    new_2 = round(players[player2] + calculateKFactor(player2) * (s2 - expected_2), 1)

    print("\r\n{name} ({cur}): Tranformed: {trans} | Results: {exp}:{act} | Updated: {new}  "
          .format(name=player1, cur=players[player1],
                  trans=transformed_rating_1, exp=expected_1,
                  act=s1, new=new_1))
    print("\r\n{name} ({cur}): Tranformed: {trans} | Results: {exp}:{act} | Updated: {new}  "
          .format(name=player2, cur=players[player2],
                  trans=transformed_rating_2, exp=expected_2,
                  act=s2, new=new_2))
    
    players[player1] = round(new_1, 0)
    players[player2] = round(new_2, 0)
def checkPlayersExist(p1, p2):
    return (p1 in players.keys()) and (p2 in players.keys())

def playGame():
    answer = input("Who should play? (Enter \"random\" to randomly select >>")
    if (answer == "random"):
        player_list = list(players.keys())
        player1 = player_list[ random.randint(0, len(player_list)-1) ]
        player2 = player_list[ random.randint(0, len(player_list)-1) ]
        print("{player_1} ({cur_1}) vs {player_2} ({cur_2})".format(
            player_1=player1, player_2=player2, cur_1=players[player1],
            cur_2=players[player2]))
        play(player1, player2)
    else:
        p2 = input("Against? >> " )
        if (checkPlayersExist(answer, p2)):
            print("Playing..")
            play(answer, p2)
        else:
            print("Sorry either \"{player1}\" or \"{player2}\" don't exist")

def main():
    while True:
        print("====== Options ======\r\n")
        print("1. Add player")
        print("2. Play a game")
        print("3. See available players")
        input_num = int(input("Please choose an option >> "))
        if (input_num == 1):
            print("Chosen add player")
            name = input("Enter name >> ")
            addPlayer(name)
        elif ( input_num == 2):
            print("Chosen play game")
            playGame()
        elif ( input_num == 3):
            print("Chosen see players")
            print (players.keys())
        else:
            print("\r\n======= ERROR: ========\r\n   Invalid option")

if __name__ == "__main__":
    main()
