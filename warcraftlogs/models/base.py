class BaseMeta(type):
    def __new__(mcs, name, parents, dct):
        # Gather attributes from class
        attributes = {
            k: v for k, v in dct.items() if not k.startswith("_") and k != "pk"
        }
        dct["attributes"] = attributes

        # Remove attributes from class
        for k in attributes.keys():
            del dct[k]

        # Create some magic methods
        if "__str__" not in dct:
            dct["__str__"] = lambda self: getattr(self, self.pk)
        if "__repr__" not in dct:

            def repr_by_pk(self):
                if isinstance(self.pk, (list, tuple)):
                    attr_repr = ", ".join(["{}"] * len(self.pk)).format(
                        *[getattr(self, i) for i in self.pk]
                    )
                else:
                    attr_repr = str(self.pk)
                return "{}{{{}}}".format(name, attr_repr)

            dct["__repr__"] = repr_by_pk
        if "__hash__" not in dct:
            dct["__hash__"] = lambda self: hash(
                tuple([getattr(self, i) for i in self.pk])
            )
        if "__eq__" not in dct:
            dct["__eq__"] = lambda self, other: isinstance(
                other, self.__class__
            ) and hash(self) == hash(other)

        # Init method to set all attributes from kwargs
        def init_attr(self, **kwargs):
            for k in self.attributes.keys():
                setattr(self, k, kwargs.get(k, None))

        dct["__init__"] = init_attr

        # Create getters for attributes
        for k in attributes.keys():
            getter_name = "_get_{}_from_dict".format(k)
            if getter_name not in dct:
                dct[getter_name] = (
                    lambda k: classmethod(
                        lambda cls, data, default=None: data.get(
                            cls.attributes[k], default.get(k, None)
                        )
                    )
                )(k)

        # Method to create instances from dict data
        def from_dict(cls, data, **default):
            model_data = {
                k: getattr(cls, "_get_{}_from_dict".format(k))(data, default)
                for k in cls.attributes.keys()
            }
            return cls(**model_data)

        dct["from_dict"] = classmethod(from_dict)

        return type(name, parents, dct)
