from datetime import datetime
import sys

class SingletonMetaClass(type):
    """
    The Singleton MetaClass can be implemented with:
    base class, decoratora and metaclass. We're using metaclass.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        When some class makes the instance that metaclass 
        will make the instance inherit an existing one.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        
        return cls._instances[cls]

class Logger(metaclass=SingletonMetaClass):
    """
    Our example application.
    Note: Singleton can be implemented with any class.
    """

    def __init__(self) -> None:
        self.log("Main logger")

    def log(self, msg: str) -> None:
        sys.stdout.write("{0} - {1}\n".format(msg, datetime.utcnow()))

if __name__ == '__main__':
    """
    Simulating a case where you need to instantiate
    the Logger class two or more times
    """
    logger_one = Logger()
    logger_two = Logger()

    #Check if is the same instance
    if id(logger_one) == id(logger_two):
        logger_one.log("Using Singleton. Same instance :D")
    else:
        logger_one.log("Without Singleton")