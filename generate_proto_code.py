import pathlib
import os
from subprocess import check_call

def generate_proto_code():
    proto_interface_dir = "./interfaces"
    generated_src_dir = "./crac_protobuf/"
    out_folder = "./"
    if not os.path.exists(generated_src_dir):
        os.mkdir(generated_src_dir)
    proto_it = pathlib.Path().glob(proto_interface_dir + "/**/*")
    proto_path = "crac_protobuf=" + proto_interface_dir
    protos = [str(proto) for proto in proto_it if proto.is_file()]
    check_call(["python", "-m", "grpc_tools.protoc"] + protos + ["--python_out", out_folder, "--grpc_python_out", out_folder, "--proto_path", proto_path])

generate_proto_code()
