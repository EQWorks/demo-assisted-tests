import unittest
from unittest.mock import MagicMock, patch
import random
import string

from revised import populate_redis_with_ids


@patch('redis.Redis')
def test_populate_redis_with_ids(mock_redis):
    # Set up mock Redis instance
    mock_r = MagicMock()
    mock_redis.return_value = mock_r

    # Define test inputs
    num_users = 10
    user_id_length = 32
    offer_id_length = 16

    # Generate expected IDs
    expected_user_ids = [''.join(random.choices(string.ascii_letters + string.digits, k=user_id_length)) for _ in range(num_users)]
    expected_offer_ids = [''.join(random.choices(string.ascii_letters + string.digits, k=offer_id_length)) for _ in range(100)]

    # Call function under test
    populate_redis_with_ids(num_users, user_id_length, offer_id_length)

    # Verify Redis calls
    mock_r.flushdb.assert_called_once()
    mock_pipeline = mock_r.pipeline.return_value.__enter__.return_value
    for user_id in expected_user_ids:
        mock_pipeline.rpush.assert_any_call(user_id, *expected_offer_ids)
    mock_pipeline.execute.assert_called_once()


if __name__ == '__main__':
    unittest.main()
