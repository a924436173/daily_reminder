FROM python:3.9-alpine
RUN mkdir -p /web/daily_reminder
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /web/daily_reminder
COPY requirements.txt /web/daily_reminder/requirements.txt
RUN pip3 config set global.index-url http://pypi.douban.com/simple/ && pip3 config set install.trusted-host pypi.douban.com && pip install -r requirements.txt
