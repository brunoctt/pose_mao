import mediapipe as mp
import numpy as np
import cv2


class HandDetector:
    """Hand detector
    """
    mp_drawing = mp.solutions.drawing_utils
    mp_ds = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands
    
    def __init__(self, model_complexity: int = 0, max_num_hands: int = 2, detection_conf: float = 0.5) -> None:
        self.hands = self.mp_hands.Hands(
            model_complexity=model_complexity,
            max_num_hands=max_num_hands,
            min_tracking_confidence=detection_conf
        )
        # Index of tips of thumb and index fingers
        self.thumb = 4
        self.index = 8

    def process(self, image: np.ndarray) -> list:
        """Processes input image to find landmarks

        :param image: Input image
        :return: List with landmarks
        """
        results = self.hands.process(image)
        if results.multi_hand_landmarks:
            return results.multi_hand_landmarks
        return []

    def get_thumb_and_index_points(self, height, width, landmarks, hand=0) -> tuple:
        """Returns (x, y) coordinates of thumb and index fingers, respectively

        :param height: Image height
        :param width: Image width
        :param landmarks: List with landmarks
        :param hand: Which hand will choose, in case of more than one, defaults to 0
        :return: (x, y) coordinates of thumb and index
        """
        if not landmarks:
            return
        
        # Points with landmark data
        p1 = landmarks[hand].landmark[self.thumb]
        p2 = landmarks[hand].landmark[self.index]
        
        # Since points have relative values, must multiply by image size
        x1, y1 = int(p1.x * width), int(p1.y * height)
        x2, y2 = int(p2.x * width), int(p2.y * height)
        
        return (x1, y1), (x2, y2)
    
    def draw_thumb_and_index(self, image, points):
        """Draws thumb and index circles in image and draws a line between them

        :param image: Image to be drawn into
        :param points: Thumb and index finger positions, respectively
        """
        if not points:
            return

        (x1, y1), (x2, y2) = points
        
        cv2.circle(image, (x1, y1), 15, (255,0,255))
        cv2.circle(image, (x2, y2), 15, (255, 0, 255))
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 3)
