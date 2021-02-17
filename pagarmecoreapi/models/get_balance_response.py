# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.get_recipient_response

class GetBalanceResponse(object):

    """Implementation of the 'GetBalanceResponse' model.

    Balance

    Attributes:
        currency (string): Currency
        available_amount (int): Amount available for transferring
        recipient (GetRecipientResponse): Recipient

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency":'currency',
        "available_amount":'available_amount',
        "recipient":'recipient'
    }

    def __init__(self,
                 currency=None,
                 available_amount=None,
                 recipient=None):
        """Constructor for the GetBalanceResponse class"""

        # Initialize members of the class
        self.currency = currency
        self.available_amount = available_amount
        self.recipient = recipient


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
        currency = dictionary.get('currency')
        available_amount = dictionary.get('available_amount')
        recipient = pagarmecoreapi.models.get_recipient_response.GetRecipientResponse.from_dictionary(dictionary.get('recipient')) if dictionary.get('recipient') else None

        # Return an object of this model
        return cls(currency,
                   available_amount,
                   recipient)


