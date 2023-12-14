from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#    plot_TITANX(im_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
def plot_TITANX(im, l1d, l2, dram, kernel, start, finish, l1d_rgb, l2_rgb, dram_rgb, power):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)
  for i in range(0, 14):
  ## L1D [0, 28]
    im.rectangle([(10 + (i*135), 10), (10 + 130 + (i*135), 10 + 130)], outline = "white", 
                          fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    im.text((11 + (i*135), 11), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    im.text((11 + (i*135), 31),  "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 46),  "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 61), "M : " + '{:.4f}'.format( l1d[i][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 76), "RF: " + '{:.4f}'.format( l1d[i][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 91), "SM: " + '{:.4f}'.format( l1d[i][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 106), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*135), 10 + 135), (10 + (i*135) + 130, 10 + 135 + 130)], outline = "white", 
                          fill = (l1d_rgb[i+14][0], l1d_rgb[i+14][1], l1d_rgb[i+14][2]))
    im.text((11 + (i*135), 11 + 135), "L1 Data-" + str(i + 14), font = font_l1d, fill=(0,0,0))
    im.text((11 + (i*135), 31 + 135),  "H : " + '{:.4f}'.format(l1d[i + 14][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 46 + 135),  "HR: " + '{:.4f}'.format(l1d[i + 14][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 61 + 135), "M : " + '{:.4f}'.format(l1d[i + 14][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 76 + 135), "RF: " + '{:.4f}'.format(l1d[i + 14][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 91 + 135), "SM: " + '{:.4f}'.format(l1d[i + 14][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*135), 106 + 135), "MH: " + '{:.4f}'.format(l1d[i + 14][5]), font = font_l1d_data, fill=(0,0,0))

  ## NOCs
  im.rectangle([(10, 285), (1910, 345)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  im.text((180+16, 295), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475, 295), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 2, 295), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 3, 295), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  font_l2 = ImageFont.truetype('FreeMonoBold.ttf', 16)
  ## L2 [0, 24]
  for i in range(0, 12):
    im.rectangle([(10 + (i*158), 355), (10 + 153 + (i*158), 80 + 355)],  outline = "white", 
                          fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    im.text((11 + (i*158),  355), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((11+(i*158), 355 + 20), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11+(i*158), 355 + 35), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11+(i*158), 355 + 50), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11+78+(i*158),355 + 20), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11+78+(i*158),355 + 35), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11+78+(i*158),355 + 50), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*158), 440), (10 + 153 + (i*158), 620)], outline = "white", 
                          fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    im.text((11 + (i*158), 441), "Dram Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [24, 31]
    im.text((11 + (i*158), 441 + 30), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*158), 441 + 50), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(10 + (i*158), 625), (10 + 153 + (i*158), 705)], outline = "white", 
                          fill = (l2_rgb[i+12][0], l2_rgb[i+12][1], l2_rgb[i+12][2]))
    im.text((11 + (i*158), 626), "L2 Cache-" + str(i+ 12), font = font_l1d, fill=(0, 0, 0)) #L2 [8, 15]
    im.text((11 + (i*158), 626 + 20), "H : " + '{:.4f}'.format(l2[i + 12][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*158), 626 + 35), "HR: " + '{:.4f}'.format(l2[i + 12][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + (i*158), 626 + 50), "M : " + '{:.4f}'.format(l2[i + 12][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + 78 + (i*158), 626 + 20), "RF: " + '{:.4f}'.format(l2[i + 12][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + 78 + (i*158), 626 + 35), "SM: " + '{:.4f}'.format(l2[i + 12][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((11 + 78 + (i*158), 626 + 50), "MH: " + '{:.4f}'.format(l2[i + 12][5]), font = font_l1d_data, fill=(0,0,0))

  power_data = ImageFont.truetype('FreeSerif.ttf', 15)
  im.line([(5, 715), (1915, 715)], fill = (0,0,0), width = 4)
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

  im.rectangle([(710, 750), (1910, 1040)], outline = "white", fill = (0,0,0))
  font_info = ImageFont.truetype('DejaVuSans.ttf', 18)
  im.text((715, 760), 
                  "- This is TITANX based on Pascal Architecture includes 28 Streaming Multiprocessors (28 L1D caches).",
                  font = font_info, fill=(255,255,255)) 
  im.text((715, 25 + 760), 
                  "- There are 12 memory partitions (12 Seperate DRAM Banks) with 2 sub-partitions (24 L2 Caches) ",
                  font = font_info, fill=(255,255,255)) 

  im.text((715, 70 + 760), "- H : Hits ", font = font_info, fill=(255,255,255)) 
  im.text((715, 95 + 760), "- M : Misses ", font = font_info, fill=(255,255,255)) 
  im.text((715, 120+ 760), "- HR : Hit Reserved Accesses", font = font_info, fill=(255,255,255))
  im.text((715, 145+ 760), "- RF : Reservation Failures", font = font_info, fill=(255,255,255))
  im.text((715, 170+ 760), "- MH : MSHR Hits", font = font_info, fill=(255,255,255))
  im.text((715, 195+ 760), "- SM : Sector Misses", font = font_info, fill=(255,255,255))
  im.text((715, 220+ 760), "- RB-H : Row Buffer Hits", font = font_info, fill=(255,255,255))
  im.text((715, 245+ 760), "- RB-M : Row Buffer Misses", font = font_info, fill=(255,255,255))

  im.rectangle([(1700, 750), (1900, 810)], outline = "white", fill = (20,20,20))
  im.text((1705, 760), " KERNEL = " + str(kernel),
                  font = ImageFont.truetype('DejaVuSans.ttf', 20), fill=(255,25,25)) 
  im.rectangle([(1110, 930), (1700, 1010)], outline = "white", fill = (50,50,100))
  im.text((1120, 935),  "Kernel: " + str(kernel), font = font_info, fill=(255,255,255)) 
  im.text((1120, 970),  "Cycle interval of the GPU: [" + str(start) + ", " + str(finish) + "]", font = font_info, fill=(255,255,255)) 


  return im
