import cv2
import numpy as np
from math import dist


class VolumeController:
    """Volume controller module, gets image and hand landmarks to controll a volume bar
    """
    MAX_VOLUME_DISTANCE = 250
    MINIMUM_DISTANCE = 0.1
    
    def __init__(self, hand_detector) -> None:
        self.cap = cv2.VideoCapture(0)
        self.hand_detector = hand_detector
        
    def get_image(self) -> np.ndarray:
        """Captures frame from webcam

        :return: Frame as numpy
        """
        ret, image = self.cap.read()
        if not ret:
            # Ignoring empty camera frame
            return
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image
    
    def process_image(self, image: np.ndarray) -> tuple:
        """Processes image to obtain points for thumb and index fingers respectively

        :param image: Input image
        :return: (x, y) points for thumb and index fingers
        """
        landmarks = self.hand_detector.process(image)
        h, w, _ = image.shape
        points = self.hand_detector.get_thumb_and_index_points(h, w, landmarks)
        return points

    def controll_volume(self) -> None:
        """Starts a loop capturing frames and controlling the volume bar based on fingers distance
        To quit, close window or press ESC
        """
        volume = 0.5
        while self.cap.isOpened():
            image = self.get_image()

            if image is None:
                continue

            points = self.process_image(image)
            # Drawing circles at thumb and index fingers locations
            self.hand_detector.draw_thumb_and_index(image, points)
            
            # Only adjust volume if points were found
            if points:
                volume = max(min((dist(*points)/self.MAX_VOLUME_DISTANCE)-self.MINIMUM_DISTANCE, 1), 0)
            
            # Go from 360 to 75
            height_volume_bar = 360 - int(285*(volume))
            green = (0, 255, 0)
            cv2.rectangle(image, (50, height_volume_bar), (100, 360), green, cv2.FILLED)

            # Printing volume percentage on image
            cv2.putText(image, f"{round(volume*100)}%", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, green, thickness=2)
            
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            cv2.imshow('Controlador de Volume', image)
            
            # Press ESC to leave
            if cv2.waitKey(5) & 0xFF == 27:
                break

        self.cap.release()
