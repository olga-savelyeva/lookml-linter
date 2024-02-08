from collections import defaultdict


def combine_error_logs(file_validator_error_log, linter_error_log):
    # Parse file_validator_error_log
    file_validator_errors = defaultdict(list)
    for line in file_validator_error_log.split('\n'):
        if line.strip():
            parts = line.split('`')
            if len(parts) >= 3:  # Ensure there are at least two backticks to extract filename and error message
                filename = parts[1]
                error_message = parts[2].strip()
                file_validator_errors[filename].append(f"    :x: File {error_message}")

    # Parse linter_error_log
    linter_errors = defaultdict(list)
    current_filename = None
    for line in linter_error_log.split('\n'):
        if line.strip():
            if line.startswith('`'):
                current_filename = line.strip('`')
            else:
                linter_errors[current_filename].append(line)

    # Combine errors
    combined_errors = []
    for filename, errors in linter_errors.items():
        if combined_errors:  # Add an extra newline between filenames
            combined_errors.append("")
        combined_errors.append(f"`{filename}`")  # Append the filename once
        combined_errors.extend(file_validator_errors.get(filename, []))
        combined_errors.extend(errors)

    # Output combined errors
    return '\n'.join(combined_errors)
