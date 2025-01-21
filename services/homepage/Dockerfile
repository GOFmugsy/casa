FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
COPY casa-compose.yml casa-compose.yml
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "-p 5050"]
