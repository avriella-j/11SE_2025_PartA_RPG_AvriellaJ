from .station_item import StationItem

class EnergyCrystal(StationItem):
    def __init__(self):
        super().__init__(
            name="Energy Crystal",
            description="The crystal pulses with an unstable, vibrant energy."
        )
