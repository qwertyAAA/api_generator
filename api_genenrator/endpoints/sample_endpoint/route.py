from api_genenrator.endpoints.sample_endpoint.apps import apps
from api_genenrator.endpoints.sample_endpoint.views import (
    get_view,
    get_list_view,
    post_view,
    put_view,
    delete_view
)
from api_genenrator.common.route import register

registered_apps = []

for task_name, app in apps.items():
    register(
        app,
        path="/{task_id}",
        view_func=get_view,
        description=f"get {task_name} test case"
    )
    register(
        app,
        path="",
        view_func=get_list_view,
        description=f"get {task_name} test cases"
    )
    register(
        app,
        path="/{task_id}",
        view_func=post_view,
        request_method="POST",
        description=f"update {task_name} test case"
    )
    register(
        app,
        path="",
        view_func=put_view,
        request_method="PUT",
        description=f"create {task_name} test case"
    )
    register(
        app,
        path="/{task_id}",
        view_func=delete_view,
        request_method="DELETE",
        description=f"delete {task_name} test case"
    )
    registered_apps.append(app)
