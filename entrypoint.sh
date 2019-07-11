#!/bin/sh

echo $UPLOAD
if [ "$UPLOAD" = "true" ]; then
    python upload.py
fi
if [ $? = 0 ]; then
	/usr/bin/supervisord -c /etc/supervisord.conf
else
	exit 1;
fi
