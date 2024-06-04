from voice_commander.conditions import ConditionBase, AHKWindowIsActive

class EliteDangerousIsActive(AHKWindowIsActive):
    def __init__(self):
        super().__init__(title='Elite - Dangerous (CLIENT)')
