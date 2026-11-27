# Changes in the StimGen 2.1 study launcher

Ben Murphy-Baum wrote the original [StimGen](https://doi.org/10.5281/zenodo.5903691). Ilya Capralov made the changes below for his rig and experiments. This comparison uses the two launchers at study commit `f1cf0116d5e16c7d91ecea67f4f0be14f2ee3336` (3 July 2025). The adaptation is released under [GPLv3](LICENSE).

## Saving and logging

- **Save before a run.** Running or exporting saves the current settings over the selected stimulus-bank file without a naming dialog. This keeps edits when switching to another stimulus for a quick check.
- **Archive each completed stimulus.** After a non-aborted run, StimGen copies the saved `.stim` to a dated log folder under a filename containing its timestamp, stimulus ID, and name. The file preserves the stimulus definition for replay. The text log remains available for reading and parsing.
- **Log global settings.** The text log includes X/Y offsets, background, bit depth, and the selected gamma table alongside the object data. These settings are needed to reproduce the stimulus on the rig.
- **Default log filename.** The date is filled in at startup in uppercase `MMM_DD_YY` format, saving a step at the start of the day.

## Timing and run display

- **Measure display refresh.** Session initialization measures the refresh rate and retries with a cleared measurement cache if the first call returns no rate.
- **Time sweeps by elapsed seconds.** The sweep loop uses elapsed time to control trial length and object onset and duration. It derives the stimulus frame index from elapsed time and the measured frame interval. Grating drift advances phase by drift frequency times the elapsed time since the previous loop.
- **Record flips and display sweep progress.** The frame timestamp array can grow when a sweep produces more flips than expected. The interface shows elapsed seconds during the sweep and keeps the last sweep count visible at normal completion.

## Rig coordinates and intensity

- **Rotate coordinates.** The launcher rotates global offsets and Cartesian object positions to match the rig optics. It subtracts 90° in polar-position and motion calculations, reverses the sign of orientation, and applies a second Cartesian transform before the shared-aperture setup.
- **Set the parallel-port address.** The trigger and settings field use `0x4FF8`, the address used by the rig. The original used a configurable address with `0xE010` as the default.
- **Default to 12-bit encoding.** The startup setting changes from 8 to 12 bits to make finer intensity steps available for low-contrast stimuli on the rig.
- **Move apertures with object position.** Grating and 2D checkerboard apertures use global and local offsets. This allows separate apertures at different locations. The draw loop recalculates local coordinates for each object. The shared aperture starts with zero local offsets before resolving Cartesian or polar position.

## Stimulus rendering and sequences

- **Seed randomization consistently.** The launcher adds `rng.py` and a master seed of 1. It resets the Python and NumPy random generators at run and sweep boundaries. Random-walk angles and checkerboard shifts use NumPy’s generator. Motion clouds and random dots use the master seed.
- **Extend checkerboard drift.** The 2D checkerboard grows from 512 × 512 to 4096 × 4096 display pixels to support longer drift. Noise-element size still comes from the preset. Drift updates the position of both 1D and 2D checkerboards using the direction and speed or the selected trajectory.
- **Build grating textures from the background.** The initial texture uses alternating background and brighter bars, with no separate texture gamma lookup at that step. The separate modulation routine builds square or sine textures from the object intensities and applies the gamma table.
- **Add a contrast ramp.** Ramp mode adds initial contrast and a sequence assignment for that value. The update interpolates between the initial and final intensities. Non-grating sinusoidal modulation maps the sine wave between the two intensity limits.
- **Buffer annuli.** The annulus is drawn from a buffered image of two circles, with the inner circle set to background intensity.
- **Edit sequences together.** The sequence editor trims whitespace and skips empty entries. **Cycle Sequences** moves each final entry to the front. **Shuffle Sequences** checks sequence lengths, but the shuffle call is commented out in this snapshot, so it leaves the order unchanged.
- **Update the interface.** The launcher applies a dark stylesheet and labels the abort button **Stop**.
