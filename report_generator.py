def generate_report(data):
    report = []
    report.append("=== TEST REPORT ===")
    report.append(f"Result: {data['result']}\n")

    report.append(f"Errors: {len(data['errors'])}")
    for e in data['errors']:
        report.append(f"- {e}")

    report.append(f"\nWarnings: {len(data['warnings'])}")

    report.append(f"\nValues over threshold: {data['over_limit']}")

    return "\n".join(report)


def save_report(report, filename="report.txt"):
    with open(filename, "w") as file:
        file.write(report)