# StimGen 2.1 study adaptation

StimGen designs and presents visual stimuli for experiments using Qt and PsychoPy. Ben Murphy-Baum wrote the [original StimGen](https://doi.org/10.5281/zenodo.5903691). Ilya Kapral adapted it for his recording rig. See [the change notes](CHANGES.md) for the changes and their experimental rationale.

**Private staging snapshot.** The launcher here is the local StimGen 2.1 file, SHA-256 `b7bcb1d4770c100016884d68f1d58b10459254bc5402a9acecf34a9a77f85374`. The separately identified rig commit `f1cf0116d5e16c7d91ecea67f4f0be14f2ee3336` contains a different launcher. Confirm the build used for the paper and resolve the redistribution terms before publishing a release.

## Run

From the repository root, create the supplied Conda environment and start the launcher.

```sh
conda env create -f environment.yml
conda activate stim
python StimGen-ilya2.1.py
```

Select the display and calibrate the pixels per micrometre, background, offsets, and gamma for your rig. The launcher assumes a 60 Hz display and uses parallel-port address `0x4FF8`. Set **Save to Path** to an existing writable log directory and select a preset before running. Run and export save current settings over the selected preset. Use a working copy of a preset to preserve the archived settings.

## Stimulus presets

Under **User → Paper 1**, 17 presets cover the stimulus labels used in the paper. Eleven are recorded stimulus files and six are matching named bank presets whose historical settings may differ. **User → Calibration** contains the pixels-per-micrometre calibration preset. The included profile and gamma tables are specific to the original setup. Playback on the rig remains to be checked for this package.

## Cite

Cite the released adaptation by its version-specific Zenodo DOI when available. Cite [Murphy-Baum, *StimGen*, v1.0.0 (2022)](https://doi.org/10.5281/zenodo.5903691) for the original software. The upstream license text is preserved in [LICENSE](LICENSE).
