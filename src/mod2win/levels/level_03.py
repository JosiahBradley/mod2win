import arcade
from mod2win.levels.BaseLevel import BaseLevel
from mod2win.mods.level3 import  Mod
import random
import time


class L3(BaseLevel):
    def __init__(self, speed, title):
        super().__init__(speed=speed, title=title)
        try:
            self.jump_speed = max(min(Mod.jump_speed, 35), 5)
        except AttributeError:
            self.jump_speed = 5
        self.exit = None
        try:
            self.num_coins = max(min(Mod.num_coins, 50), 5)
        except AttributeError:
            self.num_coins = 5
        self.coin_count = 0
        self.score_msg = None
        self.pending_win = False
        self.pending_loss = False
        self.goal = self.num_coins * 40

    def draw_map(self):
        super().draw_map()
        # Exit Door
        door = self.tile_sprite('signExit')
        door.center_x = 20 * self.conf.TILE_RADIUS
        door.center_y = 185
        self.assets["statics"].append(door)
        self.exit = door

        # Coins
        # Randomly draw some coins around the map in places that are reachable (enough)
        centers = []
        for x in range(2, 19):
            for y in range(7, 13):
                centers.append((x, y))
        # Guarantee unique centers.
        centers = random.choices(centers, k=self.num_coins)
        for x, y in centers:
            color = random.choice(['blue', 'gold', 'green', 'orange', 'pink', 'purple', 'red'])
            coin = self.obj_sprite(color + "_coin")
            coin.center_x = x * self.conf.TILE_RADIUS
            coin.center_y = y * self.conf.TILE_RADIUS
            coin.scale = 0.4
            coin.coin_color = color
            self.assets['objects'].append(coin)

    def update(self, delta_time):
        super().update(delta_time=delta_time)
        if self.is_game_over:
            return

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player, self.assets['objects'])

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.kill()
            self.coin_count += 1
            try:
                self.score += max(min(Mod.collect_coin(coin.coin_color), 55), 5)
            except AttributeError:
                self.score += 5
            if self.coin_count == self.num_coins and self.score < self.goal:
                self.pending_loss = True
                self.score_msg = time.time()
                return

        if not self.pending_loss and not self.pending_win and\
            self.player.center_x > self.exit.center_x:
            self.win()

        if self.pending_win is True:
            if self.score_msg and self.score_msg < time.time() - 3:
                # Clear msg
                arcade.set_background_color(arcade.color.SKY_BLUE)
                self.pending_win = False
                self.score_msg = None

        if self.pending_loss is True:
            if self.score_msg and self.score_msg < time.time() - 3:
                arcade.set_background_color(arcade.color.SKY_BLUE)
                self.pending_loss = False
                self.pending_win = False
                self.score_msg = None
                self.score = 0
                self.coin_count = 0
                self.game_over()

    def on_draw(self):
        super().on_draw()
        if self.is_game_over:
            arcade.draw_text(
                "YOU WIN",
                self.view_left + self.get_size()[0] * .5,
                self.view_bottom + self.get_size()[1] * .5,
                arcade.csscolor.ORANGE_RED, 32
            )

        if self.pending_win is True:
            arcade.draw_text(
                f"You need a score of at least {self.goal} to win!",
                self.view_left + self.get_size()[0] * .15,
                self.view_bottom + self.get_size()[1] * .5,
                arcade.csscolor.DARK_ORANGE, 32
            )

        if self.pending_loss is True:
            arcade.draw_text(
                f"You need a score of at least {self.goal} to win,\n but you ran out of coins.\n Restarting Level",
                self.view_left + self.get_size()[0] * .15,
                self.view_bottom + self.get_size()[1] * .8,
                arcade.csscolor.DARK_ORANGE, 32
            )

    def win(self):
        # Check if win condition is met from Mod
        if Mod is not None and Mod.win() is True and self.score > self.goal:
            super().win()
            self.audio("gameover1")
        else:
            self.player.center_x = self.conf.PLAYER_START_X
            self.pending_win = True
            self.score_msg = time.time()


def main():
    """ Main method """
    window = L3(speed=5.0, title="LEVEL 3: COINS")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
