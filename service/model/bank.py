from dataclasses import dataclass

from typing import List

from service.model import DocumentBase


@dataclass
class WorkSchedule:
    opens_at: int
    closes_at: int

    def __str__(self):
        return f"From {self.opens_at} to {self.closes_at}"

    def __repr__(self):
        return self.__str__()


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
    atms: List[ATM]

    @property
    def doc(self) -> dict:
        res = super().doc

        res['work_schedule'] = str(res['work_schedule'])
        res['atms'] = [atm.doc for atm in res['atms']]

        return res

    def __post_init__(self):
        self.work_schedule = WorkSchedule(**self.work_schedule)
        self.atms = [ATM(**entry) for entry in self.atms]
