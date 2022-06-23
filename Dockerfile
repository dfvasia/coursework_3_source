FROM python:3.10

WORKDIR /project
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY project project
COPY tests tests
COPY . .

RUN ["chmod", "+x", "./run.sh"]
CMD ./run.sh
