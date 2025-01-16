import cx_Oracle
from azure.storage.blob import BlobServiceClient

# Connect to Oracle DB
connection = cx_Oracle.connect('username', 'password', 'hostname/SID')
cursor = connection.cursor()
cursor.execute("SELECT * FROM Agent_Details")

# Fetch all data
data = cursor.fetchall()

# Connect to Azure Blob Storage
blob_service_client = BlobServiceClient(account_url="https://<account_name>.blob.core.windows.net", credential="<credential>")
container_client = blob_service_client.get_container_client("<container_name>")

# Upload data to Azure Data Lake
for row in data:
    blob_client = container_client.get_blob_client(f"data_{row[0]}.csv")
    blob_client.upload_blob(','.join(map(str, row)), overwrite=True)
