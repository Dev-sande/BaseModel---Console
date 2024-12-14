# Simple README for File Storage and HBNB Command

## Overview

This project implements a simple in-memory storage system with basic command-line interface (CLI) functionality to manage and manipulate objects using the `cmd` module in Python. The core functionality revolves around the `FileStorage` class for storing and retrieving objects, and the `HBNBCommand` class for interacting with the system through a CLI.

The system is designed to handle objects that are instances of various classes, with automatic generation of unique IDs, timestamps for creation and update, and persistence through saving to a file.

## Features

- Create a new instance: Create new instances of a class and store them.
- Show an instance: Display details of an object based on its class name and ID.
- Destroy an instance: Remove an object from the storage by its class name and ID.
- Update an instance: Modify the attributes of an existing object.
- List all instances: View all instances stored in the system, filtered by class name if desired.

## Classes

### 1. `FileStorage`
Handles the persistence of objects to a file (`file.json`) and supports operations such as saving objects, loading them from storage, and managing the collection of objects.

- `all()`: Returns all objects in storage.
- `new(obj)`: Adds a new object to the storage.
- `save()`: Serializes and writes the objects to a JSON file.
- `reload()`: Loads objects from the file into the storage.

### 2. `BaseModel`
A base class for all objects that will be stored. It provides common functionality like automatic ID generation, timestamps for creation and updates, and methods for serializing and deserializing objects.

- `__str__()`: Returns a string representation of the object.
- `save()`: Updates the timestamp and saves the object to storage.
- `to_dict()`: Returns the object as a dictionary, ready for serialization.

### 3. `HBNBCommand`
This class provides a command-line interface to interact with the storage system. It includes commands for managing objects such as creating, updating, displaying, and deleting instances.

- `do_create()`: Creates a new instance of a class.
- `do_show()`: Displays an instance's details based on class and ID.
- `do_destroy()`: Deletes an instance by its class and ID.
- `do_all()`: Lists all instances in storage.
- `do_update()`: Updates an attribute of an instance.

## Usage

### Command Line Interface (CLI)

1. Start the program:
   To start the interactive command line, run the Python file:

   ```bash
   python <filename>.py
   ```

   This will start the CLI with the prompt `(hbnb)`.

2. Commands:
   You can interact with the system using the following commands:

   - `create <class_name>`: Creates a new instance of the class specified and prints the instance ID.
   - `show <class_name> <instance_id>`: Displays the details of the instance with the given class and ID.
   - `destroy <class_name> <instance_id>`: Deletes the specified instance from storage.
   - `all <class_name>`: Lists all instances of the specified class, or all objects if no class is provided.
   - `update <class_name> <instance_id> <attribute_name> <value>`: Updates an attribute of the specified instance.

   Example usage:
   ```bash
   (hbnb) create BaseModel
   (hbnb) all
   (hbnb) show BaseModel <instance_id>
   (hbnb) update BaseModel <instance_id> name "New Name"
   ```

3. Quit:
   You can exit the CLI at any time by typing `quit` or pressing `Ctrl+D` (EOF).

### Files

- file.json: This file is used for persistent storage of objects. All changes to objects are saved to this file.

## Dependencies

- Python 3.x
- No additional external libraries are required.

## Notes

- If `file.json` does not exist when you run the program, it will be created automatically.
- The `BaseModel` class serves as the parent for other classes (if added in the future). It provides essential methods for creating, saving, and manipulating objects.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
