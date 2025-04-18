import abc


class BaseTextHandler(abc.ABC):
    next_handler: "BaseTextHandler" = None


    @abc.abstractmethod
    def _handle(self, text):
        pass

    def handle(self, text):
        text = self._handle(text)
        if self.next_handler:
            text = self.next_handler.handle(text)
        return text

    def set_next(self, next_handler):
        self.next_handler = next_handler

class UpperCaseTextHandler(BaseTextHandler):
    def _handle(self, text):
        return text.upper()



class ReplaceTextHandle(BaseTextHandler):
    def _handle(self, text):
        return text.replace("f", " ")










