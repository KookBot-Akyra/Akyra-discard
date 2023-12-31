from .. import Oauth2Client, baseAPIurl
from ...schema.Oauth2 import *


class oauth2:
    """
    OAuth2.0相关接口
    """
    @staticmethod
    async def token(
        grant_type: str, 
        client_id: str, 
        client_secret: str, 
        code: str, 
        redirect_uri: str
    ) -> oault2TokenHandler:
        """
        获取AccessToken
        :Params: grant_type 授权类型
        :Params: client_id 当前 OAuth 客户端的 client_id
        :Pamams: client_secret 当前 OAuth 客户端的 client_secret
        :Params: code 授权码
        :Params : redirect_uri 回调地址
        :Return: Oauth2.oauth2
        """
        data = {
            "grant_type": grant_type,
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "redirect_uri": redirect_uri
        }
        result = await Oauth2Client.post(url=baseAPIurl + "/oauth2/token", data=data)
        return oault2TokenHandler(**result.json())
