import pathlib
import os
import sys
from subprocess import check_call

def generate_proto_code():
    # Use absolute paths for more robustness
    base_dir = pathlib.Path(__file__).parent.absolute()
    proto_interface_dir = base_dir / "interfaces"
    generated_src_dir = base_dir / "crac_protobuf"
    
    if not generated_src_dir.exists():
        generated_src_dir.mkdir()
    
    proto_it = proto_interface_dir.glob("**/*.proto")
    protos = [str(proto) for proto in proto_it if proto.is_file()]
    
    if not protos:
        print("No .proto files found!")
        return

    check_call(
        [
            sys.executable, 
            "-m", 
            "grpc_tools.protoc", 
            f"-Icrac_protobuf={proto_interface_dir}"
        ] + protos + [
            f"--python_out={base_dir}", 
            f"--grpc_python_out={base_dir}"
        ]
    )

if __name__ == "__main__":
    generate_proto_code()
