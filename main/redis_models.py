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
    list_id: str = Field(index=True)
    task_name: str
    complete: Optional[bool] = False


Migrator().run()
