import redis
import random
import string
import argparse
import time

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Populate Redis with user IDs and offer IDs')
    parser.add_argument('N', type=int, help='number of user IDs to generate')
    args = parser.parse_args()

    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Flush Redis
    r.flushdb()

    # Generate random user IDs
    user_ids = [''.join(random.choices(string.ascii_letters + string.digits, k=32)) for _ in range(args.N)]

    # Use pipeline to speed up writes
    start_time = time.time()
    with r.pipeline() as pipeline:
        # Populate Redis with user IDs and offer IDs
        for user_id in user_ids:
            offer_ids = [''.join(random.choices(string.ascii_letters + string.digits, k=32)) for _ in range(100)]
            pipeline.rpush(user_id, *offer_ids)

        # Execute pipeline
        pipeline.execute()
