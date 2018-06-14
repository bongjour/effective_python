from datetime import datetime
from time import sleep


def log(message, when=None):
    """ Log a message with a timestamp

    :param message: message to print
    :param when: datetime of when the message occurred. default : current time.
    :return: none
    """

    when = datetime.now() if when is None else when

    print('%s: %s' % (when, message))


log('hi there!')

sleep(0.1)

log('hi again')

