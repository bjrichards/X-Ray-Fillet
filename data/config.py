class baseConfig():
    window_size = (1024, 768)
    window_name = "Base Engine"

    fps = 80

    # UI Debugging Options
    bounding_boxes = True
    show_fps = True
    show_is_grounded = True
    show_jumps_left = True
    show_bullet_count = True
    show_platforms_rendered = True


    # Gameplay Configurations
    gravity_on = True
    gravity = -.005

    player_bullet_speed = 0.8
    player_bullet_lifetime = 5

class developmentConfig(baseConfig):
    window_name = "DEV X-Ray Fillet Engine"


class uatConfig(baseConfig):
    window_name = "UAT X-Ray Fillet Engine"


class productionConfig(baseConfig):
    window_name = "PROD X-Ray Fillet Engine"
