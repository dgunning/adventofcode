from rich import print
from .pytudes import *
from typing import Tuple
from dataclasses import dataclass
from collections import Counter
from functools import cached_property

Instruction = Tuple[str, int]