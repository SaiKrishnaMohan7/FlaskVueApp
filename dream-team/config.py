# config.py

class CommonConfig(object):
    """
    Common Configurations between Envs 
    """
    DEBUG = True

class DevelopmentConfig(object):
    """ 
    Development Configurations
    """

    SQLALCHEMY_ECHO = True #helps in debugging, logs errors
    #TESTING = True -> defaults to FALSE, activates test mode 

class ProductionConfig(object):
    """
    Production Configurations
    """
    DEBUG = False

class TestingConfig(object):
    """ 
    Testing Configurations
    """

    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

#Good Resource -> http://flask.pocoo.org/docs/0.11/config/
#SQLALCHEMY -> http://flask-sqlalchemy.pocoo.org/2.1/config/