"""ENTITIES
Entities used on the project
"""

# # Native # #
from typing import Optional, List

Strings = List[str]
OptionalString = Optional[str]


class Ideology:
    name: OptionalString
    prefix: OptionalString

    def __init__(self, **kwargs):
        """The ideology must have, at least, one name or one prefix, but can have both.
        :param name: Ideology name
        :param prefix: Ideology prefix
        :raise: AttributeError if no name nor prefix given
        """
        self.name = kwargs.get("name")
        self.prefix = kwargs.get("prefix")
        if not self.name and not self.prefix:
            raise AttributeError("The ideology must have at least one name or one prefix")

    def dict(self):
        d = self.__dict__
        if not self.name:
            d.pop("name")
        if not self.prefix:
            d.pop("prefix")
        return d


Ideologies = List[Ideology]
