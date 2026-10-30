# Design, Simulation, and Characterization of 4-Bit DACs

This repository covers the circuit design, theoretical formulation, SPICE simulation (TINA-TI), and linearity characterization of 4-bit Digital-to-Analog Converters using LM741 operational amplifiers.

## Key Highlights
- **Topologies Analyzed:** Binary-Weighted Resistor DAC vs. R-2R Ladder Network DAC.
- **Reference & Operating Points:** Evaluated under $V_{REF} = -5.0\text{ V}$ with inverting op-amp power rails at $\pm 10\text{ V}$.
- **Performance Evaluation:** R-2R Ladder demonstrated superior linearity due to standard resistor ratio matching ($1\text{ k}\Omega$ and $2\text{ k}\Omega$) avoiding wide resistance dispersion.
- **Dynamic AC Analysis:** Observed transient behavior under a $100\text{ Hz}$, $5\text{ V}$ sinusoidal reference input verifying undistorted 180° inverted output.
- **Error Metrics:** Numerical INL and DNL metrics extracted across all 16 digital codes (`0000` to `1111`) using Python.
