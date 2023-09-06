from typing import List

from fastapi import APIRouter
from fastapi.param_functions import Depends

from api.db.models.timeline_posts_model import TimelinePostsModel
from api.db.dao.timeline_posts import TimelinePostsDAO
from api.web.api.timeline.public.schema import TimelinePostsDTO

router = APIRouter()

@router.get("/get", response_model=List[TimelinePostsDTO])
async def get_timeline_posts(
    limit: int = 10,
    offset: int = 0,
    timeline_dao: TimelinePostsDAO = Depends(),
    ) -> List[TimelinePostsModel] :
 
    return await timeline_dao.get_timeline_posts(limit=limit, offset=offset)

@router.post("/psot")
async def create_timeline_post(
    new_timeline_object: TimelinePostsDTO,
    timeline_dao: TimelinePostsDAO = Depends(),
) -> None:
    
    await timeline_dao.create_timeline_posts(
        user_id = new_timeline_object.user_id,
        content = new_timeline_object.content,
        image_url = new_timeline_object.image_url,
        game_ids = new_timeline_object.game_ids
    )
    
@router.get("/search", response_model=List[TimelinePostsDTO])
async def get_timeline_tag(
    game_id : int,
    timeline_dao: TimelinePostsDAO = Depends()
) -> List[TimelinePostsModel] :

    return await timeline_dao.get_timeline_tag(game_id=game_id)