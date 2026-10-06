# Singleton Design Pattern

The Singleton pattern ensures that a class has only one instance and provides a global access point to that instance.

Think of it as a single shared object that everyone in the program can use. Instead of creating a new printer, settings object, or database connection every time, the program reuses the same object.

## Example

The examples in `singleton.py` demonstrate two common uses:

1. **Shared printer** — all employees use the same printer object.
2. **Shared settings** — every part of the application receives the same configuration.

## How It Works

The class stores its instance in `_instance`:

```python
_instance = None
```

When the class is first called, Python creates the object and stores it in `_instance`:

```python
if cls._instance is None:
    cls._instance = super().__new__(cls)
```

Every later call returns the same object:

```python
return cls._instance
```

The following expression checks that both variables refer to the exact same object:

```python
assert first_printer is second_printer
```

## Run the Examples

Open a terminal in the project folder and run:

```powershell
python .\Creational_pattern\singleton.py
```

Expected output:

```text
=== Singleton: shared printer ===
[Printer] Hello from the first employee
[Printer] Hello from the second employee

=== Singleton: shared settings ===

All Singleton examples passed.
```

## When to Use Singleton

Use the Singleton pattern when a resource should be shared throughout the application, such as:

- A database connection
- A logging system
- Application configuration
- A shared printer
- A file or network service

## When Not to Use Singleton

Avoid using Singleton when the application needs multiple independent objects, such as several separate databases, different users' settings, or isolated resources for different workflows.

## Main Concepts

- `class` — creates a class.
- `__new__` — creates the object before initialization.
- `_instance` — stores the one shared object.
- `is` — checks whether two variables refer to the same object.
- `assert` — verifies that a condition is true.
- `if __name__ == "__main__"` — runs the example only when the file is executed directly.
