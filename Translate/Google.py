# -*- coding: gbk -*-
from html import unescape
from re import findall
from typing import Final, List
from urllib.parse import quote
from requests import get
from Common.Common import STRING_NONE
from Translate.TranslateAbc import TranslateAbc


GOOGLE_TRANSLATE_URL: Final[str] = r'https://translate.google.cn/m?q=%s&tl=%s&sl=%s'
RE_GOOGLE_TRANS_RESULT_CONTAINER: Final[str] = r'(?s)class="(?:t0|result-container)">(.*?)<'


google_lang_table: List[str] = ["zh-CN", "en"]  # SN is same to LanguageEnum


class GoogleTranslate(TranslateAbc):
    def __init__(self, to_lang: int, from_lang: int) -> None:
        super().__init__(to_lang, from_lang)

    def ConvertAndGetResult(self, input_text: str) -> str:
        url = GOOGLE_TRANSLATE_URL % (
            quote(input_text), 
            google_lang_table[self.to_lang], 
            google_lang_table[self.from_lang]
        )
        try:
            res = get(url)
            result = findall(RE_GOOGLE_TRANS_RESULT_CONTAINER, res.text)

            if len(result):
                return unescape(result[0])
            else:
                return STRING_NONE
        except Exception as e:
            print(f"service is not accessible, see below:\r\n {e}")
            return STRING_NONE

    def TestTranslate(self) -> None:
        """test the service."""
        url = GOOGLE_TRANSLATE_URL % (
            quote(r"Hello Python."), 
            google_lang_table[self.to_lang], 
            google_lang_table[self.from_lang]
        )
        try:
            get(url)
            print(r"service is accessible.")
        except Exception as e:
            print(f"service is not accessible, see below:\r\n {e}")
