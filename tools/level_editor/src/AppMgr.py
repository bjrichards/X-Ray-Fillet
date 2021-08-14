# Created by Braeden Richards
# Created on August 5th, 2021


# Includes
from .utils.spritesheet import SpriteSheet
from .sprites import Sprite
import json
from pygame import transform
from math import floor
from os import path


# Class
class AppMgr():
    def __init__(self, engine):
        self.engine = engine
        self.app_status = None
        self.uid = 0

        self.asset = {}

        self.selected_sprite = None
    
    def initialize(self):
        self.app_status = "MAIN"
        
        for file in self.engine.config.sources:
            # Load source name
            source_name = file[0]

            # Load source type
            source_type = file[1]

            # Load Spritesheet
            self.spritesheet = SpriteSheet(file[2])

            # Load each position of sprite
            f = open(file[3],)
            self.data = json.load(f)
            f.close()
            self.asset.update(self.data['positions'])

            # Load the tiles from spritesheet into sprites array
            index_y = 10
            index_x = 0
            for id in self.asset:
                position = self.asset[id]
                new_image = self.spritesheet.get_image(position[0], position[1], position[2], position[3])
                new_image.set_colorkey( (0, 0, 0) )
                new_image = transform.scale2x(new_image)
                temp = Sprite(self.engine, new_image, (position[2], position[3]), id, 
                                self.engine.gfx_mgr.select_window, ((10 + (index_x * 70), index_y)),
                                (32, 32))
                temp.entity_type = self.asset[id]
                temp.source_name = source_name
                temp.source_type = source_type
                self.engine.entity_mgr.sprites.append(temp)
                if index_x < 4:
                    index_x += 1
                else:
                    index_x = 0
                    index_y += 70

            # Load file if exists
            if path.exists('data\\maps\\' + self.engine.map_file):
                fi = open('data/maps/' + self.engine.map_file)
                temp_dict = json.load(fi)
                for id in temp_dict:
                    entity_type = temp_dict[id][0]
                    position = temp_dict[id][1]
                    sprite = []
                    sprite[:] = [sprite_t for sprite_t in self.engine.entity_mgr.sprites if entity_type == sprite_t.entity_type]
                    temp_placed_sprite = Sprite(self.engine, sprite[0].image, sprite[0].size, self.uid,
                                            self.engine.gfx_mgr.window, position, (32, 32))
                    temp_placed_sprite.entity_type = sprite[0].entity_type
                    self.uid += 1
                    self.engine.entity_mgr.layer_0_placed_sprites.append(temp_placed_sprite)
    

    def tick(self, dt):
        if self.app_status == "MAIN":
            pass


    def shutdown(self):
        pass


    def place_block(self, mouse_pos):
        if self.selected_sprite is not None:
            # clean mouse x pos to get proper position of window
            mouse_cleaned = (mouse_pos[0] - self.engine.gfx_mgr.select_window.get_size()[0], mouse_pos[1])

            # Make sure no sprite is there currently before placing
            placed_sprites = []
            placed_sprites[:] = [sprite for sprite in self.engine.entity_mgr.layer_0_placed_sprites if (sprite.is_clicked((mouse_cleaned[0], mouse_cleaned[1])))]

            if len(placed_sprites) == 0:

                # Find which tile mouse click is in
                mouse_cleaned_grid = (floor(mouse_cleaned[0] / 64), floor(mouse_cleaned[1] / 64))

                new_sprite = Sprite(self.engine, self.selected_sprite.image, self.selected_sprite.size,
                                self.uid, self.engine.gfx_mgr.window, 
                                    (mouse_cleaned_grid[0] * 64, mouse_cleaned_grid[1] * 64), (64, 64))
                new_sprite.entity_type = self.selected_sprite.entity_type
                self.engine.entity_mgr.layer_0_placed_sprites.append(new_sprite)
                self.uid += 1
        else:
            print("No Sprite Selected")
    
    def remove_block(self, mouse_pos):
        # clean mouse x pos to get proper position of window
        mouse_cleaned = (mouse_pos[0] - self.engine.gfx_mgr.select_window.get_size()[0], mouse_pos[1])

        # Remove block from list if exists
        self.engine.entity_mgr.layer_0_placed_sprites[:] = [sprite for sprite in self.engine.entity_mgr.layer_0_placed_sprites if not (sprite.is_clicked((mouse_cleaned[0], mouse_cleaned[1])))]