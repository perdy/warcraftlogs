from warcraftlogs.models.base import BaseMeta
from warcraftlogs.models.characters import Character


class Fight(metaclass=BaseMeta):
    pk = ("id", "encounter", "duration")
    id = "fightID"
    encounter = "encounter"
    character = "character"
    duration = "duration"
    size = "size"
    total = "total"

    @classmethod
    def _get_character_from_dict(cls, data, default=None):
        if default is None:
            default = {}
        return Character.from_dict(data, **default)
