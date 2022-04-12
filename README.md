# Sample WS App
A tiny WebSocket app using Flask and SocketIO. I made this to test a WebSocket service deployed on AWS ALB + ASG + EC2.

## Installation
```
pip3 install -r requirements.txt
```

## Quickstart
1. Run the Flask server:
```
python3 app.py
```
2. On your browser, go to `localhost:5001`.

3. Go to your browser's Console tab.

4. Your browser Console output should looks like this:

> WebSocket connection has been established
>
> PING sent
>
> PONG received
>
> PING sent
>
> PONG received
>
> ...


