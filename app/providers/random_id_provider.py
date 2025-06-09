from abc import ABC, abstractmethod
from fastapi import HTTPException

class RandomIdProvider(ABC):
    """Abstract base class for random ID providers"""
    
    def __init__(self, name: str):
        self.name = name
    
    def get_random_id(self) -> str:
        """Get a random ID with error handling"""
        try:
            return self._get_id()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @abstractmethod
    def _get_id(self) -> str:
        """Protected method that implementations must provide to get the actual ID"""
        pass 