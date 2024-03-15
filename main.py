from modules.hand_detector import HandDetector
from modules.volume_controller import VolumeController


def main():
    """Main module
    """
    hand_detector = HandDetector(detection_conf=0.7)
    volume_controller = VolumeController(hand_detector)
    volume_controller.controll_volume()


if __name__ == "__main__":
    main()
