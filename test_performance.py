import pytest
import time
import random

# Simulated Database Connection Class
class MockDB:
    def execute_query(self, query):
        # Simulate network & processing latency
        latency = random.uniform(0.01, 0.05) 
        time.sleep(latency)
        return {"status": "success", "latency": latency}

@pytest.fixture
def db_conn():
    return MockDB()

def test_query_latency_p99(db_conn):
    """Validate that 99% of queries finish under 100ms."""
    threshold = 0.100  # 100ms
    results = []
    
    print("\nRunning Performance Benchmark...")
    for _ in range(50):
        res = db_conn.execute_query("SELECT count(*) FROM table")
        results.append(res['latency'])
    
    max_latency = max(results)
    print(f"Max Latency: {max_latency:.4f}s")
    
    assert max_latency < threshold, f"Performance degradation detected! Max latency was {max_latency}s"

def test_data_ingestion_consistency(db_conn):
    """Simulate checking if 1M rows land in production without errors."""
    res = db_conn.execute_query("INSERT INTO cluster_table SELECT * FROM source")
    assert res['status'] == "success"