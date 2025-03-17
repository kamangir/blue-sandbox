# Python + OBS Studio ⏸️

https://chatgpt.com/c/67d8a46a-69dc-8005-9176-e1ec3528afdf

1️⃣ Installed [OBS Studio](https://obsproject.com/).

2️⃣ [pyvirtualcam](https://github.com/letmaik/pyvirtualcam)

Fails on Mac,

```bash
pip install pyvirtualcam
```

Instead installed from source,

```bash
pip install git+https://github.com/letmaik/pyvirtualcam.git
```

3️⃣ Fails,

```bash
python -m blue_sandbox.virtualcam
```

> RuntimeError: 'obs' backend: OBS Virtual Camera is not installed in your system. Use the Virtual Camera function in OBS to trigger installation.

Likely related to Mac Silicon. ⏸️


| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/blue-sandbox/OBS.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/blue-sandbox/virtualcam.png?raw=true) |
