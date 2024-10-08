# -*- coding: utf-8 -*-

from wechatpy.asyncio.client.api.base import BaseWeChatAPI


class MerchantCategory(BaseWeChatAPI):

    API_BASE_URL = "https://api.weixin.qq.com/"

    async def get_sub_categories(self, cate_id):
        res = await self._post(
            "merchant/category/getsub",
            data={"cate_id": cate_id},
            result_processor=lambda x: x["cate_list"],
        )
        return res

    async def get_sku_list(self, cate_id):
        res = await self._post(
            "merchant/category/getsku",
            data={"cate_id": cate_id},
            result_processor=lambda x: x["sku_table"],
        )
        return res

    async def get_properties(self, cate_id):
        res = await self._post(
            "merchant/category/getproperty",
            data={"cate_id": cate_id},
            result_processor=lambda x: x["properties"],
        )
        return res
