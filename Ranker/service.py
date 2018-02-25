# import logging
# from logging.config import fileConfig
# logging.config.fileConfig('logging.ini')

import os, sys
from CoreMMR import CoreMMR
from SoftMMR import SoftMMR
from HardMMR2 import HardMMR2

if __name__ == '__main__':
    host = os.environ.get('RABBIT_HOST', 'localhost')
    #if len(sys.argv) > 1:
    #    print 'Args: ' + str(sys.argv)
    #    host = sys.argv[1]

    print 'Host is ' + host

    print 'Declaring the services'
    services = list()
    services.append(CoreMMR(host=host))
    services.append(SoftMMR(host=host))
    services.append(HardMMR2(host=host))

    print 'Staring the services'
    for service in services:
        service.start()

    print 'Waiting for the services to terminate'
    for service in services:
        print 'Waiting for service {}'.format(service.__class__.__name__)
        service.wait_for()

    print 'Done.'
