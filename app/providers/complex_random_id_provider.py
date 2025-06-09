import requests
from fastapi import HTTPException
from .random_id_provider import RandomIdProvider

class ComplexRandomIdProvider(RandomIdProvider):
    """Example of a more complex provider with custom logic"""
    def __init__(self, name: str, url: str):
        super().__init__(name)
        self.url = url

    def _get_id(self) -> str:
        response = requests.get(self.url)
        data = response.json()
        
        # Example: Combine multiple fields to create a unique ID
        if 'results' in data and len(data['results']) > 0:
            user = data['results'][0]
            # Create a custom ID format
            return f"{user['id']['value']}-{user['login']['uuid'][:8]}"
        raise HTTPException(status_code=500, detail="No results found") 