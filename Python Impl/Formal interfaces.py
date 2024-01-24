import abc


class FormalInterfaceImpl(metaclass=abc.ABCMeta):
    """
    You must be careful when you’re combining .__subclasshook__() with .register(),
    as .__subclasshook__() takes precedence over virtual subclass registration.
    To ensure that the registered virtual subclasses are taken into consideration,
    you must add NotImplemented to the .__subclasshook__() dunder method.

    """
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and
                callable(subclass.load_data_source) and
                hasattr(subclass, 'extract_text') and
                callable(subclass.extract_text) or
                NotImplemented)

    @abc.abstractmethod
    def load_data_source(self, path: str, file_name: str):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def extract_text(self, full_file_path: str):
        """Extract text from the data set"""
        raise NotImplementedError

class PdfParserNew(FormalInterfaceImpl):
    """Extract text from a PDF."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text(self, full_file_path: str) -> dict:
        """Overrides FormalParserInterface.extract_text()"""
        pass

class EmlParserNew(FormalInterfaceImpl):
    """Extract text from an email."""
    def load_data_source(self, path: str, file_name: str) -> str:
        """Overrides FormalParserInterface.load_data_source()"""
        pass

    def extract_text_from_email(self, full_file_path: str) -> dict:
        """A method defined only in EmlParser.
        Does not override FormalParserInterface.extract_text()
        """
        pass

if __name__ == '__main__':
    pdf_parser = PdfParserNew()
    """
    Instantiating EmlParserNew will give following error
    TypeError: Can't instantiate abstract class EmlParserNew with abstract methods extract_text
    """
    # eml_parser = EmlParserNew()