FROM python:3.7
RUN mkdir /collection
WORKDIR /collection
ADD . /collection
RUN pip install -r requirements.txt

EXPOSE 8000
