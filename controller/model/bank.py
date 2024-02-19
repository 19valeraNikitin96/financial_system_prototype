from dataclasses import dataclass

from typing import List

from service.model import DocumentBase


@dataclass
class WorkSchedule:
    opens_at: int
    closes_at: int


@dataclass
class ATM(DocumentBase):
    _id: str
    is_working: bool
    cash: int


@dataclass
class BankDepartment(DocumentBase):
    _id: str
    address: str
    work_schedule: WorkSchedule
    atms: List[str]

    @property
    def doc(self) -> dict:
        res = super().doc

        res['work_schedule'] = str(res['work_schedule'])

        return res

    def __post_init__(self):
        self.work_schedule = WorkSchedule(**self.work_schedule)
