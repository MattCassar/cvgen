#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Skill:
    name: str
    keywords: List[str]
    level: Optional[str] = None


@dataclass
class Language:
    language: str
    fluency: str


@dataclass
class Interest:
    name: str
    keywords: str
