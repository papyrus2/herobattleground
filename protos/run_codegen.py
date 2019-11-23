# Generate protobuf code using the grpc_tools and replace the relative paths with
# absolute paths for the generated code.
#
# We need to update the generate files in order to be able to import the generate
# files in the project.
from grpc_tools import protoc

PROTO_DOCKER_PATH = "/opt/herobattleground/protos"
PROTO_FILES = ['character']


def inplace_change(filename, old_string, new_string):
    """ Update all occurs of old_string with the new_string. """

    # Read the file and do a sanity check to see if the string is in the file
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    # Update the file strings
    with open(filename, 'w') as f:
        print('Changing "{old_string}" to "{new_string}" in {filename}'.format(
            **locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def main():
    for proto_name in PROTO_FILES:
        python_proto_directory = '%s/python' % PROTO_DOCKER_PATH
        proto_file = '%s/%s.proto' % (PROTO_DOCKER_PATH, proto_name)
        protoc.main((
            '',
            '-I%s' % PROTO_DOCKER_PATH,
            '--python_out=%s' % python_proto_directory,
            '--grpc_python_out=%s' % python_proto_directory,
            proto_file,
        ))

        pb_file = '%s/%s_pb2_grpc.py' % (python_proto_directory, proto_name)
        old_string = 'import %s_pb2 as' % proto_name
        new_string = 'import protos.python.%s_pb2 as' % proto_name
        inplace_change(pb_file, old_string, new_string)


if __name__ == "__main__":
    main()
