import logging.handlers
from logging import Formatter, getLogger
from os import chdir, getcwd, path, pardir
from sys import stderr

from application.common.variables import LOGGER_LEVEL
from application.log_config.client_log_config import format_msg

if __name__ == '__main__':
    chdir(pardir)
app_path = getcwd()

if __name__ == '__main__':
    app_path = path.join(app_path, 'logs', 'server.log')
else:
    app_path = path.join(app_path, 'log', 'logs', 'server.log')

format_msg = Formatter('%(asctime)s %(levelname)s %(filename)s '
                       '%(message)s \n module: %(module)s function: '
                       '%(funcName)s str_line: %(lineno)d ')

log_handler = logging.handlers.TimedRotatingFileHandler(
    app_path,
    encoding='utf-8',
    backupCount=10,
    interval=1,
    when='D'
)

log_handler.setFormatter(format_msg)
log_handler.setLevel(LOGGER_LEVEL)
log_stream = logging.StreamHandler(stderr)

logger = getLogger('server')
logger.addHandler(log_handler)
logger.addHandler(log_stream)
logger.setLevel(LOGGER_LEVEL)

if __name__ == '__main__':
    logger.debug('Debug')
    logger.info('Info')
    logger.warning('Warning')
    logger.error('Error')
    logger.critical('Critical Error')
