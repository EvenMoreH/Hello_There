FROM ubuntu:22.04

ARG RUNNER_VERSION=2.328.0

# Install required packages and dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      curl ca-certificates jq git sudo libicu70 libssl3 libkrb5-3 unzip \
      gnupg2 lsb-release apt-transport-https software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Install Docker CLI and Docker Compose plugin from Docker's official repository
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends docker-ce-cli docker-compose-plugin && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /actions-runner

# Download official runner files from GitHub releases
RUN curl -fsSLo actions-runner.tar.gz \
      "https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz" && \
    tar -xzf actions-runner.tar.gz && rm actions-runner.tar.gz

# Add entrypoint that configures and runs the runner
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create non-root user and work dir (runner will run as this user)
RUN useradd -m runner && mkdir -p /runner/_work && chown -R runner:runner /actions-runner /runner

USER runner
ENV RUNNER_WORK=/runner/_work

ENTRYPOINT ["/entrypoint.sh"]