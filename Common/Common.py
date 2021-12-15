# -*- coding: gbk -*-
from enum import IntEnum
from typing import Final
from sched import scheduler
from time import time, sleep


STRING_NONE: Final[str] = ""
SYSTEM_VERSION: Final[str] = r"V0.0.1"


# event priority
class EventPriority(IntEnum):
    ClipCaptureEvent = 0,


class GSched:
    g_sched: scheduler = scheduler(time, sleep)

    @staticmethod
    def Run() -> None:
        GSched.g_sched.run()
