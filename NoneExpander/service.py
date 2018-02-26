import os, sys
import logging
from logging import config

from NoneExpander import NoneExpander

logging.config.fileConfig('logging.ini')

if __name__ == "__main__":
    logger = logging.getLogger('main')

    host = os.environ.get('RABBIT_HOST', 'localhost')

    if len(sys.argv) > 1:
        host = sys.argv[1]

    logger.info('Rabbit host is ' + host)

    # Start all of the services.
    expander = NoneExpander(host=host)
    logger.info('Starting the NoneExander service.')
    expander.start()

    logger.info("Waiting for the service to terminate.")
    expander.wait_for()

    logger.info('Done.')

