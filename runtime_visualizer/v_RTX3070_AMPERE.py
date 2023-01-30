from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# 46 L1D cache, 32 L2, 16 DRAM
def plot_RTX3070(image_draw, l1d, l2, dram, kernel, l1d_rgb, l2_rgb, dram_rgb):

  font_l1d = ImageFont.truetype('DejaVuSans.ttf', 15)
  font_l1d_data = ImageFont.truetype('FreeMonoBold.ttf', 12)
  ## L1D [0, 45]
  for i in range(0, 16):
    image_draw.rectangle([(10 + (i*118), 10), (10 + 110 + (i*118), 10 + 110)], outline = "white", 
                         fill = (l1d_rgb[i][0], l1d_rgb[i][1], l1d_rgb[i][2]))
    image_draw.text((11 + (i*118), 11), "L1 Data-" + str(i), font = font_l1d, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 29), "H : " + '{:.4f}'.format(l1d[i][0]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 29 + 13), "HR: " + '{:.4f}'.format(l1d[i][1]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 29 + 26), "M : " + '{:.4f}'.format(l1d[i][2]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 29 + 39), "RF: " + '{:.4f}'.format(l1d[i][3]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 29 + 52), "SM: " + '{:.4f}'.format(l1d[i][4]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 29 + 65), "MH: " + '{:.4f}'.format(l1d[i][5]), font = font_l1d_data, fill=(0, 0, 0))

    image_draw.rectangle([(10 + (i*118), 10 + 120), (10 + 110 + (i*118), 10 + 110 + 120)], outline = "white", 
                         fill = (l1d_rgb[i+16][0], l1d_rgb[i+16][1], l1d_rgb[i+16][2]))
    image_draw.text((11 + (i*118), 11 + 120), "L1 Data-" + str(i + 16), font = font_l1d, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 120 + 29), "H : " + '{:.4f}'.format(l1d[i+16][0]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 120 + 29 + 13), "HR: " + '{:.4f}'.format(l1d[i+16][1]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 120 + 29 + 26), "M : " + '{:.4f}'.format(l1d[i+16][2]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 120 + 29 + 39), "RF: " + '{:.4f}'.format(l1d[i+16][3]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 120 + 29 + 52), "SM: " + '{:.4f}'.format(l1d[i+16][4]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 120 + 29 + 65), "MH: " + '{:.4f}'.format(l1d[i+16][5]), font = font_l1d_data, fill=(0, 0, 0))

    if (i + 32 <= 45):
      image_draw.rectangle([(10 + (i*118), 10 + 240), (10 + 110 + (i*118), 10 + 110 + 240)], outline = "white", 
                            fill = (l1d_rgb[i+32][0], l1d_rgb[i+32][1], l1d_rgb[i+32][2]))
      image_draw.text((11 + (i*118), 11 + 240), "L1 Data-" + str(i + 32), font = font_l1d, fill=(0, 0, 0))
      image_draw.text((11 + (i*118), 240 + 29), "H : " + '{:.4f}'.format(l1d[i+32][0]), font = font_l1d_data, fill=(0, 0, 0))
      image_draw.text((11 + (i*118), 240 + 29 + 13), "HR: " + '{:.4f}'.format(l1d[i+32][1]), font = font_l1d_data, fill=(0, 0, 0))
      image_draw.text((11 + (i*118), 240 + 29 + 26), "M : " + '{:.4f}'.format(l1d[i+32][2]), font = font_l1d_data, fill=(0, 0, 0))
      image_draw.text((11 + (i*118), 240 + 29 + 39), "RF: " + '{:.4f}'.format(l1d[i+32][3]), font = font_l1d_data, fill=(0, 0, 0))
      image_draw.text((11 + (i*118), 240 + 29 + 52), "SM: " + '{:.4f}'.format(l1d[i+32][4]), font = font_l1d_data, fill=(0, 0, 0))
      image_draw.text((11 + (i*118), 240 + 29 + 65), "MH: " + '{:.4f}'.format(l1d[i+32][5]), font = font_l1d_data, fill=(0, 0, 0))
    else:
      image_draw.rectangle([(1700, 10+240), (120 + 15*118, 70+240)], outline = "white", fill = (20,20,20))
      image_draw.text((1720, 20+240), " KERNEL = " + str(kernel), font = font_l1d, fill=(255, 25, 25))

  ## NOCs
  image_draw.rectangle([(15, 240+15+10+110), (1900, 110+240+15+30+20)], outline = "white", fill = (255, 20, 20))
  ## NOCs writes onto the drawing
  font_NOCs = ImageFont.truetype('FreeMonoBold.ttf', 40)
  image_draw.text((15 + 200, 240+15+10+110), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((15 + 470 + 200, 240+15+10+110), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((15 + 470 * 2 + 200, 240+15+10+110), "NOCs", font = font_NOCs, fill=(0, 0, 0))
  image_draw.text((15 + 470 * 3 + 200, 240+15+10+110), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  for i in range (0, 8):
    image_draw.rectangle([(10 + (i*236), 425), (10 + 230 + (i*236), 425 + 90)],  outline = "white", 
                          fill = (l2_rgb[i][0], l2_rgb[i][1], l2_rgb[i][2]))
    image_draw.text((11 + (i*236), 426), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*236), 426 + 20), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*236), 426 + 35), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*236), 426 + 50), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 20), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 35), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 50), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0, 0, 0))

    image_draw.rectangle([(10 + (i*236), 425 + 95), (10 + 230 + (i*236), 425 + 185)],  outline = "white", 
                          fill = (l2_rgb[i+8][0], l2_rgb[i+8][1], l2_rgb[i+8][2]))
    image_draw.text((11 + (i*236), 426 + 95), "L2 Cache-" + str(i + 8), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*236), 426 + 95 + 20), "H : " + '{:.4f}'.format(l2[i + 8][0]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*236), 426 + 95 + 35), "HR: " + '{:.4f}'.format(l2[i + 8][1]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*236), 426 + 95 + 50), "M : " + '{:.4f}'.format(l2[i + 8][2]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 20 + 95), "RF: " + '{:.4f}'.format(l2[i + 8][3]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 35 + 95), "SM: " + '{:.4f}'.format(l2[i + 8][4]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 50 + 95), "MH: " + '{:.4f}'.format(l2[i + 8][5]), font = font_l1d_data, fill=(0, 0, 0))

    image_draw.rectangle([(10 + (i*236), 425 + 190), (10 + 230 + (i*236), 425 + 285)],  outline = "white", 
                          fill = (l2_rgb[i+16][0], l2_rgb[i+16][1], l2_rgb[i+16][2]))
    image_draw.text((10 + (i*236), 425 + 190), "L2 Cache-" + str(i + 16), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*236), 426 + 190 + 20), "H : " + '{:.4f}'.format(l2[i + 16][0]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*236), 426 + 190 + 35), "HR: " + '{:.4f}'.format(l2[i + 16][1]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*236), 426 + 190 + 50), "M : " + '{:.4f}'.format(l2[i + 16][2]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 20 + 190), "RF: " + '{:.4f}'.format(l2[i + 16][3]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 35 + 190), "SM: " + '{:.4f}'.format(l2[i + 16][4]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 50 + 190), "MH: " + '{:.4f}'.format(l2[i + 16][5]), font = font_l1d_data, fill=(0, 0, 0))

    image_draw.rectangle([(10 + (i*236), 425 + 290), (10 + 230 + (i*236), 425 + 380)],  outline = "white", 
                          fill = (l2_rgb[i+24][0], l2_rgb[i+24][1], l2_rgb[i+24][2]))
    image_draw.text((11 + (i*236), 425 + 290), "L2 Cache-" + str(i + 24), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
    image_draw.text((11 + (i*236), 426 + 290 + 20), "H : " + '{:.4f}'.format(l2[i + 24][0]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*236), 426 + 290 + 35), "HR: " + '{:.4f}'.format(l2[i + 24][1]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*236), 426 + 290 + 50), "M : " + '{:.4f}'.format(l2[i + 24][2]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 20 + 290), "RF: " + '{:.4f}'.format(l2[i + 24][3]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 35 + 290), "SM: " + '{:.4f}'.format(l2[i + 24][4]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + 115 + (i*236), 426 + 50 + 290), "MH: " + '{:.4f}'.format(l2[i + 24][5]), font = font_l1d_data, fill=(0, 0, 0))

  ## DRAM [0, 15]
  for i in range(0, 16):
    image_draw.rectangle([(10 +(i*118), 425+380+10), (10+ 110 + (i*118), 425+380+10+200)], outline = "white", 
                           fill = (dram_rgb[i][0], dram_rgb[i][1], dram_rgb[i][2]))
    image_draw.text((11 + (i*118), 425+380+10), "DRAM Bank-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [24, 31]
    image_draw.text((11 + (i*118), 425+380+40), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0, 0, 0))
    image_draw.text((11 + (i*118), 425+380+60), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0, 0, 0))

  image_draw.rectangle([(15, 425+380+10+200 + 10), (1900, 425+380+10+200 + 32)], outline = "white", fill = (0,0,0))
  font_info = ImageFont.truetype('DejaVuSans.ttf', 18)
  image_draw.text((18, 425+380+10+200 + 10), 
                  "RTX-3070 GPU based on Ampere Architecture includes 46 Streaming Multiprocessors (46 L1D caches). "
                  "There are 16 memory partitions (16 Seperate DRAM Banks) with 2 sub-partitions (32 L2 Caches) ",
                  font = font_info, fill=(255,255,255)) 

  image_draw.rectangle([(15, 425+380+10+200 + 38), (1900, 425+380+10+200 + 60)], outline = "white", fill = (0,0,0))
  font_info = ImageFont.truetype('DejaVuSans.ttf', 20)
  image_draw.text((18, 425+380+10+200 + 38), 
                  "H -> Hits ||| M -> Misses ||| HR -> Hit Reserved Accesses ||| "
                  "RF -> Reservation Failures ||| SM -> Sector Misses ||| "
                  "MH -> MSHR Hits ||| RB-H -> Row Buffer Hits ||| RB-H -> Row Buffer Misses",
                  font = font_info, fill=(255,255,255)) 


#    image_draw.rectangle([(15 + (i*236), 80 * 2 +240+15+30+20 + 10 +5), 
#                          (15 +  230 + (i*236), 80 * 3+240+15+30+20 + 10 + 230 +5)],  outline = "white", fill = (255, 255, 75))
#    image_draw.text((15+(i*240), 15 + 245), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
#
#    image_draw.rectangle([(15 + (i*236), 80 * 3+240+15+30+20 + 10 +5*2), 
#                          (15 +  230 + (i*236), 80 * 3+240+15+30+20 + 10 + 230 +5*2)],  outline = "white", fill = (255, 255, 75))
#    image_draw.text((15+(i*240), 15 + 245), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]
#
#    image_draw.rectangle([(15 + (i*236), 80 * 4 +240+15+30+20 + 10 +5*3), 
#                          (15 +  230 +  (i*236), 80 * 4 +240+15+30+20 + 10 + 230 +5*3)],  outline = "white", fill = (255, 255, 75))
#    image_draw.text((15+(i*240), 15 + 245), "L2 Cache-" + str(i), font = font_l1d, fill=(0, 0, 0)) #L2 [0, 7]



#    image_draw.rectangle([(15 + 10 + 85 + (i*190), 15), (15 + 10 + 85 * 2 + (i*190), 15 + 85)], outline = "white", fill = "green")
#    image_draw.text((15+10+85+(i*190), 15), "L1 Data-" + str(i*4+1), font = font_l1d, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 28+4), "H : " + '{:.4f}'.format(l1d[i*4+1][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 39+4), "HR: " + '{:.4f}'.format(l1d[i*4+1][1]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 50+4), "M : " + '{:.4f}'.format(l1d[i*4+1][2]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 61+4), "RF: " + '{:.4f}'.format(l1d[i*4+1][3]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 72+4), "SM: " + '{:.4f}'.format(l1d[i*4+1][4]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 83+4), "MH: " + '{:.4f}'.format(l1d[i*4+1][5]), font = font_l1d_data, fill=(0,0,0))

#    image_draw.rectangle([(15 + (i*190), 15 + 85 + 10), (15 + 85 + (i*190), 15 + 85 + 85 + 10)], 
#                          outline = "white", fill = "green")
#    image_draw.text((15+(i*190), 15+85+10), "L1 Data-" + str(i*4+2), font = font_l1d, fill=(0, 0, 0))
#    image_draw.text((17+(i*190), 28+85+10+4), "H : " + '{:.4f}'.format(l1d[i*4+2][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 39+85+10+4), "HR: " + '{:.4f}'.format(l1d[i*4+2][1]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 50+85+10+4), "M : " + '{:.4f}'.format(l1d[i*4+2][2]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 61+85+10+4), "RF: " + '{:.4f}'.format(l1d[i*4+2][3]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 72+85+10+4), "SM: " + '{:.4f}'.format(l1d[i*4+2][4]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 83+85+10+4), "MH: " + '{:.4f}'.format(l1d[i*4+2][5]), font = font_l1d_data, fill=(0,0,0))

#    image_draw.rectangle([(15 + 10 + 85 + (i*190), 15 + 85 + 10), (15 + 10 + 85 * 2 + (i*190), 15 + 85 + 85 + 10)], 
#                          outline = "white", fill = (100, 255, 100))
#    image_draw.text((15+10+85+(i*190), 15+85+10), "L1 Data-" + str(i*4+3), font = font_l1d, fill=(0, 0, 0))  
#    image_draw.text((17+10+85+(i*190), 28+85+10+4), "H : " + '{:.4f}'.format(l1d[i*4+3][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 39+85+10+4), "HR: " + '{:.4f}'.format(l1d[i*4+3][1]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 50+85+10+4), "M : " + '{:.4f}'.format(l1d[i*4+3][2]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 61+85+10+4), "RF: " + '{:.4f}'.format(l1d[i*4+3][3]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 72+85+10+4), "SM: " + '{:.4f}'.format(l1d[i*4+3][4]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 83+85+10+4), "MH: " + '{:.4f}'.format(l1d[i*4+3][5]), font = font_l1d_data, fill=(0,0,0))

  ## L1D [40, 79]
#    image_draw.rectangle([(15 + (i*190),  1080 - 15), (15 + 85 + (i*190), 1080 - (15 + 85))], outline = "white", fill = "green")
#    image_draw.rectangle([(15 + 10 + 85 + (i*190),  1080 - 15), (15 + 10 + 85 * 2 + (i*190), 1080 - (15 + 85))], outline = "white", fill = (100, 255, 100))
#    image_draw.rectangle([(15 + (i*190),  1080 - (15 + 85 + 10)), (15 + 85 + (i*190),  1080 - (15 + 85 + 85 + 10))], outline = "white", fill = (100, 255, 100))
#    image_draw.rectangle([(15 + 10 + 85 + (i*190), 1080 - (15 + 85 + 10)), (15 + 10 + 85 * 2 + (i*190), 1080 - (15 + 85 + 85 + 10))], outline = "white", fill = "green")
#
#    image_draw.text((15+(i*190), 1080 - (15 + 85 + 85 + 10)), "L1 Data-" + str(i*4+40), font = font_l1d, fill=(0, 0, 0)) #40, 44 ... 
#    image_draw.text((17+(i*190), 1080 - (+4 + 85 + 85 + 10-4)), "H : " + '{:.4f}'.format(l1d[i*4+40][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-7 + 85 + 85 + 10-4)), "HR: " + '{:.4f}'.format(l1d[i*4+40][1]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-18 + 85 + 85 +10-4)), "M : " + '{:.4f}'.format(l1d[i*4+40][2]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-29 + 85 + 85 +10-4)), "RF: " + '{:.4f}'.format(l1d[i*4+40][3]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-40 + 85 + 85 +10-4)), "SM: " + '{:.4f}'.format(l1d[i*4+40][4]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-51 + 85 + 85 +10-4)), "MH: " + '{:.4f}'.format(l1d[i*4+40][5]), font = font_l1d_data, fill=(0,0,0))

#    image_draw.text((17+10+85+(i*190), 1080 - (+4 + 85 + 85 + 10-4)),  "H : " + '{:.4f}'.format(l1d[i*4+41][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080 - (-7 + 85 + 85 + 10-4)),  "HR: " + '{:.4f}'.format(l1d[i*4+41][1]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080 - (-18 + 85 + 85+ 10-4)), "M : " + '{:.4f}'.format(l1d[i*4+41][2]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080 - (-29 + 85 + 85+ 10-4)), "RF: " + '{:.4f}'.format(l1d[i*4+41][3]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080 - (-40 + 85 + 85+ 10-4)), "SM: " + '{:.4f}'.format(l1d[i*4+41][4]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080 - (-51 + 85 + 85+ 10-4)), "MH: " + '{:.4f}'.format(l1d[i*4+41][5]), font = font_l1d_data, fill=(0,0,0))

#    image_draw.text((17+(i*190), 1080 - (+4 + 85-4)),  "H : " + '{:.4f}'.format(l1d[i*4+42][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-7 + 85-4)),  "HR: " + '{:.4f}'.format(l1d[i*4+42][1]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-18 +85-4)), "M : " + '{:.4f}'.format(l1d[i*4+42][2]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-29 +85-4)), "RF: " + '{:.4f}'.format(l1d[i*4+42][3]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-40 +85-4)), "SM: " + '{:.4f}'.format(l1d[i*4+42][4]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+(i*190), 1080 - (-51 +85-4)), "MH: " + '{:.4f}'.format(l1d[i*4+42][5]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080-(+4+85 -4)),  "H : " + '{:.4f}'.format(l1d[i*4+43][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080-(-7+85 -4)),  "HR: " + '{:.4f}'.format(l1d[i*4+43][1]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080-(-18+85-4)), "M : " + '{:.4f}'.format(l1d[i*4+43][2]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080-(-29+85-4)), "RF: " + '{:.4f}'.format(l1d[i*4+43][3]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080-(-40+85-4)), "SM: " + '{:.4f}'.format(l1d[i*4+43][4]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((17+10+85+(i*190), 1080-(-51+85-4)), "MH: " + '{:.4f}'.format(l1d[i*4+43][5]), font = font_l1d_data, fill=(0,0,0))

#
#  image_draw.rectangle([(15, 1080 - 210), (1900, 1080 - 250)], outline = "white", fill = (255, 20, 20))
#  image_draw.text((180+16, 1080 - (250 + 2)), "NOCs", font = font_NOCs, fill=(0, 0, 0))
#  image_draw.text((180+16 + 475, 1080 - (250 + 2)), "NOCs", font = font_NOCs, fill=(0, 0, 0))
#  image_draw.text((180+16 + 475 * 2, 1080 - (250 + 2)), "NOCs", font = font_NOCs, fill=(0, 0, 0))
#  image_draw.text((180+16 + 475 * 3, 1080 - (250 + 2)), "NOCs", font = font_NOCs, fill=(0, 0, 0))

  font_l2 = ImageFont.truetype('FreeMonoBold.ttf', 16)
  ## L2 [0, 15]
#  for i in range(0, 8):
#    image_draw.text((18+(i*240), 28 + 245+4), "H : " + '{:.4f}'.format(l2[i][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((18+(i*240), 39 + 245+4), "HR: " + '{:.4f}'.format(l2[i][1]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((18+(i*240), 50 + 245+4), "M : " + '{:.4f}'.format(l2[i][2]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((118+(i*240),28 + 245+4), "RF: " + '{:.4f}'.format(l2[i][3]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((118+(i*240),39 + 245+4), "SM: " + '{:.4f}'.format(l2[i][4]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((118+(i*240),50 + 245+4), "MH: " + '{:.4f}'.format(l2[i][5]), font = font_l1d_data, fill=(0,0,0))

#    image_draw.rectangle([(15 + (i*240), 15 + 245 + 65), (15 + 200 + (i*240), 15 + 245 + 65 + 60)], outline = "white", fill = (200, 200, 50))
#    image_draw.text((15+(i*240), 15+245+65), "L2 Cache-" + str(i+8), font = font_l1d, fill=(0, 0, 0)) #L2 [8, 15]
#    image_draw.text((18+(i*240), 28+245+65+4), "H : " + '{:.4f}'.format(l2[i+8][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((18+(i*240), 39+245+65+4), "HR: " + '{:.4f}'.format(l2[i+8][1]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((18+(i*240), 50+245+65+4), "M : " + '{:.4f}'.format(l2[i+8][2]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((118+(i*240),28+245+65+4), "RF: " + '{:.4f}'.format(l2[i+8][3]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((118+(i*240),39+245+65+4), "SM: " + '{:.4f}'.format(l2[i+8][4]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((118+(i*240),50+245+65+4), "MH: " + '{:.4f}'.format(l2[i+8][5]), font = font_l1d_data, fill=(0,0,0))

  ## L2 [16, 31]
#  for i in range(0, 8):
#    image_draw.rectangle([(15+(i*240), 1080-(15+245)), (15+200+(i*240), 1080-(15+245+60))], outline = "white", fill = (255, 255, 75))
#    image_draw.rectangle([(15+(i*240), 1080-(15+245+65)), (15+200+(i*240), 1080-(15+245+65+60))], outline = "white", fill = (200, 200, 50))
#
#    image_draw.text((15+(i*240),  1080-(15+245+65+60)), "L2 Cache-" + str(i+16), font = font_l1d, fill=(0, 0, 0)) #L2 [16, 23]
##    image_draw.text((18+(i*240),  1080-(-4-0+245+65+60)),  "H : " + '{:.4f}'.format(l2[i+16][0]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((18+(i*240),  1080-(-4-11+245+65+60)),  "HR: " + '{:.4f}'.format(l2[i+16][1]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((18+(i*240),  1080-(-4-22+245+65+60)), "M : " + '{:.4f}'.format(l2[i+16][2]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((118+(i*240), 1080-(-4-0+245+65+60)), "RF: " + '{:.4f}'.format(l2[i+16][3]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((118+(i*240), 1080-(-4-11+245+65+60)), "SM: " + '{:.4f}'.format(l2[i+16][4]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((118+(i*240), 1080-(-4-22+245+65+60)), "MH: " + '{:.4f}'.format(l2[i+16][5]), font = font_l1d_data, fill=(0,0,0))
#
#    image_draw.text((15+(i*240), 1080-(15+245+60)), "L2 Cache-" + str(i+24), font = font_l1d, fill=(0, 0, 0)) #L2 [24, 31]
##    image_draw.text((18+(i*240), 1080-(-4-0+245+60)),  "H : " + '{:.4f}'.format(l2[i+24][0]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((18+(i*240), 1080-(-4-11+245+60)),  "HR: " + '{:.4f}'.format(l2[i+24][1]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((18+(i*240), 1080-(-4-22+245+60)), "M : " + '{:.4f}'.format(l2[i+24][2]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((118+(i*240),1080-(-4-0+245+60)), "RF: " + '{:.4f}'.format(l2[i+24][3]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((118+(i*240),1080-(-4-11+245+60)), "SM: " + '{:.4f}'.format(l2[i+24][4]), font = font_l1d_data, fill=(0,0,0))
##    image_draw.text((118+(i*240),1080-(-4-22+245+60)), "MH: " + '{:.4f}'.format(l2[i+24][5]), font = font_l1d_data, fill=(0,0,0))

#    image_draw.text((18 + (i*118), 30+245+65+60+20+4), "RB-H: " + '{:.4f}'.format(dram[i][0]), font = font_l1d_data, fill=(0,0,0))
#    image_draw.text((18 + (i*118), 45+245+65+60+20+4), "RB-M: " + '{:.4f}'.format(dram[i][1]), font = font_l1d_data, fill=(0,0,0))

#  image_draw.rectangle([(15, 15+245+65+60+20 + 235), (1885, 15+245+65+60+20 + 258)], outline = "white", fill = (0,0,0))
#  font_info = ImageFont.truetype('DejaVuSans.ttf', 18)
#  image_draw.text((18, 15+245+65+60+20 + 235), 
#                  "QV-100 GPU based on Volta Architecture includes 80 Streaming Multiprocessors (80 L1D cache). "
#                  "There are 16 memory partitions (16 Seperate DRAM Banks) with 2 sub-partitions (32 L2 Caches) ",
#                  font = font_info, fill=(255,255,255)) 
#
#
#  image_draw.rectangle([(15, 15+245+65+60+20 + 260), (1910, 15+245+65+60+20 + 285)], outline = "white", fill = (0,0,0))
#  font_info = ImageFont.truetype('DejaVuSans.ttf', 20)
#  image_draw.text((18, 15+245+65+60+20 + 260), 
#                  "H -> Hits ||| M -> Misses ||| HR -> Hit Reserved Accesses ||| "
#                  "RF -> Reservation Failures ||| SM -> Sector Misses ||| "
#                  "MH -> MSHR Hits ||| RB-H -> Row Buffer Hits ||| RB-H -> Row Buffer Misses",
#                  font = font_info, fill=(255,255,255)) 

  return image_draw

