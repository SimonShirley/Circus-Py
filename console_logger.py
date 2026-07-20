import logging

class Logger:
    _logger: logging.Logger

    def __init__(self) -> None:
        console = logging.StreamHandler()
        console.setLevel(level=logging.DEBUG)
        console.setFormatter(logging.Formatter('%(levelname)s : %(message)s'))

        self._logger = logging.getLogger('console_logger')
        self._logger.setLevel(logging.DEBUG)
        self._logger.addHandler(console)
        

    def get_logger(self):
        return self._logger