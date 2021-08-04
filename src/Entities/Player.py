# IMPORTS #

# Libraries #
from pygame import Rect, draw, image, transform
from math import sqrt

# Custom Imports #
from ..Aspects.Physics2D import Physics2D

from .Entity import Entity
from .Bullet import Bullet

class Player(Entity):
    def __init__(self, engine, image_file_name, size, identity, display, position, image_size):
        Entity.__init__(self, engine, image_file_name, size, identity, display)
        
        self.entity_type = "Player"

        self.image_size = (image_size[0] * self.engine.config.scale, image_size[1] * self.engine.config.scale)
        
        self.color = (255, 255, 255)
        self.bullet_color = self.engine.config.player_bullet_color
        self.position = position
        self.rect = Rect(self.position[0], self.position[1], self.size[0], self.size[1])

        self.block_exlusion = 'I'

        self.image_file_path = image_file_name       
        self.image = image.load(self.image_file_path).convert()
        self.image.set_colorkey((0, 0, 0))        
        self.image = transform.scale(self.image, self.image_size)

        self.since_last_sprite_animation_frame = 0

        self.image_running = []
        self.current_running_image = 0
        for i in range(0, 7):
            new_image = self.engine.gameMgr.spritesheet_character_running.get_image(i * 32, 0, 32, 32)
            new_image.set_colorkey((0, 0, 0))
            new_image = transform.scale(new_image, self.image_size)
            self.image_running.append(new_image)

        self.image_to_display = None

        self.aspects.append(Physics2D(self))

        self.is_grounded = False

        self.max_velocity = (self.engine.config.max_player_vel[0], self.engine.config.max_player_vel[1])

        self.single_jumped = False
        self.double_jumped = False
        self.jump = 0

        self.moving_left = False
        self.moving_right = False
        self.down_button = False
        self.last_direction = "RIGHT"

        self.bullet_speed = self.engine.config.player_bullet_speed

    def tick(self, dt):
        for aspect in self.aspects:
            aspect.tick(dt)

    def load_level(self, position):
        self.position = position
        self.rect = Rect(self.position[0], self.position[1], self.size[0], self.size[1])


    def draw(self, dt):
        scroll = self.engine.gfxMgr.scroll
        v_offset = ((32 - (self.size[1] / self.engine.config.scale)) * self.engine.config.scale)
        h_offset = (self.image_size[0] / self.engine.config.scale) - (self.size[0] / self.engine.config.scale)
        position = (self.position[0] - scroll[0] - h_offset, self.position[1] - scroll[1] - v_offset)

        self.choose_display_image(dt)

        self.display_surface.blit(self.image_to_display, position)
        
        if self.engine.config.bounding_boxes:
            self.rect = Rect(self.position[0] - scroll[0], self.position[1] - scroll[1], self.size[0], self.size[1])
            draw.rect(self.display_surface, self.color, self.rect)

    def check_collisions(self):
        # if self.keep_in_screen():
        #     self.is_grounded = True
        #     self.double_jumped = False
        #     self.jump = 0
        if self.check_platform_collisions():
            self.jump = 0
        else:
            self.is_grounded = False

    def keep_in_screen(self):
        collision = False
        if self.position[1] + self.size[1]>= self.engine.config.window_size[1]:
            self.position = (self.position[0], self.engine.config.window_size[1] - self.size[1])
            self.velocity = (self.velocity[0], 0)
            self.double_jumped = False
            self.single_jumped = False

            collision = True

        elif self.position[1] < 0:
            self.position = (self.position[0], 0)
            self.velocity = (self.velocity[0], 0)

        return collision


    def jump_(self):
        if (self.is_grounded == True and self.jump == 0) or (self.is_grounded == False and self.jump < 2): 
            self.is_grounded = False

            self.jump = self.jump + 1
            
            velx = self.velocity[0]
            vely = -1.5
            
            self.velocity = (velx, vely)


    def fire(self, pos_to_fire_toward):
        distance = [pos_to_fire_toward[0] + self.engine.gfxMgr.scroll[0] - self.position[0], pos_to_fire_toward[1] + self.engine.gfxMgr.scroll[1] - self.position[1]]
        normalized = sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / normalized, distance[1] / normalized]

        velocity = (direction[0] * self.bullet_speed, direction[1] * self.bullet_speed)

        bullet = Bullet(self.engine, None, (3, 3), 0, self.display_surface, (self.position[0], self.position[1]), velocity, "player", self.bullet_color)
        self.engine.entityMgr.bullets.append(bullet)


    def choose_display_image(self, dt):
        if self.moving_right:
            self.last_direction = "RIGHT"
            self.since_last_sprite_animation_frame = self.since_last_sprite_animation_frame + self.engine.clock.get_time()
            if self.since_last_sprite_animation_frame / 1000 >= 0.08:
                self.since_last_sprite_animation_frame = 0
                self.image_to_display = self.image_running[self.current_running_image]
                self.current_running_image = (self.current_running_image + 1) % (len(self.image_running) - 1)
        elif self.moving_left:
            self.last_direction = "LEFT"
            self.since_last_sprite_animation_frame = self.since_last_sprite_animation_frame + self.engine.clock.get_time()
            if self.since_last_sprite_animation_frame / 1000 >= 0.08:
                self.since_last_sprite_animation_frame = 0
                self.image_to_display = self.image_running[self.current_running_image]
                self.image_to_display = transform.flip(self.image_to_display, True, False)
                self.current_running_image = (self.current_running_image + 1) % (len(self.image_running) - 1)
        else:
            self.current_running_image = 0
            self.since_last_sprite_animation_frame = 0
            self.image_to_display = self.image
            if self.last_direction == "LEFT":
                self.image_to_display = transform.flip(self.image_to_display, True, False)
