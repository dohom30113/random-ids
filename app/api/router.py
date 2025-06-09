from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from ..models.random_id_response import RandomIdResponse
from ..providers.provider_registry import ProviderRegistry

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "apis": ProviderRegistry.get_providers()}
    )

@router.get("/api/random-id/{api_index}", response_model=RandomIdResponse)
async def get_id(api_index: int):
    providers = ProviderRegistry.get_providers()
    if 0 <= api_index < len(providers):
        provider = providers[api_index]
        random_id = provider.get_random_id()
        return RandomIdResponse(
            name=provider.name,
            id=random_id
        )
    raise HTTPException(status_code=400, detail="Invalid API index") 