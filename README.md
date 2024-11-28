# containerised_microservice
containerise a micro service

## Key Terms
- <b>Container</b> - A standardized, lightweight software package that bundles together an application's code and dependencies to run reliably in any environment.

- <b>Container Registry</b> - A repository for storing, sharing and deploying container images, often integrated into CI/CD pipelines. Examples: Docker Hub, AWS ECR.

- <b>Container Orchestration</b> - Automated management, scaling and coordination of containers leveraging platforms like Kubernetes and Amazon ECS.

- <b>Continuous Delivery</b> - Software development practice to build, test and release containers quickly and reliably by automating deployments through CI/CD pipelines.

- <b>Infrastructure as Code</b> - Managing infrastructure like networking, compute, storage through machine-readable definition files rather than manual processes. Enables reproducibility.

- <b></b>Distroless Container</b> - Optimized container image containing only an app, run-time language, and essential system libraries, omitting shells, package managers, etc. Improves security.

## containerized microservice
- ![alt text](images/image.png)

## Containerized Countious Delivery
![alt text](images/image_1.png)

- push code to ECR
    - create a new ECR
    - open the new ECR
    - commands are listed
        - authenticate
        - build the continer
        - tag
        - push

- App Runner
    - select the image and the tag (Latest)

- AWS code build
    - contious delivery (CI/CD pipeline for AWS)
    - change in the GitHub reflected in AWS ECR
