from linter.rule import Severity
from linter.rules.id_dimension_must_be_string import IdDimensionMustBeString


def test_run_method_successfully_validates_merchant_id_string() -> None:
    params = {'search_terms': ['merchant_id']}
    rule = IdDimensionMustBeString(Severity.ERROR.value, params)

    field = {
        'name': 'merchant_id',
        'type': 'string'
    }
    rule_result = rule.run(field)
    assert rule_result == True


def test_run_method_fails_merchant_id_number() -> None:
    params = {'search_terms': ['merchant_id']}
    rule = IdDimensionMustBeString(Severity.ERROR.value, params)

    field = {
        'name': 'merchant_id',
        'type': 'number'
    }
    rule_result = rule.run(field)
    assert rule_result == False


def test_run_method_fails_sql_reference_number() -> None:
    params = {'search_terms': ['merchant_id']}
    rule = IdDimensionMustBeString(Severity.ERROR.value, params)

    field = {
        'name': 'merchant_pk',
        'type': 'number',
        'sql': '${TABLE}.merchant_id'
    }
    rule_result = rule.run(field)
    assert rule_result == False


def test_run_method_ignores_unrelated_field() -> None:
    params = {'search_terms': ['merchant_id']}
    rule = IdDimensionMustBeString(Severity.ERROR.value, params)

    field = {
        'name': 'order_amount',
        'type': 'number',
        'sql': '${TABLE}.amount'
    }
    rule_result = rule.run(field)
    assert rule_result == True