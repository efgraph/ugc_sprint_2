class UserAlreadyExists(Exception):
    pass


class UserDoesntExists(Exception):
    pass


class WrongPassword(Exception):
    pass


class EditUserException(Exception):
    pass


class RoleAlreadyExists(Exception):
    pass


class RoleDoesntExists(Exception):
    pass


class RelationDoesntExists(Exception):
    pass
