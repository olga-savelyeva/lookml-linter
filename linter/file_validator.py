from typing import Dict


class FileValidator:

    def __init__(self, raw_files: Dict) -> None:
        super().__init__()
        self.__raw_files = raw_files
        self.__errors = []

    def validate(self) -> bool:
        result = True
        for raw_file_path, raw_file_lines in self.__raw_files.items():
            if '.view.lkml' in raw_file_path or '.explore.lkml' in raw_file_path:
                valid = self.validate_comment_in_the_header(raw_file_lines)
                if not valid:
                    result = False
                    reason = "missing" if len(raw_file_lines) < 7 else "incorrect format"
                    self.__errors.append((raw_file_path, reason))
        return result

    @property
    def errors(self):
        return self.__errors

    def error_log(self):
        messages = []
        for path, reason in self.errors:
            messages.append(f"- :x: File `{path}` has a {reason} header.")
        return '\n'.join(messages)

    @staticmethod
    def validate_comment_in_the_header(raw_file_lines) -> bool:
        return len(raw_file_lines) >= 7 \
            and '###' in raw_file_lines[0] \
            and '# Squad/Team:' in raw_file_lines[1] \
            and '# Owned by:' in raw_file_lines[2] \
            and '# Created:' in raw_file_lines[3] \
            and '# Purpose:' in raw_file_lines[4] \
            and '# Updated:' in raw_file_lines[5] \
            and '# Archived:' in raw_file_lines[6]