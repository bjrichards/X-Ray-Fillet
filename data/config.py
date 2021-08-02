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
    image_file_top_0 = "assets\\img\\game\\platform_top_01.bmp"
    image_file_mid_1 = "assets\\img\\game\\platform_07.bmp"
    image_file_left_0 = "assets\\img\\game\\platform_top_left_00.bmp"
    image_file_left_1 = "assets\\img\\game\\platform_05.bmp"
    image_file_right_0 = "assets\\img\\game\\platform_03.bmp"
    image_file_right_1 = "assets\\img\\game\\platform_06.bmp"
    image_file_bottom_0 = "assets\\img\\game\\platform_04.bmp"
    image_file_mid_0 = "assets\\img\\game\\platform_00.bmp"
    image_file_character_0 = "assets\\img\\game\\character_0.bmp"
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
