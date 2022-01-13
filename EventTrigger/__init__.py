import json

def main(onTokenIssuanceStartRequest: str) -> str:
    if onTokenIssuanceStartRequest['requestStatus'] == 'Successful': 
        onTokenIssuanceStartRequest['response']['actions'].append({
            'type': 'ProvideClaimsForToken',
            'claims': [
                {
                    'id': 'DateOfBirth',
                    'value': '01/01/2000'
                },
                {
                    'id': 'CustomRoles',
                    'value': [
                        'Writer',
                        'Editor'
                    ]
                },
                {
                    'id': 'SocialSecurityNumber',
                    'value': '123-45-6789'
                }
            ]
        })

    return onTokenIssuanceStartRequest['response']



