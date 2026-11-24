# Todo app

Simple Flask web server. Prints "Server started in port NNNN" on startup
and serves an HTML page on `/` showing pod name, node, port and start time.

Environment variables:
- `PORT`: port to listen on (default 3000)
- `NODE_NAME`: node the pod runs on (set by Kubernetes via the Downward API)

## Build

```bash
cd the_project
docker build -t juju3333/todo-app:1.5 .
```

## Run locally

```bash
docker run --rm -p 8080:8080 -e PORT=8080 juju3333/todo-app:1.5
```

Then open http://localhost:8080

## Run in Kubernetes (k3d)

The cluster needs port 8082 on the host mapped to the NodePort 30080:

```bash
k3d cluster create --port 8082:30080@agent:0 -p 8081:80@loadbalancer --agents 2
```

For an existing cluster, add the mapping with
`k3d cluster edit k3s-default --port-add "8082:30080@agent:0"`.

Deploy:

```bash
k3d image import juju3333/todo-app:1.5 -c k3s-default
kubectl apply -f manifests/
kubectl logs deployment/todo-app
```

Then open http://localhost:8082

