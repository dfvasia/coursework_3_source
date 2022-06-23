FROM python:3.10

WORKDIR /project
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN ["chmod", "+x", "./run.sh"]
CMD ./run.sh
