class DamagedMaintenanceDroid:
    def __init__(self):
        self.blocking = True  # The droid starts as an obstacle

    def repair(self):
        """Simulates using the diagnostic tool to repair the droid."""
        self.blocking = False

    def is_blocking(self):
        """Returns whether the droid is still active and blocking the path."""
        return self.blocking
