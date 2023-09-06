from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class TimelinePostsDTO(BaseModel):

    post_id : int
    user_id: int
    content : str
    image_url : Optional[str]
    game_tags: List[int]
    model_config = ConfigDict(from_attributes=True)
