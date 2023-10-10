import base64
import functools

import web3

from bic_indexer import config


def get_klaytn_web3_provider_using_kas(
    kas_access_key_id: str, kas_secret_access_key: str
) -> web3.Web3:
    """
    Returns a Web3 instance that is connected to the Klaytn network using the KAS API.

    Args:
        kas_access_key_id (str): The access key ID for the KAS API.
        kas_secret_access_key (str): The secret access key for the KAS API.

    Returns:
        web3.Web3: A Web3 instance connected to the Klaytn network.
    """
    KLAYTN_CYPRESS_CHAIN_ID = "8217"
    return web3.Web3(
        web3.HTTPProvider(
            "https://node-api.klaytnapi.com/v1/klaytn",
            {
                "headers": {
                    "Authorization": "Basic "
                    + base64.b64encode(
                        f"{kas_access_key_id}:{kas_secret_access_key}".encode()
                    ).decode(),
                    "x-chain-id": KLAYTN_CYPRESS_CHAIN_ID,
                    "Content-Type": "application/json",
                }
            },
        )
    )


@functools.lru_cache
def get_klaytn_web3_provider():
    """
    Returns a Klaytn web3 provider using the Klaytn API Service (KAS).

    :return: A Klaytn web3 provider.
    """
    settings = config.Settings()
    return get_klaytn_web3_provider_using_kas(
        settings.kas_access_key_id, settings.kas_secret_key_id
    )
