#funzionamento da verificare


import pathlib
import os
from subprocess import check_call

def generate_proto_code():
    proto_interface_dir = "./interfaces"
    
    # Output per i file Python (backend)
    py_out_dir = "./crac_protobuf"

    # Output per i file JS (frontend web)
    js_out_dir = "../crac-client-web/crac_client_web/static/js/proto"

    # Crea le directory se non esistono
    os.makedirs(py_out_dir, exist_ok=True)
    os.makedirs(js_out_dir, exist_ok=True)

    # Trova tutti i file .proto
    protos = [
        p.name for p in pathlib.Path(proto_interface_dir).glob("*.proto")
    ]

    # ✅ Generazione dei file Python
    check_call(
        [
            "python", "-m", "grpc_tools.protoc",
            f"--proto_path={proto_interface_dir}",
            f"--python_out={py_out_dir}",
            f"--grpc_python_out={py_out_dir}",
        ] + protos
    )

    # ✅ Generazione dei file JS
    #check_call(
    #  [
    #       "protoc-gen-ts",
    #       f"--proto_path={proto_interface_dir}",
    #       f"--js_out=import_style=es6,binary:{js_out_dir}",
    #   ] + protos
    #
    #protos=["button.proto","chart.proto","curtains.proto","roof.proto","telescope.proto","envelope.proto"]
    #for proto in protos:
    #    check_call([
    #        "npx", "pbjs",
    #        "--es6", f"{js_out_dir}/{proto.replace('.proto', '_pb.js')}",
    #        f"{proto_interface_dir}/{proto}"
    #    ])

    print("✅ Generazione completata per Python e JS.")

if __name__ == "__main__":
    generate_proto_code()
