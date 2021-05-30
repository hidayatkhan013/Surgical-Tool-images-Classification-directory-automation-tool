import os, shutil
import numpy as np



data=np.genfromtxt('tool_video_02.txt',delimiter='\t',dtype=None, encoding=None)
data=data[1:]

for i in data:
    frame=str(i[0])
    if i[1]=='1' and i[2]=='1':
        if not os.path.isdir('GrasperBipolar'):
            os.system('mkdir GrasperBipolar')
        os.system(f"move video2_{frame}.jpg GrasperBipolar")
    elif i[1]=='1' and i[3]=='1':
        if not os.path.isdir('GrasperHook'):
            os.system('mkdir GrasperHook')
        os.system(f"move video2_{frame}.jpg GrasperHook")
    elif i[1]=='1' and i[4]=='1':
        if not os.path.isdir('GrasperScissors'):
            os.system('mkdir GrasperScissors')
        os.system(f"move video2_{frame}.jpg GrasperScissors")
    elif i[1]=='1' and i[5]=='1':
        if not os.path.isdir('GrasperClipper'):
            os.system('mkdir GrasperClipper')
        os.system(f"move video2_{frame}.jpg GrasperClipper")
    elif i[1]=='1' and i[6]=='1':
        if not os.path.isdir('GrasperIrrigator'):
            os.system('mkdir GrasperIrrigator')
        os.system(f"move video2_{frame}.jpg GrasperIrrigator")
    elif i[1]=='1' and i[7]=='1':
        if not os.path.isdir('GrasperSpecimenBag'):
            os.system('mkdir GrasperSpecimenBag')
        os.system(f"move video2_{frame}.jpg GrasperSpecimenBag")


    elif i[2]=='1' and i[3]=='1':
        if not os.path.isdir('BipolarHook'):
            os.system('mkdir BipolarHook')
        os.system(f"move video2_{frame}.jpg BipolarHook")
    elif i[2]=='1' and i[4]=='1':
        if not os.path.isdir('BipolarScissors'):
            os.system('mkdir BipolarScissors')
        os.system(f"move video2_{frame}.jpg BipolarScissors")
    elif i[2]=='1' and i[5]=='1':
        if not os.path.isdir('BipolarClipper'):
            os.system('mkdir BipolarClipper')
        os.system(f"move video2_{frame}.jpg BipolarClipper")
    elif i[2]=='1' and i[6]=='1':
        if not os.path.isdir('BipolarIrrigator'):
            os.system('mkdir BipolarIrrigator')
        os.system(f"move video2_{frame}.jpg BipolarIrrigator")
    elif i[2]=='1' and i[7]=='1':
        if not os.path.isdir('BipolarSpecimenBag'):
            os.system('mkdir BipolarSpecimenBag')
        os.system(f"move video2_{frame}.jpg BipolarSpecimenBag")



    elif i[3]=='1' and i[4]=='1':
        if not os.path.isdir('HookScissors'):
            os.system('mkdir HookScissors')
        os.system(f"move video2_{frame}.jpg HookScissors")
    elif i[3]=='1' and i[5]=='1':
        if not os.path.isdir('HookClipper'):
            os.system('mkdir HookClipper')
        os.system(f"move video2_{frame}.jpg HookClipper")
    elif i[3]=='1' and i[6]=='1':
        if not os.path.isdir('HookIrrigator'):
            os.system('mkdir HookIrrigator')
        os.system(f"move video2_{frame}.jpg HookIrrigator")
    elif i[3]=='1' and i[7]=='1':
        if not os.path.isdir('HookSpecimenBag'):
            os.system('mkdir HookSpecimenBag')
        os.system(f"move video2_{frame}.jpg HookSpecimenBag")



    elif i[4]=='1' and i[5]=='1':
        if not os.path.isdir('ScissorsClipper'):
            os.system('mkdir ScissorsClipper')
        os.system(f"move video2_{frame}.jpg ScissorsClipper")
    elif i[4]=='1' and i[6]=='1':
        if not os.path.isdir('ScissorsIrrigator'):
            os.system('mkdir ScissorsIrrigator')
        os.system(f"move video2_{frame}.jpg ScissorsIrrigator")
    elif i[4]=='1' and i[7]=='1':
        if not os.path.isdir('ScissorsSpecimenBag'):
            os.system('mkdir ScissorsSpecimenBag')
        os.system(f"move video2_{frame}.jpg ScissorsSpecimenBag")
    


    elif i[5]=='1' and i[6]=='1':
        if not os.path.isdir('ClipperIrrigator'):
            os.system('mkdir ClipperIrrigator')
        os.system(f"move video2_{frame}.jpg ClipperIrrigator")
    elif i[5]=='1' and i[7]=='1':
        if not os.path.isdir('ClipperSpecimenBag'):
            os.system('mkdir ClipperSpecimenBag')
        os.system(f"move video2_{frame}.jpg ClipperSpecimenBag")


    elif i[6]=='1' and i[7]=='1':
        if not os.path.isdir('IrrigatorSpecimenBag'):
            os.system('mkdir IrrigatorSpecimenBag')
        os.system(f"move video2_{frame}.jpg IrrigatorSpecimenBag")



    elif i[1]=="1":
        if not os.path.isdir('Grasper'):
            os.system('mkdir Grasper')
        os.system(f"move video2_{frame}.jpg Grasper")
    elif i[2]=="1":
        if not os.path.isdir('Bipolar'):
            os.system('mkdir Bipolar')
        os.system(f"move video2_{frame}.jpg Bipolar")
    elif i[3]=="1":
        if not os.path.isdir('Hook'):
            os.system('mkdir Hook')
        os.system(f"move video2_{frame}.jpg Hook")
    elif i[4]=="1":
        if not os.path.isdir('Scissors'):
            os.system('mkdir Scissors')
        os.system(f"move video2_{frame}.jpg Scissors")
    elif i[5]=="1":
        if not os.path.isdir('Clipper'):
            os.system('mkdir Clipper')
        os.system(f"move video2_{frame}.jpg Clipper")
    elif i[6]=="1":
        if not os.path.isdir('Irrigator'):
            os.system('mkdir Irrigator')
        os.system(f"move video2_{frame}.jpg Irrigator")
    elif i[7]=="1":
        if not os.path.isdir('SpecimenBag'):
            os.system('mkdir SpecimenBag')
        os.system(f"move video2_{frame}.jpg SpecimenBag")
    else:
        if not os.path.isdir('No_tool'):
            os.system('mkdir No_tool')
        os.system(f"move video2_{frame}.jpg No_tool")
