# fixer-demo

A demonstration Python package for learning how to structure, package, and publish a Python library using `setup.py`.

---

## 📦 What This Project Does

This project introduces the foundational concepts of Python packaging and demonstrates:

- How to write a valid `setup.py`
- How to create a distributable `.tar.gz` file
- How to test the package installation in a clean virtual environment
- How to install the package directly from a GitHub repository
- How to make sure the package is usable via `pip`

---

## 🧱 Project Structure

```
fixer-demo/
│
├── fixer/                    # Python module folder
│   ├── __init__.py
│   └── handler.py
├── dist/                     # Distribution files (after build)
├── fixer_demo.egg-info/      # Metadata about the package
├── setup.py                  # Package configuration file
├── requirement.txt           # Installed packages list (optional)
└── README.md
```

---

## ⚙️ Step-by-step Instructions

### 🔹 1. Build the distributable package

From inside the project directory:

```bash
python setup.py sdist
```

This generates a file like:

```
dist/fixer_demo-0.3.tar.gz
```

---

### 🔹 2. Create a virtual environment to test installation

```bash
virtualenv -p python testenv
source testenv/bin/activate
```

You should now see the virtual environment activated:
```bash
(testenv) $
```

---

### 🔹 3. Install the package directly from GitHub

```bash
pip install git+https://github.com/thisisZoya/fixer-demo
```

---

### 🔹 4. Verify that the package is installed

```bash
python
>>> from fixer import get_rates
>>> get_rates("YOUR_API_KEY")
```

---

### 🛠 Example Output

```python
{'success': False, 'error': {'code': 104, 'type': 'usage_limit_reached', 'info': 'Your monthly usage limit has been reached. Please upgrade your Subscription Plan.'}}
```

This confirms the package is installed and callable.

---

## 🚧 Notes

- Don't forget to **bump the version number** in `setup.py` each time you want to test a new version.  
  For example:
  ```python
  version="0.3"
  ```

- If you're getting errors like `ImportError`, make sure your `__init__.py` is correctly exporting the functions you need:
  ```python
  from .handler import get_rates
  ```

- If you want to track dependencies, you can export them:
  ```bash
  pip freeze > requirement.txt
  ```

---

## 📌 Git Commands Used

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:thisisZoya/fixer-demo.git
git push -u origin main
```

---

## 💬 License

MIT License (feel free to customize this section)

---

Happy coding & packaging! 🐍🚀