from flask import Flask, Response
import redis
import socket
import requests

server_id = socket.gethostname()
hits_id = f"{server_id}_hits"
headers = {"X-App-Request": server_id}
nginx_url = "http://nginx"

app = Flask(__name__)

redis_host = "redis"
redis_client = redis.StrictRedis(host=redis_host, port=6379, db=0)


@app.route('/')
def hello():
    redis_client.incr(hits_id)
    app1_response = requests.get(nginx_url, headers=headers)

    return {
        "message": f"Hello from {server_id}!",
        "app1_message": app1_response.json()
    }

@app.route('/health')
def health_check():
    try:
        response = redis_client.ping()
        if response:
            return Response('{"status": "OK", "message": "Flask OK, Redis OK"}', content_type='application/json')
    except Exception as e:
        return Response('{"status": "Error", "message": "' + str(e) + '"}', content_type='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
