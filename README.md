# StimGen 2.1 study adaptation

StimGen designs and presents visual stimuli for experiments using Qt and PsychoPy. Ben Murphy-Baum wrote the [original StimGen](https://doi.org/10.5281/zenodo.5903691). Ilya Capralov modified it for retinal recordings. The [change notes](CHANGES.md) describe the modifications and their experimental rationale.

Use the [v2.1.2 study archive](https://github.com/ilyazkaya/StimGen-study/tree/v2.1.2) for the paper. It preserves `StimGen-ilya2.1.py` and `rng.py` from the study repository’s commit `f1cf0116d5e16c7d91ecea67f4f0be14f2ee3336` (3 July 2025). The launcher’s SHA-256 is `61ca771cb5b1bbea1675ea5a3d521779c7355d78370178731379f640847171a7`. The earlier `v2.1` tag contains the staging build.

## Run

From the repository root, create the study's Conda environment and start the launcher.

```sh
conda env create -f environment.yml
conda activate stim
python StimGen-ilya2.1.py
```

Select the display and adjust the pixels per micrometre, background, offsets, and gamma for your setup. StimGen measures the display refresh rate at initialization. The parallel-port address is `0x4FF8`. For Windows, use the [PsychoPy parallel-port setup guide](https://psychopy.org/hardware/parallelPortInstr.html). Set **Save to Path** to an existing writable log directory. Run and export save over the selected preset. Use a working copy to preserve the archived settings.

## Stimulus presets

**User → NaV Bifid Stim** contains 17 study presets and `PPMCallibration.stim`. Eleven study presets come from matched recording snapshots and five from the study bank. The supplemental `NullGratFlash3.stim` is a separately preserved named preset. Historical settings for named presets may differ from those used for individual recordings.

## Cite

Cite the v2.1.2 archive by its version-specific Zenodo DOI when available. Cite [Murphy-Baum, *StimGen*, v1.0.0 (2022)](https://doi.org/10.5281/zenodo.5903691) for the original software.

## License

Original StimGen © Ben Murphy-Baum. Study modifications © Ilya Capralov. The modified work is distributed under the [GNU General Public License, version 3](LICENSE).
