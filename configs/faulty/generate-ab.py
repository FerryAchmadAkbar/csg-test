import json, random, os

def generate_ab(filename, num_ips=50000):
    """Generate Absolute Bloat dataset"""
    ips = [
        f"10.{random.randint(0,255)}"
        f".{random.randint(0,255)}"
        f".{random.randint(0,255)}"
        for _ in range(num_ips)
    ]
    config = {
        "app_name": "my-service",
        "version": "1.0.0",
        "database": {"host": "localhost", "port": 5432},
        "debug": False,
        "allowed_ips": ips  # field valid, tapi jumlahnya monstrous
    }
    os.makedirs("configs/faulty", exist_ok=True)
    with open(filename, 'w') as f:
        json.dump(config, f, indent=2)
    size_kb = os.path.getsize(filename) / 1024
    print(f"Dibuat: {filename} ({size_kb:.1f} KB)")

generate_ab("configs/faulty/ab-001.json", num_ips=50000)
# Output: ~2.5 MB — valid schema, tapi bloated