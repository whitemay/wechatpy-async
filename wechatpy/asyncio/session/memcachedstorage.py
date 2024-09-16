# -*- coding: utf-8 -*-
import json

from aiowe.session import SessionStorage
from aiowe.utils import to_text


class MemcachedStorage(SessionStorage):
    def __init__(self, mc, prefix="wechatpy"):
        super().__init__()  # 调用父类的初始化方法
        for method_name in ("get", "set", "delete"):
            assert hasattr(mc, method_name)
        self.mc = mc
        self.prefix = prefix

    def key_name(self, key):
        return f"{self.prefix}:{key}"

    def get(self, key, default=None):
        key = self.key_name(key)
        value = self.mc.get(key)  # 使用异步获取
        if value is None:
            return default
        return json.loads(to_text(value))

    def set(self, key, value, ttl=0):
        if value is None:
            return
        key = self.key_name(key)
        value = json.dumps(value)
        self.mc.set(key, value, ttl)  # 使用异步设置

    def delete(self, key):
        key = self.key_name(key)
        self.mc.delete(key)  # 使用异步删除
