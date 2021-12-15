# -*- coding: gbk -*-
from abc import ABC, abstractmethod
from enum import IntEnum


class LanguageEnum(IntEnum):
    ZH_CN   = 0,  # Simple Chinese
    EN      = 1,  # English


class TranslateAbc(ABC):
    def __init__(self, to_lang: int, from_lang: int) -> None:
        self.to_lang: int       = to_lang
        self.from_lang: int     = from_lang

    def ChangeToLang(self, to_lang: int) -> None:
        self.to_lang = to_lang

    def ChangeFromLang(self, from_lang) -> None:
        self.from_lang = from_lang

    @abstractmethod
    def ConvertAndGetResult(self, input_text: str) -> str:
        raise NotImplementedError("must realize this function.")

    @abstractmethod
    def TestTranslate(self) -> None:
        raise NotImplementedError("must realize this function.")
