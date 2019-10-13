class Mod:
    num_coins = 15
    jump_speed = 35

    @staticmethod
    def collect_coin(color):
        if color == 'blue':
            return 9
        if color == 'gold':
            return 9
        if color == 'green':
            return 9
        if color == 'orange':
            return 9
        if color == 'pink':
            return 9
        if color == 'purple':
            return 9
        if color == 'red':
            return 9

    @staticmethod
    def win():
        # return False
        return True
