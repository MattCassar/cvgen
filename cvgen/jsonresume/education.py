#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Optional

from jsonresume.datatypes import Location


@dataclass
class Education:
    institution: str
    start_date: str
    degree: Optional[str]
    majors: Optional[List[str]]
    end_date: Optional[str]
    gpa: Optional[str]
    courses: Optional[List[str]]
    minors: Optional[List[str]]
    location: Optional[Location]


@dataclass
class Publication:
    title: str
    publisher: str
    release_date: str
    url: str
    summary: Optional[str] = None
