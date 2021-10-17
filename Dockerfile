# dockerhub: theballwall/task6

FROM python:3.8-alpine

WORKDIR /task6

COPY . /task6

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "task6.py"]