def attrition_report(df):

    total = len(df)

    attrition_count = len(
        df[df["Attrition"] == "Yes"]
    )

    rate = (attrition_count / total) * 100

    print("\nAttrition Analysis")
    print("-" * 30)
    print(f"Attrition Rate: {rate:.2f}%")

    return rate