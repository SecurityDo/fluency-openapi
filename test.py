from fluency_grid_management_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://develop.cloud.fluencysecurity.com", token="xxxx", timeout=180)


from fluency_grid_management_api_client.models import Asset
from fluency_grid_management_api_client.models import User
from fluency_grid_management_api_client.models import FPLReportResult, RunInvestigationRequest

from fluency_grid_management_api_client.api.default import get_asset_by_name as get_asset
from fluency_grid_management_api_client.types import Response
from fluency_grid_management_api_client.api.default import get_user_by_name as get_user

from fluency_grid_management_api_client.api.default import run_entity_investigation
from datetime import datetime, timedelta, timezone

#response: Response[Asset] = get_my_data_model.sync_detailed(client=client, name="demo-asset-abc", account="demo")
#print(response)

asset: Asset = get_asset.sync(client=client, name="WIN-CLIENT-4", account="demo")
#print(asset)


user: User = get_user.sync(client=client, name="foo@bar.com", account="demo")
#print(user)

now = datetime.now(timezone.utc)

req = RunInvestigationRequest(report_name="Investigation Office365 Login Activity", name="foo@bar.com", range_from=now - timedelta(days = 1), range_to=now)

report: FPLReportResult = run_entity_investigation.sync(client=client, json_body=req, account="demo")

print(report)
