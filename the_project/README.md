# Todo app

Simple Flask web server. Prints "Server started in port NNNN" on startup.
The port can be set with the environment variable `PORT` (default 3000).

## Build

```bash
cd the_project
docker build -t juju3333/todo-app:1.2 .
```

## Run locally

```bash
docker run --rm -p 8080:8080 -e PORT=8080 juju3333/todo-app:1.2
```

## Run in Kubernetes (k3d)

```bash
k3d image import juju3333/todo-app:1.2 -c k3s-default
kubectl create deployment todo-app --image=juju3333/todo-app:1.2
kubectl logs deployment/todo-app
```
