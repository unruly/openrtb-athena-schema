from __future__ import print_function
import json


class AthenaSchemaFromJson(object):

    def __init__(self, file_name):
        self.file_name = file_name
        with open(file_name) as schema:
            self.json = json.load(schema)

    @staticmethod
    def write(msg):
        print(msg, end='')

    def process_list(self, spec):
        return ",".join(["%s" % (self.get_type(key)) for key in spec])

    def process_dict(self, spec):
        return ",".join(["%s:%s" % (key, self.get_type(spec[key])) for key in spec])

    def get_type(self, e):
        if isinstance(e, dict):
            return "struct<%s>" % self.process_dict(e)
        elif isinstance(e, list):
            return "array<%s>" % self.process_list(e)
        else:
            return e

    def generate(self):
        print("*** Generating schema for [%s]" % self.file_name)
        schema_filename = self.file_name.replace(".json", ".schema")

        with open(schema_filename, "w") as schema:
            schema.write(self.get_type(self.json))


if __name__ == '__main__':
    AthenaSchemaFromJson('bid-request-2.0.json').generate()
