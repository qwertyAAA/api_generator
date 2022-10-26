from pydantic import constr

from api_genenrator.common import ResponseModel


def get_view(
        task_id: constr(max_length=36)
) -> ResponseModel:
    return ResponseModel(
        data={
            "task_id": task_id
        }
    )


def get_list_view() -> ResponseModel:
    return ResponseModel(data={"items": []})


def post_view() -> ResponseModel:
    return ResponseModel()


def put_view(
        task_id: constr(max_length=36)
) -> ResponseModel:
    return ResponseModel(
        status=201,
        data={
            "task_id": task_id
        }
    )


def delete_view(
        task_id: constr(max_length=36)
) -> ResponseModel:
    return ResponseModel(data={
        "task_id": task_id
    })
