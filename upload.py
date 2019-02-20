#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from qiniu import Auth, put_file, etag
import os

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
