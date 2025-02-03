from enum import Enum


class TaxType(str, Enum):
    PIS = "PIS"
    COFINS = "COFINS"
    CLSS = "CSLL"
