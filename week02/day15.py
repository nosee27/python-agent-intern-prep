from dataclasses import dataclass,field
@dataclass(frozen=True)
class Config:
    model:str="qwen-plus",
    api_key:str=field(repr=False)

cfg=Config(api_key="222")
print(cfg)