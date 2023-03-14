import redis
import random
import string
import argparse

def generate_ids(n, length):
    for i in range(n):
        id = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        yield id

def populate_redis_with_ids(redis_client, n_users, user_id_length, n_offers, offer_id_length):
    # Flush Redis
    redis_client.flushdb()

    # Use pipeline to speed up writes
    with redis_client.pipeline() as pipeline:
        # Populate Redis with user IDs and offer IDs
        for user_id in generate_ids(n_users, user_id_length):
            offer_ids = list(generate_ids(n_offers, offer_id_length))
            pipeline.rpush(user_id, *offer_ids)

        # Execute pipeline
        pipeline.execute()

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Populate Redis with user IDs and offer IDs')
    parser.add_argument('N', type=int, help='number of user IDs to generate')
    args = parser.parse_args()

    # Connect to Redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Populate Redis with user IDs and offer IDs
    populate_redis_with_ids(r, args.N, 32, 100, 32)

    # Print out Redis memory footprint and number of keys
    info = r.info()
    print(f"Memory footprint: {info['used_memory_human']}")
    print(f"Number of keys: {info['db0']['keys']}")
