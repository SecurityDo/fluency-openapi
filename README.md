# Generate project folder
openapi-python-client generate --path grid_api.yaml
cp test.py fluency-grid-management-api-client/.
cd fluency-grid-management-api-client
python3 test.py
