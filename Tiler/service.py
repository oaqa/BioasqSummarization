import os, sys, getopt

from deiis.rabbit import Task, Message
from deiis.model import Serializer

from Concatenation import Concatenation

HOST_VAR='RABBIT_HOST'

if __name__ == "__main__":
    host = 'localhost'
    if (HOST_VAR in os.environ):
        host = os.environ[HOST_VAR]

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:", ["rabbit="])
    except getopt.GetoptError:
        print 'ERROR: Invalid option(s).'
        print sys.argv[0] + ' [-r|--rabbit <rabbit host>]'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print sys.argv[0] + ' [-r|--rabbit <host>]'
            sys.exit()
        elif opt in ("-r", "--rabbit"):
            host = arg

    print 'Starting Tiler services.'
    print 'Looking for a RabbitMQ server at ' + host
    task = Concatenation(host=host)
    task.start()
    task.wait_for()


