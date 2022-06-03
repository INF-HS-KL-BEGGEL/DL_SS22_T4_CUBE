FROM nvcr.io/nvidia/tensorflow:21.03-tf2-py3
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY / /
WORKDIR /
CMD [ "pip3", "install", '-e', "."]
CMD [ "python3", "testsuite_runner.py"]