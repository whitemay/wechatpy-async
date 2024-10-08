# -*- coding: utf-8 -*-

from wechatpy.asyncio.client.api.base import BaseWeChatAPI


class MerchantStock(BaseWeChatAPI):

    API_BASE_URL = "https://api.weixin.qq.com/"

    async def add(self, product_id, quantity, sku_info=""):
        return await self._post(
            "merchant/stock/add",
            data={"product_id": product_id, "quantity": quantity, "sku_info": sku_info},
        )

    async def reduce(self, product_id, quantity, sku_info=""):
        return await self._post(
            "merchant/stock/reduce",
            data={"product_id": product_id, "quantity": quantity, "sku_info": sku_info},
        )
