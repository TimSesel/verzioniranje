FROM python:3.8

ADD . /code
WORKDIR /code
RUN pip install numpy opencv-python pytest
CMD ["python", "linearni_operatorji.py"]