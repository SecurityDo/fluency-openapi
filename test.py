from fluency_grid_management_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://develop.cloud.fluencysecurity.com", token="xxxx")


from fluency_grid_management_api_client.models import Asset
from fluency_grid_management_api_client.models import User
from fluency_grid_management_api_client.api.default import get_api_grid_assets_name as get_asset
from fluency_grid_management_api_client.types import Response
from fluency_grid_management_api_client.api.default import get_api_grid_users_name as get_user

#response: Response[Asset] = get_asset.sync_detailed(client=client, name="demo-asset-abc", account="demo")
#print(response)

asset: Asset = get_asset.sync(client=client, name="WIN-CLIENT-4", account="demo")
print(asset)


user: User = get_user.sync(client=client, name="foo@abc.com", account="demo")
print(user)
