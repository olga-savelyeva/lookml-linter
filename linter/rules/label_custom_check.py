from linter.helpers import starts_with_capital_or_digit_or_special_char
from linter.rule import Rule
from typing import Any, Tuple, Union
import re


class LabelCustomCheck(Rule):
    @staticmethod
    def applies_to() -> Tuple[str, ...]:
        return 'explore', 'view', 'field', 'dimension', 'measure'

    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        label = lookml_object.get('label')
        if label:
            if all(char.isspace() for char in label):
                return False  # Consider it invalid if blank

            # Use regex to find liquid expressions and remove them before checking
            label = re.sub(r'{%\s*([^%]*)\s*%}', '', label)

            # Split the remaining text into words
            words_in_label = re.findall(r'\b(?:[^\W_]+(?:[-\'][^\W_]+)*|[-\']|(?:\d+))\b', label)

            # Check the remaining words using your custom logic
            return all(starts_with_capital_or_digit_or_special_char(word) for word in words_in_label)

        return True

    def message(self) -> str:
        return 'Every word in label should start with capital letter, digit or special character. Label can not be blank but can start with whitespaces and contain liquid-syntax.'
