import pydicom
import numpy as np
import os

def cell_card(dicom,file):   
    pixel_array_down = dicom.pixel_array[::16,::16]
    slope = dicom.RescaleSlope
    intercept = dicom.RescaleIntercept
    material_id = 0
    density = {"1":"0.099006","2":"0.104021","3":"0","4":"0.133974","5":"0.109823","6":"0","7":"0","0":"0"}
    width = len(pixel_array_down)
    depth = len(pixel_array_down[0])
    last_value = 26
    group_pixels_count = 0
    cell_id = 0
    for i in range(width):
        last_value = 26
        group_pixels_count = 0
        for j in range(depth):
            pixel_value = pixel_array_down[i][j]
            if pixel_value != last_value:
                if last_value > 26:
                    cell_id = cell_id+1
                    hu = last_value * slope + intercept
                    if hu <= -998:
                        continue
                    elif hu <=33 and hu >=15:
                        material_id = 1
                    elif  hu <=60 and hu >=44:
                        material_id = 2
                    elif hu <=94 and hu >=90:
                        material_id = 3
                    elif hu <=204 and hu >=190:
                        material_id = 4
                    elif hu <=1030 and hu >=816:
                        material_id = 5
                    elif hu <=1307 and hu >=1253:
                        material_id = 6
                    elif hu <=2390 and hu >=2230:
                        material_id = 7
                    else:
                        material_id = 0

                    file.write('\n'+str(cell_id)+'   '+str(material_id)+'   '+str(density[str(material_id)])+'   '+str(-cell_id))
                
                group_pixels_count = 1
                last_value = pixel_value
            else:
                group_pixels_count = group_pixels_count+1

            

def surface_card(dicom, file):

    pixel_array_down = dicom.pixel_array[::16,::16]
    pixel_size = 0.1875*8
    slide_location = dicom.get('SliceLocation')
    group_pixels_count = 0
    y = slide_location - 0.625
    last_value = 26
    pixel_id = 0

    width = len(pixel_array_down)
    depth = len(pixel_array_down[0])
    for i in range(width):
        last_value = 26
        group_pixels_count = 0
        for j in range(depth):
            pixel_value = pixel_array_down[i][j]
            if pixel_value != last_value:
                if last_value > 26:
                    pixel_id = pixel_id+1
                    xb = group_pixels_count*pixel_size
                    file.write('\n'+str(pixel_id)+' box       '+str(x)+' '+str(y)+' '+str(z)+'       '+str(pixel_size)+' 0 0       0 '+'1.25 0       0 0 '+str(xb))
                if pixel_value > 26:
                    x = i*pixel_size
                    z = j*pixel_size
                    
                group_pixels_count = 1
                last_value = pixel_value
            else:
                group_pixels_count = group_pixels_count+1
                last_value = pixel_value


def data_card(file):
    with open('data_template.txt', 'r') as content_file:
        content = content_file.read()
        file.write(content)


def parse_dicom(path_dicom, export_path):
    dicom = pydicom.dcmread(path_dicom)
    file = open(export_path,'w+')
    file.write('c   Geometry definition')
    cell_card(dicom,file)
    file.write('\n')
    file.write('\n'+'c   Bodies')
    surface_card(dicom,file)
    data_card(file)
    file.close()

    return 0


parse_dicom("80_dicom_125mm.dcm", "80_dicom_125mm.imp")