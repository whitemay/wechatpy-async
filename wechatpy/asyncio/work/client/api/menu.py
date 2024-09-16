# -*- coding: utf-8 -*-


from wechatpy.asyncio.client.api.base import BaseWeChatAPI


class WeChatMenu(BaseWeChatAPI):
    """
    自定义菜单
    """

    async def create(self, agent_id: int, menu_data: dict) -> dict:
        """
        创建菜单

        详情请参考：
        https://developer.work.weixin.qq.com/document/path/90231

        :param agent_id: 应用id
        """
        return await self._post("menu/create", params={"agentid": agent_id}, data=menu_data)

    async def get(self, agent_id: int) -> dict:
        """
        获取菜单

        详情请参考：
        https://developer.work.weixin.qq.com/document/path/90232

        :param agent_id: 应用id
        """
        return await self._get("menu/get", params={"agentid": agent_id})

    async def delete(self, agent_id: int) -> dict:
        """
        删除菜单

        详情请参考：
        https://developer.work.weixin.qq.com/document/path/90233

        :param agent_id: 应用id
        """
        return await self._get("menu/delete", params={"agentid": agent_id})

    async def update(self, agent_id: int, menu_data: dict) -> dict:
        await self.delete(agent_id)
        return await self.create(agent_id, menu_data)
