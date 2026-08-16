# Hattori 1.5

The existing Hattori 1.5 code reorganized into modules while preserving the current tool implementations and Output Manager architecture.

## Run
```bash
pip install -r requirements.txt
python main.py
```

## Structure
- `core/` — menu, help, banner, runner/output manager
- `tools/` — individual tools
- `integrations/` — external integrations such as Sherlock
- `utils/` — shared helpers
- `outputs/` — saved results
