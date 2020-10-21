""" code in this file originally from Geekgs4geeks: https://www.geeksforgeeks.org/program-for-conways-game-of-life/
    reformatted & put into class structure etc...
"""

# Python code to implement Conway's Game Of Life
from utils import *
from classes.arg_parser import ArgParser
from logger import get_root_logger


class MainProgram:
    """ the runner of the simulation
        TODO: add a reset to return to start/default state of some kind
     """
    def __init__(self, arg_parser=None, logger=None):
        # those arguments may be set from the config file
        self.foo            = 42

        self.LOG            = logger if logger else self.get_logger()
        self.arg_parser     = arg_parser if arg_parser else ArgParser(self.LOG)
        self.full_configs   = None
        self.init_args()

        self.LOG.info(f"Done init in {self.__class__.__name__}.")

    def init_args(self):
        """ parses whatever args we have & sets up this class accordingly

            attribute must already be declared in the class - otherwise they are ignored
        """
        self.arg_parser.parse_cmdline()
        self.full_configs = self.arg_parser.parse_yaml_configs()
        for k, v in self.configs_default_mp.items():
            if hasattr(self, k):
                setattr(self, k, v)
                self.LOG.info(f"Attribute {k} has been set to {getattr(self, k)}")
            else:
                self.LOG.warning(f"Config file contains an attribute that is not in this class's attribute and therefore has not been set (k,v): {k}, {v}")

        if self.mode != "default":                  # then those will complement/override the default values
            for k, v in self.full_configs[self.mode]["main_program"].items():
                if hasattr(self, k):
                    setattr(self, k, v)
                    self.LOG.info(f"Attribute {k} has been set to {getattr(self, k)}, overriding default values if any.")
                else:
                    self.LOG.warning(f"Config file contains an attribute that is not in this class's attribute and therefore has not been set (k,v): {k}, {v}")


    @property
    def configs_default_mp(self):
        """ returns the part of the config file that contains the configs by default for main program """
        return self.full_configs["default"]["main_program"]

    @property
    def mode(self):
        """ the config mode we want. defaults is set by argparser at default"""
        return self.args.mode

    @property
    def args(self):
        return self.arg_parser.args

    def get_logger(self):
        """ inits the logs. should only be if for whatever reason no logger has been defined """
        logger = get_root_logger(BASE_LOGGER_NAME, filename=f'log.log')
        logger.info(f"Initated logger in {self.__class__.__name__} ")
        logger.debug(f'logger debug level msg ')
        logger.info(f'logger info level msg ')
        logger.warning(f'logger warn level msg ')
        logger.error(f'logger error level msg ')
        logger.critical(f'logger critical level msg ')
        return logger

if __name__ == '__main__':
    mp = MainProgram()
