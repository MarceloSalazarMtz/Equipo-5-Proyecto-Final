from flask import Flask, render_template, Response
from camera import ThreadCamera
from threading import Thread
from time import sleep
import cv2

app = Flask(__name__)


@app.route('/')
def video_feed():

    # Start camera frame in separate frame
    return Response(gen(ThreadCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def gen(camera):
    camera.start()
    while True:
        image = None
        hasFrame, frame = camera.get_buffer_frame()
        if hasFrame:
            _, image = cv2.imencode('.jpg', frame)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + image.tobytes() + b'\r\n\r\n')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
