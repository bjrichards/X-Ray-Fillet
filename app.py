from src import Engine
from data import config

if __name__ == "__main__":
    config_data = config.developmentConfig()
    
    engine = Engine.Engine(config_data)
    engine.initialize()
    engine.run()
    engine.cleanup()