from typing import Optional, List, Dict
import bittensor as bt

# Model types
MODEL_TYPE_FUNDS_FLOW = "funds_flow"
MODEL_TYPE_FUNDS_FLOW_V1 = "funds_flow-v1.0"

# Networks
NETWORK_BITCOIN = "bitcoin"
NETWORK_LITECOIN = "litecoin"
NETWORK_DOGE = "doge"
NETWORK_DASH = "dash"
NETWORK_ZCASH = "zcash"
NETWORK_BITCOIN_CASH = "bitcoin_cash"


class MinerDiscoveryMetadata:
    network: str = None
    assets: List[str] = None
    model_type: str = None


class MinerDiscoveryOutput:
    metadata: MinerDiscoveryMetadata = None
    data: Optional[List[Dict]] = None


class MinerDiscovery(bt.Synapse):
    output: MinerDiscoveryOutput = None

    def deserialize(self) -> MinerDiscoveryOutput:
        return self.output


class MinerQuery(bt.Synapse):
    network: str = None
    asset: str = None
    model_type: str = None
    query: str = None
    output: Optional[List[Dict]] = None

    def deserialize(self) -> List[Dict]:
        return self.output