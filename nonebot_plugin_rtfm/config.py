from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    rtfm_page: int = 5
    use_proxy: bool = True
