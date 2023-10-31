FROM python:3.10-bookworm

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000

RUN echo test

ENV OPENAI_API_KEY=$OPENAI_API_KEY
CMD ["flask", "run", "--host", "0.0.0.0"]


RUN echo test