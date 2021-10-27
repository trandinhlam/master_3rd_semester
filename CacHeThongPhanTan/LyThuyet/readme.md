# SERMINAR TÌM HIỂU CÔNG NGHỆ KUBERNETES TRONG QUẢN LÝ CÁC HỆ THỐNG PHÂN TÁN
# Nhóm thực hiện:
+ 20C12007 - Trần Đình Lâm
+ 20C12030 - Huỳnh Lâm Phú Sĩ
____
## Mục tiêu:
____
## Giải thích lý do vì sao nên tìm hiểu Kubernetes:
____
## Các bước tìm hiểu, phân tích, thực nghiệm để đạt được mục tiêu đề ra:

### Đặt vấn đề - Hiện trạng

### Lịch sử ra đời của Kubernetes

+ Kubernetes là một công cụ mã nguồn mở (2014) giúp lập trình viên có thể triển khai, mở rộng và quản lý các ứng dụng dưới dạng container. Là một công cụ điều phối, theo dõi và xử lý việc lên lịch các container trên một cluster, đảm bảo chúng chạy đúng theo kế hoạch.

+ Kubernetes là một hệ sinh thái lớn và phát triển nhanh chóng, teckstack lớn và công cụ hỗ trợ rộng rãi.
![alt](https://d33wubrfki0l68.cloudfront.net/26a177ede4d7b032362289c6fccd448fc4a91174/eb693/images/docs/container_evolution.svg)

+ Thời đại triển khai theo cách truyền thống
+ Thời đại triển khai ảo hóa
+ Thời đại triển khai Container
  + Lợi ích:
    + Tạo container và image dễ dàng so với việc dùng VM
    + CI/CD tốt, rollbacks dễ dàng nhanh chóng
    + Phân biệt giữa Dev và Ops
    + Khả năng monitor không chỉ các metrics ở mức Hệ điều hành, mà còn cả mức application health và các tín hiệu khác
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
  
  + Control Plane Components: quản lý một cluster cố định. Các component thuộc loại này có thể chạy trên bất kỳ máy nào thuộc cluster. Gồm các loại thành phần sau:
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

+ Các cách triển khai công nghệ container phổ biến

+ Kubernetes (K8s) - công cụ quản lý ứng dụng container tốt nhất hiện nay

+ **Auto scaling** trong K8s trên nền tảng điện toán đám mây: Vì sao cần Auto scaling, các chiều và đối tượng Auto scaling, tại sao Kubernetes cần tích hợp với Cloud...
____
## Tài liệu tham khảo:
+ https://kubernetes.io/vi/docs/concepts/overview/what-is-kubernetes/
+ 
+
____