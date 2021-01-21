# Created by Braeden Richards
# Created on January ?th, 2021
# Desc: Entry to application. Creates and runs an instance of the game engine.


###########
# Imports #
###########
from src import Engine      # Contains entirety of game
from data import config     # Contains configurations used during game loading


###############
# Application #
###############
if __name__ == "__main__":
    # Load configuration data to be passed to the engine
    config_data = config.developmentConfig()
    
    # Create instance of engine and run
    engine = Engine.Engine(config_data)
    engine.initialize()
    engine.run()
    engine.cleanup()