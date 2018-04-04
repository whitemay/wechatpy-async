# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import base64
import copy
import hashlib
import socket

import six

from wechatpy.utils import to_binary, to_text


def format_url(params, api_key=None):
    data = [to_binary('{0}={1}'.format(k, params[k])) for k in sorted(params) if params[k]]
    if api_key:
        data.append(to_binary('key={0}'.format(api_key)))
    return b"&".join(data)


def calculate_signature(params, api_key):
    url = format_url(params, api_key)
    return to_text(hashlib.md5(url).hexdigest().upper())


def _check_signature(params, api_key):
    _params = copy.deepcopy(params)
    sign = _params.pop('sign', '')
    return sign == calculate_signature(_params, api_key)


def dict_to_xml(d, sign):
    xml = ['<xml>\n']
    for k in sorted(d):
        # use sorted to avoid test error on Py3k
        v = d[k]
        if isinstance(v, six.integer_types) or (isinstance(v, six.string_types) and v.isdigit()):
            xml.append('<{0}>{1}</{0}>\n'.format(to_text(k), to_text(v)))
        else:
            xml.append(
                '<{0}><![CDATA[{1}]]></{0}>\n'.format(to_text(k), to_text(v))
            )
    xml.append('<sign><![CDATA[{0}]]></sign>\n</xml>'.format(to_text(sign)))
    return ''.join(xml)


def get_external_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        wechat_ip = socket.gethostbyname('api.mch.weixin.qq.com')
        sock.connect((wechat_ip, 80))
        addr, port = sock.getsockname()
        sock.close()
        return addr
    except socket.error:
        return '127.0.0.1'


def rsa_encrypt(data, pem, b64_encode=True):
    """
    rsa 加密
    :param data: 待加密字符串
    :param pem: RSA public key 内容
    :param b64_encode: 是否对输出进行 base64 encode
    :return:
    """
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding
    encoded_data = data.encode('utf-8') if not isinstance(data, bytes) else data
    pem = pem.encode('utf-8') if not isinstance(pem, bytes) else pem
    public_key = serialization.load_pem_public_key(pem, backend=default_backend())
    encrypted_data = public_key.encrypt(
        encoded_data,
        padding=padding.OAEP(
            mgf=padding.MGF1(hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=b'',
        )
    )
    if b64_encode:
        encrypted_data = base64.b64encode(encrypted_data).decode('utf-8')
    return encrypted_data


def rsa_decrypt(encrypted_data, pem, password=None):
    """
    rsa 解密
    :param encrypted_data: 待解密 bytes
    :param pem: RSA private key 内容
    :param password: RSA private key pass phrase
    :return:
    """
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.asymmetric import padding

    pem = pem.encode('utf-8') if not isinstance(pem, bytes) else pem
    private_key = serialization.load_pem_private_key(pem, password, backend=default_backend())
    data = private_key.decrypt(
        encrypted_data,
        padding=padding.OAEP(
            mgf=padding.MGF1(hashes.SHA1()),
            algorithm=hashes.SHA1(),
            label=b'',
        )
    )
    return data
