from enum import Enum


class GenderChoices(Enum):
    MALE = 'Male'
    FEMALE = 'Female'

    @classmethod
    def choices(cls):
        return [(key.value, key.value) for key in cls]
