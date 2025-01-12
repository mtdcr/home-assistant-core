"""Demo platform that has two fake binary sensors."""
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.helpers.entity import DeviceInfo

from . import DOMAIN


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the Demo binary sensor platform."""
    async_add_entities(
        [
            DemoBinarySensor(
                "binary_1",
                "Basement Floor Wet",
                False,
                BinarySensorDeviceClass.MOISTURE,
            ),
            DemoBinarySensor(
                "binary_2", "Movement Backyard", True, BinarySensorDeviceClass.MOTION
            ),
        ]
    )


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Demo config entry."""
    await async_setup_platform(hass, {}, async_add_entities)


class DemoBinarySensor(BinarySensorEntity):
    """representation of a Demo binary sensor."""

    def __init__(
        self,
        unique_id: str,
        name: str,
        state: bool,
        device_class: BinarySensorDeviceClass,
    ) -> None:
        """Initialize the demo sensor."""
        self._unique_id = unique_id
        self._name = name
        self._state = state
        self._sensor_type = device_class

    @property
    def device_info(self) -> DeviceInfo:
        """Return device info."""
        return DeviceInfo(
            identifiers={
                # Serial numbers are unique identifiers within a specific domain
                (DOMAIN, self.unique_id)
            },
            name=self.name,
        )

    @property
    def unique_id(self):
        """Return the unique id."""
        return self._unique_id

    @property
    def device_class(self) -> BinarySensorDeviceClass:
        """Return the class of this sensor."""
        return self._sensor_type

    @property
    def should_poll(self):
        """No polling needed for a demo binary sensor."""
        return False

    @property
    def name(self):
        """Return the name of the binary sensor."""
        return self._name

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return self._state
