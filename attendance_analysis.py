import pandas as pd

def attendance_report(df):
    avg_attendance = df["Attendance"].mean()

    print("\nAttendance Analysis")
    print("-" * 30)
    print(f"Average Attendance: {avg_attendance:.2f}%")

    return avg_attendance