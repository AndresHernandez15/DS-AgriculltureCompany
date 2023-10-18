class Product(object):
    """
    Class used to represent a product.
    """
    def __init__(self, id_product: int = 0, type: str = '', weight: float = 0.0, sellprice: float = 0.0):
        """
        product Constructor Object.

        :param id_product: The unique identifier of the product.
        :type id_product: int
        :param type: The type of the product.
        :type type: str
        :param weight: The weight of the product.
        :type weight: float
        :param sellprice: The sell price of the product.
        :type sellprice: float
        """
        self._id_product = id_product
        self._type = type
        self._weight = weight
        self._sellprice = sellprice

    @property
    def id_product(self) -> int:
        """ Returns the unique identifier of the product.

        :return: The unique identifier of the product.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product: int):
        """ Sets the unique identifier of the product.

        :param id_product: The unique identifier of the product.
        :type id_product: int
        """
        self._id_product = id_product

    @property
    def type(self) -> str:
        """ Returns the type of the product.

        :return: The type of the product.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """ Sets the type of the product.

        :param type: The type of the product.
        :type type: str
        """
        self._type = type

    @property
    def weight(self) -> float:
        """ Returns the weight of the product.

        :return: The weight of the product.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        """ Sets the weight of the product.

        :param weight: The weight of the product.
        :type weight: float
        """
        self._weight = weight

    @property
    def sellprice(self) -> float:
        """ Returns the sell price of the product.

        :return: The sell price of the product.
        :rtype: int
        """
        return self._sellprice

    @sellprice.setter
    def sellprice(self, sellprice: float):
        """ Sets the sell price of the product.

        :param id_silo: The sell price of the product.
        :type id_silo: int
        """
        self._sellprice = sellprice


    def __str__(self):
        """ Returns str of product.
          :returns: string product
          :rtype: str
        """
        return '({0}, {1}, {2}, {3})'.format(self.id_product, self.type, self.weight, self._sellprice)