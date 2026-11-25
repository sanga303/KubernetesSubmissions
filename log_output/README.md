# Log output

Generates a random string on startup and keeps it in memory.

- Prints the string with a timestamp to the log every 5 seconds.
- Serves the current status (timestamp and random string) over HTTP on `/`.

Environment variables:
- `PORT`: port the web server listens on (default 3000)

## Build

```bash
cd log_output
docker build -t juju3333/log-output:1.7 .
```

## Run locally

```bash
docker run --rm -p 3000:3000 juju3333/log-output:1.7
curl localhost:3000
```

## Run in Kubernetes (k3d)

The cluster needs host port 8081 mapped to port 80 (Traefik):

```bash
k3d cluster create -p 8081:80@loadbalancer --agents 2
```

For an existing cluster: `k3d cluster edit k3s-default --port-add "8081:80@loadbalancer"`.

Deploy:

```bash
k3d image import juju3333/log-output:1.7 -c k3s-default
kubectl apply -f manifests/
kubectl logs -f deployment/log-output
```

Then open http://localhost:8081

Request path: `localhost:8081` → Traefik (port 80) → Ingress `log-output-ingress`
→ Service `log-output-svc:2345` (ClusterIP) → container port `3000`.
