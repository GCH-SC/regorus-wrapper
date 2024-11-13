import regorus
import json

def test_build():
    policy = '''
        package app.abac

        import rego.v1

        default allow := false

        allow if {
            creditor_is_valid
            debtor_is_valid
            period_is_valid
            amount_is_valid
        }
        creditor_is_valid if data.account_attributes[input.creditor_account].owner == input.creditor
        debtor_is_valid if data.account_attributes[input.debtor_account].owner == input.debtor

        period_is_valid if input.period <= 30
        amount_is_valid if data.account_attributes[input.debtor_account].amount >= input.amount
    '''
    input_data = json.dumps({
        'creditor_account':11111,
        'creditor':'alice',
        'debtor_account':22222,
        'debtor':'bob',
        'period':30,
        'amount':1000
        })

    opa_engine = regorus.Engine()
    opa_engine.add_policy('rego', policy)
    opa_engine.set_input_json(input_data)
    result = opa_engine.eval_query(f'data.app.abac')

    print('Access Allowed:', result)

    assert result['result'][0]['expressions'][0]['value'] == {'allow': False, 'period_is_valid': True}

