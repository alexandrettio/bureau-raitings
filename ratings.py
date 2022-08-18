from typing import Any, List, Optional

import requests
from pydantic import BaseModel, parse_obj_as


class Detail(BaseModel):
    course: str
    score: float
    met_deadlines: bool


class Week(BaseModel):
    score: float
    details: List[Detail]
    rank: int
    diff: Optional[int] = None


class User(BaseModel):
    uid: str
    english_name: str
    weeks: List[Week]
    started_at: str
    name: str
    gender: str
    photo: Any
    job: str
    organization: Optional[str]
    enrollment_status: str
    enrollment_granted: bool
    is_new: bool
    is_certification_started: bool
    city: str
    country: str
    diploma_title: Any
    diploma_url: Any
    diploma_score: Any
    diploma_art_director: Any
    diploma_patron: Any
    diploma_designers: Any
    diploma_editors: Any
    diploma_managers: Any


def get_rating():
    url = "https://bureau.ru/classroom/events/1637/reports/race.json"
    response = requests.get(url)
    ratings = parse_obj_as(List[User], response.json())
    print(ratings[0].uid)
