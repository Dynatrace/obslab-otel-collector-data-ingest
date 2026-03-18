from utils import *

# IMPORTANT NOTE!
# Most of the capabilities of this container are actually defined as "features" in .devcontainer/devcontainer.json
# It's only those things that DO NOT have a "feature" that we need to "manually" install here!
# It is ALWAYS best to use a devcontainer.json feature over this custom logic
# You can find features here:
# - https://containers.dev/features

createKubernetesCluster()

# # Install RunMe
# RUNME_CLI_VERSION = "3.10.2"
# run_command(["mkdir", "runme_binary"])
# run_command(["wget", "-O", "runme_binary/runme_linux_x86_64.tar.gz", f"https://download.stateful.com/runme/{RUNME_CLI_VERSION}/runme_linux_x86_64.tar.gz"])
# run_command(["tar", "-xvf", "runme_binary/runme_linux_x86_64.tar.gz", "--directory", "runme_binary"])
# run_command(["mv", "runme_binary/runme", "/usr/local/bin"])
# run_command(["rm", "-rf", "runme_binary"])

# if CODESPACE_NAME.startswith("dttest-"):
#     # Set default repository for gh CLI
#     # Required for the e2e test harness
#     # If it needs to interact with GitHub (eg. create an issue for a failed e2e test)
#     run_command(["gh", "repo", "set-default", GITHUB_REPOSITORY])

#     # Now set up a label, used if / when the e2e test fails
#     # This may already be set (when demos are re-executed in repos)
#     # so catch error and always return true
#     # Otherwise the entire post-start.sh script could fail
#     # We can do this as we know we have permission to this repo
#     # (because we're the owner and testing it)
#     run_command(["gh", "label", "create", "e2e test failed", "--force"])
#     run_command(["pip", "install", "-r", f"/workspaces/{REPOSITORY_NAME}/.devcontainer/testing/requirements.txt", "--break-system-packages"])
#     run_command(["python",  f"/workspaces/{REPOSITORY_NAME}/.devcontainer/testing/testharness.py"])

#     # Testing finished. Destroy the codespace
#     run_command(["gh", "codespace", "delete", "--codespace", CODESPACE_NAME, "--force"])
# else:
#     print("done configuring environment")
#     #send_startup_ping(demo_name="obslab-otel-collector-data-ingest")