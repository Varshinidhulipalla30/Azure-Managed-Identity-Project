from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

storage_url = "https://t030mistorage2026.blob.core.windows.net"
container_name = "appdata"

key_vault_url = "https://t030mikv260926.vault.azure.net/"
secret_name = "LegacyServiceCredential"

credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(
    account_url=storage_url,
    credential=credential
)

secret_client = SecretClient(
    vault_url=key_vault_url,
    credential=credential
)


@app.route("/")
def home():
    try:
        container_client = blob_service_client.get_container_client(container_name)
        blobs = [blob.name for blob in container_client.list_blobs()]

        secret = secret_client.get_secret(secret_name)

        return f"""
        <h1>Managed Identity Test Successful</h1>
        <p>App Service successfully accessed Azure Blob Storage.</p>
        <p>App Service successfully accessed Azure Key Vault.</p>
        <p><b>Authentication method:</b> Managed Identity</p>
        <p><b>Container:</b> {container_name}</p>
        <p><b>Blobs:</b> {blobs}</p>
        <p><b>Key Vault Secret:</b> Successfully Retrieved</p>
        """

    except Exception as e:
        return f"<h1>Authentication Failed</h1><p>{e}</p>", 500


if __name__ == "__main__":
    app.run()
