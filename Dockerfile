FROM python:alpine

COPY requirements.txt /bot/requirements.txt

WORKDIR /bot

RUN pip install -r requirements.txt

COPY . .

CMD ["python3","-u", "honeygain-bot.py"]
