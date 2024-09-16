# 特别说明

本项目是在原wechatpy的基础之上发展而来。
由于项目需要，我完整将wechatpy改写成了支持asyncio的版本。特此将项目代码共享于此。

本项目的改动说明如下：
- 尊重原始项目，同步部分实现依然保留。全部异步实现在asyncio子模块下。
- 用httpx代替了原有的requests库，从而实现网络请求的异步化。
- 去掉所有可能涉及异步操作的property定义，改为异步函数调用。
- 原session类及实现保留不变。该部分同步还是异步，对性能的影响应该不大。

相关代码我在项目中已经使用，暂时没有发现新的问题。。
本人没有太多空余时间对项目做进一步的维护，以及发布到pypi。

如果有志愿者对以上工作有兴趣，欢迎参与。

如果wechatpy项目有意收编本部分代码，欢迎联系。

---




      ___       __   _______   ________  ___  ___  ________  _________  ________  ___    ___
     |\  \     |\  \|\  ___ \ |\   ____\|\  \|\  \|\   __  \|\___   ___\\   __  \|\  \  /  /|
     \ \  \    \ \  \ \   __/|\ \  \___|\ \  \\\  \ \  \|\  \|___ \  \_\ \  \|\  \ \  \/  / /
      \ \  \  __\ \  \ \  \_|/_\ \  \    \ \   __  \ \   __  \   \ \  \ \ \   ____\ \    / /
       \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \ \  \ \  \ \  \   \ \  \ \ \  \___|\/  /  /
        \ \____________\ \_______\ \_______\ \__\ \__\ \__\ \__\   \ \__\ \ \__\ __/  / /
         \|____________|\|_______|\|_______|\|__|\|__|\|__|\|__|    \|__|  \|__||\___/ /
                                                                                \|___|/

[![Financial Contributors on Open Collective](https://opencollective.com/wechatpy/all/badge.svg?label=financial+contributors)](https://opencollective.com/wechatpy) [![GitHub Actions](https://github.com/wechatpy/wechatpy/workflows/CI/badge.svg)](https://github.com/wechatpy/wechatpy/actions?query=workflow%3ACI)
[![codecov.io](https://codecov.io/github/wechatpy/wechatpy/coverage.svg?branch=master)](https://codecov.io/github/wechatpy/wechatpy?branch=master)
[![Documentation Status](https://readthedocs.org/projects/wechatpy/badge/?version=master)](http://docs.wechatpy.org/zh_CN/master/?badge=master)
[![PyPI](https://img.shields.io/pypi/v/wechatpy.svg)](https://pypi.org/project/wechatpy)
[![Downloads](https://pepy.tech/badge/wechatpy)](https://pepy.tech/project/wechatpy)
[![Reviewed by Hound](https://img.shields.io/badge/Reviewed_by-Hound-8E64B0.svg)](https://houndci.com)

微信(WeChat) 公众平台第三方 Python SDK。

v1.x:   [【阅读文档】](https://wechatpy.readthedocs.org/zh_CN/stable/) [【快速入门】](https://wechatpy.readthedocs.org/zh_CN/stable/quickstart.html)
master: [【阅读文档】](https://wechatpy.readthedocs.org/zh_CN/master/) [【快速入门】](https://wechatpy.readthedocs.org/zh_CN/master/quickstart.html)

## 功能特性

1. 普通公众平台被动响应和主动调用 API
2. 企业微信 API
3. 微信支付 API
4. 第三方平台代公众号调用接口 API
5. 小程序云开发 API

## 安装

推荐使用 pip 进行安装:

```bash
pip install git+https://github.com/whitemay/wechatpy-async.git
```

升级版本：

    pip install -U git+https://github.com/whitemay/wechatpy-async.git


## 使用示例

使用示例参见 [examples](examples/)

## 贡献代码

请阅读 [贡献代码指南](.github/CONTRIBUTING.md)

## 支持项目

如果觉得本项目对您有帮助，请考虑[捐赠支持项目开发](http://docs.wechatpy.org/zh_CN/master/sponsor.html)

## 问题反馈

我们主要使用 [GitHub issues](https://github.com/wechatpy/wechatpy/issues) 进行问题追踪和反馈。

QQ 群：176596300

![wechatpy QQ 群](https://raw.githubusercontent.com/wechatpy/wechatpy/master/docs/_static/images/qq-group.png)


## Contributors

### Code Contributors

This project exists thanks to all the people who contribute. [[Contribute](.github/CONTRIBUTING.md)].
<a href="https://github.com/wechatpy/wechatpy/graphs/contributors"><img src="https://opencollective.com/wechatpy/contributors.svg?width=890&button=false" /></a>

### Financial Contributors

Become a financial contributor and help us sustain our community. [[Contribute](https://opencollective.com/wechatpy/contribute)]

#### Individuals

<a href="https://opencollective.com/wechatpy"><img src="https://opencollective.com/wechatpy/individuals.svg?width=890"></a>

#### Organizations

Support this project with your organization. Your logo will show up here with a link to your website. [[Contribute](https://opencollective.com/wechatpy/contribute)]

<a href="https://opencollective.com/wechatpy/organization/0/website"><img src="https://opencollective.com/wechatpy/organization/0/avatar.svg"></a>
<a href="https://opencollective.com/wechatpy/organization/1/website"><img src="https://opencollective.com/wechatpy/organization/1/avatar.svg"></a>
<a href="https://opencollective.com/wechatpy/organization/2/website"><img src="https://opencollective.com/wechatpy/organization/2/avatar.svg"></a>
<a href="https://opencollective.com/wechatpy/organization/3/website"><img src="https://opencollective.com/wechatpy/organization/3/avatar.svg"></a>
<a href="https://opencollective.com/wechatpy/organization/4/website"><img src="https://opencollective.com/wechatpy/organization/4/avatar.svg"></a>
<a href="https://opencollective.com/wechatpy/organization/5/website"><img src="https://opencollective.com/wechatpy/organization/5/avatar.svg"></a>
<a href="https://opencollective.com/wechatpy/organization/6/website"><img src="https://opencollective.com/wechatpy/organization/6/avatar.svg"></a>
<a href="https://opencollective.com/wechatpy/organization/7/website"><img src="https://opencollective.com/wechatpy/organization/7/avatar.svg"></a>
<a href="https://opencollective.com/wechatpy/organization/8/website"><img src="https://opencollective.com/wechatpy/organization/8/avatar.svg"></a>
<a href="https://opencollective.com/wechatpy/organization/9/website"><img src="https://opencollective.com/wechatpy/organization/9/avatar.svg"></a>

## License

This work is released under the MIT license. A copy of the license is provided in the [LICENSE](./LICENSE) file.
