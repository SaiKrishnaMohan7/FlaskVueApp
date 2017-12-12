# config.py

class CommonConfig(object):
    """
    Common Configurations between Envs 
    """

class DevelopmentConfig(object):
    """ 
    Development Configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True #helps in debugging, logs errors
    #TESTING = True -> defaults to FALSE, activates test mode 

class ProductionConfig(object):
    """
    Production Configurations
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

#Good Resource -> http://flask.pocoo.org/docs/0.11/config/
#SQLALCHEMY -> http://flask-sqlalchemy.pocoo.org/2.1/config/