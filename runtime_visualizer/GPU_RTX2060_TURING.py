from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


  # plot_RTX2060(im_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
def plot_RTX2060(im, l1d, l2, dram, kernel, start, finish, l1d_rgb, l2_rgb, dram_rgb, power):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)
  ## L1D [0, 30]
  for i in range(0, 15):
    im.rectangle([(10 + (i*126), 10), (10 + 121 + (i*126), 10 + 121)], outline = "white", 
                          fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    im.text((11 + (i*126), 11), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    im.text((11 + (i*126), 31), "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 46), "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 61), "M : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 76), "RF: " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 91), "SM: " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 106), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*126), 136), (10 + 121 + (i*126), 10 + 247)], outline = "white", 
                          fill = (l1d_rgb[i+15][0], l1d_rgb[i+15][1], l1d_rgb[i+15][2]))
    im.text((11 + (i*126), 11 + 125), "L1 Data-" + str(i + 15), font = font_l1d, fill=(0,0,0))
    im.text((11 + (i*126), 31 + 125), "H : " + '{:.4f}'.format(l1d[i + 15][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 46 + 125), "HR: " + '{:.4f}'.format(l1d[i + 15][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 61 + 125), "M : " + '{:.4f}'.format(l1d[i + 15][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 76 + 125), "RF: " + '{:.4f}'.format(l1d[i + 15][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 91 + 125), "SM: " + '{:.4f}'.format(l1d[i + 15][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*126), 106 + 125), "MH: " + '{:.4f}'.format(l1d[i + 15][5]), font = font_l1d_data, fill=(0,0,0))

  ## NOCs
  im.rectangle([(10, 265), (1910, 325)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  im.text((180+16, 275), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475, 275), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 2, 275), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 3, 275), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  ## L2 [0, 32]
  ## DRAM [0, 16]
  for i in range(0, 12):
    im.rectangle([(10 + (i*158), 330), (10 + 153 + (i*158), 430)],  outline = "white", 
                          fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    im.text((11 + (i*158), 331), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((11 + (i*158), 20 + 331), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*158), 35 + 331), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*158), 50 + 331), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + 75 + (i*158), 20 + 331), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + 75 + (i*158), 35 + 331), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + 75 + (i*158), 50 + 331), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*158), 435), (10 + 153 + (i*158), 600)], outline = "white", 
                          fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    im.text((11 + (i*158), 436), "Dram Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [24, 31]
    im.text((11 + (i*158), 20 + 436), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*158), 35 + 436), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*158), 605), (10 + 153 + (i*158), 705)], outline = "white", 
                          fill = (l2_rgb[i+12][0], l2_rgb[i+12][1], l2_rgb[i+12][2]))
    im.text((11 + (i*158), 606), "L2 Cache-" + str(i+12), font = font_l1d, fill=(0, 0, 0)) #L2 [8, 15]
    im.text((11 + (i*158), 20 + 606), "H : " + '{:.4f}'.format(l2[i + 12][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*158), 35 + 606), "HR: " + '{:.4f}'.format(l2[i + 12][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*158), 50 + 606), "M : " + '{:.4f}'.format(l2[i + 12][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + 75 + (i*158), 20 + 606), "RF: " + '{:.4f}'.format(l2[i + 12][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + 75 + (i*158), 35 + 606), "SM: " + '{:.4f}'.format(l2[i + 12][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + 75 + (i*158), 50 + 606), "MH: " + '{:.4f}'.format(l2[i + 12][5]), font = font_l1d_data, fill=(0,0,0))

  im.line([(5, 740), (1915, 740)], fill = (0,0,0), width = 4)

  power_data = ImageFont.truetype('FreeSerif.ttf', 15)
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
  im.text((1120, 870),  " RTX2060 GPU based on Volta Architecture includes 30 Streaming Multiprocessors (30 L1D caches)..", font = font_info, fill=(255,255,255)) 
  im.text((1120, 895),  " There are 12 memory partitions (12 Seperate DRAM Banks) with 2 sub-partitions (24 L2 Caches).", font = font_info, fill=(255,255,255)) 

  font_info = ImageFont.truetype('FreeSerif.ttf', 25)
  im.rectangle([(1110, 930), (1700, 1010)], outline = "white", fill = (50,50,100))
  im.text((1120, 935),  "Kernel: " + str(kernel), font = font_info, fill=(255,255,255)) 
  im.text((1120, 970),  "Cycle interval of the GPU: [" + str(start) + ", " + str(finish) + "]", font = font_info, fill=(255,255,255)) 


  return im
