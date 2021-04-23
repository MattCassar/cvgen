#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Optional


@dataclass
class Award:
    title: str
    date: str
    awarder: Optional[str] = None
    summary: Optional[str] = None
