# -*- coding: gbk -*-
from os import system
from Common.Common import GSched
from Capture.ClipCapture import ClipCapture


if __name__ == '__main__':
    try:
        captor = ClipCapture(0.5)
        GSched.Run()
    except KeyboardInterrupt:
        print(r"system end.")
        system("pause")
