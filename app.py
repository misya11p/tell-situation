import cv2
from object_detection import object_detection
from speech import voice_write
from playsound import playsound
import time
import argparse


def main(device_id=0, interval=5.):
    cap = cv2.VideoCapture(device_id)
    start = time.time()
    while True:
        _, img = cap.read()

        if time.time() - start > interval:
            speech_situation(img)
            start = time.time()

        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def speech_situation(img):
    objects = object_detection(img)
    names = list(set(objects['name']))
    sentence = make_sentence(names)
    wav_path = voice_write(sentence)
    playsound(wav_path)


def make_sentence(objects):
    n_obj = len(objects)
    if n_obj == 0:
        sentence = "There's nothing."
    elif n_obj == 1:
        sentence = f"In front of you are {objects[0]}."
    else:
        sentence = f"In front of you are {', '.join(objects[:-1])} and {objects[-1]}."
    return sentence


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='カメラから得た状況を音声で伝える')
    parser.add_argument('--device_id', type=int, default=0, help='デバイスのid')
    parser.add_argument('--interval', type=float, default=5., help='次に音声を読み上げるまでの時間(s)')
    args = parser.parse_args()
    main(**vars(args))
