# SERMINAR TÌM HIỂU CÔNG NGHỆ KUBERNETES TRONG QUẢN LÝ CÁC HỆ THỐNG PHÂN TÁN

# Nhóm thực hiện:

+ 20C12007 - Trần Đình Lâm
+ 20C12030 - Huỳnh Lâm Phú Sĩ

____

## Mục tiêu: Tìm hiểu vừa đủ rộng chủ đề Kubernetes, sau đó đào sâu một giải pháp cốt lõi để nhấn mạnh

____

## Giải thích lý do vì sao nên tìm hiểu Kubernetes:

____

## Các bước tìm hiểu, phân tích, thực nghiệm để đạt được mục tiêu đề ra:

### Đặt vấn đề - Hiện trạng

### Lịch sử ra đời của Kubernetes

+ Kubernetes là một công cụ mã nguồn mở (2014) giúp lập trình viên có thể triển khai, mở rộng và quản lý các ứng dụng
  dưới dạng container. Là một công cụ điều phối, theo dõi và xử lý việc lên lịch các container trên một cluster, đảm bảo
  chúng chạy đúng theo kế hoạch.

+ Kubernetes là một hệ sinh thái lớn và phát triển nhanh chóng, teckstack lớn và công cụ hỗ trợ rộng rãi.
  ![alt](https://d33wubrfki0l68.cloudfront.net/26a177ede4d7b032362289c6fccd448fc4a91174/eb693/images/docs/container_evolution.svg)

+ Thời đại triển khai theo cách truyền thống
+ Thời đại triển khai ảo hóa
+ Thời đại triển khai Container
    + Lợi ích:
        + Tạo container và image dễ dàng so với việc dùng VM
        + CI/CD tốt, rollbacks dễ dàng nhanh chóng
        + Phân biệt giữa Dev và Ops
        + Khả năng monitor không chỉ các metrics ở mức Hệ điều hành, mà còn cả mức application health và các tín hiệu
          khác
        + Tính nhất quán về môi trường dev và production
        + Tính khả chuyển giữa các platform cloud, máy thật và các platform với nhau
        + Quản lý tập trung ứng dụng
        + Cô lập các tài nguyên

+ Các lợi ích được Kubernetes cung cấp:
    + Servuce discovery và load balance
    + Điều phối bộ nhớ
    + Tự động rollout và rollback
    + Đóng gói tự động
    + Tự phục hồi
    + Quản lý cấu hình và bảo mật

+ Các concept thành phân của Kubernetes:
    + Cluster:
    + Nodes:
    + Pods:
    + Container:
+ ![alt](https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg)

    + Control Plane Components: quản lý một cluster cố định. Các component thuộc loại này có thể chạy trên bất kỳ máy
      nào thuộc cluster. Gồm các loại thành phần sau:
        + kube-apiserver:
        + etcd:
        + kube-scheduler:
        + kube-controller-manager:
        + cloud-controller-manager:
    + Node Components:
        + kubelet
        + kube-proxy
        + container runtime
    +

___

#### Dựa theo dàn ý của Bizfly Expert talk Ứng dụng công nghệ container với Kubernetes vào hệ thống IT doanh nghiệp

+ Công nghệ container
    + Lịch sử phát triển các loại hình deployment

+ Các cách triển khai công nghệ container phổ biến

+ Kubernetes (K8s) - công cụ quản lý ứng dụng container tốt nhất hiện nay
    + Giới thiệu kiến trúc Kubernetes tổng quan
    +

+ **Auto scaling** trong K8s trên nền tảng điện toán đám mây: Vì sao cần Auto scaling, các chiều và đối tượng Auto
  scaling, tại sao Kubernetes cần tích hợp với Cloud...

____

## Tài liệu tham khảo:

+ https://kubernetes.io/vi/docs/concepts/overview/what-is-kubernetes/
+ https://www.youtube.com/watch?v=X48VuDVv0do&ab_channel=TechWorldwithNana
+

____
____
____

# KUBERENETES TUTORIAL:

## What is Kubernetes?

+ open-souce **container orchestration tool**
+ Develop by Google
+ Manage containers Framework like docker
+ Manage hundreds-thousands containers in different deployment environments (physical, virtual, cloud)

## Why?

+ From Monolith to Microservies (small-independent services)
+ The controlling of multiple services across multiple envirionments is too complicated (scripts or tools)
+ We need container orchestration tool

## Features:

+ High avalability
+ Scalability
+ Disaster recovery (backup & rollback)

## K8s components:

![img.png](HinhAnh/components.png)

**Has thousand components, But most of the time we only use some of them**

+ **Node**:
  ![img.png](HinhAnh/nodeStructure.png)

+ **Pod**:
    + Smallest unit of k8s
    + Abstraction over container
    + Usually 1 application per **Pod**
    + User only interact with this abstract layer
    + Each Pod gets its own IP address. Each Pod can communicate with each other using that IP
    + Ephemeral: New IP address on re-creation => other Pod have to know that new IP :(
+ **Service**:
    + Permanent IP address
    + Lifecycle of Pod and Service NOT connected
    + Include External service & Internal service
+ **Ingress**:
    + Forwarding to the Service
+ **ConfigMap**:
    + External configuration of application (Pod)
    + **Secret**:
        + Secret, credential data
        + Base64 encoded
+ **Volumes**:
    + A storage component on local or remote machine
    + As a external hard drive plugged into the k8s cluster

+ **Deployment**: (for Stateless apps)
    + Deployment is abstraction layer of Pods
    + Blueprint for Pods
    + User will create Deployments, not just Pods
    + Scale up/down number of replicas of Pods
    + Convenient in interact with Pods
    + Warning: With database Pods, since the replicas and main Pod have to use shared-memory (statefull), we cannot use
      Deployment for this kind Pod, instead of that use **StatefulSet**
      ![img.png](HinhAnh/deplomentStruct.png)
+ **StatefulSet**:
    + Deploy StatefulSet not easy => DB are often hosted **outside** of K8s cluster

+ **ReplicaSet**:
    + Manage a set of replica for Pod, belong to specific deployment
    +

## K8s Basic Architecture

### **3 Node processes in Worker machine**:

![img.png](HinhAnh/WorkerMachine.png)

+ **Container runtime**

+ **Kubelet**:
    + Interacts with both - the container and node
    + Starts the Pod with a Container inside & assign resource to it
+ **Kube proxy**:
    + Installed on every Node
    + Intelligent forwarding request

### 4 Master proceses (Master Nodes)

![img.png](HinhAnh/MasterNodes.png)

+ **Api Server**:
    + Cluster gateway
    + Acts as a gatekeeper for authentication
    + Receive user request action onto cluster
+ **Scheduler**:
    + Scheduler in order to start application Pod on one of the Worker nodes
    + Decide where to put the scheduled Pod base on prerequisite resources
+ **Controller manager**:
    + Detect cluster state changes (node died, recover,...)
    + Send control request to Scheduler
+ **etcd**:
    + etcd is the **cluster brain**
    + Cluster changes get stored in the key-value store:
        + Is the cluster healthy?
        + What resources are available?
        + Did the cluster state change?
    + Application data is __NOT__ store in etcd!
    + etcd holds the current status of any K8s component

### Example Cluster Setup

### Minikube & Kubectl

+ **Minikube**:
    + Is basically 1-node-cluster
    + Master and Worker run on 1 machine
    + Docker pre-installed
    + Need a virtualization
    + For testing/learning purposes

+ **Kubectl**:
    + CLI for K8s control cluster
    + Do anything in the kubernetes
    + Any type of cluster setup (local, minikube, cloud)

### YAML Configuration File in Kubernetes

+ **3 parts of config file**:
    + metadata:
        + name
        + labels
    + specification:
        + replicas:
        + selector:
        + template:
    + status:
+ Connecting Deployment to Pods
+ Connecting Service to Deployments

### Demo mongo-express

### Namespace:

+ Why namespace?
    + For good organization of resource & role
    + Avoid conflicts between teams & product
+ How?
    + Cannot access most resources from another Namespace
    + Each Namespace must define own ConfigMap

+ **kube-system**:
    + system namespace, do NOT create or edit on kube-system
+ **kube-public**:
    + publicely accessible data
    + A configmap, which contains cluster information
+ **kube-node-lease**:
    + health information
+ **default**:
    + main resource

+ Create component in a Namespace

### Ingress

______
______

# K8s AutoScaling Mechanism


