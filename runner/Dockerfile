FROM ubuntu:22.04

ARG RUNNER_VERSION=2.328.0

# Install required packages, docker CLI and docker compose plugin
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      curl ca-certificates jq git sudo libicu70 libssl3 libkrb5-3 unzip ca-certificates gnupg2 lsb-release && \
    rm -rf /var/lib/apt/lists/*

# Install Docker CLI (from distro) and Docker Compose plugin (compose v2)
RUN apt-get update && \
    apt-get install -y --no-install-recommends docker.io docker-compose-plugin && \
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