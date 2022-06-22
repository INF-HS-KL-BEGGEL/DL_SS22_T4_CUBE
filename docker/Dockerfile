FROM nvcr.io/nvidia/tensorflow:21.03-tf2-py3
RUN apt update && apt upgrade -y && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx
RUN apt-get -y install python3-tk
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY /src /src
COPY /testsuite_runner.py /app/testsuite_runner.py
COPY /setup.py /setup.py
COPY /README.md /README.md
COPY /LICENSE /LICENSE
WORKDIR /
RUN pip3 install -e .
CMD [ "python3", "/app/testsuite_runner.py"]
