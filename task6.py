from flask import Flask
import os
import socket

app = Flask(__name__)
counter = 0
name = "Svyatoslav"


@app.route("/")
def show_counter():
    return str(counter)


@app.route("/stat")
def increment():
    global counter
    counter_state = counter
    counter += 1
    return str(counter_state)


@app.route("/about")
def hello():
    html = "<h3>Hello, {_your_name_}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), _your_name_=name, hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
