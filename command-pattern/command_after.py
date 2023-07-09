import pygame as pg
from abc import ABC, abstractmethod
from dataclasses import dataclass
import random


@dataclass
class Player:

    pos: pg.Vector2
    surface: pg.Surface

    def __init__(self, screen_width: int, screen_height: int):
        self.pos = pg.Vector2(screen_width / 2, screen_height / 2)
        self.surface = pg.Surface((100, 100))
        self.surface.fill("Red")


@dataclass
class Command(ABC):

    player: Player

    @abstractmethod
    def execute(self):
        pass


@dataclass
class MoveUpCommand(Command):

    def execute(self, dt):
        self.player.pos.y -= 300 * dt


@dataclass
class MoveDownCommand(Command):

    def execute(self, dt):
        self.player.pos.y += 300 * dt


@dataclass
class MoveLeftCommand(Command):

    def execute(self, dt):
        self.player.pos.x -= 300 * dt


@dataclass
class MoveRightCommand(Command):

    def execute(self, dt):
        self.player.pos.x += 300 * dt


@dataclass
class SwitchColorCommand(Command):
    colors = ["Red", "Yellow", "Blue", "White", "Green", "Purple", "Orange"]
    last = pg.time.get_ticks()
    cooldown: int = 5000

    def execute(self):
        if pg.time.get_ticks() - self.last >= self.cooldown:
            self.player.surface.fill(random.choice(self.colors))
            self.last = pg.time.get_ticks()


@dataclass
class InputHandler:
    """Represents an input handler"""
    btn_w: Command
    btn_s: Command
    btn_a: Command
    btn_d: Command
    btn_space: Command

    def handle_input(self, dt):
        """Delegate input to the commands."""
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.btn_w.execute(dt)
        if keys[pg.K_s]:
            self.btn_s.execute(dt)
        if keys[pg.K_a]:
            self.btn_a.execute(dt)
        if keys[pg.K_d]:
            self.btn_d.execute(dt)
        if keys[pg.K_SPACE]:
            self.btn_space.execute()


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1280, 720))
        self.title = pg.display.set_caption("Command Pattern: After")
        self.clock = pg.time.Clock()
        self.running = True
        self.dt = 0

        self.player = Player(
            screen_width=self.screen.get_width(),
            screen_height=self.screen.get_height()
        )
        self.ih = InputHandler(
            MoveUpCommand(self.player),
            MoveDownCommand(self.player),
            MoveLeftCommand(self.player),
            MoveRightCommand(self.player),
            SwitchColorCommand(self.player)
        )

    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

            self.screen.fill("black")

            self.screen.blit(self.player.surface, self.player.pos)
            self.ih.handle_input(self.dt)

            pg.display.flip()
            self.dt = self.clock.tick(60) / 1000

        pg.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
