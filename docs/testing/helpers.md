```python {"name":"wait for docker to start"}
import subprocess
import time

output = subprocess.run(["docker", "ps"], capture_output=True, text=True)

SEARCHING_FOR_STRING = "CONTAINER ID"
CURRENT_TIME = 1
TIMEOUT = 30
STRING_FOUND = False

# Check first to avoid any redundant loops
if SEARCHING_FOR_STRING in output.stdout:
    STRING_FOUND = True

# String not found at first
# Let's give it some time for docker to start
# Loop for a max of 5 seconds OR until string is found (early exit)
while CURRENT_TIME < 30 and not STRING_FOUND:
    
    output = subprocess.run(["docker", "ps"], capture_output=True, text=True)
    foo = output.stdout

    if SEARCHING_FOR_STRING in output.stdout:
        STRING_FOUND = True
        break

    CURRENT_TIME += 1
    time.sleep(1)

if STRING_FOUND:
    print(f"String found in {CURRENT_TIME}s")
else:
    print(f"String still not found after: {CURRENT_TIME}s")
```

```sh { "name": "sleep 15" }
sleep 15
```

```sh { "name": "sleep 30" }
sleep 30
```

```sh{ "name": "wait for all pods to be ready" }
kubectl wait --for=condition=Ready pod --all
```

```sh { "name": "get kubernetes nodes" }
kubectl get nodes
```

```sh { "name": "check collector deployment is healthy" }
kubectl rollout status deployment/dynatrace-collector-opentelemetry-collector --timeout=10m
```

```sh { "name": "check app is running" }
kubectl rollout status deployment/cart --timeout=10m
kubectl rollout status deployment/checkout --timeout=10m
kubectl rollout status deployment/currency --timeout=10m
kubectl rollout status deployment/flagd --timeout=10m
kubectl rollout status deployment/frontend --timeout=10m
kubectl rollout status deployment/frontend-proxy --timeout=10m
kubectl rollout status deployment/image-provider --timeout=10m
kubectl rollout status deployment/load-generator --timeout=10m
kubectl rollout status deployment/payment --timeout=10m
kubectl rollout status deployment/postgresql --timeout=10m
kubectl rollout status deployment/product-catalog --timeout=10m
kubectl rollout status deployment/quote --timeout=10m
kubectl rollout status deployment/shipping --timeout=10m
kubectl rollout status deployment/valkey-cart --timeout=10m
```

```sh { "name": "[background] port forward to app"}
kubectl -n default port-forward svc/frontend-proxy 8080:8080
```
