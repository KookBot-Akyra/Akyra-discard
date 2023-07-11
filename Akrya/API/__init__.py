import httpx
from ..config import BotToken, Oauth2Token

baseAPIurl = 'https://www.kookapp.cn/api/v3'

# Headers
BotHeaders = {
    "Authorization": "Bot " + BotToken
}
Oauth2Headers = {
    "Authorization": "Bearer " + Oauth2Token
}

# Request Client
BotClient = httpx.AsyncClient(headers=BotHeaders)
Oauth2Client = httpx.AsyncClient(headers=Oauth2Headers)
