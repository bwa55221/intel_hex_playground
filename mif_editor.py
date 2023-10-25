import mif
import os
import numpy as np

def form_mif_header(depth=64,width=16,addr_radix='HEX',data_radix='HEX'):
   
   header = [
   f'DEPTH = {depth};',
   f'WIDTH = {width};',
   f'',
   f'ADDRESS_RADIX = {addr_radix};',
   f'DATA_RADIX = {data_radix};',
   f''
   ]
   return header

def form_mif_content(photo):
   content = [f'CONTENT', f'BEGIN'] + form_u4_data(photo) + [f'END;']
   return content

def form_mif(photo):
   '''
   This takes the numpy.ndarray and creates the mif
   '''
   
   mif_str_arr = form_mif_header(photo.shape[0]*photo.shape[1], photo.shape[2]*4) + form_mif_content(photo)
   mif = '\n'.join(mif_str_arr)

   return mif

# ask for filname for mif data
def write_mif(photo, mode='x', file='mifData.mif'):
   '''
   this writes out the mif
   '''

   f = open(file, mode)
   f.write(form_mif(photo))
   f.close()



# dir = os.getcwd()
# path = os.path.join(dir, 'bram_cam\memory.mif')
# print(f' the dir is: {dir}')
# print(f' the path is: {path}')

# with open(path) as f:
#     width, mem = mif.load(f, packed=True)

# print(mif.dumps(mem, width=width))


if __name__ == '__main__':
#    data = np.ndarray(1,4096, dtype=np.uint8)
    # data = np.random.randint(0, 255, 4096, dtype=np.uint8)
    length = 4096
    data = np.arange(0,length, 1)
    print(data)
    print(len(data))

    header = form_mif_header(depth=16, width=256)
    print(header)


    mif_data = []
    # for row in range(1, 16+1, 1):
    #    for col in range(0, 256, 1):
    #       mif_data.append(f'{row + col} : {data[row + col]}')
    # print(mif_data)

    for i in range(0, length, 1):
       mif_data.append(f'{i} : {data[i]}')

    print(mif_data)

    content = [f'CONTENT', f'BEGIN'] + mif_data + [f'\nEND;']
    # print(content)
   
    mem_mif = header + content
    # print(mem_mif)

    dir = os.getcwd()
    path = os.path.join(dir, 'bram_cam\memory.mif')
    f = open(path, 'wb')
    # f.write(''.join(mem_mif))
    f.write(mem_mif)
    f.close()