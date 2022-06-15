FROM python:3.9-alpine AS BASE

WORKDIR /root/

RUN apk add git

# clone
RUN git clone https://github.com/qwertyAAA/api_generator.git

# install requirements
RUN pip install -r api_generator/requirements.txt

FROM BASE

WORKDIR /root/api_generator

EXPOSE 9980

CMD ["python", "main.py"]
