# AS-BUILT Marker

A lightweight Python utility for batch watermarking PDF drawings with an **“AS-BUILT”** stamp. Designed for construction, engineering, and design workflows where large sets of PDFs need consistent revision marking.

<img width="1755" height="1241" alt="AS-BUILT" src="https://github.com/user-attachments/assets/7e9a5484-24ce-4c47-80d5-548fee442f2d" />


---

## Overview

This tool automatically scans the current folder for PDF files, applies a scalable diagonal watermark to each page, and exports the processed files into a dedicated output folder.

It is built to be simple, fast, and fully offline once packaged as an executable.

---

## Use Case

Ideal for:

- Construction as-built drawing sets  
- Engineering revision marking  
- Architectural PDF stamping  
- Batch document control workflows  

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

### Windows SmartScreen Warning

When running the executable for the first time, Windows may display a **Microsoft Defender SmartScreen** warning stating that the app is from an unknown publisher. This is expected because the executable is **not digitally signed** with a code-signing certificate. These certificates are very expensive.

This does **not** necessarily indicate that the application is malicious—it simply means Windows cannot verify the publisher's identity or reputation. If you downloaded the executable from this official GitHub release and trust the source, you can click **More info** and then **Run anyway** to launch the application.

If you prefer, you can also review the source code and build the application yourself.

---

## License

MIT License
