FROM python:3.8

WORKDIR /workspace/

COPY ./requirements.txt /workspace/
RUN pip install -r requirements.txt


CMD ["python", "broadcast.py"]
