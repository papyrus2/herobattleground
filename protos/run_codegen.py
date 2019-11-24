# Generate protobuf code using the grpc_tools and replace the relative paths with
# absolute paths for the generated code.
#
# We need to update the generate files in order to be able to import the generate
# files in the project.
from grpc_tools import protoc

PROTO_DOCKER_PATH = "/opt/herobattleground/protos"
PYTHON_PROTO_DIRECTORY = '%s/python' % PROTO_DOCKER_PATH
PROTO_FILES = ['character', 'battleground']


def inplace_change(filename, old_string, new_string):
    """ Update all occurs of old_string with the new_string. """

    # Read the file and do a sanity check to see if the string is in the file
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    # Update the file strings
    with open(filename, 'w') as f:
        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(
            **locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def update_imports(proto_file_name):
    """ Update generated files to use relativ to the root repository paths. """
    for replace_string in PROTO_FILES:
        old_string = 'import %s_pb2 as' % replace_string
        new_string = 'import protos.python.%s_pb2 as' % replace_string

        pb_grpc_file = '%s/%s_pb2_grpc.py' % (PYTHON_PROTO_DIRECTORY,
                                              proto_file_name)
        inplace_change(pb_grpc_file, old_string, new_string)

        pb_file = '%s/%s_pb2.py' % (PYTHON_PROTO_DIRECTORY, proto_file_name)
        inplace_change(pb_file, old_string, new_string)


def main():
    for proto_name in PROTO_FILES:
        proto_file = '%s/%s.proto' % (PROTO_DOCKER_PATH, proto_name)
        protoc.main((
            '',
            '-I%s' % PROTO_DOCKER_PATH,
            '--python_out=%s' % PYTHON_PROTO_DIRECTORY,
            '--grpc_python_out=%s' % PYTHON_PROTO_DIRECTORY,
            proto_file,
        ))

        update_imports(proto_name)


if __name__ == "__main__":
    main()
