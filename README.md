# AS-BUILT Marker

A lightweight Python utility for batch watermarking PDF drawings with an **“AS-BUILT”** stamp. Designed for construction, engineering, and design workflows where large sets of PDFs need consistent revision marking.

---

## Overview

This tool automatically scans the current folder for PDF files, applies a scalable diagonal watermark to each page, and exports the processed files into a dedicated output folder.

It is built to be simple, fast, and fully offline once packaged as an executable.

---

## Requirements (for development)

If running as a Python script:

    - Python 3.9+
    - pypdf
    - reportlab

Install dependencies:

    pip install pypdf reportlab

---

## Usage 

### (Python)

Place your PDF files in the same folder as the script, then run:

    python as-built-marker.py

### Windows (EXE)

Download the [latest release](https://github.com/Booth-Ashley/As-Built-Marker/releases) and place it in the same folder as your PDF files and run.

---

## Use Case

Ideal for:

- Construction as-built drawing sets  
- Engineering revision marking  
- Architectural PDF stamping  
- Batch document control workflows  

---

## License

MIT License
