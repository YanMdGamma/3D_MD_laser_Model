# 3D-MD laser Model

## Description

This project contain one main branch for our essay, `3D-MD_simulation`. The `3D-MD_simulation` mainly contained the algorithm we designed: 1, the energy distribution of femtosecond laser processing upon 4H-SiC; 2, the source of $\text V_{\text S\text i}$ upon surface from original $\text V_{\text S\text i}$ or produced $\text V_{\text S\text i}$. See mor details in Refs. [1].

## 3D-MD_simulation

### Energy_distribution

According to 

Users can define the number of their ‘hemi-ellipsoidal’s, and the long axis and short axis. The ‘outputfile.txt’ is generated after energy deposition. 

### Judge the source of $\text V_{\text S\text i}$

Users need to put  $\text V_{\text S\text i}$ .xyz file and origin data file as input, then the ‘output.txt’ is generated after energy deposition. 3_coordination file is original $\text V_{\text S\text i}$, 4_coordination file is new $\text V_{\text S\text i}$.

## How to:

### determine the energy distribution of hemi-ellipsoidal shells

①、Run [ Meng3Dltech.py](3D-MD_simulation/Energy_distribution/Meng3Dltech.py) directly. Write something like:

```python
python Meng3Dltech.py --shell_number 20 --major_axis 6 --minor_axis 5 --wave_length 1030e-9 -- power 0.4 --pulse_width 285e-15 -- repetition_rate 1e5 --output_path ./outputfile --thickness 250e-6 --Refractive_index 2.5839 --Reflection_coefficient 0.19532
```

<details>
    <summary>Tips for running (click here!)</summary>
    <ol>
        <li>Users need to install the `numpy`, `math`, `matplotlib`, `sympy`, `random`,`scipy` packages in native python environment to run the program properly.</li>
        <li> Every parameter has default value, see `--help` for more details.</li>
    </ol>
</details>

- `shell_number` refer to ***shell number of 3D-model***;


- `major_axis` refers to the ***Major axis of hemi-ellipsoidal shell***;
- `minor_axis` refers to the ***Minor axis of hemi-ellipsoidal shell***;
- `wave_length` refers to the ***Wave length of femtosecond laser***;
- `power` refers to the ***Power of femtosecond laser***;
- `pulse_width` refers to the ***Pulse width of femtosecond laser***;
- `repetition_rate` refers to the ***Repetition rate of femtosecond laser***;
- `output_path` refers to the ***Path to the energy deposition file***;
- `thickness` refers to the ***Sample thickness***;
- `Refractive_index` refers to the ***Refractive index of 4H-SiC***;
- `Reflection_coefficient` refers to the ***Reflection coefficient of 4H-SiC***.

### Analyze the source of  $\text V_{\text S\text i}$​

②、Run [ Mengcentech.py](3D-MD_simulation/Energy_distribution/Meng3Dltech.py) directly. Write something like:

```python
python Mengcentech.py --matforW 20 --xyzforW 6 --matforW3_Coordination 5 --matforW4_Coordination 1030e-9 --_3_Coor_xyz_file_path 0.4 --_4_Coor_xyz_file_path 285e-15 --_3_Coor_xyz_ori_output_file_path 1e5 --_4_Coor_xyz_ori_output_file_path ./outputfile --_3_Coor_xyz_output_file_path 250e-6 --_3_Coor_xyz_output_file_path 2.5839 
```

<details>
    <summary>Tips for running (click here!)</summary>
    <ol>
        <li>Users need to install the `numpy`, `pandas`, `scipy` packages in native python environment to run the program properly.</li>
        <li> Every parameter has default value, see `--help` for more details.</li>
    </ol>
</details>

- `matforW` refer to ***.mat of all color center***;


- `xyzforW` refers to the ***.xyz of all color center***;
- `matforW3_Coordination` refers to the ***Temporary file of the original color center position***;
- `matforW4_Coordination` refers to the ***Temporary file of the new color center position*** ;
- `_3_Coor_xyz_file_path` refers to the ***Output file of the original color center***;
- `_4_Coor_xyz_file_path` refers to the ***Output file of the new color center***;
- `_3_Coor_xyz_ori_output_file_path` refers to the ***Output file of the original color center (before laser processing)***;
- `_4_Coor_xyz_ori_output_file_path` refers to the ***Output file of the new color center (before laser processing)***;
- `_3_Coor_xyz_output_file_path` refers to the ***Output file of the original color center (after laser processing)***;
- `_4_Coor_xyz_output_file_path` refers to the ***Output file of the original color center (after laser processing)***;

> [!NOTE]
>
>  The `outputfile` is generated under current folder. 

## References

If you use this code to run a defects detection process, please cite:

Yan M, Zhao J, Djurabekova F, et al. Generalized Algorithm for Recognition of Complex Point Defects in Large-Scale β-Ga2O3[J]. arXiv preprint arXiv:2401.15920, 2024.[ https://doi.org/10.48550/arXiv.2401.15920](https://doi.org/10.48550/arXiv.2401.15920)

## Contributors

- Mengzhi Yan (main)
- Junlei Zhao
- Zongwei Xu
