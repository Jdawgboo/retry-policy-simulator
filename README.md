# retry-policy-simulator

Simulate capped exponential-backoff schedules without external services.

```bash
python retry_policy_simulator.py 5 --base 2 --cap 10
python -m unittest -v
```

Use it to reason about a retry plan; it does not perform network calls. MIT licensed.