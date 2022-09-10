import plaid

from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.country_code import CountryCode
from plaid.model.depository_account_subtype import DepositoryAccountSubtype
from plaid.model.depository_account_subtypes import DepositoryAccountSubtypes
from plaid.model.depository_filter import DepositoryFilter
from plaid.model.link_token_account_filters import LinkTokenAccountFilters

from plaid.model.products import Products

client_id = '62f79beeabd03400141520036'

secret = '77804cbff47224e1f1b3682aae03556'

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)
"""
secret = '7dc061496d3a4b6cc0aec4692e8c3336'

configuration = plaid.Configuration(
    host=plaid.Environment.Development,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)

"""
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

# products - assets
# prudent to go with only transactions - Davon


def get_link_token(client_user_id):
    request = LinkTokenCreateRequest(
        # products=[Products('auth'), Products('transactions')],
        products=[Products('transactions')],
        client_name="Plaid Test App",
        country_codes=[CountryCode('US')],
        # redirect_uri='https://domainname.com/oauth-page.html',
        language='en',
        # webhook='https://sample-webhook-uri.com',
        link_customization_name='default',
        user=LinkTokenCreateRequestUser(client_user_id=client_user_id),
        account_filters=LinkTokenAccountFilters(
            depository=DepositoryFilter(
                account_subtypes=DepositoryAccountSubtypes(
                    [DepositoryAccountSubtype('checking'), DepositoryAccountSubtype('savings'), DepositoryAccountSubtype('hsa')]
                )
            )
        )
    )
    # create link token
    response = client.link_token_create(request)
    link_token = response['link_token']
    return link_token


