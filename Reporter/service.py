import os, sys
from ResultsCollector import ResultsCollector

if __name__ == '__main__':
    print 'Starting ResultsCollector'
    host = os.environ.get('RABBIT_HOST', 'localhost')

    task = ResultsCollector(host=host)
    task.start()
    print 'Waiting for the task to terminate.'
    task.wait_for()
    print 'Done.'
