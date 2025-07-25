#!/bin/bash

PROTO_DIR="./interfaces"
OUT_DIR="../crac-client-web/crac_client_web/static/js/proto"

# Crea la cartella di output se non esiste
mkdir -p "$OUT_DIR"

# Array dei file .proto da includere
PROTO_FILES=(
  button.proto
  roof.proto
  curtains.proto
  chart.proto
  telescope.proto
  envelope.proto
)
npx pbjs \
    -t static-module \
    -w es6 \
    -o "$OUT_DIR/proto_bundle_pb.js" \
    --no-imports \
    "${PROTO_FILES[@]/#/$PROTO_DIR/}"
    
echo "🧼 Pulizia import errato..."
# Rimuove eventuali import errati residui
sed -i '/protobufjs\/minimal/d' "$OUT_DIR/proto_bundle_pb.js"

echo "➕ Aggiungo import corretto..."
# Inserisce solo se non già presente
grep -q 'protobuf.minimal.js' "$OUT_DIR/proto_bundle_pb.js" || \
sed -i '1i import * as $protobuf from "./protobuf.minimal.js";' "$OUT_DIR/proto_bundle_pb.js"

echo "✅ Bundle pronto: $OUT_DIR/proto_bundle_pb.js"