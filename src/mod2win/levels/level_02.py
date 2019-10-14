import arcade
from mod2win.levels.BaseLevel import BaseLevel
from mod2win.mods.level2 import Mod
import time


class L2(BaseLevel):
    def __init__(self, speed, title):
        super().__init__(speed=speed, title=title)
        self.exit = None
        self.gate = None
        self.start = time.time()
        self.duration = 30

    def draw_map(self):
        super().draw_map()
        # Exit Door
        door = self.tile_sprite('signExit')
        door.center_x = 14 * self.conf.TILE_RADIUS
        door.center_y = 185
        self.assets["statics"].append(door)
        self.exit = door

        # Gate
        self.gate = []
        for y in range(2 * self.conf.TILE_RADIUS, 10 * self.conf.TILE_RADIUS, 2 * self.conf.TILE_RADIUS):
            g = self.tile_sprite('stoneCenter_rounded')
            g.center_x = 10 * self.conf.TILE_RADIUS
            g.center_y = y
            self.assets["block"].append(g)
            self.gate.append(g)

    def update(self, delta_time):
        super().update(delta_time=delta_time)
        if self.is_game_over:
            return

        # Need game over condition, probabaly time based
        if time.time() > self.start + self.duration:
            self.game_over()

        if self.player.center_x > self.exit.center_x:
            self.win()

        if Mod is not None:
            Mod.lift_gate(self.gate)
        for g in self.gate:
            if g.center_y > self.conf.TILE_RADIUS * 8:
                g.center_y = self.conf.TILE_RADIUS * 8

    def on_draw(self):
        super().on_draw()
        if self.is_game_over:
            arcade.draw_text(
                "YOU WIN",
                self.view_left + self.get_size()[0] * .5,
                self.view_bottom + self.get_size()[1] * .5,
                arcade.csscolor.ORANGE_RED, 32
            )

    def win(self):
        super().win()
        self.audio("gameover1")
        self.score += 1000


def main():
    """ Main method """
    window = L2(speed=1.7, title="LEVEL 2: GATE")
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
