import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1280, 720))
        self.title = pg.display.set_caption("Command Pattern: Before")
        self.clock = pg.time.Clock()
        self.running = True
        self.dt = 0

        self.player_pos = pg.Vector2(
            self.screen.get_width() / 2,
            self.screen.get_height() / 2
        )
        self.player_img = pg.Surface((100, 100))
        self.player_img.fill("Red")

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill("black")

            self.screen.blit(self.player_img, self.player_pos)

            keys = pg.key.get_pressed()
            if keys[pg.K_w]:
                self.player_pos.y -= 300 * self.dt
            if keys[pg.K_s]:
                self.player_pos.y += 300 * self.dt
            if keys[pg.K_a]:
                self.player_pos.x -= 300 * self.dt
            if keys[pg.K_d]:
                self.player_pos.x += 300 * self.dt

            pg.display.flip()
            self.dt = self.clock.tick(60) / 1000

        pg.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
