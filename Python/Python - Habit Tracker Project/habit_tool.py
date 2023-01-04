from  datetime import datetime

def break_habit(habit_name, start_date, cost_per_day, minutes_wasted):
    # Personal Details
    goal = 60
    hourly_wage = 30 # dollars
 

    # Toal time allow in seconds
    time_elapsed = (datetime.now() - start_date).total_seconds()

    # Convert timestamps to hour/days
    hours = round(time_elapsed / 60 / 60, 1)
    days = round(hours / 24, 2)

    # Random bonus detail
    money_saved = cost_per_day * days
    minutes_saved = round(days * minutes_wasted)
    total_money_saved = f'${round(money_saved * (minutes_saved / 60 * hourly_wage), 2)}'


    # goals (days to go)
    days_to_go = round(goal - days)

    # change hours to day
    if hours > 72:
        hours = str(days) + ' days'
    else:
        hours = str(hours) + ' hours'

    return {'habit': habit_name, 'time_since': hours, 'days_remaining':days_to_go, 'minutes_saved': minutes_saved, 'money_saved': total_money_saved}