#!/usr/bin/env python3
"""
Module that filters log messages
"""

import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns the log message obfuscated

    Args:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is
        separating all fields in the log line (message)

    The function should use a regex to replace occurrences
    of certain field values.

    filter_datum should be less than 5 lines long and
    use re.sub to perform the substitution with a single regex.
    """
    # Create a regex pattern that matches any of the fields to obfuscate
    field_pattern = '|'.join(fields)
    # Use a single re.sub call to replace all matching fields with redaction
    return re.sub(f'({field_pattern})=[^{separator}]*{separator}',
                  f'\\1={redaction}{separator}', message)
