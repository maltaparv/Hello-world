import logging
import sys
from logging.handlers import TimedRotatingFileHandler

# LOG_FORMATTER = logging.Formatter("%(asctime)s %(thread)d %(process)d %(levelname)s %(message)s")
LOG_FORMATTER = logging.Formatter("%(asctime)s %(thread)d %(levelname)s %(message)s")
LOG_FILE = 'C:\DRV\LOGs\TestLog.txt'
LOG_LEVEL = 'DEBUG'


# https://tproger.ru/translations/python-logging/

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(LOG_FORMATTER)
    return console_handler


def get_file_handler():
    file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
    file_handler.setFormatter(LOG_FORMATTER)
    return file_handler


def get_smtp_handler():
    # handler = logging.handlers.SMTPHandler(['',['',]], 'log@d.ru', 'log.gbsmp@mail.ru',
    #                                        'test01' )
    handler = logging.handlers.SMTPHandler(mailhost='smtp.mail.ru',
                            fromaddr='log.gbsmp@mail.ru',
                            toaddrs='log.gbsmp@mail.ru',
                            subject='The log',
                            secure=None)
    handler.setFormatter(LOG_FORMATTER)
    return handler  # SMTPHandler log.gbsmp@mail.ru


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.getLevelName(LOG_LEVEL))  # better to have too much log than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.addHandler(get_smtp_handler())
    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger


log = get_logger("my_app_name")
log.debug("a debug message")
# log.info("информация")
# log.warning('предупреждение')
# log.error('ошибка')
# log.critical('Критическая ошибка!')
