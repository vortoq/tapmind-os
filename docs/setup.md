# Setup Instructions

## Requirements

- Python 3.10+
- Raspberry Pi 4 (or test in Linux laptop)
- MicroSD card (32GB+ if on Pi)

## 1. Install Dependencies

```bash
chmod +x configs/system-setup.sh
./configs/system-setup.sh
```

## 2. Launch TapMind

```bash
cd core
python3 launcher.py
```

## 3. Run Microapps

```bash
python3 apps/voicegpt.py
python3 apps/beatforge.py
```
