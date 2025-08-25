#!/bin/bash

export DEBIAN_FRONTEND=noninteractive

apt update
apt install -y python3-pip wget sudo gh

# Install kubectl
curl -LO "https://dl.k8s.io/release/v1.30.0/bin/linux/amd64/kubectl"

# Install Helm
curl -s https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash -

# Install kind & cluster
wget -O kind https://kind.sigs.k8s.io/dl/v0.29.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

kind create cluster --config .devcontainer/kind-cluster.yml --wait 300s