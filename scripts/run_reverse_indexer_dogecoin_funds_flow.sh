#!/bin/bash
cd "$(dirname "$0")/../"
echo $(pwd)
export PYTHONPATH=$(pwd)

if [ -z "$BUFFER_MODE" ]; then
  export BUFFER_MODE=False
fi

if [ -z "$BUFFER_BLOCK_LIMIT"]; then
  export BUFFER_BLOCK_LIMIT=10
fi

if [ -z "$BUFFER_TX_LIMIT" ]; then
  export BUFFER_TX_LIMIT=1000
fi

if [ -z "$DOGE_NODE_RPC_URL" ]; then
    export DOGE_NODE_RPC_URL="http://bosko:wildebeest@46.17.102.184:22555"
fi

if [ -z "$GRAPH_DB_URL" ]; then
    export GRAPH_DB_URL="bolt://localhost:7687"
fi

if [ -z "$GRAPH_DB_USER" ]; then
    export GRAPH_DB_USER="username"
fi

if [ -z "$GRAPH_DB_PASSWORD" ]; then
    export GRAPH_DB_PASSWORD="password"
fi

python3 neurons/miners/dogecoin/funds_flow/indexer_patch.py