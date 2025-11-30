import configparser

config = configparser.RawConfigParser()
config.read("config/config.ini")

class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get("DEFAULT", "base_url")

    @staticmethod
    def get_username():
        return config.get("DEFAULT", "username")

    @staticmethod
    def get_password():
        return config.get("DEFAULT", "password")

    @staticmethod
    def get_browser():
        return config.get("DEFAULT", "browser")
