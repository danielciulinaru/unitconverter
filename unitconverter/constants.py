from typing import List

FACTOR: float = 1024
B: str = "b"
K: str = "k"
KB: str = "kb"
M: str = "m"
MB: str = "mb"
G: str = "g"
GB: str = "gb"
T: str = "t"
TB: str = "tb"
P: str = "p"
PB: str = "pb"
UNITS_B: List = [B]
UNITS_KB: List = [K, KB]
UNITS_MB: List = [M, MB]
UNITS_GB: List = [G, GB]
UNITS_TB: List = [T, TB]
UNITS_PB: List = [P, PB]
UNITS_LIST: List = UNITS_B + UNITS_KB + UNITS_MB + UNITS_GB + UNITS_TB + UNITS_PB
STANDARD_UNIT_B: str = B.upper()
STANDARD_UNIT_KB: str = K.upper()
STANDARD_UNIT_MB: str = M.upper()
STANDARD_UNIT_GB: str = G.upper()
STANDARD_UNIT_TB: str = T.upper()
STANDARD_UNIT_PB: str = P.upper()
