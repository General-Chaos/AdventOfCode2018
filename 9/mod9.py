class marble_circle():

    def __init__(self):
        self.circle = [0]
        self.current_marble_index = 0

    def add_marble(self, marble_value):
        if (marble_value % 23) == 0:
            remove_index = self.current_marble_index - 7
            if remove_index < 0:
                self.current_marble_index = len(self.circle) + remove_index
            else:
                self.current_marble_index = remove_index
            return marble_value + self.circle.pop(self.current_marble_index)
        else:
            new_index = self.current_marble_index + 1
            if new_index > (len(self.circle) -1):
                new_index = 0
            else:
                pass
            self.circle.insert((new_index + 1), marble_value)
            #self.circle = self.circle[:new_index + 1] + [marble_value] + self.circle[new_index + 1:]
            self.current_marble_index = new_index + 1
            return 0


def play_marbles(players, max_score):
    player_dict = dict()
    for i in range(players):
        player_dict.update({i: 0})
    game = marble_circle()
    marble = 1
    while marble <= max_score:
        for k in player_dict.keys():
            if marble <= max_score:
                player_dict[k] += game.add_marble(marble)
            else:
                pass
            marble += 1
#            print(game.circle)
    return player_dict

if __name__ == '__main__':
    assert max((play_marbles(9, 25).values())) == 32
    assert max(play_marbles(10, 1618).values()) == 8317
    assert max(play_marbles(13, 7999).values()) == 146373
    assert max(play_marbles(17, 1104).values()) == 2764
    assert max(play_marbles(21, 6111).values()) == 54718
    assert max(play_marbles(30, 5807).values()) == 37305
