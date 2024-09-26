import logging


class Logger:
    def __init__(self):
        self.logger_instance = logging.getLogger(__name__)
        self.logger_instance.setLevel(logging.INFO)
        self.current_info = ""

    # all this class does is log its current info
    def log_info(self, current_info):
        self.logger_instance.info(current_info)

    # basic getters and setters
    def set_current_info(self, current_info):
        self.current_info = current_info

    def get_current_info(self):
        return self.current_info
