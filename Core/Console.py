#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Core.Stylesheet.Styling import sd, bc
from Core.Validity import Validation

class Console:
    def __init__(self):
        self.Validator = Validation()

    def Success(self, Message: str) -> None:
        if (self.Validator.NotEmpty(Message)):
            print(f"{sd.sBan} {Message.strip()}{bc.BC}\n")

    def Info(self, Message: str) -> None:
        if (self.Validator.NotEmpty(Message)):
            print(f"{sd.iBan} {Message.strip()}{bc.BC}\n")

    def Error(self, Message: str) -> None:
        if (self.Validator.NotEmpty(Message)):
            print(f"{sd.eBan} {Message.strip()}{bc.BC}\n")

    def Raw(self, Message: str, AppendNewLine: bool = True, IndentMessage = False) -> None:
        if (self.Validator.NotEmpty(Message)):
            RawString = f" {bc.BC}{Message.strip()}{bc.BC}"

            if (AppendNewLine):
                RawString += "\n"

            if (IndentMessage):
                RawString = f"\t {RawString}"

            print(RawString)