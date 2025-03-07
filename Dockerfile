FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY TicketToolBot .

CMD ["python", "TicketToolBot/main.py"]