from abc import ABC, abstractmethod


class Medium(ABC):
    """
    The goal is to hide sending implementations from whom
    is going to use the class and provide devs
    with a common language to add mediums to the system.
    """

    @abstractmethod
    def send(self) -> bool:
        """
        Sends a message
        :return: True for success, False for failure
        """
        pass

    @abstractmethod
    def get_recipient(self) -> str:
        """
        Who is going to receive this message?
        May be used to manipulate recipient just before sending
        the message (E.g. adding a @ in the beginning)
        :return: str
        """
        pass

    @abstractmethod
    def get_message_details(self) -> dict:
        """
        Formats message details as a dict
        acceptable by the 3rd party.
        :return: dict
        """
        pass

    @abstractmethod
    def get_configuration(self) -> dict:
        """
        A dict containing all configuration needed for send().
        (E.g. auth tokens, username or passwords, hosts)
        :return: dict
        """
        pass
