import sys
import logging
import log_config.client_log_config
import log_config.server_log_config


if sys.argv[0].find('client') == -1:
    LOGGER = logging.getLogger('server')
else:
    LOGGER = logging.getLogger('client')


def log(func):

    def log_save(*args, **kwargs):
        result = func(*args, **kwargs)
        LOGGER.debug(f'Func name: {func.__name__}.'
                     f'Parameters: {args}, {kwargs}'
                     f'Module: {func.__module__}')
        return result
    return log_save