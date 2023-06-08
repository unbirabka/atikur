#test1
FROM python:3.9.17-alpine3.18
WORKDIR /app
COPY service-b/* .

RUN apk add curl vim
RUN python3 -m pip install -r requirements.txt

ENV FLASK_APP=main
ENV FLASK_ENV=development

CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000
