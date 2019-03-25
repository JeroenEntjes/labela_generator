"""
Model from template

"""
from ${project}.models import Base, BaseModel


class ${class_name}(Base, BaseModel):
    active = Column(Boolean, default=True)
