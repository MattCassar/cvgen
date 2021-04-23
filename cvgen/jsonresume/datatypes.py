#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Location:
    address: str
    postal_code: str
    city: str
    country_code: str
    address_line_2: Optional[str] = None
    region: Optional[str] = None
    state: Optional[str] = None
    province: Optional[str] = None


@dataclass
class Profile:
    network: str
    username: str
    url: str


@dataclass
class Position:
    position: str
    start_date: str
    highlights: List[str]
    end_date: Optional[str] = None
    summary: Optional[str] = None
    website: Optional[str] = None
    location: Optional[Location] = None

    def __lt__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        return self.start_date < other.start_date


@dataclass
class Name:
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    title: Optional[str] = None
    suffix: Optional[str] = None
