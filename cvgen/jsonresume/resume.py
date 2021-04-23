#!/usr/bin/env python3

from typing import List, Optional

from jsonresume.awards import Award
from jsonresume.basics import Basics
from jsonresume.education import Education, Publication
from jsonresume.skills import Interest, Language, Skill
from jsonresume.volunteer import Volunteer
from jsonresume.work import Work


class Resume:
    def __init__(
        self,
        basics: Basics,
        work: Optional[List[Work]] = None,
        volunteer: Optional[List[Volunteer]] = None,
        education: Optional[List[Education]] = None,
        awards: Optional[List[Award]] = None,
        publications: Optional[List[Publication]] = None,
        skills: Optional[List[Skill]] = None,
        languages: Optional[List[Language]] = None,
        interests: Optional[List[Interest]] = None,
    ):
        self.basics: Basics = basics
        self.work: Optional[List[Work]] = work
        self.volunteer: Optional[List[Volunteer]] = volunteer
        self.education: Optional[List[Education]] = education
        self.awards: Optional[List[Award]] = awards
        self.publications: Optional[List[Publication]] = publications
        self.skills: Optional[List[Skill]] = skills
        self.languages: Optional[List[Language]] = languages
        self.interests: Optional[List[Interest]] = interests
