
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Tuple, NamedTuple, Optional

class AudioSegment(NamedTuple):
    text: str
    speaker: Optional[str]
    new_visual: bool # Triggers a new visual slide/overlay
    slide_id: int = 0
    click_id: int = 0

class BaseParser(ABC):
    def __init__(self, input_path: Path):
        self.input_path = input_path

    @abstractmethod
    def parse(self) -> Tuple[List[AudioSegment], int]:
        """
        Parse the input file.
        Returns:
            - List of AudioSegment (flattened logical audio flow)
            - Estimated Visual Step Count (for validation)
        """
        pass
    
    @abstractmethod
    def generate_images(self, output_dir: Path, resolution: str) -> List[Path]:
        """
        Generate visual frames (images).
        Returns list of paths to generated images.
        """
        pass
