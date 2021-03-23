FROM python:3.8-buster

WORKDIR /home/musikinformatik

ADD requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8888

CMD ["jupyter", "lab", "--ip", "0.0.0.0", "--port", "8888", "--no-browser", "--allow-root"]
