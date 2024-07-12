from datetime import date
days_name = ["LUNEDÌ", "MARTEDÌ", "MERCOLEDÌ", "GIOVEDÌ", "VENERDÌ", "SABATO", "DOMENICA"]
months_name = ["GENNAIO", "FEBBRAIO", "MARZO", "APRILE", "MAGGIO", "GIUGNO", "LUGLIO", "AGOSTO", "SETTEMBRE",
               "OTTOBRE", "NOVEMBRE", "DICEMBRE"]


class WorkingDay:
    def __init__(self, workingday):
        self.date = workingday
        self.orders = []

    def get_day(self):
        week_day = days_name[self.date.weekday()]
        month_name = months_name[self.date.month - 1]
        return f"{week_day} {self.date.day} {month_name}\n"

    def add_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def has_orders(self):
        return len(self.orders) > 0

    def check_date(self, order_date):
        return self.date == order_date

    def get_date(self):
        return self.date
