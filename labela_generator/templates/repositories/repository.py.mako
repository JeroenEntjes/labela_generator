"""
Repository from template
"""
from ${project}.${repositories_folder}.base import BaseRepository
from ${project}.${models_folder}.${model_name} import ${model_class_name}


class ${model_class_name}Repository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, ${model_class_name})
