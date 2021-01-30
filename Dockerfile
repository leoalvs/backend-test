FROM python:alpine3.7
COPY . /backend-test
WORKDIR /backend-test
RUN apk update && apk add git
RUN pip install -r requirements.txt
EXPOSE 8000
EXPOSE 27017
CMD python -m api