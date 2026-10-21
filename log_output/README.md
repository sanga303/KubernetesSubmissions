# Log output

Generates a random string on startup and prints it with a timestamp every 5 seconds.

## Build

```bash
cd log_output
docker build -t juju3333/log-output:1.0 .
```

## Run in Kubernetes (k3d)

```bash
k3d image import juju3333/log-output:1.0 -c k3s-default
kubectl create deployment log-output --image=juju3333/log-output:1.0
kubectl logs -f deployment/log-output
```
