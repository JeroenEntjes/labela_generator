"""
Service from template
"""
from ${project}.${repositories_folder}.${model_name} import ${model_class_name}Repository
from ${project}.${services_folder}.base import BaseRepository


class ${model_class_name}Service(BaseService):
    def __init__(self, repository: ${class_name}Repository):
        self._repository = repository
        super().__init__(repository=self.repository)
