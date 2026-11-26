# Changes in Ilya’s StimGen 2.1

Ben Murphy-Baum wrote the original [StimGen](https://doi.org/10.5281/zenodo.5903691). Ilya Kapral made the changes below for his recording rig and experiments. This comparison covers the [StimGen 2.1 rig snapshot dated 6 December 2024](StimGen-ilya2.1.py) and the copy of Ben’s `StimGen.py` used as the comparison baseline. The adaptation is released under [GPLv3](LICENSE).

## Saving and logging

1. **Save stimulus before a run.** Running or exporting a stimulus saves the current settings over the selected stimulus-bank file without opening a naming dialog. This keeps edits when switching to another stimulus for a quick check.
2. **Archive the stimulus file.** After a non-aborted run, StimGen copies the selected `.stim` file into a dated folder under the log directory. The filename includes the timestamp, stimulus ID, and stimulus name. The copy preserves the stimulus definition for later replay. The text log remains available for reading and parsing. Replaying a run also requires the corresponding global settings and rig calibration.
3. **Record global settings in the log.** The text log now records X/Y offsets, background, bit depth, and the selected gamma table after each object’s parameters. These settings are needed to reproduce the stimulus on the rig.
4. **Default log filename.** StimGen fills in the date at startup in uppercase `MMM_DD_YY` format, saving a step at the start of the day.

## Rig timing, coordinates, and intensity

5. **Fixed 60 Hz timing.** StimGen uses a frame interval of 1/60 s when converting durations and motion to frames. The original measured the display refresh rate at session initialization.
6. **Rotate stimulus coordinates.** To match the rig optics, StimGen maps global offsets and object Cartesian positions from `(x, y)` to `(y, −x)`, truncating object coordinates to integers. It subtracts 90° from motion direction and polar position angle and reverses the sign of object orientation.
7. **Fixed parallel-port address.** The parallel-port trigger and settings field use the rig’s address, `0x4FF8`. The original used a configurable address with `0xE010` as the default.
8. **Default 12-bit encoding.** The startup setting changes from 8 to 12 bits to make finer intensity steps available for low-contrast stimuli on the rig.
9. **Gamma lookup for the initial grating texture.** The initial texture is built with the gamma-table lookup disabled. The separate `CalculateGrating()` routine still applies the lookup.

## Stimulus rendering

10. **Larger 2D checkerboard.** The noise stimulus is drawn at 4096 × 4096 display pixels, up from 512 × 512. Noise-element size still comes from the stimulus settings. The larger field supports longer drift before the moving checkerboard reaches its edge.
11. **Checkerboard drift.** In Drift mode, the 2D and 1D checkerboards update their position each frame using either the selected speed and direction or a defined trajectory.
12. **Checkerboard aperture position.** The 2D checkerboard’s object aperture uses both the global offset and the local position. This lets two objects be presented with separate apertures in different locations.
13. **Grating aperture setup.** A circular aperture is re-enabled for gratings with a positive object-aperture size, using the global and local offsets. The existing aperture block then creates a second circular aperture at the same center.
14. **Shared aperture position defaults.** Local X and Y start at zero before StimGen resolves the object’s Cartesian or polar coordinates for the shared aperture.
15. **Buffered annulus rendering.** StimGen draws the annulus using an image buffered from two circles, with the inner circle set to the background intensity. The buffered image is used for drawing in place of the original vector shape.

## Run display

16. **Sweep counter display.** The most recent sweep count stays visible while StimGen waits for the next sweep and at normal completion.
