from collections import Counter, defaultdict

# Simulated server logs
logs = [
    "2026-03-08 INFO auth Login successful",
    "2026-03-08 ERROR database Connection failed",
    "2026-03-08 WARNING api Slow response",
    "2026-03-08 ERROR auth Invalid password",
    "2026-03-08 INFO api Request received",
    "2026-03-08 CRITICAL database Server crash",
    "2026-03-08 ERROR api Timeout error"
]

# Parse logs into dictionaries
parsed_logs = []

for log in logs:
    parts = log.split(" ", 3)

    log_dict = {
        "timestamp": parts[0],
        "level": parts[1],
        "module": parts[2],
        "message": parts[3]
    }

    parsed_logs.append(log_dict)


# Counters
error_messages = Counter()
modules = Counter()
levels = Counter()

# defaultdict for grouping
errors_by_module = defaultdict(list)

for entry in parsed_logs:

    levels[entry["level"]] += 1
    modules[entry["module"]] += 1

    if entry["level"] == "ERROR":
        error_messages[entry["message"]] += 1
        errors_by_module[entry["module"]].append(entry["message"])


# Summary
summary = {
    "total_entries": len(parsed_logs),
    "error_rate": (levels["ERROR"] / len(parsed_logs)) * 100,
    "top_errors": error_messages.most_common(3),
    "busiest_module": modules.most_common(1)[0][0]
}

print("Summary:", summary)
print("Errors grouped by module:", dict(errors_by_module))