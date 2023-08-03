from name_that_hash import runner
from icecream import ic


def hash_analyze(hash_string: str):
    try:
        if not runner.api_return_hashes_as_dict([hash_string], {"popular_only": True}):
            text = runner.api_return_hashes_as_dict([hash_string], {"popular_only": True})
            return text[hash_string]
        else:
            text = runner.api_return_hashes_as_dict([hash_string])
            return text[hash_string]
    except Exception as e:
        ic(e)
        ic()
