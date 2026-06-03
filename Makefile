verify:
	PYTHONPATH=src python scripts/verify_runtime_safety.py
	PYTHONPATH=src python scripts/verify_challenge_12.py
	PYTHONPATH=src python scripts/verify_data_hashes.py
	PYTHONPATH=src python -m pytest -q
