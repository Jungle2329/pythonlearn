class MyDict(dict):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, item):
        if int(item) == 0:
            raise Exception
        return self[item]

    def __setattr__(self, key, value):
        self[key] = value
