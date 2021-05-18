"""Centurio IQ class (type=centurio)"""

import logging

from .base import SwitchDevice
from ..enums import State
from ..devices.centurio import Centurio
from ..update_coordinator import Coordinator
from ..const import DEVICE_CENTURIO

_LOGGER = logging.getLogger(__name__)


class CenturioSwitches:
    def __init__(self, uid: str, coordinator: Coordinator):
        """
        Initialize
        """

        device = Centurio()

        self.switches = [
            SwitchDevice(
                uid=uid,
                coordinator=coordinator,
                name=f"Self Clean",
                icon_on="",
                icon_off="",
                device=device,
                param_name="self_clean",
                property_name="self_clean",
                value_on=State.ON.value,
                value_off=State.OFF.value
            ),

            SwitchDevice(
                uid=uid,
                coordinator=coordinator,
                name=f"Timer",
                icon_on="mdi:timer",
                icon_off="mdi:timer",
                device=device,
                param_name="timer",
                property_name="timer",
                value_on=State.ON.value,
                value_off=State.OFF.value
            )
        ]

    @staticmethod
    def device_type() -> str:
        return DEVICE_CENTURIO

    def get_sensors(self):
        return self.switches