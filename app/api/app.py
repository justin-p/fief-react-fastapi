import random

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAsync
from fief_client.integrations.fastapi import FiefAuth
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    fief_base_url: str
    fief_client_id: str
    fief_client_secret: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()

fief = FiefAsync(
    settings.fief_base_url,
    settings.fief_client_id,
    settings.fief_client_secret,
    verify=False,
)

scheme = OAuth2AuthorizationCodeBearer(
    f"{settings.fief_base_url}/authorize",
    f"{settings.fief_base_url}/api/token",
    scopes={"openid": "openid", "offline_access": "offline_access"},
    auto_error=False,
)

auth = FiefAuth(fief, scheme)


app = FastAPI()


class RandomPetName(BaseModel):
    name: str


@app.get("/random_pet")
async def random_pet(
    random_pet_name: RandomPetName = Depends(auth.authenticated()),
):
    pet_names = [
        "Fluffy",
        "Buddy",
        "Luna",
        "Max",
        "Bella",
        "Charlie",
        "Lucy",
        "Rocky",
        "Daisy",
        "Bailey",
        "Molly",
        "Loki",
        "Milo",
        "Whiskers",
        "Oreo",
        "Simba",
        "Nala",
        "Oscar",
        "Coco",
        "Kitty",
    ]

    return RandomPetName(name=random.choice(pet_names))


# Add CORS middleware
origins = ["http://frontend.local.test"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
