from __future__ import annotations


from enum import Enum
from typing import Tuple, List

class Type(Enum):
    INT = 0,
    LONG = 1,
    FLOAT = 2,
    DOUBLE = 3,
    BYTE = 4,
    SHORT = 5,
    UNKNOWN = 6

    @staticmethod
    def parse_type(s: str) -> Type:
        match s.lower():
            case "int":
                return Type.INT
            case "float":
                return Type.FLOAT
            case "long":
                return Type.LONG
            case "double":
                return Type.DOUBLE
            case "short":
                return Type.SHORT
        return Type.UNKNOWN





class Format():
    def __init__(self) -> None:
        self.count = -1 
        self.cols: List[Tuple[Type, str]] = []
        self.rows = []

    def format_binary(self, bin: bytes):
        ...

    
    def debug(self) -> str:
        out = f"Count: {self.count}\n"
        for col in self.cols:
            out += f"{col[1]}:{col[0]}\n"
 
        return out


    def parse(self, input: str):
        input_lines = input.strip().split("\n")
        f = open("test.txt", "w")
        
        for line in input_lines:
            try:
                name, type_ = line.split(":")
                name = name.strip()
                type_= type_.strip()
                if name.lower() == "count":
                    self.count = int(type_)
                else:
                    self.cols.append((Type.parse_type(type_), name))
            except:
                ...
        f.write(self.debug())
