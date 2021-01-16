class baseConfig():
    window_size = (1280, 768)
    window_name = "Base Engine"

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


    # Gameplay Configurations
    gravity_on = True
    gravity = -.005

    player_bullet_speed = 0.8
    player_bullet_lifetime = 5

    enemy_bullet_speed = 0.6


    # Image Files
    start_game_button_0 = "assets\\img\\ui\\button_unpause.bmp" 
    image_file_grass_0 = "assets\\img\\game\\grass_0.bmp"
    image_file_dirt_0 = "assets\\img\\game\\dirt.bmp"
    image_file_character_0 = "assets\\img\\game\\character_0.bmp"
    image_file_enemy_0 = "assets\\img\\game\\enemy_0.bmp"

class developmentConfig(baseConfig):
    window_name = "DEV X-Ray Fillet Engine"


class uatConfig(baseConfig):
    window_name = "UAT X-Ray Fillet Engine"


class productionConfig(baseConfig):
    window_name = "PROD X-Ray Fillet Engine"
