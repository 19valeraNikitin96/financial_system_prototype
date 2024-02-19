from dataclasses import dataclass

from typing import List


@dataclass
class WorkSchedule:
    opens_at: int
    closes_at: int


@dataclass
class ATM:
    _id: str
    is_working: bool
    cash: int


@dataclass
class BankDepartment:
    _id: str
    address: str
    work_schedule: WorkSchedule
    atms: List[ATM]
