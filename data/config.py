class baseConfig():
    window_size = (1920, 1080)
    window_name = "Base Engine"
    scale = 2

    fps = 800

    # UI Debugging Options
    bounding_boxes = False
    show_fps = True
    show_is_grounded = True
    show_jumps_left = True
    show_bullet_count = True
    show_platforms_rendered = True
    show_total_enemy_count = True
    show_total_enemy_rendered = True
    show_game_status = True


    # Gameplay Debugging
    enemies_can_fire = True

    # Gameplay Configurations
    gravity_on = True
    gravity = -.005

    player_bullet_speed = 0.8
    player_bullet_color = (255, 0, 0)
    player_bullet_lifetime = 5
    max_player_vel = (0.5, 1.5)

    enemy_bullet_speed = 0.5
    enemy_bullet_color = (0, 0, 255)

    bullet_particle_lifetime = 1


    # Image Files
    start_game_button_0 = "assets\\img\\ui\\button_unpause.bmp" 

    platform_top_mid        = (32, 0, 32, 32)
    platform_edge           = (128, 32, 32, 32)
    platform_top_left       = (0, 0, 32, 32)
    platform_bottom_left    = (0, 32, 32, 32)
    platform_top_right      = (64, 0, 32, 32)
    platform_bottom_right   = (64, 32, 32, 32)
    platform_bottom_mid     = (32, 32, 32, 32)
    platform_mid_0          = (32, 32, 32, 32)
    platform_bottom_mid_mid = (96, 32, 32, 32)

    image_file_character_0              = "assets\\img\\game\\character_0.bmp"
    image_file_character_stand          = "assets\\img\\game\\player_standing.bmp"
    spritesheet_file_character_running  = "assets\\img\\game\\player_running.bmp"

    image_file_enemy_0 = "assets\\img\\game\\enemy_0.bmp"

class developmentConfig(baseConfig):
    window_name = "DEV X-Ray Fillet Engine"


class uatConfig(baseConfig):
    window_name = "UAT X-Ray Fillet Engine"

    bounding_boxes = False
    show_fps = True
    show_is_grounded = False
    show_jumps_left = False
    show_bullet_count = False
    show_platforms_rendered = False
    show_total_enemy_count = False
    show_total_enemy_rendered = False
    show_game_status = False


class productionConfig(baseConfig):
    window_name = "PROD X-Ray Fillet Engine"
