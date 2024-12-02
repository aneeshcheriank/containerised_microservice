# containerised_microservice
containerise a micro service
[![Python application test with GitHub Actions](https://github.com/aneeshcheriank/containerised_microservice/actions/workflows/makefile.yml/badge.svg)](https://github.com/aneeshcheriank/containerised_microservice/actions/workflows/makefile.yml)

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


## AWS Echosystem
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

## sample.py
- simple function to add 2 numbers
- FastAPI wrapped

## ML model Containerized
- Cloud9
    - clone the repo
    - push the image to ECR
    - commands will be given when create a new ECR to push the image
- ECR
    - ECR login
    - tag the image
    - push the image 
- AWS app runner
    - 

## Architecture
    - platforms
        - model
        - data
        - notebooks
    - model (containerize)-> ECR -> appRunner (Microservice)

- ![alt text](images/image_2.png)

## Dustiriless Containers
- small images size (docker image)
    - 36 MB compared to some 100s of MBs

## Additional Reading
|Title|Tye|Lenght<br>(minutes)|Brief Descrition|
|---|---|---|---|
|[Virtualization and Elasticity](https://paiml.com/docs/home/books/cloud-computing-for-data/chapter03-virtualization-containers-elasticity/)|Reading|15-30|A reading on virtualization and elasticity that provides a foundational overview of cloud computing concepts.|
|["Distroless" Container Images](https://github.com/GoogleContainerTools/distroless)|Documentation|10-15|The official GitHub Repo for distroless containers that reduce the size of container images.|
|[Example GitHub project with Rust distroless](https://github.com/alfredodeza/rust-distroless-azure)|Interactive Tutorial|10-15|A Rust example project that uses distroless container technology to deploy Rust to Azure.|
|[Creating a congare image for use on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html)|Reading|5-10|Documentation showing how to build and use container images on ECS.|
|[Azuere Functions with Rust](https://learn.microsoft.com/azure/azure-functions/create-first-function-vs-code-other?tabs=go%2Cmacos&WT.mc_id=academic-0000-alfredodeza)|Reading|5-10|An official Microsoft reading on how to use Azure Functions with Rust|
|[Introductiion to Containers](https://docs.google.com/presentation/d/1uBlq4CMeQSffU3wwyU0xRrSR7buud20t/edit#slide=id.p1)|Reading|15-30|AWS official powerpoint presentation discussing container technology.|

## Reflections
- <b>Summary</b> This lesson explained containers for encapsulating reusable, reliable ML applications, leveraging continuous delivery pipelines, Kubernetes orchestration, infrastructure as code, and optimized distroless images.

### Key Points
- Containers enable portable ML applications
- Automated pipelines deploy containers
- Orchestration cooridates scale

### Reflection Questions
- How could containers improve collaboration in an ML team?
- What dependencies should be included in a container image?
- What expertise is required to orchestrate containers?
- Why define infrastructure as code?
- What security risks do non-distroless containers introduce?

### Excercises
1. Containerize an ML model API with Docker
2. Set up a container registry to store images
3. Deploy a container to a Kubernetes cluster
4. Write Terraform configs to spin up container infrastructure
5. Compare size and security of distroless vs regular containers
