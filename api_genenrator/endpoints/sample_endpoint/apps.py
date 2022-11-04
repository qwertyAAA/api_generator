from fastapi import APIRouter

available_resources = [
    "sample_resource1",
    "sample_resource2",
    "sample_resource3"
]

# get all available apps
apps = []
for resource_name in available_resources:
    assert resource_name.find("/") == -1
    apps.append(APIRouter(prefix=f"/{resource_name}", tags=[resource_name, ]))
