from ultralytics/ultralytics

RUN pip install fastapi
RUN pip install cffi cryptography
COPY requirements.txt requirements.txt
RUN pip install requirements.txt
