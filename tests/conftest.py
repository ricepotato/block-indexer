import pytest
import dotenv
from bicxer import w3


@pytest.fixture
def env():
    dotenv.load_dotenv("./bicxer/.env")


@pytest.fixture
def klaytn_web3_provider(env):
    yield w3.get_klaytn_web3_provider()
