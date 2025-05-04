# Streaming AD Plots

**Repository for generating anomaly detection visualizations in streaming data**
A toolkit for creating standardized plots used in research and presentations about streaming anomaly detection in Python.

## 🚀 Purpose

This repository provides tools for generating consistent visualizations of time series data with anomalies, specifically designed for technical presentations and research. Key features:

* Unified plot styling through config files
* Support for multi-variate time series
* Flexible anomaly visualization

## 📂 Repository Structure

```
streaming-ad-plots/
├── config.json              # Visualization configuration
├── examples/                # Usage examples
│   ├── basic_usage.ipynb    
│   └── advanced_plots.ipynb 
├── plots/                   # Output directory
├── requirements.txt         
└── README.md   
```

## ⚙️ Quick Start

1. Clone the repository:

```bash
git clone https://github.com/onixlas/streaming-ad-plots.git
cd streaming-ad-plots
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🎨 Customization

All visualization parameters are controlled via `config.json`:

```json
{
  "visualization": {
    "colors": {
      "normal": "#2ecc71",
      "anomaly": "#e74c3c"
    },
    "output": {
      "format": "png",
      "dpi": 300
    }
  }
}
```

Configurable elements:
* Colors and marker styles
* Sizing and transparency
* Export settings

## 📜 License

CC0 1.0 Universal - Public Domain Dedication

### 🔧 Status: Active development