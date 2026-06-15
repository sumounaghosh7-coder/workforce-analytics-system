import pandas as pd

from attendance_analysis import attendance_report
from attrition_analysis import attrition_report
from department_analysis import department_report
from salary_analysis import salary_report
from visualization import (
    plot_department_performance,
    plot_salary_distribution
)

df = pd.read_csv("employee_data.csv")

attendance_report(df)

attrition_report(df)

dept_data = department_report(df)

salary_report(df)

plot_department_performance(
    dept_data
)

plot_salary_distribution(df)