from analyzer import analyze_log
from report_generator import generate_report, save_report

log_file = "sample_logs/test_log.txt"

data = analyze_log(log_file)

report = generate_report(data)

print(report)

save_report(report)