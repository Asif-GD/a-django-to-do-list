from typing import Optional

from redis_om import (
    Field,
    JsonModel,
    Migrator
)


class ToDoList(JsonModel):
    username: str = Field(index=True)
    list_name: str


class Task(JsonModel):
    list_pk: str = Field(index=True)
    task_name: str
    task_complete: Optional[bool] = False


Migrator().run()
