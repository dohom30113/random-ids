from typing import List
from .random_id_provider import RandomIdProvider
from .simple_random_id_provider import SimpleRandomIdProvider

class ProviderRegistry:
    """Registry for all random ID providers"""
    
    @staticmethod
    def get_providers() -> List[RandomIdProvider]:
        """Get all registered providers"""
        return [
            SimpleRandomIdProvider(
                name='Random User',
                url='https://randomuser.me/api/',
                id_field='results[0].id.value'
            )
        ] 