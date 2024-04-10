from sdk.client import Client
from sdkgen import OAuth2, MemoryTokenStore

tokenStore = MemoryTokenStore()
scopes = ["backend"]

credentials = OAuth2(
    "test",
    "FRsNh1zKCXlB",
    "https://demo.fusio-project.org/authorization/token",
    "",
    tokenStore,
    scopes
)

client = Client("https://demo.fusio-project.org", credentials)

print("Operations:")
collection = client.backend().operation().get_all(0, 16, "")

for operation in collection.entry:
    print(" * " + operation.http_method + " " + operation.http_path)
