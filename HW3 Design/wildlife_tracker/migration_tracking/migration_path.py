from typing import Optional

from wildlife_tracker.Migration_management.Migration import Migration
from wildlife_tracker.Migration_management.Migration_Path import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self,
                migration_path_id: int,
                path_id: int,
                species = str,
                destination = Habitat,
                start_location = Habitat,
                duration: Optional[int] = None) -> None:
        self.path_id = path_id
        self.migration_path_id = migration_path_id
        self.species = species 
        self.duration = duration
        self.destination = Habitat
        self.start_location = Habitat

def get_migration_path_details(path_id) -> dict:
    pass

def update_migration_path_details(path_id: int, **kwargs) -> None:
    pass