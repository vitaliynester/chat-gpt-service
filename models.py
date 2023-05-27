from dataclasses import dataclass


@dataclass
class RequestDTO:
    message: str


@dataclass
class ResponseDTO:
    message: str
