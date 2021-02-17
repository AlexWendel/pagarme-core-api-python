# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateSplitOptionsRequest(object):

    """Implementation of the 'CreateSplitOptionsRequest' model.

    The Split Options Request

    Attributes:
        liable (bool): Liable options
        charge_processing_fee (bool): Charge processing fee
        charge_remainder_fee (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "liable":'liable',
        "charge_processing_fee":'charge_processing_fee',
        "charge_remainder_fee":'charge_remainder_fee'
    }

    def __init__(self,
                 liable=None,
                 charge_processing_fee=None,
                 charge_remainder_fee=None):
        """Constructor for the CreateSplitOptionsRequest class"""

        # Initialize members of the class
        self.liable = liable
        self.charge_processing_fee = charge_processing_fee
        self.charge_remainder_fee = charge_remainder_fee


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
        liable = dictionary.get('liable')
        charge_processing_fee = dictionary.get('charge_processing_fee')
        charge_remainder_fee = dictionary.get('charge_remainder_fee')

        # Return an object of this model
        return cls(liable,
                   charge_processing_fee,
                   charge_remainder_fee)


