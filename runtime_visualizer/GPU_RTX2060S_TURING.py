from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

  # plot_RTX2060S(im_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
def plot_RTX2060S(im, l1d, l2, dram, kernel, start, finish, l1d_rgb, l2_rgb, dram_rgb, power):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)
  ## L1D [0, 33]
  for i in range(0, 17):
    im.rectangle([(10 + (i*111), 10), (10 + 106 + (i*111), 10 + 106)], outline = "white", 
                           fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    im.text((11 + (i*111), 11), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    im.text((11 + (i*111), 11 + 18), "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 11 + 32), "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 11 + 46), "M : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 11 + 60), "RF: " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 11 + 74), "SM: " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 11 + 88), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*111), 10 + 111), (10 + 106 + (i*111), 10 + 217)], outline = "white", 
                           fill = (l1d_rgb[i+17][0], l1d_rgb[i+17][1], l1d_rgb[i+17][2]))
    im.text((11 + (i*111), 122), "L1 Data-" + str(i + 17), font = font_l1d, fill=(0,0,0))
    im.text((11 + (i*111), 122 + 18), "H : " + '{:.4f}'.format(l1d[i+17][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 122 + 32), "HR: " + '{:.4f}'.format(l1d[i+17][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 122 + 46), "M : " + '{:.4f}'.format(l1d[i+17][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 122 + 60), "RF: " + '{:.4f}'.format(l1d[i+17][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 122 + 74), "SM: " + '{:.4f}'.format(l1d[i+17][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*111), 122 + 88), "MH: " + '{:.4f}'.format(l1d[i+17][5]), font = font_l1d_data, fill=(0,0,0))

  ## NOCs
  im.rectangle([(10, 235), (1910, 295)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  im.text((180+16, 245), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475, 245), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 2, 245), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 3, 245), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  font_l2 = ImageFont.truetype('FreeMonoBold.ttf', 16)
  ## L2 [0, 31]
  for i in range(0, 8):
    im.rectangle([(10 + (i*237), 300), (10 + 232 + (i*237), 380)],  outline = "white", 
                           fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    im.text((11 + (i*237), 301), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) 
    im.text((11 + (i*237), 20 + 301), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*237), 35 + 301), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*237), 50 + 301), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 20 + 301), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 35 + 301), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 50 + 301), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*237), 385), (10 + 232 + (i*237), 465)],  outline = "white", 
                           fill = (l2_rgb[i+8][0], l2_rgb[i+8][1], l2_rgb[i+8][2]))
    im.text((11 + (i*237), 386), "L2 Cache-" + str(i + 8), font = font_l1d, fill=(0, 0, 0)) 
    im.text((11 + (i*237), 20 + 386), "H : " + '{:.4f}'.format(l2[i + 8][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*237), 35 + 386), "HR: " + '{:.4f}'.format(l2[i + 8][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*237), 50 + 386), "M : " + '{:.4f}'.format(l2[i + 8][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 20 + 386), "RF: " + '{:.4f}'.format(l2[i + 8][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 35 + 386), "SM: " + '{:.4f}'.format(l2[i + 8][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 50 + 386), "MH: " + '{:.4f}'.format(l2[i + 8][5]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*237), 655), (10 + 232 + (i*237), 735)],  outline = "white", 
                           fill = (l2_rgb[i+16][0], l2_rgb[i+16][1], l2_rgb[i+16][2]))
    im.text((11 + (i*237), 656), "L2 Cache-" + str(i + 16), font = font_l1d, fill=(0, 0, 0)) 
    im.text((11 + (i*237), 20 + 656), "H : " + '{:.4f}'.format(l2[i + 16][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*237), 35 + 656), "HR: " + '{:.4f}'.format(l2[i + 16][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*237), 50 + 656), "M : " + '{:.4f}'.format(l2[i + 16][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 20 + 656), "RF: " + '{:.4f}'.format(l2[i + 16][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 35 + 656), "SM: " + '{:.4f}'.format(l2[i + 16][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 50 + 656), "MH: " + '{:.4f}'.format(l2[i + 16][5]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*237), 740), (10 + 232 + (i*237), 820)],  outline = "white", 
                           fill = (l2_rgb[i+24][0], l2_rgb[i+24][1], l2_rgb[i+24][2]))
    im.text((11 + (i*237), 741), "L2 Cache-" + str(i + 24), font = font_l1d, fill=(0, 0, 0)) 
    im.text((11 + (i*237), 20 + 741), "H : " + '{:.4f}'.format(l2[i + 24][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*237), 35 + 741), "HR: " + '{:.4f}'.format(l2[i + 24][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*237), 50 + 741), "M : " + '{:.4f}'.format(l2[i + 24][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 20 + 741), "RF: " + '{:.4f}'.format(l2[i + 24][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 35 + 741), "SM: " + '{:.4f}'.format(l2[i + 24][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 +  115 + (i*237), 50 + 741), "MH: " + '{:.4f}'.format(l2[i + 24][5]), font = font_l1d_data, fill=(0,0,0))

  ## L2 [0, 31]
  for i in range(0, 16):
    im.rectangle([(10 + (i*118), 470), (10 + 113 + (i*118), 650)],  outline = "white", 
                           fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    im.text((11 + (i*118), 471), "DRAM Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) 
    im.text((11 + (i*118), 30 + 471), "RB-H " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*118), 50 + 471), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

  power_data = ImageFont.truetype('FreeSerif.ttf', 15)
  im.line([(5, 850), (1915, 850)], fill = (0,0,0), width = 4)
  im.rectangle([(10, 890), (200, 1000)], outline = "white", fill = (100, 150, 100))
  im.text((15, 900), "Peak Dynamic (W) : "       , font = power_data, fill=(0, 0, 0))
  im.text((15, 925), "Sub-Threshold Leakage (W): ", font = power_data, fill=(0, 0, 0))
  im.text((15, 950), "Gate Leakage (W) : "       , font = power_data, fill=(0, 0, 0))
  im.text((15, 975), "Run Time Dynamic (W) : "    , font = power_data, fill=(0, 0, 0))

  im.rectangle([(210, 860), (300, 885)], outline = "white", fill = (50, 150, 250))
  im.text((215, 865), "MC FEE", font = power_data, fill=(0, 0, 0))
  im.rectangle([(210, 890), (300, 1000)], outline = "white", fill = (150, 50, 150))
  im.text((215, 900), '{:.4f}'.format(power['mc_fee']["PeakDynamic(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((215, 925), '{:.4f}'.format(power['mc_fee']["SubthresholdLeakage(W)"]), font = power_data, fill=(0, 0, 0))
  im.text((215, 950), '{:.4f}'.format(power['mc_fee']["GateLeakage(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((215, 975), '{:.4f}'.format(power['mc_fee']["RunTimeDynamic(W)"]),      font = power_data, fill=(0, 0, 0))

  im.rectangle([(310, 860), (400, 885)], outline = "white", fill = (50, 150, 250))
  im.text((315, 865), "PHY(mc/dram)", font = power_data, fill=(0, 0, 0))
  im.rectangle([(310, 890), (400, 1000)], outline = "white", fill = (150, 250, 50))
  im.text((315, 900), '{:.4f}'.format(power['mc_phy']["PeakDynamic(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((315, 925), '{:.4f}'.format(power['mc_phy']["SubthresholdLeakage(W)"]), font = power_data, fill=(0, 0, 0))
  im.text((315, 950), '{:.4f}'.format(power['mc_phy']["GateLeakage(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((315, 975), '{:.4f}'.format(power['mc_phy']["RunTimeDynamic(W)"]),      font = power_data, fill=(0, 0, 0))

  im.rectangle([(410, 860), (500, 885)], outline = "white", fill = (50, 150, 250))
  im.text((415, 865), "MC-TE(BEE)", font = power_data, fill=(0, 0, 0))
  im.rectangle([(410, 890), (500, 1000)], outline = "white", fill = (150, 50, 250))
  im.text((415, 900), '{:.4f}'.format(power['mc_te']["PeakDynamic(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((415, 925), '{:.4f}'.format(power['mc_te']["SubthresholdLeakage(W)"]), font = power_data, fill=(0, 0, 0))
  im.text((415, 950), '{:.4f}'.format(power['mc_te']["GateLeakage(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((415, 975), '{:.4f}'.format(power['mc_te']["RunTimeDynamic(W)"]),      font = power_data, fill=(0, 0, 0))

  im.rectangle([(510, 860), (600, 885)], outline = "white", fill = (50, 150, 250))
  im.text((525, 865), "DRAM", font = power_data, fill=(0, 0, 0))
  im.rectangle([(510, 890), (600, 1000)], outline = "white", fill = (150, 50, 250))
  im.text((515, 900), '{:.4f}'.format(power['mc_total']["PeakDynamic(W)"] - 
                                      (power['mc_te']["PeakDynamic(W)"] + power['mc_phy']["PeakDynamic(W)"] + power['mc_fee']["PeakDynamic(W)"])),
                                      font = power_data, fill=(0, 0, 0))
  im.text((515, 925), '{:.4f}'.format(power['mc_total']["SubthresholdLeakage(W)"] - 
                                      (power['mc_te']["SubthresholdLeakage(W)"] + power['mc_phy']["SubthresholdLeakage(W)"] + power['mc_fee']["SubthresholdLeakage(W)"])),
                                      font = power_data, fill=(0, 0, 0))
  im.text((515, 950), '{:.4f}'.format(power['mc_total']["GateLeakage(W)"] - 
                                      (power['mc_te']["GateLeakage(W)"] + power['mc_phy']["GateLeakage(W)"] + power['mc_fee']["GateLeakage(W)"])),
                                      font = power_data, fill=(0, 0, 0))
  im.text((515, 975), '{:.4f}'.format(power['mc_total']["RunTimeDynamic(W)"] - 
                                      (power['mc_te']["RunTimeDynamic(W)"] + power['mc_phy']["RunTimeDynamic(W)"] + power['mc_fee']["RunTimeDynamic(W)"])),
                                      font = power_data, fill=(0, 0, 0))

  im.rectangle([(610, 860), (700, 885)], outline = "white", fill = (50, 150, 250))
  im.text((625, 865), "TOTAL", font = power_data, fill=(0, 0, 0))
  im.rectangle([(610, 890), (700, 1000)], outline = "white", fill = (250, 150, 50))
  im.text((615, 900), '{:.4f}'.format(power['mc_total']["PeakDynamic(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((615, 925), '{:.4f}'.format(power['mc_total']["SubthresholdLeakage(W)"]), font = power_data, fill=(0, 0, 0))
  im.text((615, 950), '{:.4f}'.format(power['mc_total']["GateLeakage(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((615, 975), '{:.4f}'.format(power['mc_total']["RunTimeDynamic(W)"]),      font = power_data, fill=(0, 0, 0))

  font_info = ImageFont.truetype('FreeSerif.ttf', 18)
  im.rectangle([(800, 860), (1100, 1045)], outline = "white", fill = (20,20,20))
  im.text((810, 870),  " - H -> Hit", font = font_info, fill=(255,255,255)) 
  im.text((810, 895),  " - HR -> Hit Reserved", font = font_info, fill=(255,255,255)) 
  im.text((810, 920),  " - M -> Miss", font = font_info, fill=(255,255,255)) 
  im.text((810, 945),  " - RF -> Reservation Failure", font = font_info, fill=(255,255,255)) 
  im.text((810, 970),  " - SM -> Sector Miss", font = font_info, fill=(255,255,255)) 
  im.text((810, 995),  " - MH -> MSHR Hit", font = font_info, fill=(255,255,255)) 
  im.text((810, 1020), " - RB-H/M -> Row Buffer Hit/Miss", font = font_info, fill=(255,255,255)) 

  im.rectangle([(1110, 860), (1880, 920)], outline = "white", fill = (20,20,20))
  im.text((1120, 870),  " RTX2060S GPU based on Turing Architecture includes 34 Streaming Multiprocessors (34 L1D cache). .", font = font_info, fill=(255,255,255)) 
  im.text((1120, 895),  " There are 16 memory partitions (16 Seperate DRAM Banks) with 2 sub-partitions (32 L2 Caches).", font = font_info, fill=(255,255,255)) 

  font_info = ImageFont.truetype('FreeSerif.ttf', 25)
  im.rectangle([(1110, 930), (1700, 1010)], outline = "white", fill = (50,50,100))
  im.text((1120, 935),  "Kernel: " + str(kernel), font = font_info, fill=(255,255,255)) 
  im.text((1120, 970),  "Cycle interval of the GPU: [" + str(start) + ", " + str(finish) + "]", font = font_info, fill=(255,255,255)) 


  return im
