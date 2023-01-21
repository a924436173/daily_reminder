FROM python:3.9-alpine
RUN mkdir -p /web/daily_reminder_birthday
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /web/daily_reminder_birthday
COPY requirements.txt /web/daily_reminder_birthday/requirements.txt
RUN pip3 config set global.index-url http://pypi.douban.com/simple/ && pip3 config set install.trusted-host pypi.douban.com && pip install -r requirements.txt
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#RUN python main.py