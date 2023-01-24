FROM python:3.8 AS builder

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY media /media
COPY train_gan /train_gan
COPY welcome.webp /
COPY bot.py /
COPY config.py /
COPY transfer.py /
COPY transfer_gan.py /

CMD ["python3", "bot.py"]
