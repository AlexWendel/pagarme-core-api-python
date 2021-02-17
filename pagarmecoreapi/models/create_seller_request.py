# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import pagarmecoreapi.models.create_address_request

class CreateSellerRequest(object):

    """Implementation of the 'CreateSellerRequest' model.

    TODO: type model description here.

    Attributes:
        name (string): Name
        code (string): Seller's code identification
        description (string): Description
        document (string): Document number (individual / company)
        address (CreateAddressRequest): Address
        mtype (string): Person type (individual / company)
        metadata (dict<object, string>): Metadata

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "metadata":'metadata',
        "code":'code',
        "description":'description',
        "document":'document',
        "address":'address',
        "mtype":'type'
    }

    def __init__(self,
                 name=None,
                 metadata=None,
                 code=None,
                 description=None,
                 document=None,
                 address=None,
                 mtype=None):
        """Constructor for the CreateSellerRequest class"""

        # Initialize members of the class
        self.name = name
        self.code = code
        self.description = description
        self.document = document
        self.address = address
        self.mtype = mtype
        self.metadata = metadata


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
        name = dictionary.get('name')
        metadata = dictionary.get('metadata')
        code = dictionary.get('code')
        description = dictionary.get('description')
        document = dictionary.get('document')
        address = pagarmecoreapi.models.create_address_request.CreateAddressRequest.from_dictionary(dictionary.get('address')) if dictionary.get('address') else None
        mtype = dictionary.get('type')

        # Return an object of this model
        return cls(name,
                   metadata,
                   code,
                   description,
                   document,
                   address,
                   mtype)


