from dataclasses import dataclass


@dataclass
class BaseQuality:
    obj_name: str
    obj_data: str

@dataclass
class QualityWithDot(BaseQuality):
    dots: int = 0



class Character:
    def __init__(
            self, 
            name: str,
            chronicle: str
    ):
        pass
    
    
    