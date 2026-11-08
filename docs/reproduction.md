# Research and reproducibility

The library supports general schema-generation workflows. The experiments
reported in the Schematize paper are maintained separately in the repository's
[`research/` directory](https://github.com/pwr-ai/schematize/tree/master/research).

That directory contains the fixed Polish legal-research dialogues, expert
question sets, Hydra configurations, baseline integrations, and analysis
notebooks. It is intentionally excluded from the installed package API.

From a source checkout:

```bash
uv sync --extra dev --extra research --extra huggingface
make research-check
```

`research-check` is offline: it validates runners, paths, shell scripts,
configurations, data files, and notebooks without API credentials or dataset
downloads.

See the [research README](https://github.com/pwr-ai/schematize/tree/master/research)
for the full reproduction order, corpus provenance, paper parameters, and
ScheMatiQ baseline setup.
