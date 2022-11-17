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

from plaidlink.models import plaidUser,plaidUserHistory
from datetime import datetime, timedelta

from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions


client_id = '62f79beeabd0340014152003'

secret = '77804cbff47224e1f1b3682aae0355'
dt=datetime.utcnow()
configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': client_id,
        'secret': secret,
    }
)
"""
secret = '7dc061496d3a4b6cc0aec4692e8c333'

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
        
    )
    # create link token
    response = client.link_token_create(request)
    link_token = response['link_token']
    return link_token

def insertPlaidHistory(id,username):
    instance=plaidUser.objects.get(Sugan_id=id)
    pobj=plaidUserHistory.objects.create(
            Sugan_id_id      =id,
            plaid_id_id      =instance.plaid_id,
            access_token   =instance.access_token,
            linkReason     ="connecting bank",
            creUser=username,
            CreatedTs = dt,
            UpdateTs =dt,
            InsUpdFlag ="I",)
    # print(pobj.EventID)
    return

def getAccountsDetails(token):
    timespan_weeks = 4 * 24  # Plaid only goes back 24 months
    start_date = datetime.now() + timedelta(weeks=(-timespan_weeks))
    start_date = start_date.date()
    end_date = datetime.now().date()

    request = TransactionsGetRequest(
        access_token=token,
        start_date=start_date,
        end_date=end_date,
        options=TransactionsGetRequestOptions()
    )
    response = client.transactions_get(request)
    transactions = response['transactions']
    # Manipulate the count and offset parameters to paginate
    # transactions and retrieve all available data
    accounts = response['accounts']
    while len(transactions) < response['total_transactions']:
        request = TransactionsGetRequest(
            access_token=token,
            start_date=start_date,
            end_date=end_date,
            options=TransactionsGetRequestOptions(
                offset=len(transactions)
            )
        )
        response = client.transactions_get(request)
        transactions.extend(response['transactions'])

    keys1 = ['account_id'
        , 'account_owner'
        , 'amount'
        , 'authorized_date'
        , 'authorized_datetime'
        , 'category'
        , 'category_id'
        , 'check_number'
        , 'date'
        , 'datetime'
        , 'iso_currency_code'
        , 'location'
        , 'merchant_name'
        , 'name'
        , 'payment_channel'
        , 'payment_meta'
        , 'pending'
        , 'pending_transaction_id'
        , 'personal_finance_category'
        , 'transaction_code'
        , 'transaction_id'
        , 'transaction_type'
        , 'unofficial_currency_code'
             ]

    location_keys = ['address', 'city', 'country', 'lat', 'lon', 'postal_code', 'region', 'store_number']
    payment_meta_keys = ['by_order_of', 'payee', 'payer', 'payment_method', 'payment_processor', 'ppd_id', 'reason',
                         'reference_number']

    final_out = []
    out = []

    for j in keys1:
        if j == "location":
            for k in location_keys:
                out.append(k)
        elif j == "payment_meta":
            for k in payment_meta_keys:
                out.append(k)
        else:
            out.append(j)

    header_str = "|".join(out)
    final_out.append(header_str)

    for i in transactions:
        out = []
        for j in keys1:
            if j == "location":
                for k in location_keys:
                    i1 = i.get(j, '')
                    out.append(i1.get(k, ''))
            elif j == "payment_meta":
                for k in payment_meta_keys:
                    i1 = i.get(j, '')
                    out.append(i1.get(k, ''))
            else:
                out.append(i.get(j, ""))
        data_str = "|".join([str(i) for i in out])
        final_out.append(data_str)

    account_xs = []
    account_keys = ["account_id", "balances", "mask", "name", "official_name", "subtype", "type"]
    balance_keys = ["available", "current", "iso_currency_code", "limit", "unofficial_currency_code"]

    out = []
    for i in account_keys:
        if i == "balances":
            for j in balance_keys:
                out.append(j)
        else:
            out.append(i)
    header_str = "|".join(out)
    account_xs.append(header_str)

    for k in accounts:
        print(k)
        out = []
        for i in account_keys:
            print(i)
            if i == "balances":
                for j in balance_keys:
                    val = k.get(i, '')
                    print(val)
                    out.append(val.get(j, ''))
            else:
                print(k.get(i, ''))
                out.append(k.get(i, ''))
        print(out)
        data_str = "|".join([str(i) for i in out])
        account_xs.append(data_str)

    return final_out, account_xs
