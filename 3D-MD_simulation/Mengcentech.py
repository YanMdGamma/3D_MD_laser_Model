import Judge_the_oriornew
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enter your XYZ file for color center analysis.')

    # -----------------------------------------------------------------------------------
    parser.add_argument('--matforW', type=str, help='.mat of all color center',
                        default='./file_0.2 W/Colorcen.mat')
    parser.add_argument('--xyzfor02W', type=str, help='.xyz of all color center',
                        default='./file_0.2 W/0.2_final.xyz')
    # --------------------------------------------------------------------------------


    parser.add_argument('--matforW3_Coordination', type=str, help='Temporary file of the original color center',
                        default='./file_0.2 W/3_Coor.mat')
    parser.add_argument('--matforW4_Coordination', type=str, help='Temporary file of the new color center',
                        default='./file_0.2 W/4_Coor.mat')

    # use for 0.2 W
    parser.add_argument('--_3_Coor_xyz_file_path', type=str, help='Output file of the original color center',
                        default='./file_0.2 W/Ori_3.xyz')
    parser.add_argument('--_4_Coor_xyz_file_path', type=str, help='Output file of the new color center',
                        default='./file_0.2 W/Ori_4.xyz')

    parser.add_argument('--_3_Coor_xyz_ori_output_file_path', type=str, help='Output file of the original color center',
                        default='./file_0.2 W/file_3_Coordination_ori_output.xyz')
    parser.add_argument('--_4_Coor_xyz_ori_output_file_path', type=str, help='Output file of the new color center',
                        default='./file_0.2 W/file_4_Coordination_ori_output.xyz')

    parser.add_argument('--_3_Coor_xyz_output_file_path', type=str, help='Output file of the original color center',
                        default='./file_0.2 W/file_4_Coordination_output.xyz')
    parser.add_argument('--_4_Coor_xyz_output_file_path', type=str, help='Output file of the new color center',
                        default='./file_0.2 W/file_3_Coordination_output.xyz')

    args = parser.parse_args()
    # Show user command line reminder
    print("Laser energy deposition of different hemi-ellipsoidal shell:")
    print(f" matforW: {args.matforW}")
    print(f" xyzforW : {args.xyzforW}")
    print(f" matforW3_Coordination : {args.matforW3_Coordination}")
    print(f" matforW4_Coordination: {args.matforW4_Coordination}")
    print(f" 3_Coor_xyz_file_path: {args._3_Coor_xyz_file_path}")
    print(f" 4_Coor_xyz_file_path : {args._4_Coor_xyz_file_path}")
    print(f" 3_Coor_xyz_ori_output_file_path : {args._3_Coor_xyz_ori_output_file_path}")
    print(f" 4_Coor_xyz_ori_output_file_path : {args._4_Coor_xyz_ori_output_file_path}")
    print(f" 3_Coor_xyz_output_file_path : {args._3_Coor_xyz_output_file_path}")
    print(f" 4_Coor_xyz_output_file_path : {args._4_Coor_xyz_output_file_path}")

    Judge_the_oriornew.main(args.matforW, args.xyzforW, args.matforW3_Coordination, args.matforW4_Coordination, args._3_Coor_xyz_file_path,
                     args._4_Coor_xyz_file_path, args._3_Coor_xyz_ori_output_file_path, args._4_Coor_xyz_ori_output_file_path, args._3_Coor_xyz_output_file_path
                            , args._4_Coor_xyz_output_file_path)
