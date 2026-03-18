# SV API Performance Analyzer

## Overview
Enterprise-grade API performance testing and analysis system.

## Features
- Load testing using Locust
- API simulation using FastAPI
- Performance analytics with Pandas
- Graph generation

## Run API
uvicorn app.main:app --reload

## Run Load Test
locust -f load_tests/locustfile.py

## Analyze Results
python analysis/analyzer.py <csv_file>
