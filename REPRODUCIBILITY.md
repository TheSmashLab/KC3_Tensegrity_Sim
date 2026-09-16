# Reproducing the Paper Results

This guide records the software environment and commands needed to reproduce results associated with “TensegritySim Python Package Using Virtual Work.” Complete the paper-specific mapping below before creating the archival release.

## Archival version

- Software version: `1.0.0`
- Git tag: `v1.0.0` *(create after the reproduction mapping has been verified)*
- Commit: `TODO: insert the release commit SHA`
- Archive DOI: `TODO: insert the Zenodo DOI`
- Supported Python: 3.9–3.12

## Environment

```bash
git clone https://github.com/TheSmashLab/KC3_Tensegrity_Sim.git
cd KC3_Tensegrity_Sim
git checkout v1.0.0
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows PowerShell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -q
```

## Running a configuration

```bash
python main.py yaml/1-box.yaml
```

The current runner is interactive and opens Matplotlib figures. Record any control-length inputs in the table below in the exact order entered. If paper figures require post-processing, add those commands as well.

## Paper-to-configuration mapping

Replace every `TODO` with verified information from the submitted manuscript. Do not claim complete reproducibility until every reported computational result has an entry.

| Paper result | Configuration | Exact command and inputs | Expected output | Tolerance |
|---|---|---|---|---|
| TODO: Figure/table/case | `yaml/1-box.yaml` | `python main.py yaml/1-box.yaml`; TODO: inputs | TODO | TODO |
| TODO | `yaml/2-box.yaml` | TODO | TODO | TODO |
| TODO | `yaml/2-box-connected.yaml` | TODO | TODO | TODO |
| TODO | `yaml/2-box-force.yaml` | TODO | TODO | TODO |
| TODO | `yaml/2x10-cylinder.yaml` | TODO | TODO | TODO |
| TODO | `yaml/3Bar.yaml` | TODO | TODO | TODO |
| TODO | `yaml/6-box.yaml` | TODO | TODO | TODO |
| TODO | `yaml/6-box-cylinder.yaml` | TODO | TODO | TODO |

## Verification checklist

- [ ] Confirm author names and ORCIDs in `CITATION.cff`.
- [ ] Add the accepted paper metadata and DOI to `CITATION.cff`.
- [ ] Verify every mapping against the submitted manuscript.
- [ ] Record exact numerical outputs and tolerances.
- [ ] Run the complete workflow from a clean clone.
- [ ] Create and publish the `v1.0.0` GitHub release.
- [ ] Archive the release and add its DOI here and to the paper.
