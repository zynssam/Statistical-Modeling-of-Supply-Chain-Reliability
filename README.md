# Statistical Modeling of Supply Chain Reliability

A small Python project for simulating, processing, and visualizing logistics data to study supply chain reliability and variance.

## Overview

This project provides tools to:

- Generate synthetic logistics/supply chain data
- Process and transform that data through a lightweight SQL-based pipeline
- Visualize variance and reliability metrics to surface patterns in delivery performance

## Contents

```
.
├── main.py                        # Project entry point with example workflows
├── requirements.txt                # Python dependencies
├── logistics_raw_data.csv          # Example/raw dataset used by the scripts
└── src/
    ├── generate_logistics_data.py  # Synthetic data generator
    ├── sql_pipeline.py             # SQL-based transform/load pipeline helpers
    └── visual_variance.py          # Variance and reliability visualizations
```

## Prerequisites

- Python 3.10+
- pip

## Setup

1. Clone the repository and navigate into it:

   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS / Linux
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script for a quick demonstration of the full workflow:

```bash
python main.py
```

### Generate synthetic data

```bash
python -m src.generate_logistics_data
```

### Run the SQL pipeline

The transform/load functions live in `src/sql_pipeline.py` and are meant to be imported and called from a script or REPL:

```python
from src.sql_pipeline import run_pipeline

run_pipeline("logistics_raw_data.csv")
```

### Produce visualizations

```bash
python -m src.visual_variance
```

## Data

Place your CSV datasets in the repository root, or point the scripts to a custom path. `logistics_raw_data.csv` is included as a starting example — adjust column names and preprocessing steps in `src/generate_logistics_data.py` or `src/sql_pipeline.py` to match your own data.

## Project Structure and Notes

- `main.py` demonstrates typical workflows — open it to see usage examples and function calls.
- The modules in `src/` are intentionally small and are designed to be imported into analysis notebooks or standalone scripts.
- If you connect the SQL pipeline to a live database, configure connection settings in your own calling script — no credentials or connection strings are committed to this repository.
