# -*- coding: gbk -*-
from abc import ABC, abstractmethod
from enum import IntEnum
from Translate.TranslateAbc import LanguageEnum
from Translate.Google import GoogleTranslate
from Common.Common import EventPriority, GSched


class TaskStatusEnum(IntEnum):
    InitDone = 0,
    Detecting = 1,
    ConvertDone = 2,
    ClipChanged = 3,


class ClipCaptureAbc(ABC):
    def __init__(self, interval: float) -> None:
        self.recent_value: str = ''
        self.translator = GoogleTranslate(LanguageEnum.ZH_CN, LanguageEnum.EN)
        self.status: TaskStatusEnum = TaskStatusEnum.InitDone
        self._interval: float = interval
        GSched.g_sched.enter(0, EventPriority.ClipCaptureEvent, self._DetectTask)

    def _DetectTask(self):
        GSched.g_sched.enter(self._interval, EventPriority.ClipCaptureEvent, self._DetectTask)
        temp_value: str = self.StartDetectTask()
        if self.status == TaskStatusEnum.InitDone:
            self.InitDoneTask(temp_value)

        elif self.status == TaskStatusEnum.Detecting:
            self.DetectingTask(temp_value)

        elif self.status == TaskStatusEnum.ConvertDone:
            self.ConvertDoneTask(temp_value)

    @abstractmethod
    def InitDoneTask(self, temp_value: str)-> None:
        raise NotImplementedError("must realize this function.")

    @abstractmethod
    def DetectingTask(self, temp_value: str) -> None:
        raise NotImplementedError("must realize this function.")

    @abstractmethod
    def ConvertDoneTask(self, temp_value: str) -> None:
        raise NotImplementedError("must realize this function.")

    @abstractmethod
    def StartDetectTask(self) -> str:
        raise NotImplementedError("must realize this function.")