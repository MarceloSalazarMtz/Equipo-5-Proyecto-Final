import cv2
from threading import Thread
from time import sleep
from darknet import *
from notifier import notify_police

import cv2


class ThreadCamera(object):
    def __init__(self, src=0):
        self.detection_buffer = []
        self.detection_backlog = []
        self.fps = 40
        self.frame_rate = (1000.0 / self.fps) / 1000.0
        self.stream = cv2.VideoCapture(src)
        self.realtime_buffer = []
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.network, self.class_names, self.class_colors = load_network(
            "./model/yolov4-obj.cfg", "./model/obj.data", "./model/yolov4-obj_best.weights")

        self.width = network_width(self.network)
        self.height = network_height(self.network)

    def __del__(self):
        self.stream.release()

    def copy(self, frame, times):
        for i in range(0, times):
            self.detection_buffer.append(frame)

    def get_buffer_frame(self):
        if len(self.detection_buffer) > 0:
            detected = self.detection_buffer.pop()
            self.realtime_buffer = []
            return True, detected
        elif len(self.realtime_buffer) > 0:
            return True, self.realtime_buffer.pop()
        return False, None

    def detect(self):
        while True:
            print('detecting')
            if len(self.detection_backlog) <= 0:
                print('no frame to detect, skipping frame')
                continue

            frame = self.detection_backlog.pop()
            print('starting detection')
            detections, width_ratio, height_ratio = self.darknet_helper(
                frame, self.width, self.height)

            if len(detections) == 0:
                print("no detections, next frame")
                continue

            frame, type, confidence = self.overlay_boxes(
                self.frame, detections, width_ratio, height_ratio)

            self.copy(frame, 60 * 3)
            print('detections: ' + str(len(detections)))
            notify_police(type, confidence)

    def start(self):
        Thread(target=self.get, args=()).start()
        Thread(target=self.detect, args=()).start()

        return self

    def overlay_boxes(self, img, detections, width_ratio, height_ratio):
        for label, confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(
                top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
            cv2.rectangle(img, (left, top), (right, bottom),
                          self.class_colors[label], 2)
            cv2.putText(img, "{} [{:.2f}]".format(label, float(
                confidence)), (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.class_colors[label], 2)
        return img, label, confidence

    def darknet_helper(self, img, width, height):
        darknet_image = make_image(width, height, 3)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img_rgb, (width, height),
                                 interpolation=cv2.INTER_LINEAR)

        # get image ratios to convert bounding boxes to proper size
        img_height, img_width, _ = img.shape
        width_ratio = img_width/width
        height_ratio = img_height/height

        # run model on darknet style image to get detections
        copy_image_from_bytes(darknet_image, img_resized.tobytes())
        detections = detect_image(
            self.network, self.class_names, darknet_image)
        free_image(darknet_image)
        return detections, width_ratio, height_ratio

    def get(self):
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                _, frame = self.stream.read()
                self.detection_backlog.append(frame)
                self.realtime_buffer.append(frame)
                sleep(self.frame_rate)

    def stop(self):
        self.stopped = True
