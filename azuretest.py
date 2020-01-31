from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

# Tenant ID for your Azure subscription
TENANT_ID = 'ad654bce-b5cb-4cc7-92b1-9683ec967c14'

# Your service principal App ID
CLIENT = 'a84ff698-df73-4c4f-b715-bf44519f60e7'

# Your service principal password
KEY = '09807e8d5020485d817809e07eaa047c'

subscription_id = '2b7ba058-853a-4632-8d3d-31206ae17523'

credentials = ServicePrincipalCredentials(
    client_id = CLIENT,
    secret = KEY,
    tenant = TENANT_ID
)

client = ComputeManagementClient(credentials, subscription_id)


