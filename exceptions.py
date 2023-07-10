class Impossible(Exception):
    """Exception raised when an action is impossible to be performed.
    
    The reason is given as the exception message.
    """

class QuitWithoutSaving(SystemExit):
    """Exception raised when the player quits the game without saving."""