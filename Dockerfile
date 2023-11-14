FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install psycopg2-binary

RUN pip install -r requirements.txt
