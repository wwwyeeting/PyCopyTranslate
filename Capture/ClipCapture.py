# -*- coding: gbk -*-
from pyperclip import copy, paste
from Capture.ClipCaptureAbc import ClipCaptureAbc, TaskStatusEnum


class ClipCapture(ClipCaptureAbc):
    def __init__(self, interval: float) -> None:
        super().__init__(interval)

    def InitDoneTask(self, temp_value: str)-> None:
        self.recent_value = temp_value  # copying string must after system run
        self.status = TaskStatusEnum.Detecting
        print('system init done.')
        print('-----------------------------------------------------------')

    def DetectingTask(self, temp_value: str) -> None:
        if temp_value != self.recent_value:
            self.recent_value = temp_value
            tsdata_done = self.translator.ConvertAndGetResult(temp_value)
            print(tsdata_done)
            print('-----------------------------------------------------------')
            copy(tsdata_done)
            self.status = TaskStatusEnum.ConvertDone

    def ConvertDoneTask(self, temp_value: str) -> None:
        self.recent_value = temp_value  # copying string must after system run
        self.status = TaskStatusEnum.Detecting

    def StartDetectTask(self) -> str:
        return paste().replace('\n', ' ').replace('\r', ' ')
