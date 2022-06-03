FROM nvcr.io/nvidia/tensorflow:21.03-tf2-py3
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY src /src
CMD [ "pip3", "install", "."]
CMD [ "python3", "./src/testsuite_runner.py"]