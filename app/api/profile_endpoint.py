from fastapi import APIRouter
from fastapi import HTTPException, Depends

from tracardi.service.storage.factory import StorageFor
from .auth.authentication import get_current_user
from tracardi.domain.profile import Profile

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.get("/profile/{id}", tags=["profile"], response_model=Profile)
async def get_profile_by_id(id: str):
    try:
        profile = Profile(id=id)
        # return await profile.storage().load()
        return await StorageFor(profile).index().load()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/profile/{id}", tags=["profile"], response_model=dict)
async def delete_profile(id: str):
    try:
        profile = Profile(id=id)
        # return await profile.storage().delete()
        return await StorageFor(profile).index().delete()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
