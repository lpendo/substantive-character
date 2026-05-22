from dataclasses import dataclass


@dataclass
class BaseQuality:
    obj_name: str
    obj_data: str

@dataclass
class DotQuality(BaseQuality):
    dots: int = 0



# class Character:
#     def __init__(
#             self, 
#             name: str,
#             chronicle: str
#     ):
#         pass

@dataclass
class Character:
    name: str
    chronicle: str

    inherent_splat: BaseQuality
    social_splat: BaseQuality

    soul_trait_1: BaseQuality
    soul_trait_2: BaseQuality

    big_goal: BaseQuality
    small_goal: BaseQuality

    health: int
    willpower: int
    integrity: BaseQuality

    
    
    
    
    
    