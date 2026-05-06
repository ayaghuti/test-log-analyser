def analyze_log(file_path, threshold=80):
    errors = []
    warnings = []
    values = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if "ERROR" in line:
                errors.append(line)

            elif "WARNING" in line:
                warnings.append(line)

            elif "Value=" in line:
                try:
                    value = int(line.split("=")[1])
                    values.append(value)
                except:
                    pass

    over_limit = [v for v in values if v > threshold]

    result = "FAIL" if errors or over_limit else "PASS"

    return {
        "result": result,
        "errors": errors,
        "warnings": warnings,
        "values": values,
        "over_limit": over_limit
    }