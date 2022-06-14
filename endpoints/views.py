from pydantic import constr

from common import ResponseModel


def get_view(
        task_id: constr(max_length=36)
) -> ResponseModel:
    return ResponseModel(data={
        "task_id": task_id
    })


def get_list_view() -> ResponseModel:
    return ResponseModel()


def post_view(
        task_id: constr(max_length=36)
) -> ResponseModel:
    return ResponseModel(data={
        "task_id": task_id
    })


def put_view() -> ResponseModel:
    # todo implement idempotence
    return ResponseModel(code=201)


def delete_view(
        task_id: constr(max_length=36)
) -> ResponseModel:
    return ResponseModel(data={
        "task_id": task_id
    })
