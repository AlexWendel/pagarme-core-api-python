# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.create_seller_request

class CreateOrderItemRequest(object):

    """Implementation of the 'CreateOrderItemRequest' model.

    Request for creating an order item

    Attributes:
        amount (int): Amount
        description (string): Description
        quantity (int): Quantity
        seller (CreateSellerRequest): Item seller
        seller_id (string): seller identificator
        category (string): Category
        code (string): The item code passed by the client

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount":'amount',
        "description":'description',
        "quantity":'quantity',
        "category":'category',
        "seller":'seller',
        "seller_id":'seller_id',
        "code":'code'
    }

    def __init__(self,
                 amount=None,
                 description=None,
                 quantity=None,
                 category=None,
                 seller=None,
                 seller_id=None,
                 code=None):
        """Constructor for the CreateOrderItemRequest class"""

        # Initialize members of the class
        self.amount = amount
        self.description = description
        self.quantity = quantity
        self.seller = seller
        self.seller_id = seller_id
        self.category = category
        self.code = code


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
        amount = dictionary.get('amount')
        description = dictionary.get('description')
        quantity = dictionary.get('quantity')
        category = dictionary.get('category')
        seller = pagarmecoreapi.models.create_seller_request.CreateSellerRequest.from_dictionary(dictionary.get('seller')) if dictionary.get('seller') else None
        seller_id = dictionary.get('seller_id')
        code = dictionary.get('code')

        # Return an object of this model
        return cls(amount,
                   description,
                   quantity,
                   category,
                   seller,
                   seller_id,
                   code)


