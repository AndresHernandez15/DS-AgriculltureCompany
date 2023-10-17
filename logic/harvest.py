from datetime import datetime


class Harvest(object):
    """
    Class used to represent a harvest.
    """

    def __init__(self, id_harvest: int = 0, type: str = 'type', date: datetime = datetime(1900, 1, 1), weight: float = 0):
        """
        harvest Constructor Object.

        :param id_harvest: The unique identifier of the harvest.
        :type id_harvest: int
        :param type: The type of the harvest.
        :type type: str
        :param date: The date of the harvest.
        :type date: datetime
        :param weight: The weight of the harvest.
        :type weight: float
        """
        self._id_harvest = id_harvest
        self._type = type
        self._date = date
        self._weight = weight

    @property
    def id_harvest(self) -> int:
        """ Returns the unique identifier of the harvest.

        :return: The unique identifier of the harvest.
        :rtype: int
        """
        return self._id_harvest

    @id_harvest.setter
    def id_harvest(self, id_harvest: int):
        """ Sets the unique identifier of the harvest.

        :param id_harvest: The unique identifier of the harvest.
        :type id_harvest: int
        """
        self._id_harvest = id_harvest

    @property
    def type(self) -> str:
        """ Returns the type of the harvest.

        :return: The type of the harvest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """ Sets the type of the harvest.

        :param type: The type of the harvest.
        :type type: str
        """
        self._type = type

    @property
    def date(self) -> datetime:
        """ Returns the date of the harvest.

        :return: The date of the harvest.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date: datetime):
        """ Sets the date of the harvest.

        :param date: The date of the harvest.
        :type date: datetime
        """
        self._date = date

    @property
    def weight(self) -> float:
        """ Returns the weight of the harvest.

        :return: The weight of the harvest.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        """ Sets the weight of the harvest.

        :param weight: The weight of the harvest.
        :type weight: int
        """
        self._weight = weight

    def __str__(self):
        """ Returns str of crop.
          :returns: sting crop
          :rtype: str
        """
        return '({0}, {1}, {2}, {3})'.format(self.id_harvest, self.type, self.date, self.weight)
