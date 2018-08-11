import os

from mycroblog import create_app

config_name = os.getenv('APP_SETTINGS')
mycroblog = create_app(config_name)

if __name__ == '__main__':
    mycroblog.run()