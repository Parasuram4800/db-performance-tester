import time

def simulate_query_load():
    print("--- Starting SQL Performance Test ---")
    # In a real scenario, you'd connect to the DB here
    for i in range(1, 6):
        print(f"Executing Batch {i}: Success (Latency: {i*10}ms)")
        time.sleep(0.5)
    print("--- Test Complete: 100% Data Consistency ---")

if __name__ == "__main__":
    simulate_query_load()