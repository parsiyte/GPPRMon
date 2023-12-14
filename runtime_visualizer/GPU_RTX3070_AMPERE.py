from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#   plot_RTX3070(im_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
def plot_RTX3070(im, l1d, l2, dram, kernel, start, finish, l1d_rgb, l2_rgb, dram_rgb, power):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)
  ## L1D [0, 45]
  for i in range(0, 16):
    im.rectangle([(5 + (i*118), 5), (5 + 110 + (i*118), 110)], outline = "white", fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    im.text((8 + (i*118), 8), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    im.text((8 + (i*118), 29 - 3), "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 29 - 3 + 13), "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 29 - 3 + 26), "M : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 29 - 3 + 39), "RF: " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 29 - 3 + 52), "SM: " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 29 - 3 + 65), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0, 0, 0))

    im.rectangle([(5 + (i*118), 115), (5 + 110 + (i*118), 220)], outline = "white", 
                         fill = (l1d_rgb[i+16][0], l1d_rgb[i+16][1], l1d_rgb[i+16][2]))
    im.text((8 + (i*118), 110 + 8), "L1 Data-" + str(i + 16), font = font_l1d, fill=(0, 0, 0))
    im.text((8 + (i*118), 110 - 3 + 29), "H : " + '{:.4f}'.format(l1d[i+16][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 110 - 3 + 29 + 13), "HR: " + '{:.4f}'.format(l1d[i+16][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 110 - 3 + 29 + 26), "M : " + '{:.4f}'.format(l1d[i+16][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 110 - 3 + 29 + 39), "RF: " + '{:.4f}'.format(l1d[i+16][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 110 - 3 + 29 + 52), "SM: " + '{:.4f}'.format(l1d[i+16][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 110 - 3 + 29 + 65), "MH: " + '{:.4f}'.format(l1d[i+16][5]), font = font_l1d_data, fill=(0, 0, 0))

    if (i + 32 <= 45):
      im.rectangle([(5 + (i*118), 225), (5 + 110 + (i*118), 340)], outline = "white", fill = (l1d_rgb[i+32][0], l1d_rgb[i+32][1], l1d_rgb[i+32][2]))
      im.text((8 + (i*118), 225 - 3 + 11), "L1 Data-" + str(i + 32), font = font_l1d, fill=(0, 0, 0))
      im.text((8 + (i*118), 225 - 3 + 29), "H : " + '{:.4f}'.format(l1d[i+32][0]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((8 + (i*118), 225 - 3 + 29 + 13), "HR: " + '{:.4f}'.format(l1d[i+32][1]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((8 + (i*118), 225 - 3 + 29 + 26), "M : " + '{:.4f}'.format(l1d[i+32][2]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((8 + (i*118), 225 - 3 + 29 + 39), "RF: " + '{:.4f}'.format(l1d[i+32][3]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((8 + (i*118), 225 - 3 + 29 + 52), "SM: " + '{:.4f}'.format(l1d[i+32][4]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((8 + (i*118), 225 - 3 + 29 + 65), "MH: " + '{:.4f}'.format(l1d[i+32][5]), font = font_l1d_data, fill=(0, 0, 0))

  ## NOCs
  im.rectangle([(5, 350), (1915, 375)], outline = "white", fill = (255, 20, 20))
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 20)
  im.text((180+16, 353), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475,     353), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 2, 353), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 3, 353), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  for i in range (0, 8):
    im.rectangle([(5 + (i*236), 385), (5 + 230 + (i*236), 455)],  outline = "white", fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    im.text((8 + (i*236), 388), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((8 + (i*236), 388 + 20), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*236), 388 + 35), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*236), 388 + 50), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 388 + 20), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 388 + 35), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 388 + 50), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0, 0, 0))

    im.rectangle([(5 + (i*236), 460), (5 + 230 + (i*236), 530)],  outline = "white", fill = (l2_rgb[i+8][0], l2_rgb[i+8][1], l2_rgb[i+8][2]))
    im.text((8 + (i*236), 463), "L2 Cache-" + str(i + 8), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((8 + (i*236), 463 + 20), "H : " + '{:.4f}'.format(l2[i + 8][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*236), 463 + 35), "HR: " + '{:.4f}'.format(l2[i + 8][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*236), 463 + 50), "M : " + '{:.4f}'.format(l2[i + 8][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 463 + 20), "RF: " + '{:.4f}'.format(l2[i + 8][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 463 + 35), "SM: " + '{:.4f}'.format(l2[i + 8][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 463 + 50), "MH: " + '{:.4f}'.format(l2[i + 8][5]), font = font_l1d_data, fill=(0, 0, 0))

    im.rectangle([(5 + (i*236), 535), (5 + 230 + (i*236), 605)],  outline = "white", fill = (l2_rgb[i+16][0], l2_rgb[i+16][1], l2_rgb[i+16][2]))
    im.text((8 + (i*236), 538), "L2 Cache-" + str(i + 16), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((8 + (i*236), 538 + 20), "H : " + '{:.4f}'.format(l2[i + 16][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*236), 538 + 35), "HR: " + '{:.4f}'.format(l2[i + 16][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*236), 538 + 50), "M : " + '{:.4f}'.format(l2[i + 16][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 538 + 20), "RF: " + '{:.4f}'.format(l2[i + 16][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 538 + 35), "SM: " + '{:.4f}'.format(l2[i + 16][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 538 + 50), "MH: " + '{:.4f}'.format(l2[i + 16][5]), font = font_l1d_data, fill=(0, 0, 0))

    im.rectangle([(5 + (i*236), 610), (5 + 230 + (i*236), 680)],  outline = "white", 
                          fill = (l2_rgb[i+24][0], l2_rgb[i+24][1], l2_rgb[i+24][2]))
    im.text((8 + (i*236), 613), "L2 Cache-" + str(i + 24), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((8 + (i*236), 613 + 20), "H : " + '{:.4f}'.format(l2[i + 24][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*236), 613 + 35), "HR: " + '{:.4f}'.format(l2[i + 24][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*236), 613 + 50), "M : " + '{:.4f}'.format(l2[i + 24][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 613 + 20), "RF: " + '{:.4f}'.format(l2[i + 24][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 613 + 35), "SM: " + '{:.4f}'.format(l2[i + 24][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + 115 + (i*236), 613 + 50), "MH: " + '{:.4f}'.format(l2[i + 24][5]), font = font_l1d_data, fill=(0, 0, 0))

  ## DRAM [0, 15]
  for i in range(0, 16):
    im.rectangle([(5 +(i*118), 690), (10+ 110 + (i*118), 800)], outline = "white", fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    im.text((8 + (i*118), 695), "DRAM Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [24, 31]
    im.text((8 + (i*118), 695 + 40), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((8 + (i*118), 695 + 60), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0, 0, 0))

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
  im.text((1120, 870),  " RTX-3070 GPU based on Ampere Architecture includes 46 Streaming Multiprocessors (46 L1D caches). ", font = font_info, fill=(255,255,255)) 
  im.text((1120, 895),  " There are 16 memory partitions (16 Seperate DRAM Banks) with 2 sub-partitions (32 L2 Caches). ", font = font_info, fill=(255,255,255)) 

  font_info = ImageFont.truetype('FreeSerif.ttf', 25)
  im.rectangle([(1110, 930), (1700, 1010)], outline = "white", fill = (50,50,100))
  im.text((1120, 935),  "Kernel: " + str(kernel), font = font_info, fill=(255,255,255)) 
  im.text((1120, 970),  "Cycle interval of the GPU: [" + str(start) + ", " + str(finish) + "]", font = font_info, fill=(255,255,255)) 


  return im

