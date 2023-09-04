import uuid
import json
import cmd
from datetime import datetime

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                for key, data in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**data)
        except FileNotFoundError:
            pass


storage = FileStorage()
storage.reload()


class BaseModel:
    def __init__(self, *args, **kwargs):

        if kwargs:
            kwargs.pop('__class__', None)

            for key, value in kwargs.items():
                setattr(self, key, value)

            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = self.created_at


    # def __str__(self):
    #     return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, repr(self.__dict__))

    def save(self):
        self.updated_at = datetime.now()
        storage.save


    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "


    def do_quit(self, args):
        return


    def do_EOF(self, args):
        return


    def emptyline(self):
        pass

    def do_create(self, args):
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)


    def show(self):
        str_rep = str()

    def do_show(self, args):
        if not args:
            print("** class name missing **")
            return

        arguments = args.split()
        class_name = arguments[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()

        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        if not args:
            print("** class name missing **")
            return

        arguments = args.split()
        class_name = arguments[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()

        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            class_name = args.split()[0]
            if class_name not in globals():
                print("** class doesn't exist **")
                return

            filtered_objects = [str(obj) for obj in objects.values() if isinstance(obj, globals()[class_name])]
            print(filtered_objects)


    def do_update(self, args):
        if not args:
            print("** class name missing **")
            return

        arguments = args.split()
        class_name = arguments[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(arguments) < 2:
            print("** instance id missing **")
            return

        instance_id = arguments[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(arguments) < 3:
            print("** attribute name missing **")
            return

        if len(arguments) < 4:
            print("** value missing **")
            return

        attribute_name = arguments[2]
        attribute_value = arguments[3]

        instance = objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

storage = FileStorage()
storage.reload()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

