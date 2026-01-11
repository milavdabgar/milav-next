
import shutil
from pathlib import Path
from typing import Tuple

class CacheManager:
    def __init__(self, input_path: Path, keep_residuals: bool = False):
        self.input_path = input_path
        self.keep_residuals = keep_residuals
        
        # Unique workdir based on stem
        self.work_dir = self.input_path.parent / f"video_work_{self.input_path.stem}"
        self.images_dir = self.work_dir / "images"
        self.audio_dir = self.work_dir / "audio"

    def setup(self) -> Tuple[Path, Path]:
        """
        Prepare directory. Cleans existing if present (Clean Start).
        Returns (images_dir, audio_dir).
        """
        if self.work_dir.exists():
            print(f"🧹 Cleaning previous run: {self.work_dir}")
            shutil.rmtree(self.work_dir)
            
        self.images_dir.mkdir(parents=True, exist_ok=True)
        self.audio_dir.mkdir(parents=True, exist_ok=True)
        
        return self.images_dir, self.audio_dir
        
    def cleanup(self):
        """
        Clean residues if not kept.
        """
        if not self.keep_residuals and self.work_dir.exists():
            print(f"🧹 Cleaning up residuals in {self.work_dir}...")
            shutil.rmtree(self.work_dir)
        elif self.keep_residuals:
            print(f"📁 Residuals kept at: {self.work_dir}")
