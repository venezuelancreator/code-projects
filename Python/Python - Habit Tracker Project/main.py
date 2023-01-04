from datetime import datetime
from habit_tool import break_habit
import pandas as pd
from tabulate import tabulate

habits = [
    break_habit('Coffee', datetime(2023, 1, 3, 10), cost_per_day=2, minutes_wasted=15),
    break_habit('Soda', datetime(2023, 1, 3, 10), cost_per_day=2, minutes_wasted=15),
    break_habit('Fap', datetime(2023, 1, 3, 10), cost_per_day=2, minutes_wasted=15),
    break_habit('Gaming', datetime(2023, 1, 3, 10), cost_per_day=2, minutes_wasted=15),
]

df = pd.DataFrame(habits)

print(tabulate(df, headers='keys', tablefmt='psql'))

