FROM jude95/nginx-docker

LABEL maintainer="Jude95 (https://github.com/Jude95)"

WORKDIR /

ENV UPLOAD=false \
	AK=""	\
	SK=""	\
	BUCKET=""	\
	LOCAL_PATH=""	\
	REMOTE_PATH=""

RUN pip install qiniu

COPY entrypoint.sh upload.py /

ENTRYPOINT sh entrypoint.sh