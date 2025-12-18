from linter.rule import Rule
from typing import Any, Tuple


class PrimaryKeyIsFirstDimensionInView(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('view',)

    def run(self, view: Any) -> bool:
        # If the view extends another view, the Primary Key order check can be skipped.
        if 'extends' in view:
            return True
        dimensions = view.get('dimensions', [])
        if len(dimensions) > 0 and dimensions[0].get('primary_key') != 'yes':
            return False
        return True
