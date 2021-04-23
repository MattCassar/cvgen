#!/usr/bin/env python3

from typing import List

from jsonresume.datatypes import Location, Name, Profile


class Basics:
    def __init__(
        self,
        name: Name,
        label: str,
        picture: str,
        email: str,
        phone: str,
        website: str,
        location: Location,
        profiles: List[Profile],
    ):
        self.name: Name = name
        self.label: str = label
        self.picture: str = picture
        self.email: str = email
        self.phone: str = phone
        self.website: str = website
        self.location: Location = location
        self.profiles: List[Profile] = profiles
