from unittest.mock import patch
import web3

from bic_indexer.w3 import get_klaytn_web3_provider


def test_klaytn_web3_provider(klaytn_web3_provider: web3.Web3):
    result = klaytn_web3_provider.eth.get_balance(
        "0x45EB6D727FB8C1EB89284b65D336f2C6bcbA0f73"
    )
    assert result

    block_number = klaytn_web3_provider.eth.block_number
    assert isinstance(block_number, int)


def test_get_klaytn_web3_provider(env):
    # create a mock settings object
    class MockSettings:
        kas_access_key_id = "access_key"
        kas_secret_key_id = "secret_key"

    # patch the config.Settings class to return the mock settings object
    with patch("bic_indexer.w3.config.Settings", return_value=MockSettings()):
        # call the function to get the provider
        provider = get_klaytn_web3_provider()

        # assert that the provider is not None
        assert provider is not None

        # assert that the provider is an instance of Web3
        assert isinstance(provider, web3.Web3)
