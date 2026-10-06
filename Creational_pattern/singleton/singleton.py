
"""Beginner-friendly examples of the Singleton design pattern.

A Singleton creates one object for a class and gives every part of the program
access to that same object.  It is useful when a resource should be shared,
such as a printer, a database connection, or application settings.

Think of it as a single shared desk: everyone uses the same desk instead of
creating a new one every time they need one.
"""


class Printer:
    """A shared printer that can be used by every office employee."""

    _instance = None

    def __new__(cls):
        # Create the object only the first time the class is requested.
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def print(self, message):
        print(f"[Printer] {message}")


class Settings:
    """Application settings shared by all parts of the program."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "dark"
            cls._instance.language = "en"
        return cls._instance


def demonstrate_printer():
    """Show that two requests use the exact same printer object."""
    first_printer = Printer()
    second_printer = Printer()

    assert first_printer is second_printer
    first_printer.print("Hello from the first employee")
    second_printer.print("Hello from the second employee")


def demonstrate_settings():
    """Show that settings are shared by the whole application."""
    first_settings = Settings()
    second_settings = Settings()

    assert first_settings is second_settings
    assert first_settings.theme == "dark"
    assert second_settings.language == "en"

    # Changing the shared settings affects every caller.
    first_settings.theme = "light"
    assert second_settings.theme == "light"


def main():
    """Run all examples."""
    print("=== Singleton: shared printer ===")
    demonstrate_printer()

    print("\n=== Singleton: shared settings ===")
    demonstrate_settings()

    print("\nAll Singleton examples passed.")


if __name__ == "__main__":
    main()