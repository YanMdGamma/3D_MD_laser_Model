import Model_construction
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enter your hemi-ellipsoidal shell parameters.')
    parser.add_argument('--shell_number', type=float, help='shell number of 3D-model', default=20)
    parser.add_argument('--major_axis', type=float, default=6,
                        help='Major axis of hemi-ellipsoidal shell')
    parser.add_argument('--minor_axis', type=float, default=5,
                        help='Minor axis of hemi-ellipsoidal shell')
    parser.add_argument('--wave_length', type=float, default=1030e-9,
                        help='Wave length of femtosecond laser')
    parser.add_argument('--power', type=float, default=0.4,
                        help='Power of femtosecond laser')
    parser.add_argument('--pulse_width', type=float, default=285e-15,
                        help='Pulse width of femtosecond laser')
    parser.add_argument('--repetition_rate', type=float, default=1e5,
                        help='Repetition rate of femtosecond laser')
    parser.add_argument('--output_path', type=str, help='Path to the energy deposition file.', default='./outputfile')
    parser.add_argument('--thickness', type=float, default=350e-6,
                        help='Sample thickness')
    parser.add_argument('--Refractive_index', type=float, default=2.5839,
                        help='Refractive index of 4H-SiC')
    parser.add_argument('--Reflection_coefficient', type=float, default=0.19532,
                        help='Reflection coefficient of 4H-SiC')


    args = parser.parse_args()
    # Show user command line reminder
    print("Laser energy deposition of different hemi-ellipsoidal shell:")
    print(f"  Shell number: {args.shell_number}")
    print(f"  Major axis of hemi-ellipsoidal shell : {args.major_axis}")
    print(f"  Minor axis of hemi-ellipsoidal shell : {args.minor_axis}")
    print(f"  Wave length of femtosecond laser: {args.wave_length}")
    print(f"  Power of femtosecond laser: {args.power}")
    print(f"  Pulse width of femtosecond laser : {args.pulse_width}")
    print(f"  Repetition rate of femtosecond laser : {args.repetition_rate}")
    print(f"  Energy deposition file output path : {args.output_path}")
    print(f"  Sample thickness : {args.thickness}")
    print(f"  Refractive index of 4H-SiC : {args.Refractive_index}")
    print(f"  Reflection coefficient of 4H-SiC : {args.Reflection_coefficient}")

    Model_construction.main(args.shell_number, args.major_axis, args.minor_axis, args.wave_length, args.power,
                     args.pulse_width, args.repetition_rate, args.output_path, args.thickness, args.Refractive_index,
                            args.Reflection_coefficient)
