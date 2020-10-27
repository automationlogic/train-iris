FROM faizanbashir/python-datascience:3.6
COPY requirements.txt /
COPY train.py /
WORKDIR /
RUN apk add libffi-dev python3-dev
RUN pip3 install -r requirements.txt
