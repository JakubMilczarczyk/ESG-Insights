# ESG Insights: Scoring Tracker and Enrichment Pipeline 🇪🇺

**Project Goal:**  
Design a modern, scalable data pipeline that collects and enriches ESG scores of companies using both official sources and alternative data — such as corporate reports, news articles, and regulatory updates — to monitor ESG score shifts and identify their potential drivers.

---

## 📦 Architecture & Tech Stack

- **Cloud:** AWS (S3, Lambda, ECS/EKS, CloudWatch)
- **Data Ingestion:** Apache Kafka, Apache Airflow
- **Data Processing:** Apache Spark
- **Containerization:** Docker
- **Programming Language:** Python
- **Version Control:** Git
- **(Later stages):** NLP / AI (text classification, NER, LLMs)
- **Project Type:** Public educational project, potentially extendable to MVP SaaS

---

## 📁 Directory Structure

esg-insights/ ├── dags/ # Airflow DAGs ├── data/ │ ├── raw/ # Raw ESG data from APIs │ ├── processed/ # Enriched and processed ESG data │ └── samples/ # Sample JSON / CSV files ├── docker/ # Dockerfiles and docker-compose config ├── notebooks/ # EDA and analysis notebooks ├── scripts/ # ETL, ingestion, enrichment scripts ├── tests/ # Unit and integration tests ├── README.md └── requirements.txt

---

## 🛤️ Project Roadmap

### ✅ Stage 0: **Base ESG Score Dataset**
- [x] Select target companies (e.g. DAX index)
- [x] Retrieve ESG scores via public APIs (e.g. yfinance, ESG Book)
- [x] Store base scores in `.json` and `.csv` formats
- [x] Upload example data in `data/samples/`

### 🔜 Stage 1: **Data Enrichment (Alt Data)**
- [ ] Crawl and collect reports, press releases, news articles
- [ ] Parse and clean unstructured data
- [ ] Classify ESG-related text impact using NLP (later)

### 🔜 Stage 2: **Streaming & Monitoring**
- [ ] Use Kafka to stream articles or company updates
- [ ] Use Spark Streaming to process incoming texts
- [ ] Store enriched data into S3 (partitioned by time/company)

### 🔜 Stage 3: **Orchestration and Automation**
- [ ] Define Airflow DAGs for scheduled ETL & enrichment
- [ ] Containerize everything with Docker
- [ ] Set up monitoring and alerting

### 🔜 Stage 4: **Visualization & API**
- [ ] Build lightweight dashboard (e.g. Streamlit)
- [ ] Expose enriched ESG data through a REST API
- [ ] Enable data exports for external use (CSV/JSON/UI)

---

## 📄 Sample Data

### `data/samples/esg_sample.json`

```json
{
  "company": "Siemens AG",
  "ticker": "SIE.DE",
  "industry": "Industrials",
  "esg_score": {
    "environment": 61,
    "social": 54,
    "governance": 72,
    "total": 62
  },
  "controversy_level": 2,
  "source": "yfinance",
  "retrieved_at": "2025-04-13"
}
data/samples/esg_sample.csv
```
```csv

company,ticker,industry,environment_score,social_score,governance_score,total_score,controversy_level,source,retrieved_at
Siemens AG,SIE.DE,Industrials,61,54,72,62,2,yfinance,2025-04-13
```

🎯 Key Goals

Demonstrate strategic and technical skills as a Data Engineer

Combine structured ESG data with unstructured alternative signals

Train lightweight AI/NLP models to detect ESG-related events

Make the pipeline extensible, production-ready, and cloud-native

Enable future SaaS product or enterprise-level PoC for ESG intelligence

❗ License and Terms of Use
This project is protected by a proprietary license.
It is provided strictly for demonstration and educational purposes.

All rights reserved.
Commercial use, redistribution, or code modification is not allowed without the author's explicit permission.
Any unauthorized use of the contents or ideas in this repository is strictly prohibited.

🤝 Contributions & Contact
This is a public learning project.
Feedback, issues, and ideas are welcome via GitHub issues.

If you're a recruiter, engineer, or founder and want to discuss the idea — feel free to reach out!
