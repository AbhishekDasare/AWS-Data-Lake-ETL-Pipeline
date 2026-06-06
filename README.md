# AWS-Data-Lake-ETL-Pipeline

## Overview

This project demonstrates an end-to-end AWS Data Lake ETL Pipeline for processing customer and sales data. The pipeline ingests raw data into Amazon S3, performs transformations using AWS Glue and PySpark, and loads curated datasets into Amazon Redshift for analytics and reporting.

## Technology Stack

- AWS S3
- AWS Glue
- AWS Lambda
- Amazon Redshift
- PySpark
- Apache Spark
- Python
- SQL
- Data Lake Architecture


## Data Flow

1. Source files are uploaded to Amazon S3.
2. AWS Glue Crawler updates the Data Catalog.
3. AWS Glue ETL Job transforms the raw data.
4. Curated data is stored back into Amazon S3.
5. Amazon Redshift loads transformed data.
6. BI tools generate dashboards and reports.


## Key Features

- Automated ETL Pipeline
- Serverless Data Processing
- Scalable Data Lake Architecture
- Metadata Management
- Data Transformation using PySpark
- Data Warehousing with Redshift


## Business Benefits

- Centralized Data Storage
- Faster Analytics
- Reduced Processing Time
- Improved Data Governance
- Scalable Cloud Architecture


## Future Enhancements

- Delta Lake Integration
- Real-Time Data Streaming
- AWS Step Functions
- Data Quality Monitoring
