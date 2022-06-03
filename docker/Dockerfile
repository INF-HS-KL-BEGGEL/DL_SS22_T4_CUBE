FROM nvcr.io/nvidia/tensorflow:21.03-tf2-py3
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY /src /src
COPY /suites /suites
COPY /testsuite_runner.py /testsuite_runner.py
COPY /setup.py /setup.py
COPY /README.md /README.md
COPY /LICENSE /LICENSE
WORKDIR /
RUN pip3 install -e .
CMD [ "python3", "testsuite_runner.py"]