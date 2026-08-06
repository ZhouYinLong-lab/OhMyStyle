# Core resource registry

`index.yaml` is the generated catalog of executable visual-style resources.
It is intentionally separate from the legacy `styles/` catalog and from
render tasks.

Each structured package owns a local `resource.yaml` contract. The contract
declares:

- maturity (`L0` through `L4`);
- whether the package is independent of subject and narrative;
- the visual dimensions it focuses on;
- the canonical package, reference, prompt, provenance, and evaluation files;
- reference evidence and generated-demo policy.

The registry adds discovery metadata and evidence counts. Do not edit
`index.yaml` by hand:

```bash
python tools/scaffold-resource-manifests.py style-packages
python tools/build-registry.py
python tools/validate-resources.py style-packages
```

`L2` means reference-backed and executable. `L3` additionally has an accepted
generated example. `L4` is reserved for a package with evaluated
interoperability across providers or adapters. A package can be useful before
it reaches L4; the maturity field makes that limitation visible.
