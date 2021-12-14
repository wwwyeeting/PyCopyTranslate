# -*- coding: gbk -*-
import pyperclip
from threading import Timer
from enum import IntEnum
from Translate.TranslateAbc import LanguageEnum
from Translate.Google import GoogleTranslate


class TaskStatusEnum(IntEnum):
    InitDone = 0,
    Detecting = 1,
    ConvertDone = 2,
    ClipChanged = 3,


class ClipCapture:
    def __init__(self, interval: float) -> None:
        self._recent_value: str = ''
        self._translator = GoogleTranslate(LanguageEnum.ZH_CN, LanguageEnum.EN)
        self._status: TaskStatusEnum = TaskStatusEnum.InitDone
        self._task = Timer(interval, function=self.DetectTask)

    def DetectTask(self):
        temp_value: str = pyperclip.paste().replace('\n', ' ').replace('\r', ' ')
        if (self._status == TaskStatusEnum.InitDone) or (self._status == TaskStatusEnum.ConvertDone):
            self._recent_value = temp_value  # copying string must after system run
            self._status = TaskStatusEnum.Detecting

        elif self._status == TaskStatusEnum.Detecting:
            if temp_value != self._recent_value:
                self._recent_value = temp_value
                tsdata_done = self._translator.ConvertAndGetResult(temp_value)
                print(tsdata_done)
                pyperclip.copy(tsdata_done)
                self._status = TaskStatusEnum.ConvertDone

        self._task.run()

    def StartTask(self):
        self._task.run()
