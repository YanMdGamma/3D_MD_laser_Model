import numpy as np
import pandas as pd
from scipy.io import savemat
import argparse
import scipy.io as sio

def read_xyz(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    comment = lines[1].strip()  # Read comment line
    data = []

    # Skip the first two lines and parse the following atomic information
    for line in lines[2:]:
        parts = line.split()
        atom_Id, atom_type, x, y, z, coor, ep, ek = map(float, parts[0:8])
        data.append([atom_Id, atom_type, x, y, z, coor, ep, ek])

    df = pd.DataFrame(data, columns=['Atom_Id', 'Atom_Type', 'X', 'Y', 'Z', 'Coordination', 'ep', 'ek'])
    return df, comment

def xyz_to_mat(xyz_file_path, mat_file_path):
    df, comment = read_xyz(xyz_file_path)

    # Convert DataFrame to dictionary with numpy arrays
    mat_data = df.to_numpy()

    # Save to .mat file
    savemat(mat_file_path, {'test1': mat_data})
    print(f"Saved {mat_file_path}")
    return comment

if __name__ =="__main__":
    # parser = argparse.ArgumentParser(description='Enter your XYZ particle data file path.')
    # parser.add_argument('Colorcen_xyz_file_path', type=str, help='Path to the input Color center XYZ file.')
    # parser.add_argument('_3_Coor_xyz_file_path', type=str, help='Path to the input original 3 coordination XYZ file.')
    # parser.add_argument('_4_Coor_xyz_file_path', type=str, help='Path to the input original 4 coordination XYZ file.')
    #
    # args = parser.parse_args()
    #
    # print(f" Color center XYZ File: {args.Colorcen_xyz_file_path}")

    # # used for 0.09 W
    # mat_file_path_Color_cen = './Colorcen.mat'
    # Colorcen_file_path = './file2_colorcen.xyz'

    # # use for 0.4 W
    # mat_file_path_Color_cen = './file_0.4 W/Colorcen.mat'
    # Colorcen_file_path = './file_0.4 W/0.4_100ps_part_use.xyz'

    # use for 0.2 W
    mat_file_path_Color_cen = './file_0.2 W/Colorcen.mat'
    Colorcen_file_path = './file_0.2 W/0.2_final.xyz'

    message_comment = xyz_to_mat(Colorcen_file_path, mat_file_path_Color_cen)
    # print('message_comment: ', message_comment)
    #

    # # use for 0.09 W
    # # print(f" 3 Coordination XYZ File: {args._3_Coor_xyz_file_path}")
    # mat_file_path_3_Coor = './3_Coor.mat'
    # # print(f" 4 Coordination XYZ File: {args._4_Coor_xyz_file_path}")
    # mat_file_path_4_Coor = './4_Coor.mat'

    # # use for 0.4 W
    # mat_file_path_3_Coor = './file_0.4 W/3_Coor.mat'
    # # print(f" 4 Coordination XYZ File: {args._4_Coor_xyz_file_path}")
    # mat_file_path_4_Coor = './file_0.4 W/4_Coor.mat'

    # use for 0.2 W
    mat_file_path_3_Coor = './file_0.2 W/3_Coor.mat'
    # print(f" 4 Coordination XYZ File: {args._4_Coor_xyz_file_path}")
    mat_file_path_4_Coor = './file_0.2 W/4_Coor.mat'

    # # use for 0.09 W
    # _3_Coor_xyz_file_path = './file2_3_Coordination.xyz'
    # _4_Coor_xyz_file_path = './file2_4_Coordination.xyz'
    #
    # _3_Coor_xyz_ori_output_file_path = './file_3_Coordination_ori_output.xyz'
    # _4_Coor_xyz_ori_output_file_path = './file_4_Coordination_ori_output.xyz'
    # Others_Coor_xyz_ori_output_file_path = './file_others_Coordination_ori_output.xyz'
    #
    #
    # _3_Coor_xyz_output_file_path = './file_3_Coordination_output.xyz'
    # _4_Coor_xyz_output_file_path = './file_4_Coordination_output.xyz'
    # Others_Coor_xyz_output_file_path = './file_others_Coordination_output.xyz'
    #
    # xyz_to_mat(_3_Coor_xyz_file_path, mat_file_path_3_Coor)
    # xyz_to_mat(_4_Coor_xyz_file_path, mat_file_path_4_Coor)
    #
    # data = sio.loadmat('Colorcen.mat')
    # All_color_center = data['test1']
    # data = sio.loadmat('3_Coor.mat')
    # _3_coordination = data['test1']
    # data = sio.loadmat('4_Coor.mat')
    # _4_coordination = data['test1']
    # ----------------------------------------------------------------------------------------
    # # use for 0.4 W
    # _3_Coor_xyz_file_path = './file_0.4 W/Ori_3.xyz'
    # _4_Coor_xyz_file_path = './file_0.4 W/Ori_4.xyz'
    #
    # _3_Coor_xyz_ori_output_file_path = './file_0.4 W/file_3_Coordination_ori_output.xyz'
    # _4_Coor_xyz_ori_output_file_path = './file_0.4 W/file_4_Coordination_ori_output.xyz'
    # Others_Coor_xyz_ori_output_file_path = './file_0.4 W/file_others_Coordination_ori_output.xyz'
    #
    # _3_Coor_xyz_output_file_path = './file_0.4 W/file_3_Coordination_output.xyz'
    # _4_Coor_xyz_output_file_path = './file_0.4 W/file_4_Coordination_output.xyz'
    # Others_Coor_xyz_output_file_path = './file_0.4 W/file_others_Coordination_output.xyz'
    #
    # xyz_to_mat(_3_Coor_xyz_file_path, mat_file_path_3_Coor)
    # xyz_to_mat(_4_Coor_xyz_file_path, mat_file_path_4_Coor)
    #
    # data = sio.loadmat('./file_0.4 W/Colorcen.mat')
    # All_color_center = data['test1']
    # data = sio.loadmat('./file_0.4 W/3_Coor.mat')
    # _3_coordination = data['test1']
    # data = sio.loadmat('./file_0.4 W/4_Coor.mat')
    # _4_coordination = data['test1']
    # ----------------------------------------------------------------------------------------
    # use for 0.2 W
    _3_Coor_xyz_file_path = './file_0.2 W/Ori_3.xyz'
    _4_Coor_xyz_file_path = './file_0.2 W/Ori_4.xyz'

    _3_Coor_xyz_ori_output_file_path = './file_0.2 W/file_3_Coordination_ori_output.xyz'
    _4_Coor_xyz_ori_output_file_path = './file_0.2 W/file_4_Coordination_ori_output.xyz'
    Others_Coor_xyz_ori_output_file_path = './file_0.2 W/file_others_Coordination_ori_output.xyz'

    _3_Coor_xyz_output_file_path = './file_0.2 W/file_3_Coordination_output.xyz'
    _4_Coor_xyz_output_file_path = './file_0.2 W/file_4_Coordination_output.xyz'
    Others_Coor_xyz_output_file_path = './file_0.2 W/file_others_Coordination_output.xyz'

    xyz_to_mat(_3_Coor_xyz_file_path, mat_file_path_3_Coor)
    xyz_to_mat(_4_Coor_xyz_file_path, mat_file_path_4_Coor)

    data = sio.loadmat('./file_0.2 W/Colorcen.mat')
    All_color_center = data['test1']
    data = sio.loadmat('./file_0.2 W/3_Coor.mat')
    _3_coordination = data['test1']
    data = sio.loadmat('./file_0.2 W/4_Coor.mat')
    _4_coordination = data['test1']
    # --------------------------------------------------------------------------------------

    _3_ID = _3_coordination[:,0]
    _4_ID = _4_coordination[:,0]
    print('_3_ID:\n', _3_ID.shape[0])
    # print('\n_4_ID_all:\n', _4_ID_all)


    _3_ID_all = np.zeros((1, 8))
    _3_ID_all_later = np.zeros((1, 8))
    _4_ID_all = np.zeros((1, 8))
    _4_ID_all_later = np.zeros((1, 8))
    count_other_ID_all = np.zeros((1, 8))
    count_other_ID_all_later = np.zeros((1, 8))
    print('_3_ID_all:\n', _3_ID_all)
    # print('\n_4_ID_all:\n', _4_ID_all)

    count_3 = 0
    count_4 = 0
    count_other = 0
    for i in range(All_color_center.shape[0]):
        if All_color_center[i, 0] in _3_ID:
            count_3 = count_3 + 1
            _3_ID_all = np.vstack((_3_ID_all, np.concatenate(
                (All_color_center[i, :]), axis=None)))

        elif All_color_center[i, 0] in _4_ID:
            count_4 = count_4 + 1
            _4_ID_all = np.vstack((_4_ID_all, np.concatenate(
                (All_color_center[i, :]), axis=None)))

        else:
            count_other = count_other + 1
            count_other_ID_all = np.vstack((count_other_ID_all, np.concatenate(
                (All_color_center[i, :]), axis=None)))


    _4_ID_all = _4_ID_all[1:, :]
    _3_ID_all = _3_ID_all[1:, :]
    count_other_ID_all = count_other_ID_all[1:, :]
    print('3_Coordination number:\n', count_3)
    print('\n4_Coordination number:\n', count_4)
    print('\nOther type of Color center, the number of them is:\n', count_other)
    print('3_Coordination atoms: \n', _3_ID_all.shape)

    print('_3_ID_all_Coordination atoms: \n', _3_ID_all[0, 0])


    with open(_3_Coor_xyz_ori_output_file_path, 'w') as xyz_file:
        num_3_Coor_atoms = count_3

        xyz_file.write(f"{count_3}\n")
        # xyz_file.write(f"{massage_comment}\n")
        xyz_file.write(xyz_to_mat(Colorcen_file_path, mat_file_path_Color_cen))

        # The last one is coordination
        for i in range(0, count_3):
            # x, y, z = map(float, _3_ID_all[i, 2:])
            xyz_file.write(f"\n{_3_ID_all[i, 0]} {_3_ID_all[i, 1]} {_3_ID_all[i, 2]} {_3_ID_all[i, 3]} {_3_ID_all[i, 4]} {_3_ID_all[i, 5]} {_3_ID_all[i, 6]} {_3_ID_all[i, 7]}")

    with open(_4_Coor_xyz_ori_output_file_path, 'w') as xyz_file:
        num_4_Coor_atoms = count_4

        xyz_file.write(f"{count_4}\n")
        xyz_file.write(xyz_to_mat(Colorcen_file_path, mat_file_path_Color_cen))

        # The last one is coordination
        for i in range(0, count_4):
            # x, y, z = map(float, _4_ID_all[i, 1:][0:])
            xyz_file.write(f"\n{_4_ID_all[i, 0]} {_4_ID_all[i, 1]} {_4_ID_all[i, 2]} {_4_ID_all[i, 3]} {_4_ID_all[i, 4]} {_4_ID_all[i, 5]} {_4_ID_all[i, 6]} {_4_ID_all[i, 7]} ")


    with open(Others_Coor_xyz_ori_output_file_path, 'w') as xyz_file:
        num_other_atoms = count_other

        xyz_file.write(f"{count_other}\n")
        xyz_file.write(xyz_to_mat(Colorcen_file_path, mat_file_path_Color_cen))

        # The last one is coordination
        for i in range(0, num_other_atoms):
            # x, y, z = map(float, count_other_ID_all[i, 1:][0:])
            xyz_file.write(f"\n{count_other_ID_all[i, 0]} {count_other_ID_all[i, 1]} {count_other_ID_all[i, 2]} {count_other_ID_all[i, 3]} {count_other_ID_all[i, 4]} {count_other_ID_all[i, 5]} {count_other_ID_all[i, 6]} {count_other_ID_all[i, 7]}")




    # after processing
    _3_ID_later = _3_ID_all[:, 0]
    _4_ID_later = _4_ID_all[:, 0]
    _other_ID_later = count_other_ID_all[:, 0]

    for i in range(_3_ID.shape[0]):
        if _3_coordination[i, 0] in _3_ID_later:
            _3_ID_all_later = np.vstack((_3_ID_all_later, np.concatenate(
                (_3_coordination[i, :]), axis=None)))
        elif _3_coordination[i, 0] in _other_ID_later:
            count_other_ID_all_later = np.vstack((count_other_ID_all_later, np.concatenate(
                (_3_coordination[i, :]), axis=None)))

    for i in range(_4_ID.shape[0]):
        if _4_coordination[i, 0] in _4_ID_later:
            _4_ID_all_later = np.vstack((_4_ID_all_later, np.concatenate(
                (_4_coordination[i, :]), axis=None)))
        elif _4_coordination[i, 0] in _other_ID_later:
            count_other_ID_all_later = np.vstack((count_other_ID_all_later, np.concatenate(
                (_4_coordination[i, :]), axis=None)))

    _4_ID_all_later = _4_ID_all_later[1:, :]
    _3_ID_all_later = _3_ID_all_later[1:, :]
    count_other_ID_all_later = count_other_ID_all_later[1:, :]

    print('\nOther type of Color center is:\n', count_other_ID_all_later)

    with open(_3_Coor_xyz_output_file_path, 'w') as xyz_file:
        num_3_Coor_atoms = count_3

        xyz_file.write(f"{count_3}\n")
        # xyz_file.write(f"{massage_comment}\n")
        xyz_file.write(xyz_to_mat(Colorcen_file_path, mat_file_path_Color_cen))

        # The last one is coordination
        for i in range(0, count_3):
            # x, y, z = map(float, _3_ID_all[i, 2:])
            xyz_file.write(f"\n{_3_ID_all_later[i, 0]} {_3_ID_all_later[i, 1]} {_3_ID_all_later[i, 2]} {_3_ID_all_later[i, 3]} {_3_ID_all_later[i, 4]} {_3_ID_all_later[i, 5]} {_3_ID_all_later[i, 6]} {_3_ID_all_later[i, 7]}")

    with open(_4_Coor_xyz_output_file_path, 'w') as xyz_file:
        num_4_Coor_atoms = count_4

        xyz_file.write(f"{count_4}\n")
        xyz_file.write(xyz_to_mat(Colorcen_file_path, mat_file_path_Color_cen))

        # The last one is coordination
        for i in range(0, count_4):
            # x, y, z = map(float, _4_ID_all[i, 1:][0:])
            xyz_file.write(f"\n{_4_ID_all_later[i, 0]} {_4_ID_all_later[i, 1]} {_4_ID_all_later[i, 2]} {_4_ID_all_later[i, 3]} {_4_ID_all_later[i, 4]} {_4_ID_all_later[i, 5]} {_4_ID_all_later[i, 6]} {_4_ID_all_later[i, 7]} ")


    # I need to find 2 atoms from 12312000 atoms too hard.
    # with open(Others_Coor_xyz_output_file_path, 'w') as xyz_file:
    #     num_other_atoms = count_other
    #
    #     xyz_file.write(f"{count_other}\n")
    #     xyz_file.write(xyz_to_mat(Colorcen_file_path, mat_file_path_Color_cen))
    #
    #     # The last one is coordination
    #     for i in range(0, num_other_atoms):
    #         # x, y, z = map(float, count_other_ID_all[i, 1:][0:])
    #         xyz_file.write(f"\n{count_other_ID_all_later[i, 0]} {count_other_ID_all_later[i, 1]} {count_other_ID_all_later[i, 2]} {count_other_ID_all_later[i, 3]} {count_other_ID_all_later[i, 4]} {count_other_ID_all_later[i, 5]} {count_other_ID_all_later[i, 6]} {count_other_ID_all_later[i, 7]}")
    #

