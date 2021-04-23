#!/usr/bin/env python3

from typing import Optional

from jsonresume.datatypes import Location, Position


class Work(Position):
    def __init__(
        self,
        company: str = "",
        position: str = "",
        start_date: str = "",
        highlights: str = "",
        end_date: Optional[str] = None,
        summary: Optional[str] = None,
        website: Optional[str] = None,
        location: Optional[Location] = None,
    ):
        Position.__init__(
            self,
            position=position,
            website=website,
            start_date=start_date,
            end_date=end_date,
            summary=summary,
            highlights=highlights,
            location=location,
        )
        self.company: str = company
