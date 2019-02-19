# Docker Nginx Qiniu
在启动nginx前，自动上传网站资源到七牛。

# Usage
```dockerfile
FROM jude95/nginx-qiniu

ENV UPLOAD=true \
	AK="xxx"	\
	SK="xxx"	\
	BUCKET="xxx"	\
	LOCAL_PATH="/usr/share/nginx/html/"	\
	REMOTE_PATH="xxx"

```