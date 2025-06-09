from fastapi import HTTPException
import requests
from .random_id_provider import RandomIdProvider

class SimpleRandomIdProvider(RandomIdProvider):
    """Simple implementation that gets ID from a JSON field"""
    def __init__(self, name: str, url: str, id_field: str):
        super().__init__(name)
        self.url = url
        self.id_field = id_field

    def _get_id(self) -> str:
        try:
            response = requests.get(self.url)
            data = response.json()
            
            # Extract ID based on the specified field
            fields = self.id_field.split('.')
            result = data
            for field in fields:
                if field.endswith(']'):
                    key, index = field[:-1].split('[')
                    result = result[key][int(index)]
                else:
                    result = result[field]
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e)) 