from linter.rule import Severity
from linter.rules.id_dimension_must_be_string import IdDimensionMustBeString


def test_run_method_successfully_validates_merchant_id_string() -> None:
    rule = IdDimensionMustBeString(Severity.ERROR.value)

    field = {
        'name': 'merchant_id',
        'type': 'string'
    }
    rule_result = rule.run(field)
    assert rule_result == True

def test_run_method_fails_merchant_id_number() -> None:
    rule = IdDimensionMustBeString(Severity.ERROR.value)

    field = {
        'name': 'merchant_id',
        'type': 'number'
    }
    rule_result = rule.run(field)
    assert rule_result == False


def test_run_method_fails_sql_reference_number() -> None:
    rule = IdDimensionMustBeString(Severity.ERROR.value)

    field = {
        'name': 'merchant_pk',
        'type': 'number',
        'sql': '${TABLE}.merchant_id'
    }
    rule_result = rule.run(field)
    assert rule_result == False

def test_run_method_ignores_unrelated_field() -> None:
    rule = IdDimensionMustBeString(Severity.ERROR.value)

    field = {
        'name': 'order_amount',
        'type': 'number',
        'sql': '${TABLE}.amount'
    }
    rule_result = rule.run(field)
    assert rule_result == True