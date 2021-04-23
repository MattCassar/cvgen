#!/usr/bin/env python3

import json

import pytest

from jsonresume.awards import Award
from jsonresume.basics import Basics
from jsonresume.datatypes import Location, Name, Position, Profile
from jsonresume.education import Education, Publication
from jsonresume.resume import Resume
from jsonresume.skills import Interest, Language, Skill
from jsonresume.volunteer import Volunteer
from jsonresume.work import Work


def test_constructing_complete_resume():
    name = Name(first_name="Matt", last_name="Cassar")
    location = Location(
        address="1600 Pennsylvania Ave",
        postal_code="11111",
        city="Cambridge",
        state="MA",
        country_code="US",
    )
    linkedin_profile = Profile(
        network="LinkedIn",
        username="Matt Cassar",
        url="https://www.linkedin.com/in/matt-cassar-b6062b10b/",
    )
    basics = Basics(
        name=name,
        label="some_label",
        picture="headshot.jpg",
        email="matthew.cassar@tufts.edu",
        phone="111-111-1111",
        website="https://github.com/MattCassar",
        location=location,
        profiles=[linkedin_profile],
    )
    work = [
        Work(
            company="Amazon",
            position="SDE I",
            start_date="2019-07-08",
            highlights=["Did some random stuff for money"],
            location=Location(
                address="410 Terry Ave. North",
                postal_code="98109",
                city="Seattle",
                state="WA",
                country_code="US",
            ),
        )
    ]
    volunteer = [
        Volunteer(
            organization="Princton Plainsborough",
            position="Hospital Volunteer",
            start_date="2012-06-01",
            end_date="2012-09-01",
            highlights=["Did some random stuff for no money"],
            location=Location(
                address="Some St",
                postal_code="01111",
                city="Princeton",
                state="NJ",
                country_code="US",
            ),
        )
    ]
    education = [
        Education(
            institution="Tufts University",
            start_date="2015-09-01",
            end_date="2019-05-01",
            degree="BS",
            majors=["Engineering Science"],
            gpa="3.6",
            courses=["Numerical Linear Algebra", "Algorithms"],
            minors=["Math"],
            location=Location(
                address="419 Boston Ave",
                postal_code="02155",
                city="Medford",
                state="MA",
                country_code="US",
            ),
        )
    ]
    awards = [Award(title="Medal of Honor", date="1942-12-22", awarder="US Govt")]
    publications = [
        Publication(
            title="On the Origin of Species",
            publisher="NAS",
            release_date="1800-01-01",
            url="www.google.com",
        )
    ]
    skills = [
        Skill(name="Programming Languages", keywords=["Python", "Java", "C++"]),
        Skill(name="Tools", keywords=["Linux", "Git", "AWS"]),
    ]
    languages = [Language(language="English", fluency="native")]
    interests = [
        Interest(
            name="Sports",
            keywords=[
                "Sports with a ball",
                "Sports without a ball",
                "Sports outside",
                "Sports inside",
            ],
        )
    ]
    resume = Resume(
        basics,
        education=education,
        work=work,
        volunteer=volunteer,
        publications=publications,
        skills=skills,
        languages=languages,
        interests=interests,
    )
