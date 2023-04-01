from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

  # plot_TITANV(im_memory, l1d, l2, dram, kernel, int_start, int_finish, l1d_rgb, l2_rgb, dram_rgb, power_mem)
def plot_TITANV(im, l1d, l2, dram, kernel, start, finish, l1d_rgb, l2_rgb, dram_rgb, power):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)

  font_l1d = ImageFont.truetype('FreeSerif.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 11)
  # L1D [0, 44]
  for i in range(0, 22):
    im.rectangle([(5 + (i*87), 5), (85 + (i*87), 90)], outline = "white", fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    im.text((7 + (i*87), 7), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    im.text((10 + (i*87), 22), "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 33), "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 44), "M : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 55), "RF: " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 66), "SM: " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 77), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0, 0, 0))

    im.rectangle([(5 + (i*87), 95), (85 + (i*87), 180)], outline = "white", fill = (l1d_rgb[i+22][0], l1d_rgb[i+22][1], l1d_rgb[i+22][2]))
    im.text((7 + (i*87), 97), "L1 Data-" + str(i + 22), font = font_l1d, fill=(0, 0, 0))
    im.text((10 + (i*87), 112), "H : " + '{:.4f}'.format(l1d[i+22][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 123), "HR: " + '{:.4f}'.format(l1d[i+22][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 134), "M : " + '{:.4f}'.format(l1d[i+22][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 145), "RF: " + '{:.4f}'.format(l1d[i+22][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 156), "SM: " + '{:.4f}'.format(l1d[i+22][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 167), "MH: " + '{:.4f}'.format(l1d[i+22][5]), font = font_l1d_data, fill=(0, 0, 0))

  ## NOCs
  im.rectangle([(5, 185), (1915, 210)], outline = "white", fill = (255, 20, 20))
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 20)
  im.text((180+16, 188), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475, 188), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 2, 188), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  im.text((180+16 + 475 * 3, 188), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  ## L2 [0, 48]
  ## DRAM [0, 24]
  font_l2 = ImageFont.truetype('FreeSerif.ttf', 15)
  font_l2_data = ImageFont.truetype('FreeSerif.ttf', 11)
  for i in range(0, 12):
    im.rectangle([(5 + (i*158), 215), (5 + 153 + (i*158), 285)],  outline = "white", fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    im.text((8 + (i*158), 218), "L2 Cache-" + str(i), font = font_l2, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((8 + (i*158), 20 + 218), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + (i*158), 35 + 218), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + (i*158), 50 + 218), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 20 + 218), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 35 + 218), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 50 + 218), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l2_data, fill=(0,0,0))

    im.rectangle([(5 + (i*158), 290), (5 + 153 + (i*158), 360)],  outline = "white", fill = (l2_rgb[i+12][0], l2_rgb[i+12][1], l2_rgb[i+12][2]))
    im.text((8 + (i*158), 293), "L2 Cache-" + str(i + 12), font = font_l2, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((8 + (i*158), 20 + 293), "H : " + '{:.4f}'.format(l2[i + 12][0]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + (i*158), 35 + 293), "HR: " + '{:.4f}'.format(l2[i + 12][1]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + (i*158), 50 + 293), "M : " + '{:.4f}'.format(l2[i + 12][2]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 20 + 293), "RF: " + '{:.4f}'.format(l2[i + 12][3]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 35 + 293), "SM: " + '{:.4f}'.format(l2[i + 12][4]), font = font_l2_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 50 + 293), "MH: " + '{:.4f}'.format(l2[i + 12][5]), font = font_l2_data, fill=(0,0,0))

    im.rectangle([(5 + (i*158), 370), (5 + 153 + (i*158), 450)],  outline = "white", fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    im.text((8 + (i*158), 373), "DRAM Bank-" + str(i), font = font_l2, fill=(0, 0, 0)) #L2 [8, 15]
    im.text((8 + (i*158), 373 + 30), "RB-H : " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + (i*158), 373 + 50), "RB-M : " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(5 + (i*158), 455), (5 + 153 + (i*158), 535)],  outline = "white", fill = (dram_rgb[i+12][0], dram_rgb[i+12][1], dram_rgb[i+12][2]))
    im.text((8 + (i*158), 458), "DRAM Bank-" + str(i+12), font = font_l2, fill=(0, 0, 0)) #L2 [8, 15]
    im.text((8 + (i*158), 458 + 30), "RB-H : " + '{:.4f}'.format(dram[i+12][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + (i*158), 458 + 50), "RB-M : " + '{:.4f}'.format(dram[i+12][1]), font = font_l1d_data, fill=(0,0,0))

    im.rectangle([(5 + (i*158), 545), (5 + 153 + (i*158), 615)],  outline = "white", fill = (l2_rgb[i+24][0], l2_rgb[i+24][1], l2_rgb[i+24][2]))
    im.text((8 + (i*158), 548), "L2 Cache-" + str(i+24), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((8 + (i*158), 20 + 548), "H : " + '{:.4f}'.format(l2[i + 24][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + (i*158), 35 + 548), "HR: " + '{:.4f}'.format(l2[i + 24][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + (i*158), 50 + 548), "M : " + '{:.4f}'.format(l2[i + 24][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 20 + 548), "RF: " + '{:.4f}'.format(l2[i + 24][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 35 + 548), "SM: " + '{:.4f}'.format(l2[i + 24][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 50 + 548), "MH: " + '{:.4f}'.format(l2[i + 24][5]), font = font_l1d_data, fill=(0,0,0)) 
    
    im.rectangle([(5 + (i*158), 620), (5 + 153 + (i*158), 690)],  outline = "white", fill = (l2_rgb[i+36][0], l2_rgb[i+36][1], l2_rgb[i+36][2]))
    im.text((8 + (i*158), 623), "L2 Cache-" + str(i+36), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    im.text((8 + (i*158), 20 + 623), "H : " + '{:.4f}'.format(l2[i + 36][0]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + (i*158), 35 + 623), "HR: " + '{:.4f}'.format(l2[i + 36][1]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + (i*158), 50 + 623), "M : " + '{:.4f}'.format(l2[i + 36][2]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 20 + 623), "RF: " + '{:.4f}'.format(l2[i + 36][3]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 35 + 623), "SM: " + '{:.4f}'.format(l2[i + 36][4]), font = font_l1d_data, fill=(0,0,0))
    im.text((8 + 75 + (i*158), 50 + 623), "MH: " + '{:.4f}'.format(l2[i + 36][5]), font = font_l1d_data, fill=(0,0,0)) 

  for i in range(0, 22):
    im.rectangle([(5 + (i*87), 700), (85 + (i*87), 785)], outline = "white", fill = (l1d_rgb[i + 44][0], l1d_rgb[i + 44][1], l1d_rgb[i + 44][2]))
    im.text((8 + (i*87),  695 + 7), "L1 Data-" + str(i + 44), font = font_l1d, fill=(0, 0, 0))
    im.text((10 + (i*87), 695 + 22), "H : " + '{:.4f}'.format(l1d[i + 44][0]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 695 + 33), "HR: " + '{:.4f}'.format(l1d[i + 44][1]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 695 + 44), "M : " + '{:.4f}'.format(l1d[i + 44][2]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 695 + 55), "RF: " + '{:.4f}'.format(l1d[i + 44][3]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 695 + 66), "SM: " + '{:.4f}'.format(l1d[i + 44][4]), font = font_l1d_data, fill=(0, 0, 0))
    im.text((10 + (i*87), 695 + 77), "MH: " + '{:.4f}'.format(l1d[i + 44][5]), font = font_l1d_data, fill=(0, 0, 0))

    if i + 66 < 80:
      im.rectangle([(5 + (i*87), 790), (85 + (i*87), 875)], outline = "white", fill = (l1d_rgb[i + 66][0], l1d_rgb[i + 66][1], l1d_rgb[i + 66][2]))
      im.text((8 + (i*87),  695 + 97), "L1 Data-" + str(i + 66), font = font_l1d, fill=(0, 0, 0))
      im.text((10 + (i*87), 695 + 112), "H : " + '{:.4f}'.format(l1d[i + 66][0]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((10 + (i*87), 695 + 123), "HR: " + '{:.4f}'.format(l1d[i + 66][1]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((10 + (i*87), 695 + 134), "M : " + '{:.4f}'.format(l1d[i + 66][2]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((10 + (i*87), 695 + 145), "RF: " + '{:.4f}'.format(l1d[i + 66][3]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((10 + (i*87), 695 + 156), "SM: " + '{:.4f}'.format(l1d[i + 66][4]), font = font_l1d_data, fill=(0, 0, 0))
      im.text((10 + (i*87), 695 + 167), "MH: " + '{:.4f}'.format(l1d[i + 66][5]), font = font_l1d_data, fill=(0, 0, 0))

  power_data = ImageFont.truetype('FreeSerif.ttf', 15)
  im.line([(5, 850 + 40), (1915, 850 + 40)], fill = (0,0,0), width = 4)
  im.rectangle([(10, 890 + 40), (200, 1000 + 40)], outline = "white", fill = (100, 150, 100))
  im.text((15, 900 + 40), "Peak Dynamic (W) : "       , font = power_data, fill=(0, 0, 0))
  im.text((15, 925 + 40), "Sub-Threshold Leakage (W): ", font = power_data, fill=(0, 0, 0))
  im.text((15, 950 + 40), "Gate Leakage (W) : "       , font = power_data, fill=(0, 0, 0))
  im.text((15, 975 + 40), "Run Time Dynamic (W) : "    , font = power_data, fill=(0, 0, 0))

  im.rectangle([(210, 860 + 40), (300, 885 + 40)], outline = "white", fill = (50, 150, 250))
  im.text((215, 865 + 40), "MC FEE", font = power_data, fill=(0, 0, 0))
  im.rectangle([(210, 890 + 40), (300, 1000 + 40)], outline = "white", fill = (150, 50, 150))
  im.text((215, 900 + 40), '{:.4f}'.format(power['mc_fee']["PeakDynamic(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((215, 925 + 40), '{:.4f}'.format(power['mc_fee']["SubthresholdLeakage(W)"]), font = power_data, fill=(0, 0, 0))
  im.text((215, 950 + 40), '{:.4f}'.format(power['mc_fee']["GateLeakage(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((215, 975 + 40), '{:.4f}'.format(power['mc_fee']["RunTimeDynamic(W)"]),      font = power_data, fill=(0, 0, 0))

  im.rectangle([(310, 860 + 40), (400, 885 + 40)], outline = "white", fill = (50, 150, 250))
  im.text((315, 865 + 40), "PHY(mc/dram)", font = power_data, fill=(0, 0, 0))
  im.rectangle([(310, 890 + 40), (400, 1000 + 40)], outline = "white", fill = (150, 250, 50))
  im.text((315, 900 + 40), '{:.4f}'.format(power['mc_phy']["PeakDynamic(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((315, 925 + 40), '{:.4f}'.format(power['mc_phy']["SubthresholdLeakage(W)"]), font = power_data, fill=(0, 0, 0))
  im.text((315, 950 + 40), '{:.4f}'.format(power['mc_phy']["GateLeakage(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((315, 975 + 40), '{:.4f}'.format(power['mc_phy']["RunTimeDynamic(W)"]),      font = power_data, fill=(0, 0, 0))

  im.rectangle([(410, 860 + 40), (500, 885 + 40)], outline = "white", fill = (50, 150, 250))
  im.text((415, 865 + 40), "MC-TE(BEE)", font = power_data, fill=(0, 0, 0))
  im.rectangle([(410, 890 + 40), (500, 1000 + 40)], outline = "white", fill = (150, 50, 250))
  im.text((415, 900 + 40), '{:.4f}'.format(power['mc_te']["PeakDynamic(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((415, 925 + 40), '{:.4f}'.format(power['mc_te']["SubthresholdLeakage(W)"]), font = power_data, fill=(0, 0, 0))
  im.text((415, 950 + 40), '{:.4f}'.format(power['mc_te']["GateLeakage(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((415, 975 + 40), '{:.4f}'.format(power['mc_te']["RunTimeDynamic(W)"]),      font = power_data, fill=(0, 0, 0))

  im.rectangle([(510, 860 + 40), (600, 885 + 40)], outline = "white", fill = (50, 150, 250))
  im.text((525, 865 + 40), "DRAM", font = power_data, fill=(0, 0, 0))
  im.rectangle([(510, 890 + 40), (600, 1000 + 40)], outline = "white", fill = (150, 50, 250))
  im.text((515, 900 + 40), '{:.4f}'.format(power['mc_total']["PeakDynamic(W)"] - 
                                      (power['mc_te']["PeakDynamic(W)"] + power['mc_phy']["PeakDynamic(W)"] + power['mc_fee']["PeakDynamic(W)"])),
                                      font = power_data, fill=(0, 0, 0))
  im.text((515, 925 + 40), '{:.4f}'.format(power['mc_total']["SubthresholdLeakage(W)"] - 
                                      (power['mc_te']["SubthresholdLeakage(W)"] + power['mc_phy']["SubthresholdLeakage(W)"] + power['mc_fee']["SubthresholdLeakage(W)"])),
                                      font = power_data, fill=(0, 0, 0))
  im.text((515, 950 + 40), '{:.4f}'.format(power['mc_total']["GateLeakage(W)"] - 
                                      (power['mc_te']["GateLeakage(W)"] + power['mc_phy']["GateLeakage(W)"] + power['mc_fee']["GateLeakage(W)"])),
                                      font = power_data, fill=(0, 0, 0))
  im.text((515, 975 + 40), '{:.4f}'.format(power['mc_total']["RunTimeDynamic(W)"] - 
                                      (power['mc_te']["RunTimeDynamic(W)"] + power['mc_phy']["RunTimeDynamic(W)"] + power['mc_fee']["RunTimeDynamic(W)"])),
                                      font = power_data, fill=(0, 0, 0))

  im.rectangle([(610, 860 + 40), (700, 885 + 40)], outline = "white", fill = (50, 150, 250))
  im.text((625, 865 + 40), "TOTAL", font = power_data, fill=(0, 0, 0))
  im.rectangle([(610, 890 + 40), (700, 1000 + 40)], outline = "white", fill = (250, 150, 50))
  im.text((615, 900 + 40), '{:.4f}'.format(power['mc_total']["PeakDynamic(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((615, 925 + 40), '{:.4f}'.format(power['mc_total']["SubthresholdLeakage(W)"]), font = power_data, fill=(0, 0, 0))
  im.text((615, 950 + 40), '{:.4f}'.format(power['mc_total']["GateLeakage(W)"]),         font = power_data, fill=(0, 0, 0))
  im.text((615, 975 + 40), '{:.4f}'.format(power['mc_total']["RunTimeDynamic(W)"]),      font = power_data, fill=(0, 0, 0))

  font_info = ImageFont.truetype('FreeSerif.ttf', 18)
  im.rectangle([(725, 860 + 40), (1000, 1075)], outline = "white", fill = (20,20,20))
  im.text((725, 865 + 40),  " - H -> Hit", font = font_info, fill=(255,255,255)) 
  im.text((725, 865 + 23 + 40),  " - HR -> Hit Reserved", font = font_info, fill=(255,255,255)) 
  im.text((725, 865 + 46 + 40),  " - M -> Miss", font = font_info, fill=(255,255,255)) 
  im.text((725, 865 + 69 + 40),  " - RF -> Reservation Failure", font = font_info, fill=(255,255,255)) 
  im.text((725, 865 + 92 + 40),  " - SM -> Sector Miss", font = font_info, fill=(255,255,255)) 
  im.text((725, 865 + 115 + 40),  " - MH -> MSHR Hit", font = font_info, fill=(255,255,255)) 
  im.text((725, 865 + 138 + 40), " - RB-H/M -> Row Buffer Hit/Miss", font = font_info, fill=(255,255,255)) 

  im.rectangle([(1050, 860 + 40), (1880, 920 + 40)], outline = "white", fill = (20,20,20))
  im.text((1060, 870 + 40), "- This is TITAN V based on Volta Architecture includes 80 Streaming Multiprocessors (80 L1D caches).", font = font_info, fill=(255,255,255)) 
  im.text((1060, 895 + 40), "- There are 24 memory partitions (24 Seperate DRAM Banks) with 2 sub-partitions (48 L2 Caches).", font = font_info, fill=(255,255,255)) 

  font_info = ImageFont.truetype('FreeSerif.ttf', 25)
  im.rectangle([(1050, 930 + 40), (1700, 1010 + 40)], outline = "white", fill = (50,50,100))
  im.text((1060, 935 + 40),  "KERNEL: " + str(kernel), font = font_info, fill=(255,255,255)) 
  im.text((1060, 970 + 40),  "Cycle interval of the GPU: [" + str(start) + ", " + str(finish) + "]", font = font_info, fill=(255,255,255)) 

  return im
