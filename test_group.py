from pprint import pprint
from facebook_scraper import _scraper
from facebook_scraper import *
from facebook_scraper.fb_types import Page
import json


set_cookies("cookie.json")

groups_list = [
    "2389065407971693",
    "ConstJobs",
    "1604035263187804",
    "537613993341852",
    "LondonConstructionJobs",
    "397659453953374",
    "263428594257052",
    "constructionandfm",
    "4JobSeekers.London",
    "4JobSeekers.Bristol",
    "495539547584818",
    "193641431514637",
    "397659453953374",
    "537613993341852",
    "1503654339941272",
]

for group in groups_list:
    print(group, len(list(get_posts(group=group, pages=1, options={"allow_extra_requests": False}))))