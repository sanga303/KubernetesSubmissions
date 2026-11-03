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

```bash
k3d image import juju3333/todo-app:1.5 -c k3s-default
kubectl apply -f manifests/deployment.yaml
kubectl logs deployment/todo-app
kubectl port-forward deployment/todo-app 3003:3000
```

Then open http://localhost:3003
