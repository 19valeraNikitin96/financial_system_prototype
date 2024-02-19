from dataclasses import dataclass

from typing import List


@dataclass
class ATMJSON:
    is_working: bool
    cash: int


@dataclass
class WorkSchedule:
    opens_at: int
    closes_at: int


@dataclass
class BankDepartmentJSON:
    address: str
    work_schedule: WorkSchedule
    atms_ids: List[str]

    def __post_init__(self):
        self.work_schedule = WorkSchedule(**self.work_schedule)

