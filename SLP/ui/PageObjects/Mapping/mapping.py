from SLP.ui.PageObjects.Mapping.mapper_map import MapperMap
from tests.value_provider import ValueProvider


class Mapping:
    def __init__(self, driver):
        self.driver = driver

    def mapping(self):
        mapper_provider = ValueProvider.get_mapping_configuration()["MappersProvider"]
        if mapper_provider:
            MapperMap(self.driver).mapper_map(mapper_provider)
