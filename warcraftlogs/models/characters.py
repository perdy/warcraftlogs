from warcraftlogs.models.base import BaseMeta

__all__ = ["Class", "Spec"]


class Gear(metaclass=BaseMeta):
    pk = ("id", "name")
    id = "id"
    name = "name"
    quality = "quality"


class Talent(metaclass=BaseMeta):
    pk = ("id", "name")
    id = "id"
    name = "name"


class Spec(metaclass=BaseMeta):
    pk = ("id", "name")
    id = "id"
    name = "name"


class Class(metaclass=BaseMeta):
    pk = ("id", "name")
    id = "id"
    name = "name"
    specs = "specs"

    @classmethod
    def _get_specs_from_dict(cls, data, default=None):
        return {
            s.id: s
            for s in [Spec.from_dict(i) for i in data.get(cls.attributes["specs"], [])]
        }


class Character(metaclass=BaseMeta):
    pk = ("name", "server", "region")
    name = "name"
    server = "server"
    region = "region"
    klass = "class"
    spec = "spec"
    talents = "talents"
    ilvl = "itemLevel"
    gear = "gear"
    guild = "guild"

    @classmethod
    def _get_talents_from_dict(cls, data, default=None):
        return {
            t.id: t
            for t in [
                Talent.from_dict(i) for i in data.get(cls.attributes["talents"], [])
            ]
        }

    @classmethod
    def _get_gear_from_dict(cls, data, default=None):
        return {
            g.id: g
            for g in [Gear.from_dict(i) for i in data.get(cls.attributes["gear"], [])]
        }
