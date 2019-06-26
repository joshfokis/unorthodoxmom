FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
# RUN mkdir /code/frontend
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
# ADD ./frontend /code/frontend
# WORKDIR /code/frontend
# RUN npm install
# WORKDIR /code
EXPOSE 80