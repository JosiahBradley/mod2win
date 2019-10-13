class Mod:
    num_coins = 15
    jump_speed = 25

    @staticmethod
    def collect_coin(color):
        if color == 'blue':
            return 99
        if color == 'gold':
            return 99
        if color == 'green':
            return 99
        if color == 'orange':
            return 99
        if color == 'pink':
            return 99
        if color == 'purple':
            return 99
        if color == 'red':
            return 99

    @staticmethod
    def win():
        # return False
        return True
