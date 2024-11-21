class CurrentUser:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CurrentUser, cls).__new__(cls)
            cls._instance.user = None
        return cls._instance

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user

