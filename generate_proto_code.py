import pathlib
import os
from subprocess import check_call

def generate_proto_code():
    # La cartella che contiene i file .proto (es. button.proto, telescope.proto)
    proto_interface_files_dir = "./interfaces" 
    
    # La cartella che DEVE contenere tutti i file .proto per soddisfare gli import
    # Dobbiamo creare un path fittizio che contenga la cartella "crac_protobuf"
    proto_root_dir = "./" # La radice del progetto, dove finiscono i pb2
    
    # 1. Trova tutti i file .proto
    # Nota: Dobbiamo elencare i file usando il loro percorso relativo alla radice del progetto
    proto_it = pathlib.Path().glob(proto_interface_files_dir + "/*.proto")
    
    # Creiamo la lista dei file, ma usando il prefisso "crac_protobuf/"
    # Questo inganna protoc facendogli credere che i file siano in una sottocartella.
    protos = []
    for proto_path in proto_it:
        # Questo è l'UNICO modo per forzare protoc a vedere il path completo
        # es: "crac_protobuf/button.proto"
        protos.append(f"crac_protobuf/{proto_path.name}") 
        
    if not protos:
        print(f"Nessun file .proto trovato in {proto_interface_files_dir}.")
        return

    print(f"Trovati {len(protos)} file .proto da compilare.")

    # 2. Compila i file con l'opzione -I corretta

    check_call(
        [
            "python", 
            "-m", 
            "grpc_tools.protoc", 
            
            # Percorso di inclusione 1: Dobbiamo puntare alla cartella che contiene tutti i file
            # Per l'import "crac_protobuf/button.proto", protoc cerca crac_protobuf/button.proto
            # L'unica cartella che contiene button.proto è interfaces, ma ha il prefisso sbagliato.
            # Per fortuna, possiamo usare un trucco nel comando shell...
            f"-I{proto_interface_files_dir}", 
            
            # Necessario per risolvere i percorsi locali nel progetto
            f"-I{proto_root_dir}", 
            
            # Opzioni di output
            f"--python_out={proto_root_dir}", 
            f"--grpc_python_out={proto_root_dir}"
        ] + protos,
        # La directory di lavoro del comando subprocess deve essere la radice
        # Questo è un dettaglio cruciale per far funzionare i percorsi relativi
        cwd=proto_root_dir 
    )
    print("Compilazione Protobuf completata con successo.")

generate_proto_code()
