from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def plot_GV100(im, l1d, l2, dram, kernel, start, finish, l1d_rgb, l2_rgb, dram_rgb, power):

  font_l1d = ImageFont.truetype('FreeSerif.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 11)
  # L1D [0, 44]
  for i in range(0, 8):
    im.rectangle([(5 + (i*87), 5), (85 + (i*87), 90)], outline = "white", fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    im.text((7 + (i*87), 7), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    im.text((10 + (i*87), 22), "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 33), "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 44), "M : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 55), "RF: " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 66), "SM: " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 77), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0, 0, 0))

#    im.rectangle([(5 + (i*87), 95), (85 + (i*87), 180)], outline = "white", fill = (l1d_rgb[i+22][0], l1d_rgb[i+22][1], l1d_rgb[i+22][2]))
#    im.text((7 + (i*87), 97), "L1 Data-" + str(i + 22), font = font_l1d, fill=(0, 0, 0))
#    im.text((10 + (i*87), 112), "H : " + '{:.4f}'.format(l1d[i+22][0]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 123), "HR: " + '{:.4f}'.format(l1d[i+22][1]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 134), "M : " + '{:.4f}'.format(l1d[i+22][2]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 145), "RF: " + '{:.4f}'.format(l1d[i+22][3]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 156), "SM: " + '{:.4f}'.format(l1d[i+22][4]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 167), "MH: " + '{:.4f}'.format(l1d[i+22][5]), font = font_l1d_data, fill=(0, 0, 0))

  ## NOCs
  im.rectangle([(5, 185), (1915, 210)], outline = "white", fill = (255, 20, 20))
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 20)
  im.text((180+16, 188), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475, 188), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 2, 188), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 3, 188), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  font_l2 = ImageFont.truetype('FreeSerif.ttf', 15)
  font_l2_data = ImageFont.truetype('FreeSerif.ttf', 11)
  for i in range(0, 16):
    im.rectangle([(5 + (i*119), 215), (115 + (i*119), 275)], outline = "white", fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    im.text((8 + (i*119), 217), "L2 Cache - " + str(i), font = font_l2, fill=(0, 0, 0))
    im.text((8 + (i*119), 234),  "H : " + '{:.3f}'.format(l2[i][0]),  font = font_l2_data, fill=(0,0,0))
    im.text((8 + (i*119), 245),  "HR: " + '{:.3f}'.format(l2[i][1]),  font = font_l2_data, fill=(0,0,0))
    im.text((8 + (i*119), 256),  "M : " + '{:.3f}'.format(l2[i][2]),  font = font_l2_data, fill=(0,0,0))
    im.text((67 + (i*119), 234), "RF: " + '{:.3f}'.format(l2[i][3]), font = font_l2_data, fill=(0,0,0))
    im.text((67 + (i*119), 245), "SM: " + '{:.3f}'.format(l2[i][4]), font = font_l2_data, fill=(0,0,0))
    im.text((67 + (i*119), 256), "MH: " + '{:.3f}'.format(l2[i][5]), font = font_l2_data, fill=(0,0,0))

#    im.rectangle([(5 + (i*119), 280), (115 + (i*119), 340)], outline = "white", fill = (l2_rgb[i+16][0], l2_rgb[i+16][1], l2_rgb[i+16][2]))
#    im.text((8 + (i*119), 282), "L2 Cache - " + str(i + 16), font = font_l1d, fill=(0, 0, 0))
#    im.text((8 + (i*119), 299),  "H : " + '{:.3f}'.format(l2[i+16][0]),  font = font_l2_data, fill=(0,0,0))
#    im.text((8 + (i*119), 310),  "HR: " + '{:.3f}'.format(l2[i+16][1]),  font = font_l2_data, fill=(0,0,0))
#    im.text((8 + (i*119), 321),  "M : " + '{:.3f}'.format(l2[i+16][2]),  font = font_l2_data, fill=(0,0,0))
#    im.text((67 + (i*119), 299), "RF: " + '{:.3f}'.format(l2[i+16][3]), font = font_l2_data, fill=(0,0,0))
#    im.text((67 + (i*119), 310), "SM: " + '{:.3f}'.format(l2[i+16][4]), font = font_l2_data, fill=(0,0,0))
#    im.text((67 + (i*119), 321), "MH: " + '{:.3f}'.format(l2[i+16][5]), font = font_l2_data, fill=(0,0,0))

  font_dram = ImageFont.truetype('FreeSerif.ttf', 15)
  font_dram_data = ImageFont.truetype('FreeMonoBold.ttf', 11)
  for i in range(0, 8):
    im.rectangle([(5 + (i*119), 345), (115 + (i*119), 420)], outline = "white", fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    im.text((8 + (i*119), 350), "Dram Bank - " + str(i), font = font_dram, fill=(0, 0, 0)) #L2 [24, 31]
    im.text((8 + (i*119), 370), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_dram_data, fill=(0,0,0))
    im.text((8 + (i*119), 385), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_dram_data, fill=(0,0,0))

#    im.rectangle([(5 + (i*119), 425), (115 + (i*119), 500)], outline = "white", fill = (dram_rgb[i+16][0], dram_rgb[i+16][1], dram_rgb[i+16][2]))
#    im.text((8 + (i*119), 430), "Dram Bank - " + str(i + 16), font = font_dram, fill=(0, 0, 0)) #L2 [24, 31]
#    im.text((8 + (i*119), 450), "RB-H: " + '{:.4f}'.format(dram[i+16][0]), font = font_dram_data, fill=(0,0,0))
#    im.text((8 + (i*119), 465), "RB-M: " + '{:.4f}'.format(dram[i+16][1]), font = font_dram_data, fill=(0,0,0))

#  for i in range(0, 16):
#    im.rectangle([(5 + (i*119), 505), (115 + (i*119), 565)], outline = "white", fill = (l2_rgb[i+32][0], l2_rgb[i+32][1], l2_rgb[i+32][2]))
#    im.text((8 + (i*119), 507), "L2 Cache - " + str(i+32), font = font_l2, fill=(0, 0, 0))
#    im.text((8 + (i*119), 524),  "H : " + '{:.3f}'.format(l2[i+32][0]),  font = font_l2_data, fill=(0,0,0))
#    im.text((8 + (i*119), 535),  "HR: " + '{:.3f}'.format(l2[i+32][1]),  font = font_l2_data, fill=(0,0,0))
#    im.text((8 + (i*119), 545),  "M : " + '{:.3f}'.format(l2[i+32][2]),  font = font_l2_data, fill=(0,0,0))
#    im.text((67 + (i*119), 524), "RF: " + '{:.3f}'.format(l2[i+32][3]), font = font_l2_data, fill=(0,0,0))
#    im.text((67 + (i*119), 535), "SM: " + '{:.3f}'.format(l2[i+32][4]), font = font_l2_data, fill=(0,0,0))
#    im.text((67 + (i*119), 545), "MH: " + '{:.3f}'.format(l2[i+32][5]), font = font_l2_data, fill=(0,0,0))

#    im.rectangle([(5 + (i*119), 570), (115 + (i*119), 630)], outline = "white", fill = (l2_rgb[i+48][0], l2_rgb[i+48][1], l2_rgb[i+48][2]))
#    im.text((8 + (i*119),  572), "L2 Cache - " + str(i + 48), font = font_l1d, fill=(0, 0, 0))
#    im.text((8 + (i*119), 589),  "H : " + '{:.3f}'.format(l2[i+48][0]),  font = font_l2_data, fill=(0,0,0))
#    im.text((8 + (i*119), 600),  "HR: " + '{:.3f}'.format(l2[i+48][1]),  font = font_l2_data, fill=(0,0,0))
#    im.text((8 + (i*119), 611),  "M : " + '{:.3f}'.format(l2[i+48][2]),  font = font_l2_data, fill=(0,0,0))
#    im.text((67 + (i*119), 589), "RF: " + '{:.3f}'.format(l2[i+48][3]), font = font_l2_data, fill=(0,0,0))
#    im.text((67 + (i*119), 600), "SM: " + '{:.3f}'.format(l2[i+48][4]), font = font_l2_data, fill=(0,0,0))
#    im.text((67 + (i*119), 611), "MH: " + '{:.3f}'.format(l2[i+48][5]), font = font_l2_data, fill=(0,0,0))

  im.rectangle([(5, 635), (1915, 660)], outline = "white", fill = (255, 20, 20))
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 20)
  im.text((180+16, 638), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475,     638), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 2, 638), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 3, 638), "NOCs", font = font_NOCs, fill=(0, 0, 0))

#  for i in range(0, 22):
#    im.rectangle([(5 + (i*87), 665), (85 + (i*87), 750)], outline = "white", fill = (l1d_rgb[i+44][0], l1d_rgb[i+44][1], l1d_rgb[i+44][2]))
#    im.text((7 + (i*87),  660 + 7), "L1 Data-" + str(i + 44), font = font_l1d, fill=(0, 0, 0))
#    im.text((10 + (i*87), 660 + 22), "H : " + '{:.4f}'.format(l1d[i + 44][0]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 660 + 33), "HR: " + '{:.4f}'.format(l1d[i + 44][1]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 660 + 44), "M : " + '{:.4f}'.format(l1d[i + 44][2]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 660 + 55), "RF: " + '{:.4f}'.format(l1d[i + 44][3]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 660 + 66), "SM: " + '{:.4f}'.format(l1d[i + 44][4]), font = font_l1d_data, fill=(0, 0, 0))
#    im.text((10 + (i*87), 660 + 77), "MH: " + '{:.4f}'.format(l1d[i + 44][5]), font = font_l1d_data, fill=(0, 0, 0))
#
#    if i + 66 < 80:
#      im.rectangle([(5 + (i*87), 755), (85 + (i*87), 840)], outline = "white", fill = (l1d_rgb[i+66][0], l1d_rgb[i+66][1], l1d_rgb[i+66][2]))
#      im.text((7 + (i*87),  97  + 660), "L1 Data-" + str(i + 66), font = font_l1d, fill=(0, 0, 0))
#      im.text((10 + (i*87), 112 + 660), "H : " + '{:.4f}'.format(l1d[i+66][0]), font = font_l1d_data, fill=(0, 0, 0))
#      im.text((10 + (i*87), 123 + 660), "HR: " + '{:.4f}'.format(l1d[i+66][1]), font = font_l1d_data, fill=(0, 0, 0))
#      im.text((10 + (i*87), 134 + 660), "M : " + '{:.4f}'.format(l1d[i+66][2]), font = font_l1d_data, fill=(0, 0, 0))
#      im.text((10 + (i*87), 145 + 660), "RF: " + '{:.4f}'.format(l1d[i+66][3]), font = font_l1d_data, fill=(0, 0, 0))
#      im.text((10 + (i*87), 156 + 660), "SM: " + '{:.4f}'.format(l1d[i+66][4]), font = font_l1d_data, fill=(0, 0, 0))
#      im.text((10 + (i*87), 167 + 660), "MH: " + '{:.4f}'.format(l1d[i+66][5]), font = font_l1d_data, fill=(0, 0, 0))
#
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
  im.text((1120, 870),  " QV-100 GPU based on Volta Architecture includes 80 Streaming Multiprocessors (80 L1D Caches).", font = font_info, fill=(255,255,255)) 
  im.text((1120, 895),  " There are 32 memory partitions (32 Seperate DRAM Banks) with 2 sub-partitions (64 L2 Caches).", font = font_info, fill=(255,255,255)) 

  font_info = ImageFont.truetype('FreeSerif.ttf', 25)
  im.rectangle([(1110, 930), (1700, 1010)], outline = "white", fill = (50,50,100))
  im.text((1120, 935),  "Kernel: " + str(kernel), font = font_info, fill=(255,255,255)) 
  im.text((1120, 970),  "Cycle interval of the GPU: [" + str(start) + ", " + str(finish) + "]", font = font_info, fill=(255,255,255)) 
  return im
