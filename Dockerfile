FROM python:3

ADD . .

RUN pip install coverage

CMD [ "python", "./Statistics/statscalctest.py" ]


