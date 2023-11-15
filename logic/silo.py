from logic.product import Product


class Silo(object):
    _silo_id_counter = 0
    """
    Class used to represent a silo.
    """
    def __init__(self, capacity: int = 0):
        """
        silo Constructor Object.

        :param capacity: The capacity of the silo.
        :type capacity: int
        """
        Silo._silo_id_counter += 1
        self._id_silo = Silo._silo_id_counter
        self._capacity = capacity
        self._products = []
    @property
    def id_silo(self) -> int:
        """ Returns the unique identifier of the silo.

        :return: The unique identifier of the silo.
        :rtype: int
        """
        return self._id_silo

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
    def products(self, product: Product):
        """ Adds a product to the list.

        :param product: The list of products in the silo.
        :type product: list
        """
        self._products.append(product)

    def __str__(self):
        """ Returns str of silo.
          :returns: string silo
          :rtype: str
        """
        return '({0}, {1}, {2})'.format(self.id_silo, self.capacity, self.products)
