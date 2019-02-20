# Docker Nginx Qiniu
在启动nginx前，自动上传网站资源到七牛。

# Usage
直接在 dockerfile 中配置
```dockerfile
FROM jude95/nginx-qiniu

ENV UPLOAD=true \
	AK="xxx"	\
	SK="xxx"	\
	BUCKET="xxx"	\
	LOCAL_PATH="/usr/share/nginx/html/"	\
	REMOTE_PATH="xxx"

```

或者使用配置文件来设置七牛配置：

```dockerfile
FROM jude95/nginx-qiniu

# 设置配置文件名
ENV UPLOAD=true \
	CONFIG_FILE="qiniu_config"

# 添加配置文件到容器内部
COPY qiniu_config /

```
以及 `qiniu_config` 内容
```
AK=xxxx
SK=xxxx
BUCKET=xxx
LOCAL_PATH=/usr/share/nginx/html/
REMOTE_PATH=xxx
```
