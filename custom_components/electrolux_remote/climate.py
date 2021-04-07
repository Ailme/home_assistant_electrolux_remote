"""
Adds Support for Electrolux Convector

Configuration for this platform:

logger:
  default: info
  logs:
    custom_components.electrolux_remote: debug

climate:
  - platform: electrolux_remote
    name: Electrolux Convector
    username: phone
    password: 123456
"""

import logging

from .convector2_to_climate import Convector2Climate
from .thermostat_to_climate import Thermostat2Climate

from .api import RusclimatApi, TestApi

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.aiohttp_client import async_create_clientsession

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_devices):
    """
    Setup the climate platform
    """
    _LOGGER.debug("climate.async_setup_entry")

    data = config_entry.options if config_entry.options != {} else config_entry.data
    devices = []

    try:
        session = async_create_clientsession(hass)
        api = RusclimatApi(
            data["host"],
            data["username"],
            data["password"],
            data["appcode"],
            session
        )
        json = await api.login()

        for deviceData in json["result"]["device"]:
            _LOGGER.debug(f"device: {deviceData}")

            if deviceData["type"] == Convector2Climate.device_type():
                device = Convector2Climate(deviceData["uid"], api, deviceData)
                devices.append(device)

            if deviceData["type"] == Thermostat2Climate.device_type():
                device = Thermostat2Climate(deviceData["uid"], api, deviceData)
                devices.append(device)
    except Exception as err:
        _LOGGER.error(err)

    async_add_devices(devices)
