import deco
import write_orders
from working_day import WorkingDay

if __name__ == "__main__":
    workingdays = []

    weekdays = deco.get_week_days()
    for day in weekdays:
        new_day = WorkingDay(day)
        workingdays.append(new_day)

    for workingday in workingdays:
        orders = deco.get_daily_priorities(workingday.get_date())
        for order in orders:
            workingday.add_order(order)

    write_orders.dump_orders(workingdays)
