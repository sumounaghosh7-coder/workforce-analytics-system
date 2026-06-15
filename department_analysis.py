def department_report(df):

    performance = (
        df.groupby("Department")
        ["Attendance"]
        .mean()
    )

    print("\nDepartment Performance")
    print("-" * 30)

    print(performance)

    return performance