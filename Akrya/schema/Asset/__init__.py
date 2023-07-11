from .. import Base

class create(Base):
    class Data:
        url: str
    code: int
    message: str
    data: Data