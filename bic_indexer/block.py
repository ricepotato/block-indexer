from eth_typing import BlockIdentifier
import web3

"""
logic

블록을 가져온다.
- 재개 블록이 없으면 가장 최근 블록을 가져온다.
- 재개 블록이 있으면 재개 블록을 가져온다.

블록으로부터 트랜젝션 목록을 가져온다.
트랜젝션 목록에서 
"""


def get_block(provider: web3.Web3, block_identifier: BlockIdentifier):
    return provider.eth.get_block(block_identifier)
