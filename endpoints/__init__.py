from fastapi import APIRouter

available_resources = {
    "test1": "t1",
    "test2": "t2",
    "test3": "t3"
}

# get all available apps
apps = {}
for resource_name in available_resources:
    assert resource_name.find("/") == -1
    apps[resource_name] = APIRouter(prefix=f"/{resource_name}", tags=[resource_name, ])

__all__ = [
    "apps",
]
