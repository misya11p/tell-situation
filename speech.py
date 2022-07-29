import subprocess
import os
import argparse
from playsound import playsound

duration = 'intel/text-to-speech-en-0001/text-to-speech-en-0001-duration-prediction/FP16/text-to-speech-en-0001-duration-prediction.xml'
forword = 'intel/text-to-speech-en-0001/text-to-speech-en-0001-regression/FP16/text-to-speech-en-0001-regression.xml'
generation = 'intel/text-to-speech-en-0001/text-to-speech-en-0001-generation/FP16/text-to-speech-en-0001-generation.xml'


def main(text, tmp_dir):
    wav_path = voice_write(text, tmp_dir)
    playsound(wav_path)


def voice_write(text, tmp_dir='tmp'):
    text_file = os.path.join(tmp_dir, 'input.txt')
    with open(text_file, 'w') as f:
        f.write(text)
    wav = os.path.join(tmp_dir, 'output.wav')
    command = f'python text_to_speech_demo.py -i {text_file} -o {wav} --model_duration {duration} --model_forward {forword} -m_melgan {generation}'
    subprocess.run(command, shell=True)
    return wav


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='喋るよ')
    parser.add_argument('text', type=str, help='テキスト')
    parser.add_argument('--tmp_dir', default='tmp/', type=str, help='tmpディレクトリのパス')
    args = parser.parse_args()
    main(**vars(args))
