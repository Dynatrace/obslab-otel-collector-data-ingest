---
# Runme needs this so that it navigates up one dir to teh root
# to search properly for files.
cwd: ..
---

--8<-- "snippets/tenant-id.md"
--8<-- "snippets/bizevent-getting-started.js"

### Gather Details: Create API Token

In Dynatrace:

* Press `ctrl + k`. Search for `access tokens`.
* Create a new access token with the following permissions:
    * `metrics.ingest`
    * `logs.ingest`
    * `openTelemetryTrace.ingest`

--8<-- "snippets/info-required.md"

## Start Demo

=== "Run in Cloud"
    --8<-- "snippets/codespace-details-warning-box.md"

    Click this button to launch the demo in a new tab.

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/dynatrace/obslab-otel-collector-data-ingest){target=_blank}

=== "Run Locally"
    * Clone the repository to your local machine

    ```
    git clone https://github.com/dynatrace/obslab-otel-collector-data-ingest
    ```

    * Open the folder in Visual Studio code
    * Create a file called `.env` and populate it with your details like the following sample:

    ```
    export DT_ENVIRONMENT_ID=abc12345
    export DT_ENVIRONMENT_TYPE=live
    export DT_API_TOKEN=dt0c01.******.***********
    ```
    
    (optional: if using Podman) Run the following to symlink podman to docker so that `docker ps` works:

    ```
    # Create a symlink to a false docker process
    # Restart vscode
    sudo ln -s $(command -v podman) /usr/local/bin/docker
    ```

    Restart vscode (to reload the terminal) and `docker ps` should work.

    * Create the environment:

    ```
    podman machine init
    podman machine set --rootful=true
    podman machine set --memory 6000
    podman machine start
    ```

    * Go to the "Remote Explorer" icon in the left menu bar (the computer sceen with the little circle), then click the blue "Open Folder in Container" button.

    The container will build. You should see: `Connecting to Dev Container (show log)`. Click this to watch the installation log.
    
    It will take some time as it downloads the `ubuntu:noble` base image + all required tools.

    When it is complete, you should see some log output like this:

    ```
    2026-03-18 03:50:58.123 | INFO     | utils:createKubernetesCluster:490 - Kind cluster creation completed.
    Running the postAttachCommand from devcontainer.json...

    [47919 ms] Start: Run in container: /bin/sh -c python on_attach.py
    2026-03-18 03:50:59.088 | INFO     | utils:configureClusterConnection:419 - Container ID (hostname): b'8e43c3cc6746'
    2026-03-18 03:50:59.088 | INFO     | utils:configureClusterConnection:425 - Starting obslab-otel-collector-data-ingest-cluster-control-plane in case it is stopped...
    obslab-otel-collector-data-ingest-cluster-control-plane
    2026-03-18 03:50:59.130 | INFO     | utils:configureClusterConnection:433 - Connecting container b'8e43c3cc6746' to Docker network obslab-otel-collector-data-ingest-cluster (if not already connected)...
    2026-03-18 03:50:59.194 | INFO     | utils:configureClusterConnection:436 - Connected to 'obslab-otel-collector-data-ingest-cluster' network.
    2026-03-18 03:50:59.195 | INFO     | utils:configureClusterConnection:445 - Inspecting 'obslab-otel-collector-data-ingest-cluster-control-plane' container to find IP on 'obslab-otel-collector-data-ingest-cluster' network...
    2026-03-18 03:50:59.210 | INFO     | utils:configureClusterConnection:458 - Found obslab-otel-collector-data-ingest-cluster-control-plane IP on 'kind' network: 10.89.0.7
    2026-03-18 03:50:59.210 | INFO     | utils:configureClusterConnection:466 - Updating kubeconfig cluster 'kind-obslab-otel-collector-data-ingest-cluster' to use API server https://10.89.0.7:6443 ...
    Cluster "kind-obslab-otel-collector-data-ingest-cluster" set.
    2026-03-18 03:50:59.299 | INFO     | utils:configureClusterConnection:468 - kubeconfig updated.
    Done. Press any key to close the terminal.
    ```
    
    Do as it suggests and press a key. A new terminal should start that looks like this:

    ```
    root@a1925c1cf511:/workspaces/obslab-otel-collector-data-ingest#
    ```

You will now have an empty Kubernetes cluster. Test it by running `kubectl get nodes` which should work:

```
# kubectl get nodes
NAME                                                      STATUS   ROLES           AGE     VERSION
obslab-otel-collector-data-ingest-cluster-control-plane   Ready    control-plane   2m19s   v1.35.1
```

It is time to install the applications.

<div class="grid cards" markdown>
- [Click Here to Install Components :octicons-arrow-right-24:](install-opentelemetry-components.md)
</div>