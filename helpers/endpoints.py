from moralis import evm_api

def get_contract_info(api_key, address, chain):
    params = {
        "address": address,
        "chain": chain,
    }


    result = evm_api.nft.get_nft_contract_metadata(
        api_key=api_key,
        params=params,
    )

    return result


def get_nft_holders(api_key, address, chain, limit, cursor):
    params = {
        "address": address,
        "chain": chain,
        "format": "decimal",
        "limit": limit,
        "cursor": cursor,
        "normalizeMetadata": True,
        "disable_total": False
    }

    result = evm_api.nft.get_nft_owners(
        api_key=api_key,
        params=params,
    )

    return result