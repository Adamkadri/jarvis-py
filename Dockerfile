From python:3

ADD jarvis.py /

RUN python -m pip install --upgrade pip

RUN pip install SpeechRecognition
RUN pip install requests2

CMD [ "python", "jarvis.py"]
