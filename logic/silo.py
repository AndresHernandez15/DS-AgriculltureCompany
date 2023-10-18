class Silo(object):
    """
    Class used to represent a silo.
    """
    def __init__(self, id_silo: int = 0, capacity: int = 0):
        """
        silo Constructor Object.

        :param id_silo: The unique identifier of the silo.
        :type id_silo: int
        :param capacity: The capacity of the silo.
        :type capacity: int
        """
        self._id_silo = id_silo
        self._capacity = capacity
        self._products = []

    @property
    def id_silo(self) -> int:
        """ Returns the unique identifier of the silo.

        :return: The unique identifier of the silo.
        :rtype: int
        """
        return self._id_silo

    @id_silo.setter
    def id_silo(self, id_silo: int):
        """ Sets the unique identifier of the silo.

        :param id_silo: The unique identifier of the silo.
        :type id_silo: int
        """
        self._id_silo = id_silo

    @property
    def capacity(self) -> int:
        """ Returns the capacity of the silo.

        :return: The capacity of the silo.
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int):
        """ Sets the capacity of the silo.

        :param capacity: The capacity of the silo.
        :type capacity: int
        """
        self._capacity = capacity

    @property
    def products(self) -> list:
        """ Returns the list of products in the silo.

        :return: The list of products in the silo.
        :rtype: list
        """
        return self._products

    @products.setter
    def products(self, products: list):
        """ Sets the list of products in the silo.

        :param products: The list of products in the silo.
        :type products: list
        """
        self._products = products

    def __str__(self):
        """ Returns str of silo.
          :returns: string silo
          :rtype: str
        """
        return '({0}, {1}, {2})'.format(self.id_silo, self.capacity, self.products)
