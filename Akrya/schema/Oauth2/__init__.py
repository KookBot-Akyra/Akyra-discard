from ...schema import Base


class getOauth(Base):
    access_token:str
    expires_in:int
    token_type:str
    scope:str