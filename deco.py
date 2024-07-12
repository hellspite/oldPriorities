import requests
import os
from datetime import datetime, date, timedelta, timezone

USERNAME = os.environ["DECO_USER"]
PASSWORD = os.environ["DECO_PASS"]
API_URL = "https://straighttohell.eu/api/json/manage_orders/find"


def get_daily_priorities(day):
    day_start_formatted = day.strftime("%Y-%m-%dT08:00:00")
    day_end_formatted = day.strftime("%Y-%m-%dT23:59:59")
    # Compensate the different timezone during the search
    # day_end = day + timedelta(days=1)
    # day_end_formatted = day_end.strftime("%Y-%m-%dT08:59:59")

    params = {
        "field": "5",
        "condition": "7",
        "date1": day_start_formatted,
        "date2": day_end_formatted,
        "sortby": 1,
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.get(API_URL, params=params)
    priorities = get_priorities(response.json())

    return priorities


def get_weekly_priorities():
    """Return a list of priorities for the current week

    Retrieve the data of the orders from Deco API
    """

    first_day, last_day = get_days()

    first_day_formatted = first_day.strftime("%Y-%m-%dT00:00:00")
    last_day_formatted = last_day.strftime("%Y-%m-%dT00:00:00")

    params = {
        "field": "5",
        "condition": "7",
        "date1": first_day_formatted,
        "date2": last_day_formatted,
        "sortby": 5,
        "username": USERNAME,
        "password": PASSWORD
    }

    response = requests.get(API_URL, params=params)
    priorities = get_priorities(response.json())

    return priorities


def get_days():
    """Return the starting end ending days of the current week"""
    today_day = datetime.today()

    starting_day = today_day - timedelta(35)

    return starting_day, today_day


def get_week_days():
    first_day, last_day = get_days()

    week_days = []
    day = date(first_day.year, first_day.month, first_day.day)

    for i in range(36):
        week_days.append(day)
        day = day + timedelta(1)

    return week_days


def get_priorities(json_response):
    """"""
    priorities = []

    for order in json_response["orders"]:
        if order["is_priority"] and order["order_status"] != 7 and order["order_status"] != 4\
                and order["order_status"] != 2 and order["order_status"] != 3:
            priorities.append(order)

    return priorities
