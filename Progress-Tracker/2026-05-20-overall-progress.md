# 📊 Overall Progress Tracker
**Student:** Mounish | **Target:** Data Engineer (Job-Ready)

---

## Phase Progress

| Phase | Status | Weeks | Completion |
|-------|--------|-------|------------|
| Phase 1 — Foundations | 🔵 In Progress | 1–3 | 0% |
| Phase 2 — Core DE Stack | ⬜ Not Started | 4–8 | 0% |
| Phase 3 — Streaming & Advanced | ⬜ Not Started | 9–11 | 0% |
| Phase 4 — Portfolio Projects | ⬜ Not Started | 12–16 | 0% |

---

## Daily Session Log

| Date | Day # | Topic | Quiz Score | Status |
|------|-------|-------|------------|--------|
| 2026-05-20 | Day 1 | DE Landscape + Best Strategies | 9/10 ⭐ | ✅ Complete |

---

## Concepts Mastered Checklist

### Phase 1 — Foundations
**Python**
- [ ] Data types, control flow, functions
- [ ] OOP — classes, inheritance, magic methods
- [ ] File I/O — reading/writing CSV, JSON, Parquet
- [ ] Working with APIs (requests library)
- [ ] pandas — DataFrames, groupby, merge, apply
- [ ] numpy — arrays, vectorized operations
- [ ] Generators and iterators
- [ ] Decorators and context managers
- [ ] Error handling and logging
- [ ] Virtual environments and dependency management

**SQL**
- [ ] SELECT, WHERE, GROUP BY, HAVING, ORDER BY
- [ ] JOINs (INNER, LEFT, RIGHT, FULL, CROSS, SELF)
- [ ] Subqueries and correlated subqueries
- [ ] CTEs (Common Table Expressions)
- [ ] Window functions (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER)
- [ ] Query optimization and indexing
- [ ] Transactions and ACID properties
- [ ] Stored procedures and views

**Linux / Bash / Git**
- [ ] File system navigation
- [ ] Shell scripting basics
- [ ] cron jobs
- [ ] Git init, add, commit, push, pull
- [ ] Branching and merging
- [ ] Docker — images, containers, volumes, compose

### Phase 2 — Core DE Stack
**Data Modeling**
- [ ] OLTP vs OLAP
- [ ] Star schema vs snowflake schema
- [ ] Fact and dimension tables
- [ ] Slowly Changing Dimensions (SCDs)
- [ ] Kimball methodology

**Cloud & Data Warehouse**
- [ ] Cloud platform basics (GCP or AWS)
- [ ] Object storage (S3 or GCS)
- [ ] BigQuery or Snowflake setup
- [ ] Loading data into warehouse
- [ ] Warehouse optimization (partitioning, clustering)

**dbt**
- [ ] dbt project structure
- [ ] Models — staging, intermediate, mart
- [ ] Tests — generic and singular
- [ ] Documentation and lineage
- [ ] Incremental models
- [ ] Seeds and sources

**Apache Airflow**
- [ ] DAGs and task dependencies
- [ ] Operators (Python, Bash, SQL)
- [ ] Scheduling with cron
- [ ] XComs — passing data between tasks
- [ ] Connections and hooks
- [ ] Monitoring and retries

**Apache Spark / PySpark**
- [ ] Spark architecture (driver, executor, cluster manager)
- [ ] RDDs vs DataFrames vs Datasets
- [ ] Spark SQL
- [ ] Transformations vs actions
- [ ] Partitioning and shuffling
- [ ] Reading/writing Parquet, CSV, JSON
- [ ] Spark optimization

### Phase 3 — Streaming
**Apache Kafka**
- [ ] Topics, partitions, offsets
- [ ] Producers and consumers
- [ ] Consumer groups
- [ ] Kafka Connect
- [ ] Schema Registry and Avro

**Stream Processing**
- [ ] Spark Streaming fundamentals
- [ ] Windowing operations
- [ ] Stateful processing
- [ ] Exactly-once semantics

**Data Lakehouse**
- [ ] Medallion architecture (Bronze/Silver/Gold)
- [ ] Delta Lake basics
- [ ] Apache Iceberg
- [ ] Time travel and versioning

### Phase 4 — Infrastructure, Security & CI/CD
**Terraform / IaC**
- [ ] Provision GCS bucket and BigQuery dataset with Terraform
- [ ] Provision Cloud Composer (managed Airflow) with Terraform
- [ ] Terraform state management (remote backend in GCS)
- [ ] Destroy and rebuild entire cloud setup in under 10 minutes

**CI/CD for Data**
- [ ] GitHub Actions workflow that runs dbt tests on every PR
- [ ] GitHub Actions workflow that validates Airflow DAG integrity
- [ ] Automated deployment to staging before prod promotion
- [ ] Branch protection rules: no merge without tests passing

**Security & Governance**
- [ ] IAM roles with least-privilege principle applied
- [ ] Secrets in Secret Manager — zero credentials in code
- [ ] PII column masking with dbt macros
- [ ] Data access audit logging enabled

**Cost Optimization**
- [ ] BigQuery tables partitioned and clustered appropriately
- [ ] Query cost analysis with INFORMATION_SCHEMA
- [ ] Spark cluster right-sizing for a real workload
- [ ] Airflow executor tuning (LocalExecutor vs CeleryExecutor trade-offs)

### Phase 5 — Portfolio
**Project 1: Production Batch Data Platform**
- [ ] Terraform provisions all infrastructure
- [ ] dbt models with 100% test coverage
- [ ] Airflow DAG with SLA alerts + Slack notifications
- [ ] Great Expectations data quality checks
- [ ] GitHub Actions CI/CD (tests run on every PR)
- [ ] Multi-environment (dev + prod)
- [ ] dbt docs site deployed with full lineage
- [ ] README with architecture diagram + data dictionary

**Project 2: Real-Time Streaming Pipeline**
- [ ] Kafka cluster with Schema Registry (Avro contracts)
- [ ] Dead-letter queue for bad events with alerting
- [ ] Spark Streaming writing to Delta Lake (medallion architecture)
- [ ] Consumer lag dashboard in Grafana
- [ ] Exactly-once semantics implemented
- [ ] Automated data quality assertions per micro-batch
- [ ] Terraform + CI/CD
- [ ] README with system design diagram + trade-off documentation

**Project 3: Open Source Contribution / Real-World Work**
- [ ] PR submitted to an open-source DE project
- [ ] OR pipeline built for a real organization with documented impact

**Career**
- [ ] LinkedIn profile updated with DE skills + project links
- [ ] Resume updated (quantified impact, not just tool names)
- [ ] GitHub contribution graph is green (daily commits)
- [ ] dbt Fundamentals certification
- [ ] Google Professional Data Engineer or AWS Certified Data Engineer
- [ ] Databricks Spark certification (optional but strong)

---

## GitHub Contribution Tracker
| Week | Commits | Repos Created |
|------|---------|---------------|
| Week 1 | 0 | 0 |

---

*Updated automatically after each session*
