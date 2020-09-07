from decimal import Decimal
from typing import List, NewType, Union, AnyStr

Digit = NewType('Digit', Union[str, float, int])

FACTOR: Decimal = Decimal(1024)
B: AnyStr = "b"
K: AnyStr = "k"
KB: AnyStr = "kb"
M: AnyStr = "m"
MB: AnyStr = "mb"
G: AnyStr = "g"
GB: AnyStr = "gb"
T: AnyStr = "t"
TB: AnyStr = "tb"
P: AnyStr = "p"
PB: AnyStr = "pb"
UNITS_B: List = [B]
UNITS_KB: List = [K, KB]
UNITS_MB: List = [M, MB]
UNITS_GB: List = [G, GB]
UNITS_TB: List = [T, TB]
UNITS_PB: List = [P, PB]
UNITS_LIST: List = UNITS_B + UNITS_KB + UNITS_MB + UNITS_GB + UNITS_TB + UNITS_PB
STANDARD_UNIT_B: AnyStr = B.upper()
STANDARD_UNIT_KB: AnyStr = K.upper()
STANDARD_UNIT_MB: AnyStr = M.upper()
STANDARD_UNIT_GB: AnyStr = G.upper()
STANDARD_UNIT_TB: AnyStr = T.upper()
STANDARD_UNIT_PB: AnyStr = P.upper()
