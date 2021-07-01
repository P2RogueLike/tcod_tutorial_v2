import tcod

import game.entity
import game.game_map
import game.input_handlers


class Engine:
    game_map: game.game_map.GameMap
    player: game.entity.Entity

    def render(self, console: tcod.Console) -> None:
        self.game_map.render(console)