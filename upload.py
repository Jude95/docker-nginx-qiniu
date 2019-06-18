#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from qiniu import Auth, put_file, etag
import os
if 'CONFIG_FILE' in os.environ:
    config_file = os.environ['CONFIG_FILE']
    if config_file is not None:
        print("read config file "+config_file)
        file = open(config_file)
        config_map = {}
        while 1:
            line = file.readline().strip('\n')
            entry = line.split("=")
            if not line:
                break
            config_map[entry[0]] = entry[1]
        access_key = config_map['AK']
        secret_key = config_map['SK']
        bucket_name = config_map['BUCKET']
        local_path = config_map['LOCAL_PATH']
        remote_path = config_map['REMOTE_PATH']
    else:
        print("no found qiniu config")

else:
    access_key = os.environ['AK']
    secret_key = os.environ['SK']
    bucket_name = os.environ['BUCKET']
    local_path = os.environ['LOCAL_PATH']
    remote_path = os.environ['REMOTE_PATH']

print("start upload to qiniu")

if not os.path.isdir(local_path):
    print(local_path + " is not exist")

q = Auth(access_key, secret_key)

local_files = os.walk(local_path)

for root, dirs, files in local_files:
    for name in files:
        file = os.path.join(root, name)
        relpath = os.path.relpath(file, local_path)

        remote_file = remote_path + '/' + relpath
        token = q.upload_token(bucket_name, remote_file, 3600)

        ret, info = put_file(token, remote_file, file)
        print(info)
