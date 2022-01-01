kubectl get crds
kubectl apply -f crds
kubectl get crds

kubectl appy -f prometheus-operator
kubectl get pods -n monitoring
kubectl logs -f <pod-monitoring-above> -n monitoring

kubectl get storageclass

kubectl apply -f prometheus
kubectl get pods -n monitoring
kubectl get svc -n monitoring
kubectl -n monitoring port-forward svc/prometheus-operated 9090:9090

kubectl get endpoints -n monitoring

kubectl describe endpoints prometheus-operated -n monitoring

kubectl get endpoints -n monitoring
kubectl describe endpoints prometheus-operator -n monitoring

kubectl apply -f prometheus-operator

kubectl apply -f grafana
kubectl get pods -n monitoring

kubectl get svc -n monitoring
kubectl -n monitoring port-forward svc/grafana 3000:3000