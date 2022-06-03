FROM nvcr.io/nvidia/tensorflow:21.03-tf2-py3
WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY test/testsuite /test
COPY src /src
CMD [ "python3", "-m" , "test/testsuite_runner.py"]
