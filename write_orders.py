import os
from datetime import date
import deco

DESKTOP_PATH = os.path.join(os.path.join(os.path.expanduser('~')), 'Scrivania')
FILE_PATH = DESKTOP_PATH + "/old_priorities.txt"

week_days = deco.get_week_days()
days_name = ["LUNEDÌ", "MARTEDÌ", "MERCOLEDÌ", "GIOVEDÌ", "VENERDÌ", "SABATO", "DOMENICA"]


def link_days_orders(orders):
    days_orders = []
    i = 0
    for week_day in week_days:
        days_orders.append({'day': week_day, 'orders': []})
        for order in orders:
            order_date = format_day(order)
            if order_date == week_day:
                days_orders[i]['orders'].append(order)

        i += 1

    return days_orders


def format_day(order):
    due_date = order["date_due"]
    due_year = due_date[0:4]
    due_month = due_date[5:7]
    due_day = due_date[8:10]

    order_date = date(int(due_year), int(due_month), int(due_day))
    return order_date


def dump_orders(workingdays):

    with open(FILE_PATH, "w") as f:
        for day in workingdays:
            if day.has_orders():
                f.write(day.get_day())
                f.write("----------------\n")
                for order in day.get_orders():
                    billing_details = order["billing_details"]
                    if billing_details["company"] != "":
                        customer_name = billing_details["company"]
                    else:
                        customer_name = f"{billing_details['firstname']} {billing_details['lastname']}"

                    if order["job_name"] == "":
                        job_name = customer_name
                    else:
                        job_name = order["job_name"]

                    item_name = f"{order['order_id']} - {customer_name} - {job_name}"
                    f.write(f"Ordine {item_name}\n")
                f.write("\n\n")
