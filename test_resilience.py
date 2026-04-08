import pytest
import time

class ClusterManager:
    def __init__(self):
        self.nodes = ["node1", "node2", "node3"]
        self.is_healthy = True

    def kill_node(self, node_name):
        print(f"SHUTTING DOWN: {node_name}")
        self.nodes.remove(node_name)

    def check_replication_status(self):
        # In a real system, if 2 nodes remain, the system stays healthy
        return len(self.nodes) >= 2

@pytest.fixture
def cluster():
    return ClusterManager()

def test_node_failure_resilience(cluster):
    """Verify that the cluster stays healthy if 1 node fails."""
    print("\nStarting Chaos Test...")
    
    # 1. Check initial state
    assert cluster.check_replication_status() is True
    
    # 2. Simulate a node crash (Chaos Engineering)
    cluster.kill_node("node2")
    
    # 3. System should still be healthy because node1 and node3 are up
    status = cluster.check_replication_status()
    print(f"Cluster Status after failure: {'HEALTHY' if status else 'FAILED'}")
    
    assert status is True, "Cluster failed after losing only one node!"