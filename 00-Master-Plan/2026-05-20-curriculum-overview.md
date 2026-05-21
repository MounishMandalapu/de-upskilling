# 🗺️ Data Engineering Upskilling — Master Curriculum
**Student:** Mounish | **Started:** May 20, 2026
**Study Schedule:** 10pm – 4am EST daily (6 hours/session)
**Standard:** Production-grade. Everything you build here reflects how real companies run data at scale.

---

## ⚠️ The Production-First Mandate

Most DE tutorials teach you to build a pipeline that works once on your laptop. That is NOT what this curriculum does.

A real data engineer at a company is responsible for:
- Pipelines that run **reliably at 3am without anyone watching**
- Data that is **trusted** — your stakeholders bet business decisions on it
- Systems that handle **billions of rows**, not thousands
- Code that **other engineers can read, test, and modify**
- Infrastructure that can be **torn down and rebuilt in minutes** (not days)
- Pipelines that **alert you before the business notices** something is wrong
- Deployments that go through **CI/CD**, not manual clicks

Every session in this curriculum applies that standard. You will not be building toy pipelines. You will be building the kind of systems that would pass a code review at a real company.

---

## How the Full Production Stack Interlocks

```
┌─────────────────────────────────────────────────────────────────┐
│                    INFRASTRUCTURE LAYER                         │
│  Terraform (IaC) — provision EVERYTHING as code                 │
│  Docker + Kubernetes — run services reliably, anywhere          │
│  GitHub + GitHub Actions (CI/CD) — test & deploy automatically  │
└───────────────────────────┬─────────────────────────────────────┘
                            │ provisions & deploys
                            ▼
┌──────────────┐    ┌──────────────────┐    ┌──────────────────────┐
│  INGESTION   │    │   EVENT STREAM   │    │   BATCH INGESTION    │
│  Airbyte /   │    │   Apache Kafka   │    │   Python scripts /   │
│  custom APIs │    │   (real-time)    │    │   Singer / Fivetran  │
└──────┬───────┘    └────────┬─────────┘    └──────────┬───────────┘
       │                     │                          │
       └─────────────────────┼──────────────────────────┘
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      STORAGE LAYER                              │
│  AWS S3 / GCS  — raw data lake                                  │
│  Delta Lake / Apache Iceberg — table format (ACID, time travel) │
│  Schema Registry (Avro/Protobuf) — data contracts enforced      │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PROCESSING LAYER                             │
│  Apache Spark / PySpark — batch, large-scale transformations    │
│  Apache Flink / Spark Streaming — real-time stream processing   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    WAREHOUSE LAYER                              │
│  Snowflake or BigQuery — analytics-optimized, petabyte-scale    │
│  Partitioning + Clustering — query cost & speed optimization    │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  TRANSFORMATION LAYER                           │
│  dbt — SQL models, tests, docs, lineage, incremental loads      │
│  Great Expectations / Soda Core — data quality validation       │
│  Data Contracts — schema agreements between producer/consumer   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  ORCHESTRATION LAYER                            │
│  Apache Airflow — DAGs, scheduling, retries, SLA monitoring     │
│  Multi-environment: dev → staging → prod promotion              │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   CONSUMPTION LAYER                             │
│  BI tools (Looker, Metabase, Tableau), ML pipelines, APIs       │
└─────────────────────────────────────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OBSERVABILITY (runs across every layer)
  Prometheus + Grafana — pipeline metrics & dashboards
  dbt tests + Great Expectations — data quality gates
  Airflow SLA alerts — pipeline latency monitoring
  PagerDuty / Slack alerts — incident response
  Data lineage (dbt, OpenLineage) — trace data from source to BI

SECURITY & GOVERNANCE (runs across every layer)
  IAM (roles, least-privilege access)
  PII detection and masking
  Secrets management (AWS Secrets Manager / GCP Secret Manager)
  Data governance (ownership, retention policies, access logs)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## Curriculum Phases

### PHASE 1 — Foundations (Weeks 1–3)
*Every concept is taught at production scale from day one*

| Week | Topic | Production Angle |
|------|-------|-----------------|
| 1 | Python for DE | Write production-quality Python: type hints, logging, error handling, retries, unit tests — not scripts that crash silently |
| 2 | SQL Advanced | Query optimization for billion-row tables, partitioned queries, explain plans, warehouse cost implications |
| 3 | Linux/Bash + Docker + Git | Multi-stage Dockerfiles, docker-compose for local dev environments, Git branching strategy used in real teams (Gitflow) |

**Milestone:** Python ingestion script with full error handling, retry logic, logging, and a unit test suite. Runs in Docker. Lives on GitHub with a proper README.

---

### PHASE 2 — Core Production DE Stack (Weeks 4–9)
*Industry tools used the way they're used in real companies*

| Week | Topic | Production Angle |
|------|-------|-----------------|
| 4 | Data Modeling | Slowly Changing Dimensions in production, modeling for query performance, working with data contracts |
| 5 | Cloud + Warehouse (GCP/BigQuery) | IAM roles, cost monitoring, partitioning/clustering strategies, multi-environment setup (dev/staging/prod) |
| 6 | dbt — Core | Models with tests at every layer, documentation that auto-generates, CI checks that block bad data from reaching prod |
| 7 | dbt — Production | Incremental models on billion-row tables, snapshots for SCD Type 2, dbt Cloud CI/CD integration, alerting on test failures |
| 8 | Apache Airflow | Production DAG patterns, SLA monitoring, XCom for passing metadata (not data), dynamic DAGs, alerting on failure |
| 9 | Apache Spark + PySpark | Spark on a real cluster (Dataproc/EMR), performance tuning, handling data skew, reading/writing Parquet at scale |

**Milestone:** A dbt + Airflow + BigQuery pipeline that: ingests real public data, applies transformations with tests, deploys via GitHub Actions CI/CD, and sends a Slack alert if an SLA is missed.

---

### PHASE 3 — Streaming, Lakehouse & Observability (Weeks 10–13)
*The skills most DE candidates are weak on — your differentiator*

| Week | Topic | Production Angle |
|------|-------|-----------------|
| 10 | Apache Kafka — Core | Kafka in production: replication factor, ISR, consumer lag monitoring, dead-letter queues |
| 11 | Kafka — Advanced | Schema Registry with Avro (data contracts enforced at the wire), Kafka Connect for source/sink connectors |
| 12 | Stream Processing | Exactly-once semantics (why it's hard), stateful processing, windowing strategies, Spark Streaming vs Flink tradeoffs |
| 13 | Data Lakehouse + Observability | Medallion architecture in Delta Lake, time travel, schema evolution, Great Expectations for data quality, OpenLineage for lineage tracking |

**Milestone:** A Kafka → Spark Streaming → Delta Lake pipeline with: schema enforcement via Avro, consumer lag dashboard in Grafana, dead-letter queue for bad events, and automated data quality checks.

---

### PHASE 4 — Infrastructure, Security & CI/CD (Week 14)
*Most DE courses skip this entirely. Real engineers live here.*

| Days | Topic | Production Angle |
|------|-------|-----------------|
| Days 92–98 | Terraform (IaC) | Provision GCS buckets, BigQuery datasets, Airflow environments, Kafka clusters — all as version-controlled code |
| Days 99–101 | CI/CD for Data Pipelines | GitHub Actions workflows: run dbt tests on PR, validate Airflow DAGs, deploy to staging before prod |
| Days 102–105 | Security & Governance | IAM least-privilege design, PII masking with dbt macros, secrets in Secret Manager (never in code), data access audit logs |
| Days 106–108 | Cost Optimization | BigQuery slot reservation vs on-demand, Spark cluster right-sizing, Airflow executor tuning, warehouse query cost analysis |

**Milestone:** Your entire cloud infrastructure for the portfolio projects is provisioned with Terraform. Destroyed and rebuilt in under 10 minutes.

---

### PHASE 5 — Production Portfolio Projects (Weeks 15–20)
*Three projects that prove you can work in a real data platform*

#### Project 1 — Production Batch Data Platform (Weeks 15–17)
**What it does:** Ingests real public data (e.g. NYC taxi trips, GitHub events, or a stock market API), runs through a full ELT pipeline, and serves a BI dashboard.

**Production requirements:**
- [ ] Infrastructure provisioned with Terraform (GCS + BigQuery + Cloud Composer)
- [ ] Data ingested to raw layer (Bronze) with schema validation
- [ ] dbt models for Silver and Gold layers with 100% test coverage
- [ ] Airflow DAG with SLA alerts, Slack failure notifications, and retry logic
- [ ] CI/CD: GitHub Actions runs dbt tests on every PR, blocks merge on failure
- [ ] Data quality checks with Great Expectations before Gold layer promotion
- [ ] Data lineage documented (dbt docs site deployed)
- [ ] Cost-optimized: BigQuery tables partitioned + clustered
- [ ] Multi-environment: dev and prod environments with separate GCP projects
- [ ] README with architecture diagram, setup guide, and data dictionary

#### Project 2 — Real-Time Streaming Pipeline (Weeks 18–19)
**What it does:** Streams real events (e.g. Wikipedia edit stream, a financial market feed, or a simulated IoT sensor stream) and processes them in near-real-time.

**Production requirements:**
- [ ] Kafka cluster (on Confluent Cloud free tier or self-hosted on GCP VM)
- [ ] Schema Registry enforcing Avro schemas (data contracts)
- [ ] Dead-letter queue for malformed events with alerting
- [ ] Spark Streaming consumer writing to Delta Lake medallion layers
- [ ] Consumer lag dashboard in Grafana
- [ ] Exactly-once delivery semantics implemented and documented
- [ ] Automated data quality assertion on each micro-batch
- [ ] Terraform for all infrastructure
- [ ] GitHub Actions CI/CD
- [ ] README with system design diagram explaining every trade-off made

#### Project 3 — Open Source Contribution or Real Client Work (Week 20)
**Why:** Portfolio projects are good. A merged pull request to Apache Airflow, dbt, or Great Expectations is better. Or a real pipeline built for a small business, non-profit, or open dataset project.

**Options:**
- Contribute a bug fix or feature to an open-source DE tool
- Build a pipeline for a real organization (non-profit data, local business)
- Write a detailed technical blog post walking through Project 1 or 2

---

## Full Tool Inventory

| Category | Tool | Production Use | Priority |
|----------|------|---------------|----------|
| Language | Python 3.12 | Pipeline code, Airflow DAGs, Spark jobs, tests | ⭐ Essential |
| Language | SQL | dbt models, warehouse queries, optimization | ⭐ Essential |
| Warehouse | BigQuery | Primary warehouse — petabyte-scale analytics | ⭐ Essential |
| Warehouse | Snowflake | Secondary — many companies use this | ⭐ Essential |
| Transform | dbt Core | SQL transformation, testing, documentation | ⭐ Essential |
| Orchestrate | Apache Airflow | Schedule, monitor, alert on all pipelines | ⭐ Essential |
| Processing | Apache Spark / PySpark | Distributed large-scale batch processing | ⭐ Essential |
| Streaming | Apache Kafka | Real-time event streaming | ⭐ Essential |
| Streaming | Apache Flink | Stateful stream processing at scale | 🔶 Important |
| Storage | AWS S3 / GCS | Raw data lake storage | ⭐ Essential |
| Lakehouse | Delta Lake | ACID transactions on data lake | ⭐ Essential |
| Lakehouse | Apache Iceberg | Table format — used at Netflix, Apple, LinkedIn | 🔶 Important |
| Contracts | Avro + Schema Registry | Enforce schemas between Kafka producers/consumers | 🔶 Important |
| Quality | Great Expectations | Automated data validation at every pipeline stage | 🔶 Important |
| Quality | dbt tests | In-warehouse data assertions | ⭐ Essential |
| IaC | Terraform | Provision all cloud resources as version-controlled code | 🔶 Important |
| CI/CD | GitHub Actions | Automated testing and deployment pipeline for data | 🔶 Important |
| Container | Docker | Local dev environments, reproducible builds | ⭐ Essential |
| Container | Kubernetes | Run Airflow, Spark, Kafka at scale in production | 🔷 Advanced |
| Monitoring | Prometheus + Grafana | Pipeline metrics, consumer lag, SLA dashboards | 🔶 Important |
| Lineage | OpenLineage / dbt docs | Track data from source to BI, impact analysis | 🔶 Important |
| Cloud | GCP | Primary cloud platform | ⭐ Essential |
| Cloud | AWS | Secondary — most companies also use | 🔶 Important |
| Governance | IAM + Secret Manager | Access control, secrets management | ⭐ Essential |
| Version Control | Git + GitHub | Everything lives here | ⭐ Essential |

---

## Production Principles (Applied Every Session)

1. **Never hardcode credentials.** Use environment variables or a secrets manager.
2. **Every pipeline needs a failure path.** What happens when the source is down? Handle it.
3. **Test your data, not just your code.** dbt tests and Great Expectations run before every promotion.
4. **Infrastructure is code.** If you can't rebuild it from scratch with one command, it's fragile.
5. **Idempotency is non-negotiable.** Running a pipeline twice should produce the same result as running it once.
6. **Monitor everything.** If it's in production and there's no alert, it will fail silently.
7. **Partitioning is not optional.** Unpartitioned tables at scale cost money and time.
8. **Code review standard.** Everything you write should be readable and mergeable by another engineer.
9. **Document as you build.** Lineage, data dictionaries, and runbooks are part of the deliverable.
10. **Multi-environment by default.** Your pipeline has a dev and prod version from day one.

---

## Study Strategy (6 hrs/night)

| Time Block | Activity |
|------------|----------|
| 10:00–10:30 PM | Review morning briefing + set tonight's concrete goal |
| 10:30 PM–1:00 AM | Core learning — concept + production context + hands-on coding |
| 1:00–1:15 AM | Break |
| 1:15–3:00 AM | Build: apply the concept to a real, production-standard exercise |
| 3:00–3:30 AM | Document: write notes, commit to GitHub, update checklist |
| 3:30–4:00 AM | End-of-session quiz + brief review of missed answers |

---

## Certification Path

1. **dbt Fundamentals** (free) — target during Week 6
2. **Google Professional Data Engineer** — target after Phase 3
3. **Databricks Certified Associate Developer for Apache Spark** — target after Week 9
4. **Confluent Certified Developer for Apache Kafka** — target after Week 11

---

*Generated: 2026-05-20 | Standard: Production-Grade Real-World DE | Last updated: 2026-05-20*
