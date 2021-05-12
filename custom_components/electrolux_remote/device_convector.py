"""Convector class (type=convector24)"""

import logging

from enum import IntEnum

_LOGGER = logging.getLogger(__name__)

TEMP_MIN = 5
TEMP_MAX = 35

class State(IntEnum):
    OFF = 0
    ON = 1


class PowerMode(IntEnum):
    POWER_0 = 0
    POWER_1 = 1
    POWER_2 = 2
    POWER_3 = 3
    POWER_4 = 4
    POWER_5 = 5


class WorkMode(IntEnum):
    COMFORT = 0
    ECO = 1
    NO_FROST = 2
    OFF = 3


class Convector:
    def __init__(self):
        self._state = State.OFF.value
        self._online = State.OFF.value
        self._temp_goal = 24
        self._current_temp = 0
        self._power = PowerMode.POWER_0.value   # мощность обогрева
        self._mode = WorkMode.COMFORT.value             # режим работы
        # таймер
        self._hours = 0
        self._minutes = 0
        self._timer = State.OFF.value

        self._tempid = None
        self._mac = None
        self._room = None   # название помещения
        self._lock = State.OFF.value    # режим блокировки

    def from_json(self, data: dict):
        """Fill self from json data"""
        for key in data:
            setattr(self, f"_{key}", data[key])

    @property
    def current_temp(self) -> float:
        return float(self._current_temp)

    @property
    def mode(self) -> WorkMode:
        return WorkMode(int(self._mode))

    @property
    def temp_goal(self) -> float:
        return float(self._temp_goal)

    @property
    def power(self) -> int:
        return int(self._power)

    @property
    def lock(self) -> bool:
        return int(self._lock) == State.ON.value

    @property
    def room(self) -> str:
        return self._room

    @property
    def state(self) -> bool:
        return int(self._state) == State.ON.value

    @property
    def online(self) -> bool:
        return int(self._online) == State.ON.value

    @property
    def delta_eco(self) -> int:
        return 4

    @property
    def hours(self) -> int:
        return int(self._hours)

    @property
    def minutes(self) -> int:
        return int(self._minutes)

    @property
    def timer(self) -> int:
        return int(self._timer)