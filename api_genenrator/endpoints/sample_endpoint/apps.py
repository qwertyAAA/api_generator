from fastapi import APIRouter

available_resources = {
    "sample_resource1": "r1",
    "sample_resource2": "r2",
    "sample_resource3": "r3"
}

# get all available apps
apps = {}
for resource_name in available_resources:
    assert resource_name.find("/") == -1
    apps[resource_name] = APIRouter(prefix=f"/{resource_name}", tags=[resource_name, ])
