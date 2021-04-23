#!/usr/bin/env python3

from typing import Optional

from jsonresume.datatypes import Location, Position


class Volunteer(Position):
    def __init__(
        self,
        organization: str = "",
        position: str = "",
        start_date: str = "",
        highlights: str = "",
        end_date: Optional[str] = None,
        website: Optional[str] = None,
        summary: Optional[str] = None,
        location: Optional[Location] = None,
    ):
        Position.__init__(
            self,
            position=position,
            start_date=start_date,
            end_date=end_date,
            highlights=highlights,
            website=website,
            summary=summary,
            location=location,
        )
        self.organization: str = organization
