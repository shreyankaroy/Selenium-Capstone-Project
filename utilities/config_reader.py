import configparser


class ConfigReader:

    def __init__(self):

        self.config = configparser.ConfigParser()

        self.config.read("config/config.ini")

    def get_base_url(self):

        return self.config["DEFAULT"]["base_url"]

    def get_browser(self):

        return self.config["DEFAULT"]["browser"]

    def get_timeout(self):

        return int(
            self.config["DEFAULT"]["timeout"]
        )