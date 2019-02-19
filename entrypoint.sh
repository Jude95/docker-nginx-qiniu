#!/bin/sh

echo $UPLOAD
if [ "$UPLOAD" = "true" ]; then
    python upload.py
fi
/usr/bin/supervisord -c /etc/supervisord.conf