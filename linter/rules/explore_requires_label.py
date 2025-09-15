from linter.rule import Rule
from typing import Any, Tuple


class ExploreRequiresLabel(Rule):
    def applies_to() -> Tuple[str, ...]:
        return ('explore',)

    def run(self, explore: Any) -> bool:
        if not 'label' in explore:
            return False
        label = explore['label']
        valid_prefixes = ("PFY", "SNOW", "PFL", "FYUL")
        return any(label.startswith(prefix) for prefix in valid_prefixes)

    def message(self) -> str:
        return "Explore must have a label starting with PFY, PFL, SNOW or FYUL."
