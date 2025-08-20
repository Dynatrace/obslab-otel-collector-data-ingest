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
    * Ensure the [Microsoft Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers){target=_blank} and [Dev Containers CLI](https://code.visualstudio.com/docs/devcontainers/devcontainer-cli#_installation){target=_blank} are installed in VSCode
    * Open a new terminal in VSCode and set your environment variables as appropriate:

    ```
    set DT_ENVIRONMENT_ID=abc12345
    set DT_ENVIRONMENT_TYPE=live
    set DT_API_TOKEN=dt0c01.******.***********
    ```

    * Start Docker / Podman
    * Create the environment

    ```
    devcontainer up
    ```

    It will take a few moments but you should see:

    ```
    {"outcome":"success","containerId":"...","remoteUser":"root","remoteWorkspaceFolder":"/workspaces/obslab-k6"}
    ```

    * Connect to the demo environment. This will launch a new Visual Studio Code window
    ```
    devcontainer open
    ```

    In the new Visual Studio code window, open a new terminal and continue with the tutorial.

You will now have an empty Kubernetes cluster. It is time to install the applications.

<div class="grid cards" markdown>
- [Click Here to Install Components :octicons-arrow-right-24:](install-opentelemetry-components.md)
</div>