# add to repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
helm repo update

https://github.com/helm/charts/tree/master/stable/prometheus-operator
# install
helm install prometheus stable/prometheus-operator
# Create CRDs (Deprecated)
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/release-0.38/example/prometheus-operator-crd/monitoring.coreos.com_alertmanagers.yaml
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/release-0.38/example/prometheus-operator-crd/monitoring.coreos.com_podmonitors.yaml
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/release-0.38/example/prometheus-operator-crd/monitoring.coreos.com_prometheuses.yaml
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/release-0.38/example/prometheus-operator-crd/monitoring.coreos.com_prometheusrules.yaml
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/release-0.38/example/prometheus-operator-crd/monitoring.coreos.com_servicemonitors.yaml
kubectl apply -f https://raw.githubusercontent.com/coreos/prometheus-operator/release-0.38/example/prometheus-operator-crd/monitoring.coreos.com_thanosrulers.yaml

# https://gitlab.com/nanuchi/youtube-tutorial-series/-/blob/master/prometheus-exporter/install-prometheus-commands.md

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
helm repo update

helm install prometheus prometheus-community/kube-prometheus-stack


# exporter
https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-mongodb-exporter

helm install mongodb-exporter prometheus-community/prometheus-mongodb-exporter -f values.yaml
helm install node-exporter prometheus-community/prometheus-node-exporter

# HPA with Custom metric Tutorial:
https://www.youtube.com/watch?v=iodq-4srXA8&ab_channel=AntonPutra
# AlertManager send message
https://www.youtube.com/watch?v=mtE4migphGE&ab_channel=AntonPutra
