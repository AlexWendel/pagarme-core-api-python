# -*- coding: utf-8 -*-

"""
    pagarmecoreapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from pagarmecoreapi.decorators import lazy_property
from pagarmecoreapi.configuration import Configuration
from pagarmecoreapi.controllers.plans_controller import PlansController
from pagarmecoreapi.controllers.subscriptions_controller import SubscriptionsController
from pagarmecoreapi.controllers.orders_controller import OrdersController
from pagarmecoreapi.controllers.invoices_controller import InvoicesController
from pagarmecoreapi.controllers.customers_controller import CustomersController
from pagarmecoreapi.controllers.charges_controller import ChargesController
from pagarmecoreapi.controllers.transfers_controller import TransfersController
from pagarmecoreapi.controllers.recipients_controller import RecipientsController
from pagarmecoreapi.controllers.tokens_controller import TokensController
from pagarmecoreapi.controllers.transactions_controller import TransactionsController


class PagarmecoreapiClient(object):

    config = Configuration

    @lazy_property
    def plans(self):
        return PlansController()

    @lazy_property
    def subscriptions(self):
        return SubscriptionsController()

    @lazy_property
    def orders(self):
        return OrdersController()

    @lazy_property
    def invoices(self):
        return InvoicesController()

    @lazy_property
    def customers(self):
        return CustomersController()

    @lazy_property
    def charges(self):
        return ChargesController()

    @lazy_property
    def transfers(self):
        return TransfersController()

    @lazy_property
    def recipients(self):
        return RecipientsController()

    @lazy_property
    def tokens(self):
        return TokensController()

    @lazy_property
    def transactions(self):
        return TransactionsController()


    def __init__(self,
                 basic_auth_user_name=None,
                 basic_auth_password=None):
        if basic_auth_user_name is not None:
            Configuration.basic_auth_user_name = basic_auth_user_name
        if basic_auth_password is not None:
            Configuration.basic_auth_password = basic_auth_password

