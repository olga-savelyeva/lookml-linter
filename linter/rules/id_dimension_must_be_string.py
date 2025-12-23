from linter.rule import Rule
from typing import Any, Tuple, Union


class IdDimensionMustBeString(Rule):
    @staticmethod
    def applies_to() -> Tuple[str, ...]:
        return 'dimension',

    def run(self, lookml_object, runtime_params: Union[Any, None] = None) -> bool:
        name = lookml_object.get('name', '')
        sql = lookml_object.get('sql', '')
        field_type = lookml_object.get('type', 'string')

        target_ids = self.params.get('search_terms', [])

        for target in target_ids:
            if target in name or target in sql:
                if field_type == 'yesno':
                    continue
                if field_type != 'string':
                    return False

        return True

    def message(self) -> str:
        return 'Dimensions referencing "merchant_id" must be type: string.'
