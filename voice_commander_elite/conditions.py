from typing import Any, Self

from voice_commander.conditions import ConditionBase, AHKWindowIsActive

class EliteDangerousIsActive(AHKWindowIsActive):
    def __init__(self, **kwargs):
        simplified_serialization = kwargs.pop('_simplified_serialization', False)
        self._simplified_serialization = simplified_serialization
        super().__init__(title='Elite - Dangerous (CLIENT)', **kwargs)

    def to_dict(self) -> dict[str, Any]:
        d = super().to_dict()
        if self._simplified_serialization:
            d['condition_type'] = AHKWindowIsActive.fqn()
        else:
            d['condition_config'] = {}
        return d

    @classmethod
    def with_simplified_serialization(cls, **kwargs) -> Self:
        return cls(_simplified_serialization=True, **kwargs)

    wss = with_simplified_serialization
