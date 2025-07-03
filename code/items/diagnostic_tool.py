from .station_item import StationItem

class DiagnosticTool(StationItem):
    def __init__(self):
        super().__init__(
            name="Diagnostic Tool",
            description="This diagnostic tool seems designed to interface with maintenance droids."
        )
