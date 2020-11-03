import logging
import logging.config
import os

import plaster
import toml


class Loader(plaster.ILoader):
    def __init__(self, uri):
        self.uri = uri
        path = os.path.abspath(uri.path)
        with open(path) as fh:
            self.config = toml.load(fh)

    def get_sections(self):
        return self.config.keys()

    def get_settings(self, section=None, defaults=None):
        if section is None:
            section = self.uri.fragment

        if section not in self.get_sections():
            return {}

        result = {}
        if defaults is not None:
            result.update(defaults)

        result.update(self.config[section])
        return result

    def setup_logging(self, defaults=None):
        if "logging" in self.config:
            config = {}
            if defaults is not None:
                config.update(defaults)

            config.update(self.config["logging"])
            config["disable_existing_loggers"] = False

            logging.config.dictConfig(config)
        else:
            logging.basicConfig()
