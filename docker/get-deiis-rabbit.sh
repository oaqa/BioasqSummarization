#!/usr/bin/env bash

TGZ=deiis-rabbit.tgz

cd ../deiis
if [ -e $TGZ ] ; then 
	echo "Removing existing package."
	rm $TGZ 
fi

tar czf $TGZ README.md setup.cfg setup.py deiis/
cd -
mv ../deiis/$TGZ .
