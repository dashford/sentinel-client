FROM arm32v7/python:3.6.5-jessie

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip3 install --no-cache-dir -r ./requirements.txt

COPY . .

CMD ["python", "./sentinel.py"]
