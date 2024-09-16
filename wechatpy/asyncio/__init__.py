# -*- coding: utf-8 -*-
import logging

from wechatpy.asyncio.client import WeChatClient  # NOQA
from wechatpy.asyncio.component import ComponentOAuth, WeChatComponent  # NOQA
from wechatpy.asyncio.exceptions import (
    WeChatClientException,
    WeChatException,
    WeChatOAuthException,
    WeChatPayException,
)  # NOQA
from wechatpy.asyncio.oauth import WeChatOAuth  # NOQA
from wechatpy.asyncio.parser import parse_message  # NOQA
from wechatpy.asyncio.pay import WeChatPay  # NOQA
from wechatpy.asyncio.replies import create_reply  # NOQA

__version__ = "0.0.1"
__author__ = "aston"

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
