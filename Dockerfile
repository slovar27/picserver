FROM alpine:3.18.2

RUN apk add python3

RUN pip3 install --upgrade pip

RUN python3 -m pip install --upgrade Pillow

RUN pip3 install flask

RUN apk add --no-cache gcc python3-dev musl-dev jpeg-dev zlib-dev

COPY ./ /flask/

CMD [ "python3", "/flask/app.py" ]