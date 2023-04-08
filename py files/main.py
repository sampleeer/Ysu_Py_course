import time
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple
from uuid import UUID

from task import DAGRunTask


class ExecutionStatus(Enum):
    FREE = 0
    EXECUTING = 1
    READY = 2

@dataclass
class Executor:
    is_connected: bool
    current_task: Optional[Tuple[UUID, DAGRunTask]] = None

    def tick(self):
        if self.current_task is not None:
            if not self.current_task[1].is_finished:
                self.current_task[1].tick()

    @property
    def execution_status(self):
        if self.current_task is None:
            return ExecutionStatus.FREE
        if self.current_task[1].is_finished:
            return ExecutionStatus.READY
        return ExecutionStatus.EXECUTING


class ExecutionManager:
    def __init__(self, count_executors: int):
        self.__active = [self.__create_executor() for i in range(count_executors)]
        self.__inactive = []
        self.__task_queue = []
        self.__ready_tasks = set()

    def __create_executor(self):
        time.sleep(60)
        return Executor(is_connected=True)

    def tick(self):
        to_deactivate_list = []
        for i, executor in enumerate(self.__active):
            executor.tick()
            if executor.execution_status == ExecutionStatus.READY:
                current_uuid, current_task = executor.current_task
                self.__ready_tasks[current_uuid] = current_task
                executor.current_task = None

            if executor.execution_status == ExecutionStatus.FREE:
                if len(self.__task_queue) > 0:
                    executor.current_task = self.__task_queue.pop()
                else:
                    to_deactivate_list.append()

        for idx in to_deactivate_list[::-1]:
            executor = self.__active.pop(idx)
            executor.is_connected = False
            self.__inactive.append(executor)

    def add_task_to_execution_queue(self, uuid: UUID, task: DAGRunTask):
        if len(self.__inactive) > 0:
            executor = self.__inactive.pop()
            executor.is_connected = True
            executor.current_task = task
            self.__active.append(executor)
        else:
            self.__task_queue.append(task)

    def get_task_if_ready(self, task_uuid: UUID) -> Optional[DAGRunTask]:
        if task_uuid in self.__ready_tasks:
            return self.__ready_tasks.pop()
        else:
            return None
