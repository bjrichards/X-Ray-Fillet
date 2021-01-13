class baseConfig():
    window_size = (1024, 768)
    window_name = "Base Engine"

    fps = 80

    bounding_boxes = True

    show_fps = True

    gravity_on = True
    gravity = -.005


class developmentConfig(baseConfig):
    window_name = "DEV Base Engine"


class uatConfig(baseConfig):
    window_name = "UAT Base Engine"


class productionConfig(baseConfig):
    window_name = "PROD Base Engine"
