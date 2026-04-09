import json, os

def generate_gra_pair():
    """Buat pasangan file baseline + anomaly"""
    os.makedirs("configs/valid", exist_ok=True)
    os.makedirs("configs/faulty", exist_ok=True)

    # Commit 1: file baseline normal
    baseline = {
        "app_name": "my-service",
        "version": "1.0.0",
        "database": {"host": "localhost", "port": 5432, "max_connections": 100},
        "debug": False
    }
    with open("configs/valid/gra-baseline.json", 'w') as f:
        json.dump(baseline, f, indent=2)

    # Commit 2: file yang sama tapi membengkak (semua field valid!)
    anomaly = baseline.copy()
    anomaly["feature_flags"] = {
        f"user_{i}": {"enabled": True, "rollout": 0.5}
        for i in range(20000)  # 20.000 entri — tiba-tiba!
    }
    with open("configs/faulty/gra-anomaly.json", 'w') as f:
        json.dump(anomaly, f, indent=2)

    b_size = os.path.getsize("configs/valid/gra-baseline.json")
    a_size = os.path.getsize("configs/faulty/gra-anomaly.json")
    growth = (a_size - b_size) / b_size * 100
    print(f"Baseline: {b_size/1024:.1f}KB")
    print(f"Anomaly:  {a_size/1024:.0f}KB")
    print(f"Growth rate: {growth:.0f}% ← ini yang Config Size Guard bisa deteksi!")

generate_gra_pair()