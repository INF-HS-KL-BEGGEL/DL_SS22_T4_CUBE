FROM python:3.8
WORKDIR ../
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY /test/testsuite test
COPY /src src
CMD [ "python3", "-m" , "testsuite_runner.py"]
