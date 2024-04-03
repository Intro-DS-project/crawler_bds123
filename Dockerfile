FROM python:3.11.8-alpine3.19

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]