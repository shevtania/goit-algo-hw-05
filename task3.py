import sys

parse_log_line(line: str) -> dict
load_logs(file_path: str) -> list
filter_logs_by_level(logs: list, level: str) -> list 
count_logs_by_level(logs: list) -> dict
display_log_counts(counts: dict)