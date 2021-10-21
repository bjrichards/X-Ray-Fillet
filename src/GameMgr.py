# Created by Braeden Richards
# Created on January 5th, 2021
# Desc:


# Includes
from .utils.spritesheet import SpriteSheet
from .Entities.Enemy import Enemy
from .Entities.Player import Player
from .Entities.Platform import Platform
from .Entities.sprites import Sprite
from pygame import transform
from os import path
import json

# Class
class GameMgr():
    def __init__(self, engine):
        self.engine = engine

        self.platforms_layer_0 = []
        self.platforms_layer_1 = []
        self.game_status = None
        self.player_load_pos = None
        self.player_lives = 10
        self.goal = None

        self.spritesheet = None
        self.spritesheet_character_running = None
        
        self.current_level = 0
        self.max_level = 3
    
    def initialize(self):
        self.game_status = 'MENU'
        # self.spritesheet = SpriteSheet("assets\\img\\game\\spritesheet.bmp")
        self.spritesheet_character_running = SpriteSheet("assets\\img\\game\\player_running.bmp")


    def load_level(self, level):

        self.clean_values_on_load()

        self.engine.gravity = 0

        self.create_active_map_reconstructed(level)
        self.engine.entityMgr.load_map()
        
        self.engine.gfxMgr.scroll[0] = 0#self.goal[0]
        self.engine.gfxMgr.scroll[1] = 0#self.goal[1]

        self.game_status = 'ENTRY_ANIMATION'
        self.engine.gravity = self.engine.config.gravity

        self.current_level = level

    def tick(self, dt):
        if self.game_status == 'MENU':
            pass
        elif self.game_status == 'START':
            self.load_level(1)
        elif self.player_lives == 0:
            self.load_level(self.current_level)
        elif len(self.engine.entityMgr.enemies) == 0:
            if self.current_level + 1 <= self.max_level:
                self.load_level(self.current_level + 1)
            else:
                self.game_status = 'MENU'
                self.current_level = 0


    def shutdown(self):
        pass


    def clean_values_on_load(self):
        # Clean Player values
        if self.engine.entityMgr.player:
            self.player_lives = 10
            self.engine.entityMgr.player.moving_left = False
            self.engine.entityMgr.player.moving_right = False

        # Set scroll animation to go on
        self.engine.gfxMgr.scroll_locked = False


    def create_active_map_reconstructed(self, level):
        self.platforms_layer_0 = []
        self.platforms_layer_1 = []

        self.engine.entityMgr.platforms_layer_0 = []
        self.engine.entityMgr.platforms_layer_1 = []
        self.engine.entityMgr.particles = []
        self.engine.entityMgr.bullets = []
        # Load all the sprites
        index_y = 10
        index_x = 0
        for file in self.engine.config.sources:
            # Load source name
            source_name = file[0]

            # Load source type
            source_type = file[1]

            # Load Spritesheet
            self.spritesheet = SpriteSheet(file[2])

            # Load each position of sprite
            f = open(file[3],)
            print(file[3])
            data = json.load(f)
            f.close()
            self.asset = {}
            self.asset.update(data['positions'])

            index = 0
            for id in self.asset:
                index += 1
                position = self.asset[id]
                new_image = self.spritesheet.get_image(position[0], position[1], position[2], position[3])
                new_image.set_colorkey( (0, 0, 0) )
                new_image = transform.scale2x(new_image)
                temp = Sprite(self.engine, new_image, (position[2], position[3]), id, 
                                None, ((10 + (index_x * 70), index_y)),
                                (32, 32))
                temp.entity_type = self.asset[id]
                temp.source_name = source_name
                temp.source_type = source_type
                self.engine.entityMgr.sprites.append(temp)
                if index_x < 4:
                    index_x += 1
                else:
                    index_x = 0
                    index_y += 70

        # Load file if exists
        if path.exists('data\\' + str(level)):
            fi = open('data/' + str(level))
            temp_dict = json.load(fi)
            for id in temp_dict:
                source = temp_dict[id][0]
                entity_type = temp_dict[id][1]
                position = temp_dict[id][2]
                layer = temp_dict[id][3]
                sprite = []
                sprite[:] = [sprite_t for sprite_t in self.engine.entityMgr.sprites if (entity_type == sprite_t.entity_type and source == sprite_t.source_name)]

                # temp_placed_sprite = Sprite(self.engine, sprite[0].image, sprite[0].size, None,
                #                         self.engine.gfxMgr.window, position, (32, 32))
                if source != "Character_Image":
                    if source != "Enemy_Image":
                        temp_platform = Platform(self.engine, sprite[0].image, (32, 32), 0, self.engine.gfxMgr.window, position, "P")
                        temp_platform.entity_type = sprite[0].entity_type
                        temp_platform.source_name = sprite[0].source_name
                        temp_platform.source_type = sprite[0].source_type
                        if layer == 0:
                            self.engine.entityMgr.platforms_layer_0.append(temp_platform)
                        else:
                            self.engine.entityMgr.platforms_layer_1.append(temp_platform)
                    else:
                        newEnemy = Enemy(self.engine, sprite[0].image, (16, 32), len(self.engine.entityMgr.enemies), self.engine.gfxMgr.window)
                        newEnemy.position = position
                        self.engine.entityMgr.enemies.append(newEnemy)
                else:
                    self.engine.entityMgr.player = Player(self.engine, sprite[0].image, (8, 27), 0, self.engine.gfxMgr.window, position, (32, 32))
                    self.player_load_pos = position


    def create_active_map(self, level):
        self.platforms = []
        self.enemies = []

        scale = (32, 32)

        nmap = []
        
        row = 0
        col = 0

        self.f = open("data\map" + str(level) + ".txt", 'r')
        for line in self.f.read().split('\n'):
            nmap.append(line)
        self.f.close()

        self.player_load_pos = (0, 0)

        for line in nmap:
            col = 0
            for char in line:                
                # Check for Platform
                if char == 'G':
                    platform = (col * scale[0], row * scale[1], 'G')
                    self.platforms.append(platform)
                elif char == 'D':
                    platform = (col * scale[0], row * scale[1], 'D')
                    self.platforms.append(platform)
                elif char == 'I':
                    platform = (col * scale[0], row * scale[1], 'I')
                    self.platforms.append(platform)
                elif char == 'L':
                    platform = (col * scale[0], row * scale[1], 'L')
                    self.platforms.append(platform)
                elif char == 'l':
                    platform = (col * scale[0], row * scale[1], 'l')
                    self.platforms.append(platform)
                elif char == 'B':
                    platform = (col * scale[0], row * scale[1], 'B')
                    self.platforms.append(platform)
                elif char == 'R':
                    platform = (col * scale[0], row * scale[1], 'R')
                    self.platforms.append(platform)
                elif char == 'r':
                    platform = (col * scale[0], row * scale[1], 'r')
                    self.platforms.append(platform)
                elif char == 'E':
                    platform = (col * scale[0], row * scale[1], 'E')
                    self.platforms.append(platform)
                elif char == 'X':
                    self.player_load_pos = (col * scale[0], row * scale[1])

                elif char == '0':
                    enemy = (col * scale[0], row * scale[1])
                    self.enemies.append(enemy)
                
                elif char == '?':
                    self.goal = (col * scale[0], row * scale[1])

                col += 1
            row += 1