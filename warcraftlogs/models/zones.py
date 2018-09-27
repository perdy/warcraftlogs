from warcraftlogs.models.base import BaseMeta

__all__ = ["Encounter", "Zone"]


class Encounter(metaclass=BaseMeta):
    pk = ("id", "name")
    id = "id"
    name = "name"


class Bracket(metaclass=BaseMeta):
    pk = ('type',)
    type = 'type'
    min = 'min'
    max = 'max'
    bucket = 'bucket'


class Zone(metaclass=BaseMeta):
    pk = ("id", "name")
    id = "id"
    name = "name"
    encounters = "encounters"
    brackets = "brackets"

    @classmethod
    def _get_encounters_from_dict(cls, data, default=None):
        return {
            e.id: e
            for e in [
                Encounter.from_dict(i)
                for i in data.get(cls.attributes["encounters"], [])
            ]
        }

    @classmethod
    def _get_brackets_from_dict(cls, data, default=None):
        bracket = data.get(cls.attributes['brackets'],[])
        if not isinstance(bracket, list):
            bracket = [bracket]
        return {b.type: b for b in [Bracket.from_dict(i) for i in bracket]}