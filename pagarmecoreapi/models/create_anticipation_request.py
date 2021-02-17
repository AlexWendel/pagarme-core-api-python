# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.api_helper import APIHelper

class CreateAnticipationRequest(object):

    """Implementation of the 'CreateAnticipationRequest' model.

    Request for creating an anticipation

    Attributes:
        amount (int): Amount requested for the anticipation
        timeframe (string): Timeframe
        payment_date (datetime): Payment date

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount":'amount',
        "timeframe":'timeframe',
        "payment_date":'payment_date'
    }

    def __init__(self,
                 amount=None,
                 timeframe=None,
                 payment_date=None):
        """Constructor for the CreateAnticipationRequest class"""

        # Initialize members of the class
        self.amount = amount
        self.timeframe = timeframe
        self.payment_date = APIHelper.RFC3339DateTime(payment_date) if payment_date else None


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
        timeframe = dictionary.get('timeframe')
        payment_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("payment_date")).datetime if dictionary.get("payment_date") else None

        # Return an object of this model
        return cls(amount,
                   timeframe,
                   payment_date)


