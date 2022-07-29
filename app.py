import cv2
from object_detection import object_detection
from speech import voice_write
from playsound import playsound
import time

INTERVAL = 5

def main():
    cap = cv2.VideoCapture(0)
    start = time.time()
    while True:
        _, img = cap.read()
        if time.time() - start > INTERVAL:
            objects = object_detection(img)
            names = list(set(objects['name'])) # 名前だけ抽出
            sentence = make_sentence(names)
            wav_path = voice_write(sentence)
            playsound(wav_path)
            start = time.time()

        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

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
    main()
