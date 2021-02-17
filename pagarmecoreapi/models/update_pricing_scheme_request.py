# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.update_price_bracket_request

class UpdatePricingSchemeRequest(object):

    """Implementation of the 'UpdatePricingSchemeRequest' model.

    Request for updating a pricing scheme

    Attributes:
        scheme_type (string): Scheme type
        price_brackets (list of UpdatePriceBracketRequest): Price brackets
        price (int): Price
        minimum_price (int): Minimum price
        percentage (float): percentual value used in pricing_scheme Percent

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scheme_type":'scheme_type',
        "price_brackets":'price_brackets',
        "price":'price',
        "minimum_price":'minimum_price',
        "percentage":'percentage'
    }

    def __init__(self,
                 scheme_type=None,
                 price_brackets=None,
                 price=None,
                 minimum_price=None,
                 percentage=None):
        """Constructor for the UpdatePricingSchemeRequest class"""

        # Initialize members of the class
        self.scheme_type = scheme_type
        self.price_brackets = price_brackets
        self.price = price
        self.minimum_price = minimum_price
        self.percentage = percentage


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        scheme_type = dictionary.get('scheme_type')
        price_brackets = None
        if dictionary.get('price_brackets') != None:
            price_brackets = list()
            for structure in dictionary.get('price_brackets'):
                price_brackets.append(pagarmecoreapi.models.update_price_bracket_request.UpdatePriceBracketRequest.from_dictionary(structure))
        price = dictionary.get('price')
        minimum_price = dictionary.get('minimum_price')
        percentage = dictionary.get('percentage')

        # Return an object of this model
        return cls(scheme_type,
                   price_brackets,
                   price,
                   minimum_price,
                   percentage)


