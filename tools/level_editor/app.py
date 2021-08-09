# Created by Braeden Richards
# Created on August 5th, 2021
# Desc:
#   Reads in spritesheets/images, lets you build levels via mouse / keyboard on a visual screen
#   Exports to JSON

from src import Engine      # Contains entirety of game
from data import config     # Contains configurations used during game loading
import sys


###############
# Application #
###############
if __name__ == "__main__":
    # Load configuration data to be passed to the engine
    config_data = config.baseConfig()
    
    # Create instance of engine and run
    engine = Engine.Engine(config_data, sys.argv[1])
    engine.initialize()
    engine.run()
    engine.clean_up()