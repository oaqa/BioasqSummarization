import os, sys

from Concatenation import Concatenation

if __name__ == "__main__":
    host = os.environ.get('RABBIT_HOST', 'localhost')

    # if len(sys.argv) > 1:
    #     host = sys.argv[1]

    print 'Starting Tiler services.'
    print 'Looking for a RabbitMQ server at ' + host
    task = Concatenation(host=host)
    task.start()
    task.join()


