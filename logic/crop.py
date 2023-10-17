from datetime import datetime


class Crop(object):
    """
    Class used to represent a Crop.
    """

    def __init__(self, id_crop: int = 0, type: str = 'type', area: float = 0.0, price: float = 0.0,
                 date: datetime = datetime(1900, 1, 1), amount: int = 0):
        """
        Crop Constructor Object.

        :param id_crop: The unique identifier of the crop.
        :type id_crop: int
        :param type: The type of the crop.
        :type type: str
        :param area: The area of the crop in square units.
        :type area: float
        :param price: The price of the crop per unit area.
        :type price: float
        :param date: The date when the crop was planted.
        :type date: datetime
        :param amount: The total amount of this crop.
        :type amount: int
        """
        self._id_crop = id_crop
        self._type = type
        self._area = area
        self._price = price
        self._date = date
        self._amount = amount

    @property
    def id_crop(self) -> int:
        """ Returns the unique identifier of the crop.

        :return: The unique identifier of the crop.
        :rtype: int
        """
        return self._id_crop

    @id_crop.setter
    def id_crop(self, id_crop: int):
        """ Sets the unique identifier of the crop.

        :param id_crop: The unique identifier of the crop.
        :type id_crop: int
        """
        self._id_crop = id_crop

    @property
    def type(self) -> str:
        """ Returns the type of the crop.

        :return: The type of the crop.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """ Sets the type of the crop.

        :param type: The type of the crop.
        :type type: str
        """
        self._type = type

    @property
    def area(self) -> float:
        """ Returns the area of the crop in square units.

        :return: The area of the crop.
        :rtype: float
        """
        return self._area

    @area.setter
    def area(self, area: float):
        """ Sets the area of the crop in square units.

        :param area: The area of the crop.
        :type area: float
        """
        self._area = area

    @property
    def price(self) -> float:
        """ Returns the price of the crop per unit area.

        :return: The price of the crop.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price: float):
        """ Sets the price of the crop per unit area.

        :param price: The price of the crop.
        :type price: float
        """
        self._price = price

    @property
    def date(self) -> datetime:
        """ Returns the date when the crop was planted.

        :return: The date when the crop was planted.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date: datetime):
        """ Sets the date when the crop was planted.

        :param date: The date when the crop was planted.
        :type date: datetime
        """
        self._date = date

    @property
    def amount(self) -> int:
        """ Returns the total amount of this crop.

        :return: The total amount of this crop.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """ Sets the total amount of this crop.

        :param amount: The total amount of this crop.
        :type amount: int
        """
        self._amount = amount

    def __str__(self):
        """ Returns str of crop.
          :returns: sting crop
          :rtype: str
        """
        return '({0}, {1}, {2}, {3}, {4}, {5})'.format(self.id_crop, self.type, self.area, self.price, self.date,
                                                       self.amount)
