
Fusio Python CLI sample
=====

# About

This is a simple Python CLI application which shows how to use the Python SDK to access a Fusio instance.
In this example we simply output all registered routes.
Fusio is an open source API management which helps to build and manage great APIs more information at:
https://www.fusio-project.org/

```python
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

```
