# -*- coding: utf-8 -*-


import xmltodict

from aiowe.work.events import EVENT_TYPES
from aiowe.work.messages import MESSAGE_TYPES
from aiowe.messages import UnknownMessage
from aiowe.utils import to_text


def parse_message(xml):
    if not xml:
        return
    message = xmltodict.parse(to_text(xml))["xml"]
    message_type = message["MsgType"].lower()
    if message_type == "event":
        event_type = message["Event"].lower()
        message_class = EVENT_TYPES.get(event_type, UnknownMessage)
    else:
        message_class = MESSAGE_TYPES.get(message_type, UnknownMessage)
    return message_class(message)
