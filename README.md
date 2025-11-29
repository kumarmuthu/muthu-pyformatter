# muthu-pyformatter

[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)](https://github.com/kumarmuthu/muthu-pyformatter)
![GitHub License](https://img.shields.io/github/license/kumarmuthu/muthu-pyformatter?style=for-the-badge)
![GitHub Forks](https://img.shields.io/github/forks/kumarmuthu/muthu-pyformatter?style=for-the-badge)
![GitHub Stars](https://img.shields.io/github/stars/kumarmuthu/muthu-pyformatter?style=for-the-badge)
![GitHub Contributors](https://img.shields.io/github/contributors/kumarmuthu/muthu-pyformatter?style=for-the-badge)

[![Build Status](https://github.com/kumarmuthu/muthu-pyformatter/actions/workflows/python-app.yml/badge.svg)](https://github.com/kumarmuthu/muthu-pyformatter/actions/workflows/python-app.yml)
[![PyPI Version](https://img.shields.io/pypi/v/muthu-pyformatter?label=PyPI%20Version&color=brightgreen)](https://pypi.org/project/muthu-pyformatter/)
[![Test PyPI Version](https://img.shields.io/badge/dynamic/json?color=blue&label=Test%20PyPI&query=info.version&url=https://test.pypi.org/pypi/muthu-pyformatter/json&cacheSeconds=0)](https://test.pypi.org/project/muthu-pyformatter/)

![GitHub Image](https://avatars.githubusercontent.com/u/53684606?v=4&s=40)

---

A lightweight Python code-quality utility that checks PEP8 compliance using **pycodestyle** and auto-formats code using **autopep8**, enforcing a strict **120-character line limit**.

---

## ✨ Features

- ✔ Scans all Python files in any directory  
- ✔ Enforces **max line length = 120**  
- ✔ Automatically fixes code formatting using `autopep8`  
- ✔ Shows detailed style errors using `pycodestyle`  
- ✔ Supports custom `--path` argument (defaults to current directory)  
- ✔ Works on Windows, Linux, and macOS  

---

## 📦 Installation

### **1️⃣ Install via PyPI (recommended)**

```bash
pip install muthu-pyformatter
````

### **2️⃣ Clone the repository (optional / development)**

```bash
git clone https://github.com/kumarmuthu/muthu-pyformatter
cd muthu-pyformatter
```

---

## ▶️ Usage

### **CLI via PyPI**

Check and auto-format Python files in a directory:

```bash
muthu-pyformatter --path "C:\users\kumar\repo\"
```

or on Linux/macOS:

```bash
muthu-pyformatter --path ./src
```

### **Using Python module (Git clone / development)**

```bash
python -m muthu_pyformatter.formatter --path "C:\users\kumar\repo\"
```

or on Linux/macOS:

```bash
python3 -m muthu_pyformatter.formatter --path ./src
```

---

## 🧰 What the Script Does

### 1️⃣ Installs required tools (if missing)

* `pycodestyle`
* `autopep8`
* `colorama`

### 2️⃣ Runs `pycodestyle`

* Detects PEP8 violations
* Enforces 120-character limit
* Prints all issues

### 3️⃣ Runs `autopep8`

* Auto-formats Python files
* Fixes spacing, indentation, blank lines
* Recursively processes all `.py` files

### 4️⃣ Re-runs `pycodestyle` to validate fixes

---

## 📁 Script File Name

```
muthu_pyformatter/formatter.py
```

or via CLI after PyPI install:

```
muthu-pyformatter
```

---

## 📝 License

MIT License
Feel free to use, modify, and contribute.

---
