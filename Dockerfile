FROM python:3.9-alpine AS BASE

WORKDIR /root/

RUN apk add git

# clone
RUN git clone https://github.com/qwertyAAA/api_generator.git

# install requirements
RUN pip install -r api_generator/requirements.txt

RUN sed -i "s/https:\/\/cdn.jsdelivr.net\/npm\/swagger-ui-dist\@4/https:\/\/petstore.swagger.io/g" /usr/local/lib/python3.9/site-packages/fastapi/openapi/docs.py

FROM BASE

WORKDIR /root/api_generator

EXPOSE 9980

CMD ["python", "main.py"]
