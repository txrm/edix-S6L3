FROM alpine:3.18.4

WORKDIR /app

COPY app.py .
COPY requirements.txt .

RUN apk --no-cache add python3 py3-pip && \
    pip3 install -r requirements.txt && \
    apk --purge del py3-pip

EXPOSE 5000

CMD ["python", "app.py"]