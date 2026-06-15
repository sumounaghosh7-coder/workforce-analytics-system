def salary_report(df):

    stats = df["Salary"].describe()

    print("\nSalary Statistics")
    print("-" * 30)

    print(stats)

    return stats