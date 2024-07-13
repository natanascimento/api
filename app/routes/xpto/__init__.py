from app.routes.factory import RouterFactory
from app.routes.xpto.contracts import XPTORequest
from app.domain.case.use_cases import CreateXPTOTemplate
from fastapi import Depends

router = RouterFactory(version="v1", tag="xpto").get


@router.post("/data/xpto",
             response_description="Create a xpto",
             status_code=201)
def create_xpto_data(xpto_create_request: XPTORequest,
                     xpto_create: CreateXPTOTemplate = Depends()):
    return xpto_create.execute(xpto_create_request).message
