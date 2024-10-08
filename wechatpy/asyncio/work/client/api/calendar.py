# -*- coding: utf-8 -*-


import operator as op

from wechatpy.asyncio.client.api.base import BaseWeChatAPI


class WeChatCalendar(BaseWeChatAPI):
    """
    https://developer.work.weixin.qq.com/document/path/93624
    """

    async def add(self, organizer, summary, color, description="", shares=()):
        """
        创建日历

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93647

        :param organizer: 指定的组织者userid。注意该字段指定后不可更新
        :param summary: 日历标题。1 ~ 128 字符
        :param color: 日历在终端上显示的颜色，RGB颜色编码16进制表示，例如：”#0000FF” 表示纯蓝色
        :param description: 日历描述。0 ~ 512 字符
        :param shares: 日历共享成员列表。最多2000人
        :type shares: list[str]

        :return: 日历ID
        :rtype: str
        """
        data = {
            "calendar": {
                "organizer": organizer,
                "summary": summary,
                "color": color,
                "description": description,
                "shares": [{"userid": userid} for userid in shares],
            }
        }
        return await self._post("oa/calendar/add", data=data, result_processor=op.itemgetter("cal_id"))

    async def update(self, calendar_id, summary, color, description="", shares=()):
        """
        更新日历

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93647

        :param calendar_id: 日历ID
        :param summary: 日历标题。1 ~ 128 字符
        :param color: 日历在终端上显示的颜色，RGB颜色编码16进制表示，例如：”#0000FF” 表示纯蓝色
        :param description: 日历描述。0 ~ 512 字符
        :param shares: 日历共享成员列表。最多2000人
        :type shares: list[str]
        """
        data = {
            "calendar": {
                "cal_id": calendar_id,
                "summary": summary,
                "color": color,
                "description": description,
                "shares": [{"userid": userid} for userid in shares],
            }
        }
        return await self._post("oa/calendar/update", data=data, result_processor=op.itemgetter("cal_id"))

    async def get(self, calendar_ids):
        """
        获取日历

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93647

        :param calendar_ids: 日历ID列表。一次最多可获取1000条
        :type calendar_ids: list[str]

        :return: 日历列表
        :rtype: list[dict]
        """
        return await self._post(
            "oa/calendar/get",
            data={"cal_id_list": calendar_ids},
            result_processor=op.itemgetter("calendar_list"),
        )

    async def delete(self, calendar_id):
        """
        删除日历

        详情请参考
        https://developer.work.weixin.qq.com/document/path/93647

        :param calendar_id: 日历ID
        """
        return await self._post("oa/calendar/del", data={"cal_id": calendar_id})
