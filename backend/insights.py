from collections import defaultdict

def calculate_insights(expenses):
    totals = defaultdict(float)

    for e in expenses:
        totals[e.category] += e.amount

    if not totals:
        return {"average": 0, "overspending": []}

    average = sum(totals.values()) / len(totals)

    overspending = [
        {
            "category": category,
            "total": total
        }
        for category, total in totals.items()
        if total > average * 1.2
    ]

    return {
        "average": round(average, 2),
        "overspending": overspending
    }
