from functools import lru_cache


class Storage:
    def __init__(self):
        self.value = None


@lru_cache()
def get_storage() -> Storage:
    return Storage()
