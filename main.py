# -*- coding: utf-8 -*-

import keyboard

from pythainlp.util import isthai
from pythainlp import spell

data = []
emp_key = ["shift","enter","backspace","tab","caps","esc","ctrl"]
def detect_key():
    while True:
        if str(keyboard.read_key()) == "esc":
            break
        else:
            word = str(keyboard.read_key())
            if word in emp_key:
                data.append("")
            else:
                data.append(word)
detect_key()         
def ListToString(s):
    str1=""
    return (str1.join(s))         
          
EN_TH_KEYB_PAIRS = {
    "Z": "(",
    "z": "ผ",
    "X": ")",
    "x": "ป",
    "C": "ฉ",
    "c": "แ",
    "V": "ฮ",
    "v": "อ",
    "B": "\u0e3a",  # พินทุ
    "b": "\u0e34",  # สระอุ
    "N": "\u0e4c",  # การันต์
    "n": "\u0e37",  # สระอือ
    "M": "?",
    "m": "ท",
    "<": "ฒ",
    ",": "ม",
    ">": "ฬ",
    ".": "ใ",
    "?": "ฦ",
    "/": "ฝ",
    "A": "ฤ",
    "a": "ฟ",
    "S": "ฆ",
    "s": "ห",
    "D": "ฏ",
    "d": "ก",
    "F": "โ",
    "f": "ด",
    "G": "ฌ",
    "g": "เ",
    "H": "\u0e47",  # ไม้ไต่คู้
    "h": "\u0e49",  # ไม้โท
    "J": "\u0e4b",  # ไม้จัตวา
    "j": "\u0e48",  # ไม้เอก
    "K": "ษ",
    "k": "า",
    "L": "ศ",
    "l": "ส",
    ":": "ซ",
    ";": "ว",
    '"': ".",
    "'": "ง",
    "Q": "๐",
    "q": "ๆ",
    "W": '"',
    "w": "ไ",
    "E": "ฎ",
    "e": "\u0e33",  # สระอำ
    "R": "ฑ",
    "r": "พ",
    "T": "ธ",
    "t": "ะ",
    "Y": "\u0e4d",  # นิคหิต
    "y": "\u0e31",  # ไม้หันอากาศ
    "U": "\u0e4a",  # ไม้ตรี
    "u": "\u0e35",  # สระอ ี
    "I": "ณ",
    "i": "ร",
    "O": "ฯ",
    "o": "น",
    "P": "ญ",
    "p": "ย",
    "{": "ฐ",
    "[": "บ",
    "}": ",",
    "]": "ล",
    "|": "ฅ",
    "\\": "ฃ",
    "~": "%",
    "`": "_",
    "@": "๑",
    "2": "/",
    "#": "๒",
    "3": "-",
    "$": "๓",
    "4": "ภ",
    "%": "๔",
    "5": "ถ",
    "^": "\u0e39",  # สระอู
    "6": "\u0e38",  # สระอุ
    "&": "฿",
    "7": "\u0e36",  # สระอึ
    "*": "๕",
    "8": "ค",
    "(": "๖",
    "9": "ต",
    ")": "๗",
    "0": "จ",
    "_": "๘",
    "-": "ข",
    "+": "๙",
    "=": "ช",
}

TH_EN_KEYB_PAIRS = {v: k for k, v in EN_TH_KEYB_PAIRS.items()}

EN_TH_TRANSLATE_TABLE = str.maketrans(EN_TH_KEYB_PAIRS)
TH_EN_TRANSLATE_TABLE = str.maketrans(TH_EN_KEYB_PAIRS)

def eng_to_thai(text: str) -> str:
    return text.translate(EN_TH_TRANSLATE_TABLE)

def thai_to_eng(text: str) -> str:
    return text.translate(TH_EN_TRANSLATE_TABLE)

message = ListToString(data)
print(thai_to_eng(message))

'''
def checkLang(m):
    if isthai(m) == True:
        print(thai_to_eng(m))
    else:
        print(eng_to_thai(m))
'''        
        

            
    

