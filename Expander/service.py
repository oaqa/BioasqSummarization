import os, sys
import logging
from logging import config

from Expander import NoneExpander
# from SnomedctExpander import SnomedctExpander
from UMLSExpander import UMLSExpander

logging.config.fileConfig('logging.ini')

ENV_VAR='RABBIT_HOST'

if __name__ == "__main__":
    host = os.environ.get(ENV_VAR, 'localhost')

    if len(sys.argv) > 1:
        host = sys.argv[1]

    print 'Rabbit host is ' + host

    logger = logging.getLogger('main')
    tasks = []
    for cls in (NoneExpander, UMLSExpander):
        instance = cls(host=host)
        tasks.append(instance)
        logger.info('Staring service %s', cls.__name__)
        instance.start()

    # And wait for them to terminate
    logger.info('Waiting for the tasks to end.')
    for task in tasks:
        task.wait_for()

    logger.info('Done.')

