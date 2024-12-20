from linter.helpers import starts_with_capital_or_digit_or_special_char
from linter.rule import Rule
from typing import Any, Tuple, Union
import re


class LabelCustomCheck(Rule):
    @staticmethod
    def applies_to() -> Tuple[str, ...]:
        return 'explore', 'view', 'field', 'dimension', 'measure'

        def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
            # List of lowercase words or units that should be ignored for capitalization checks
            allowed_lowercase_words = {
                "of", "in", "at", "on", "with", "without", "by", "and", "or", "but", "for", "to",
                "a", "an", "across", "per", "over", "nor"
            }
            measurement_units = {
                "g", "kg", "m", "cm", "mm", "min", "s", "h", "l", "ml", "km"
            }
    
            label = lookml_object.get('label')
            if label:
                if all(char.isspace() for char in label):
                    return False  # Consider it invalid if blank
    
                # Use regex to find liquid expressions and remove them before checking
                label = re.sub(r'{%\s*([^%]*)\s*%}', '', label)
    
                # Split the remaining text into words, retaining words with apostrophes
                words_in_label = re.findall(r'\b(?:\w+(?:\'\w+)?)\b', label)
    
                # Filter out measurement units and allowed lowercase words
                filtered_words = [
                    word for word in words_in_label
                    if word.lower() not in allowed_lowercase_words and word.lower() not in measurement_units
                ]
    
                # Check if remaining words start with a capital letter, a digit, or a special character
                return all(
                    word[0].isupper() or word[0].isdigit() or not word[0].isalnum()
                    for word in filtered_words
                )
    
            return True

    def message(self) -> str:
        return 'Every word in label should start with capital letter, digit or special character. Label can not be blank but can start with whitespaces and contain liquid-syntax.'
