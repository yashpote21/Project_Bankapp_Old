import configparser


config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")



class ReadConfigFileData:

    # Reading data from [login data] section.
    @staticmethod
    def GetLoginUsername():
        username = config.get('login data', 'LoginUsername')
        return username

    @staticmethod
    def GetLoginPassword():
        password = config.get('login data', 'LoginPassword')
        return password


    # Reading data from [registration data] section.
    @staticmethod
    def GetRegUsername():
        username = config.get('registration data', 'RegisterUsername')
        return username

    @staticmethod
    def GetRegPassword():
        password = config.get('registration data', 'RegisterPassword')
        return password

    @staticmethod
    def GetRegEmail():
        email = config.get('registration data', 'RegisterEmail')
        return email

    @staticmethod
    def GetRegPhone():
        phone = config.get('registration data', 'RegisterPhone')
        return phone

