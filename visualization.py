import os
import matplotlib.pyplot as plt

os.makedirs("reports", exist_ok=True)

def plot_department_performance(data):

    plt.figure(figsize=(8, 5))

    data.plot(kind="bar")

    plt.title("Department Performance")
    plt.ylabel("Average Attendance")
    plt.xlabel("Department")

    plt.tight_layout()

    plt.savefig("reports/department_report.png")

    plt.show()


def plot_salary_distribution(df):

    plt.figure(figsize=(8, 5))

    plt.hist(df["Salary"], bins=5)

    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Number of Employees")

    plt.tight_layout()

    plt.savefig("reports/salary_report.png")

    plt.show()