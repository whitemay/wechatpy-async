# -*- coding: utf-8 -*-
import logging

from aiowe.client import WeChatClient  # NOQA
from aiowe.component import ComponentOAuth, WeChatComponent  # NOQA
from aiowe.exceptions import (
    WeChatClientException,
    WeChatException,
    WeChatOAuthException,
    WeChatPayException,
)  # NOQA
from aiowe.oauth import WeChatOAuth  # NOQA
from aiowe.parser import parse_message  # NOQA
from aiowe.pay import WeChatPay  # NOQA
from aiowe.replies import create_reply  # NOQA

__version__ = "0.0.1"
__author__ = "aston"

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
