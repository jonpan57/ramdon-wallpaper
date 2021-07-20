from dataclasses import dataclass, field
from typing import Literal, List, Dict


@dataclass(frozen=True)
class Wallpaper:
    id: str
    url: str
    short_url: str = field(repr=False)
    uploader: Dict[str, str]
    views: int = field(repr=False)
    favorites: int = field(repr=False)
    source: str = field(repr=False)
    purity: Literal["sfw", "sketchy", "nsfw"]
    category: Literal["general", "anime", "people"]
    dimension_x: int = field(repr=False)
    dimension_y: int = field(repr=False)
    resolution: str = field(repr=False)
    ratio: str = field(repr=False)
    file_size: int = field(repr=False)
    file_type: Literal["image/jpeg", "image/png"]
    created_at: str = field(repr=False)
    colors: List[str] = field(repr=False)
    path: str = field(repr=False)
    thumbs: Dict[str, str] = field(repr=False)


api_endpoints = {
    'wallpaper': 'https://wallhaven.cc/api/v1/w/{id}',
    'search': 'https://wallhaven.cc/api/v1/search',
    'tag': 'https://wallhaven.cc/api/v1/tag/{id}',
    'settings': 'https://wallhaven.cc/api/v1/settings',
    'collections': 'https://wallhaven.cc/api/v1/collections/{username}',
    'collections_api-key': 'https://wallhaven.cc/api/v1/collections',
    'collection_listing': 'https://wallhaven.cc/api/v1/collections/{username}/{id}'
}

header = 'X-API-Key:{api-key}'
