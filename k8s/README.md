# K8S

## Lab 9
### Deployment by hands in terminal
```
Create deployment
> kubectl create deployment devopsapp --image=cendien/devopsapp
> deployment.apps/devopsapp created

Get deployments
> kubectl get deployments
> NAME        READY   UP-TO-DATE   AVAILABLE   AGE
  devopsapp   1/1     1            1           2m18s

View pods
> kubectl get pods
> NAME                         READY   STATUS    RESTARTS   AGE
  devopsapp-78ff894f8f-cs67q   1/1     Running   0          3m27s

Expose the deployment to the external network
> kubectl expose deployment devopsapp --type=LoadBalancer --port=8000
> service/devopsapp exposed


Information about pods and services
> kubectl get pods,svc
> NAME                             READY   STATUS    RESTARTS   AGE
  pod/devopsapp-78ff894f8f-v4x56   1/1     Running   0          3m53s

> NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
  service/devopsapp    LoadBalancer   10.107.197.227   <pending>     8000:31660/TCP   3m12s
  service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP          140m

Now we can start the app:
> minikube service devopsapp
> |-----------|-----------|-------------|---------------------------|
  | NAMESPACE |   NAME    | TARGET PORT |            URL            |
  |-----------|-----------|-------------|---------------------------|
  | default   | devopsapp |        8000 | http://192.168.49.2:31660 |
  |-----------|-----------|-------------|---------------------------|
  🎉  Opening service default/devopsapp in default browser...


After this app will be opened in browser with its ip and port,
we can go to the /docs route and check if API is working:
```
![](https://i.imgur.com/3GjpfSs.png)

```
And as we can see, it works

Now we need to clean everything up:
> kubectl delete deployment app-node
> deployment.apps "devopsapp" deleted

> kubectl delete service devopsapp
> service "devopsapp" deleted
```

### Deployment by configuration files
```
After the creation of the configuration files: deployment.yml and service.yml we can start our claster:
> kubectl apply -f .
> deployment.apps/devopsapp-deployment created
  service/devopsapp-service created
  
Information about pods and services:
> kubectl get pods,svc
> NAME                                        READY   STATUS    RESTARTS   AGE
  pod/devopsapp-deployment-69fcbc6d4f-58bqm   1/1     Running   0          5m3s
  pod/devopsapp-deployment-69fcbc6d4f-kgl84   1/1     Running   0          5m3s
  pod/devopsapp-deployment-69fcbc6d4f-kkrm9   1/1     Running   0          5m3s

> NAME                        TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
  service/devopsapp-service   LoadBalancer   10.97.77.232   <pending>     8000:31662/TCP   5m7s
  service/kubernetes          ClusterIP      10.96.0.1      <none>        443/TCP          177m


Now we can start the app:
> minikube service devopsapp-service
> |-----------|-------------------|-------------|---------------------------|
  | NAMESPACE |       NAME        | TARGET PORT |            URL            |
  |-----------|-------------------|-------------|---------------------------|
  | default   | devopsapp-service |        8000 | http://192.168.49.2:31662 |
  |-----------|-------------------|-------------|---------------------------|
  🎉  Opening service default/devopsapp-service in default browser...


In the browser app will be opened, we can check if API works by going
to /docs route:
```
![](https://i.imgur.com/eRk2IUU.png)
```
As we can see it works. Now we can clean everything up:
> kubectl delete deployment devopsapp-deployment
> deployment.apps "devopsapp-deployment" deleted

> kubectl delete service devopsapp-service
> service "devopsapp-service" deleted
```

## Lab 10
```
Creating new chart:
> helm create devopsapp-chart
> Creating devopsapp-chart

Change repository and tag in values.yaml, change port number in deployment.yaml.
Also for livenessProbe and readinessProbe I needed to change path to /api/time/moscow.

After this we can install our new chart:
> helm install devopsapp-chart ./devopsapp-chart

And we need to check this chart:
> minikube dashboard
> 🤔  Verifying dashboard health ...
  🚀  Launching proxy ...
  🤔  Verifying proxy health ...
  🎉  Opening http://127.0.0.1:37323/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy/ in your default browser...
   Opening in existing browser session.
   [75985:75985:0100/000000.194101:ERROR:sandbox_linux.cc(374)] InitializeSandbox() called with multiple threads in process gpu-process.

In browser we can see our chart without any other services and pods:
```
![](https://i.imgur.com/GZLYbwh.png)

```
Now we can check our dashboard with our configured service after:
> kubectl apply -f .
```
![](https://i.imgur.com/4lLUhaE.png)

![](https://i.imgur.com/1xm7V8X.png)

```
And we can check our pods and services:
> kubectl get pods,svc
> NAME                                        READY   STATUS    RESTARTS   AGE
  pod/devopsapp-chart-84745fbc9c-hxfdj        1/1     Running   0          8m57s
  pod/devopsapp-deployment-69fcbc6d4f-fmg2c   1/1     Running   0          2m34s
  pod/devopsapp-deployment-69fcbc6d4f-gfjlw   1/1     Running   0          2m34s
  pod/devopsapp-deployment-69fcbc6d4f-smstq   1/1     Running   0          2m34s

> NAME                        TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
  service/devopsapp-chart     ClusterIP      10.110.136.9   <none>        80/TCP           8m57s
  service/devopsapp-service   LoadBalancer   10.98.49.213   <pending>     8000:32689/TCP   2m34s
  service/kubernetes          ClusterIP      10.96.0.1      <none>        443/TCP          3h51m

```

