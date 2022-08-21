from collections import defaultdict
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


def get_rating(url="https://bureau.ru/classroom/events/1637/reports/race.json"):
    response = requests.get(url)
    users = parse_obj_as(List[User], response.json())
    
    results = []
    for _ in range(17):
        results.append(defaultdict(list))

    for user in users:
        for week_number, week_info in enumerate(user.weeks):
            for discipline in week_info.details:
                results[week_number][discipline.course].append((discipline.score, user.name))

    for week_number, week in enumerate(results, 1):
        for d in week.keys():
            if len(week[d]) != 0:
                week[d].sort()
                print(f"{d}-{week_number}")
                for u in week[d]:
                    print(u)


get_rating()
