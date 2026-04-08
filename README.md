# Distributed Database Performance & Chaos Testing Framework
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-supported-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Project Overview
This repository contains a lightweight, containerized automation framework designed to validate the **performance, consistency, and resilience** of distributed database systems. 

Originally built to simulate OLAP workloads, this framework automates the setup of a multi-node environment using **Docker**, executes analytical SQL stress tests via **Python (Pytest)**, and introduces **Chaos Engineering** principles to test system recovery.

## 🚀 Key Features
* **Automated Infrastructure:** One-command deployment of database clusters using Docker Compose.
* **Performance Benchmarking:** Python-based suite to measure query latency (P99 metrics) and data ingestion throughput.
* **Resilience Testing:** Integrated chaos scripts to simulate node failures and network partitions.
* **Validation Logic:** Automated C++ source code validation hooks (simulated) to ensure data integrity across shards.

## 🛠 Tech Stack
* **Languages:** Python (Pytest, Pandas), SQL, Bash.
* **Infrastructure:** Docker, Docker Compose, Linux CLI.
* **Focus Areas:** Distributed Systems, OLAP Internals, Release Engineering.

## 📂 Project Structure
```bash
.
├── docker-compose.yml     # Defines the distributed DB cluster
├── tests/
│   ├── test_performance.py # Benchmarking and latency logic
│   └── test_resilience.py  # Chaos engineering/Node failure tests
├── scripts/
│   └── setup_db.sh        # Shell scripts for environment config
├── requirements.txt       # Python dependencies
└── README.md
