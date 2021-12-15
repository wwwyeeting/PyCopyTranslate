# -*- coding: gbk -*-
from os import system
from Capture.ClipCapture import ClipCapture


if __name__ == '__main__':
    try:
        captor = ClipCapture(0.5)
        captor.StartTask()
    except KeyboardInterrupt:
        print(r"system end.")
        system("pause")
