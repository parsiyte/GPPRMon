from PIL import ImageFont

''' cta_id -> thread block id 
    cluster_id -> SM id
    kernel -> kernel id
    cta_iss is the cta information for the issued cta
      cta_iss[i] -> i'th item of the instruction in cta || cta_iss[i]['pc'] -> hex
      cta_iss[i]['opcode'] -> opcode of the corresponding warp instruction
      cta_iss[i]['operands'] -> operands of the corresponding warp instruction
      cta_iss[i]['warps'] -> this is a list including active warps in CTA []
      cta_iss[i]['cycle'] -> this is a list including the issue cycles of the warps within in CTA []
    cta_comp[i] -> i'th item 
      cta_comp[i]['pc'] -> pc of the CTA for some of the warps
      cta_comp[i]['warps'] -> this is a list including active warps in CTA []
      cta_comp[i]['cycle'] -> this is a list including the issue cycles of the warps within in CTA []  '''

def plotCTAonSM(image, cta_id, cid, kid, issued, completed, l1d, l1d_rgb, ipc_cluster, power_core,
                int_start, int_finish):

  image.rectangle([(2, 2), (1918, 1078)], outline = "white", fill = (255, 255, 130))
  font_title = ImageFont.truetype('FreeMonoBold.ttf', 20)

  #upper line
  image.line([(5, 5), (1915, 5)], fill = (255,20,20), width = 2)    

  image.rectangle([(10, 10), (50, 850)], fill = (0,255,20), width = 2)    
  image.text((11, 11), "PC" , font = font_title, fill=(0, 0, 0))
  image.line([(5, 5), (5, 855)], fill = (255,20,20), width = 2)    
 
  image.rectangle([(60, 10), (200, 850)], fill = (40, 175, 100), width = 2)    
  image.text((61, 11), "OPCODE" , font = font_title, fill=(0, 0, 0))
  image.line([(55, 5), (55, 855)], fill = (255,20,20), width = 2)    

  image.rectangle([(210, 10), (650, 850)], fill = (200, 150, 180), width = 2)    
  image.text((210, 11), "OPERAND" , font = font_title, fill=(0, 0, 0))
  image.line([(205, 5), (205, 855)], fill = (255,20,20), width = 2)    

  image.rectangle([(660, 10), (1910, 850)], fill = (140, 255, 255), width = 2)    
  image.text((1200, 11), "ISSUE/COMPLETION" , font = font_title, fill=(0, 0, 0))
  image.line([(655, 5), (655, 855)], fill = (255,20,20), width = 2)    
  image.line([(1915, 5), (1915, 855)], fill = (255,20,20), width = 2)

  #bottom line
  image.line([(5, 855), (1915, 855)], fill = (255,20,20), width = 2)    

  font_data = ImageFont.truetype('FreeSerif.ttf', 18)
  font_cycle_wid = ImageFont.truetype('FreeSerif.ttf', 10)

  image.line([(5, 40), (1915, 40)], fill = (0,0,0), width = 1)    
  for i in range(0, len(issued)):
    image.text((11, 20 + (i + 1) * 20),  str(issued[i]['pc']) , font = font_data, fill=(0, 0, 0))
    image.text((60, 20 + (i + 1) * 20),  str(issued[i]['opcode']) , font = font_data, fill=(0, 0, 0))
    image.text((210, 20 + (i + 1) * 20), str(issued[i]['operand']) , font = font_data, fill=(0, 0, 0))
    image.line([(5, 20 + (i + 2) * 20), (1915, 20 + (i + 2) * 20)], fill = (0,0,0), width = 1)    
    for j in range(0, len(issued[i]['warps'])):
      image.text((660 + j * 60, 20 + (i + 1) * 20), str(issued[i]['warps'][j]) + '-' 
                      + str(issued[i]['cycle'][j]) , font = font_cycle_wid, fill=(0, 0, 0))
    
    for j in range(0, len(completed)):
      if issued[i]['pc'] == completed[j]['pc']:
        for k in range(0, len(completed[j]['warps'])):
          image.text((660 + k * 60, 30 + (i + 1) * 20),  str(completed[j]['warps'][k]) + '-'
                          + str(completed[j]['cycle'][k]) , font = font_cycle_wid, fill=(0, 0, 0))

  headline = (0,130,0)
  font_title = ImageFont.truetype('FreeMonoBold.ttf', 20)
  font_text = ImageFont.truetype('FreeMonoBold.ttf', 20) 

  image.rectangle([(350, 940), (700, 1070)], outline = "white", fill = (150, 200, 200))
  image.text((355, 945),      "Interval   : ", font = font_title, fill=(0, 0, 0))
  image.text((355, 945 + 30), "SM ID      : ", font = font_title, fill=(0, 0, 0))
  image.text((355, 945 + 60), "Kernel ID  : ", font = font_title, fill=(0, 0, 0))
  image.text((355, 945 + 90), "ThrdBlck ID: ", font = font_title, fill=(0, 0, 0))
  image.text((500, 945), str(int_start) + "-" + str(int_finish), font = font_text, fill=(0, 0, 0))
  image.text((500, 945 + 30), str(cid) ,font = font_text, fill=(0, 0, 0))
  image.text((500, 945 + 60), str(kid) ,font = font_text, fill=(0, 0, 0))
  image.text((500, 945 + 90), str(cta_id) ,font = font_text, fill=(0, 0, 0))

  # Execution Units
  image.rectangle([(705, 905), (770+125, 1070)], outline = "white", fill = (200, 50, 50))
  image.text((710, 880 + 30 ), "PeakDynm(W)   : ", font = font_title, fill=(0, 0, 0))
  image.text((710, 880 + 60 ), "PeakDynmEn(E) : ", font = font_title, fill=(0, 0, 0))
  image.text((710, 880 + 90 ), "SubThreshL(W) : ", font = font_title, fill=(0, 0, 0))
  image.text((710, 880 + 120), "GateLeakage(W): ", font = font_title, fill=(0, 0, 0))
  image.text((710, 880 + 150), "RunTimeDynm(W): ", font = font_title, fill=(0, 0, 0))

#  font_title = ImageFont.truetype('FreeSerif.ttf', 20)
  image.rectangle([(775+125, 870), (900+125, 905)], outline = "white", fill = headline)
  image.rectangle([(775+125, 905), (900+125, 1070)], outline = "white", fill = (50, 100, 150))
  image.text((780+125, 880), "Exe-Units", font = font_title, fill=(0, 0, 0))
  image.text((780+125, 880 + 30), '{:.3f}'.format(power_core['eu_core']['PeakDynamic(W)']) , font = font_text, fill=(0, 0, 0))
  image.text((780+125, 880 + 60), '{:.3f}'.format(power_core['eu_core']['PeakDynamicEnergy(W)']), font = font_text, fill=(0, 0, 0))
  image.text((780+125, 880 + 90), '{:.3f}'.format(power_core['eu_core']['SubthresholdLeakage(W)']), font = font_text, fill=(0, 0, 0))
  image.text((780+125, 880 + 120), '{:.3f}'.format(power_core['eu_core']['GateLeakage(W)']), font = font_text, fill=(0, 0, 0))
  image.text((780+125, 880 + 150), '{:.3f}'.format(power_core['eu_core']['RunTimeDynamic(W)']), font = font_text, fill=(0, 0, 0))

  # Instruction functionals
  image.rectangle([(905+125, 870), (1030+125, 1070)], outline = "white", fill = (100, 255, 100))
  image.rectangle([(905+125, 870), (1030+125, 905)], outline = "white", fill = headline)
  image.text((910+125, 880), "Func-Units", font = font_title, fill=(0, 0, 0))
  image.text((910+125, 880 + 30), '{:.3f}'.format(power_core['inst_fu_core']['PeakDynamic(W)']), font = font_text, fill=(0, 0, 0))
  image.text((910+125, 880 + 90), '{:.3f}'.format(power_core['inst_fu_core']['SubthresholdLeakage(W)']), font = font_text, fill=(0, 0, 0))
  image.text((910+125, 880 + 120), '{:.3f}'.format(power_core['inst_fu_core']['GateLeakage(W)']), font = font_text, fill=(0, 0, 0))
  image.text((910+125, 880 + 150), '{:.3f}'.format(power_core['inst_fu_core']['RunTimeDynamic(W)']), font = font_text, fill=(0, 0, 0))

  # Load Store Units
  image.rectangle([(1035+125, 870), (1160+125, 1070)], outline = "white", fill = (125, 125, 100))
  image.rectangle([(1035+125, 870), (1160+125, 905)], outline = "white", fill = headline)
  image.text((1040+125, 880), "Ld/Str-Uni", font = font_title, fill=(0, 0, 0))
  image.text((1040+125, 880 + 30), '{:.3f}'.format(power_core['ldst_core']['PeakDynamic(W)']), font = font_text, fill=(0, 0, 0))
  image.text((1040+125, 880 + 90), '{:.3f}'.format(power_core['ldst_core']['SubthresholdLeakage(W)']), font = font_text, fill=(0, 0, 0))
  image.text((1040+125, 880 + 120), '{:.3f}'.format(power_core['ldst_core']['GateLeakage(W)']), font = font_text, fill=(0, 0, 0))
  image.text((1040+125, 880 + 150), '{:.3f}'.format(power_core['ldst_core']['RunTimeDynamic(W)']), font = font_text, fill=(0, 0, 0))

  # Idle consumption on core
  image.rectangle([(1165+125, 870), (1290+125, 1070)], outline = "white", fill = (200, 100, 50))
  image.rectangle([(1165+125, 870), (1290+125, 905)], outline = "white", fill = headline)
  image.text((1170+125, 880), "Idle-Core", font = font_title, fill=(0, 0, 0))
  image.text((1170+125, 880 + 150), '{:.3f}'.format(power_core['idle_core']['RunTimeDynamic(W)']), font = font_text, fill=(0, 0, 0))

  # Total on Cores
  image.rectangle([(1295 + 125, 870), (1420 + 120, 1070)], outline = "white", fill = (50, 100, 200))
  image.rectangle([(1295 + 125, 870), (1420 + 120, 905)], outline = "white", fill = headline)
  image.text((1300 + 125, 880), "Tot Core", font = font_title, fill=(0, 0, 0))
  image.text((1300 + 125, 880 + 30),  '{:.3f}'.format(power_core['total_core']['PeakDynamic(W)']), font = font_text, fill=(0, 0, 0))
  image.text((1300 + 125, 880 + 90),  '{:.3f}'.format(power_core['total_core']['SubthresholdLeakage(W)']), font = font_text, fill=(0, 0, 0))
  image.text((1300 + 125, 880 + 120), '{:.3f}'.format(power_core['total_core']['GateLeakage(W)']), font = font_text, fill=(0, 0, 0))
  image.text((1300 + 125, 880 + 150), '{:.3f}'.format(power_core['total_core']['RunTimeDynamic(W)']), font = font_text, fill=(0, 0, 0))

  image.rectangle([(1545, 870), (1645, 905)], outline = "white", fill = headline)
  image.rectangle([(1545, 905), (1645, 950)], outline = "white", fill = (240, 100, 150))
  image.text((1547, 880), "IPC Rate", font = font_title, fill=(0, 0, 0))
  image.text((1550, 40 + 880), '{:.3f}'.format(ipc_cluster), font = font_text, fill=(0, 0, 0))
  
  image.rectangle([(1650, 870), (1910, 1070)], outline = "white", fill = (l1d_rgb[0], l1d_rgb[1], l1d_rgb[2]))
  image.text((1690, 880), "L1D Cache Stats", font = font_title, fill=(0, 0, 0))
  image.text((1660, 40 + 880),      "Hit Rate  : " + '{:.3f}'.format(l1d[0]) , font = font_title, fill=(0, 0, 0))
  image.text((1660, 40 + 880),      "Hit Rate  : " + '{:.3f}'.format(l1d[0]) , font = font_title, fill=(0, 0, 0))
  image.text((1660, 40 + 900),      "Hit Res   : " + '{:.3f}'.format(l1d[1]) , font = font_title, fill=(0, 0, 0))
  image.text((1660, 40 + 900 + 20), "Miss Rate : " + '{:.3f}'.format(l1d[2]) , font = font_title, fill=(0, 0, 0))
  image.text((1660, 40 + 900 + 40), "Res Fail  : " + '{:.3f}'.format(l1d[3]) , font = font_title, fill=(0, 0, 0))
  image.text((1660, 40 + 900 + 60), "SecMiss R : " + '{:.3f}'.format(l1d[4]) , font = font_title, fill=(0, 0, 0))
  image.text((1660, 40 + 900 + 80), "MSHR Hit R: " + '{:.3f}'.format(l1d[5]) , font = font_title, fill=(0, 0, 0))

  return image

