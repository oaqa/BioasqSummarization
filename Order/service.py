import os, sys
from MajorityOrder import MajorityOrder
from MajorityCluster import MajorityCluster
from KMeansSimilarityOrderer import KMeansSimilarityOrderer

if __name__ == '__main__':
    print 'Starting ResultsCollector'
    host = os.environ.get('RABBIT_HOST', 'localhost')
    if len(sys.argv) > 1:
        if sys.argv[1] != '/bin/bash':
            host = sys.argv[1]

    print "Rabbit host is " + host

    services = []
    services.append(MajorityCluster(host=host))
    services.append(MajorityOrder(host=host))
    services.append(KMeansSimilarityOrderer(host=host))

    for service in services:
        print("Staring service " + service.__class__.__name__)
        service.start()

    print 'Waiting for the task to terminate.'
    for service in services:
        service.wait_for()

    print 'Done.'
