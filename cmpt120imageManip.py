# Image Processer
# Author: Nicholas Kang
# Date: November 28, 2021

import cmpt120imageProjHelper

# ---- Basic Function Manipulations ----

def applyRedFilter(pixels):
  width = len(pixels[0])
  height = len(pixels)
  # applying manipulations to a black image called blankimg
  blankimg = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      blankimg[row][col] = pixels[row][col]
      blankimg[row][col][1] = 0 # set green to 0
      blankimg[row][col][2] = 0 # set blue to 0
  return blankimg

def applyGreenFilter(pixels):
  width = len(pixels[0])
  height = len(pixels)
  blankimg = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      blankimg[row][col] = pixels[row][col]
      blankimg[row][col][0] = 0 # set red to 0
      blankimg[row][col][2] = 0 # set blue to 0
  return blankimg

def applyBlueFilter(pixels):
  width = len(pixels[0])
  height = len(pixels)
  blankimg = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      blankimg[row][col] = pixels[row][col]
      blankimg[row][col][0] = 0 # set red to 0
      blankimg[row][col][1] = 0 # set green to 0
  return blankimg

def applySepiaFilter(pixels):
  width = len(pixels[0])
  height = len(pixels)
  blankimg = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]

      # sepia rgb value calculations
      sepia_r = int((r*0.393) + (g*0.769) + (b*0.189))
      sepia_g = int((r*0.349) + (g*0.686) + (b*0.168))
      sepia_b = int((r*0.272) + (g*0.534) + (b*0.131))

      # if the calculated sepia r, g, b values are over 255 (the max value for rgb)
      # then it will be set to 255, and then the new values will be set as
      # the pixels on the blankimg
      blankimg[row][col][0] = min(255, sepia_r)
      blankimg[row][col][1] = min(255, sepia_g)
      blankimg[row][col][2] = min(255, sepia_b)
  return blankimg

def applyWarmFilter(pixels):
  width = len(pixels[0])
  height = len(pixels)
  blankimg = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]

      # for warm colour, r scales up, b scales down
      if r < 64:
        scaled_r = r/64*80
      elif r >= 64 and r < 128:
        scaled_r = ((r-64)/(128-64) * (160-80) + 80)
      else:
        scaled_r = ((r-128)/(255-128) * (255-160) + 160)

      if b < 64:
        scaled_b = b/64*50
      elif b >= 64 and b < 128:
        scaled_b = ((b-64)/(128-64) * (100-50) + 50)
      else:
        scaled_b = ((b-128)/(255-128) * (255-100) + 100)

      # converted scaled r and g to integers because they were floats
      blankimg[row][col][0] = int(scaled_r)
      blankimg[row][col][1] = g # g value stays same
      blankimg[row][col][2] = int(scaled_b)
  return blankimg

def applyColdFilter(pixels):
  width = len(pixels[0])
  height = len(pixels)
  blankimg = cmpt120imageProjHelper.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      pixel = pixels[row][col]
      r = pixel[0]
      g = pixel[1]
      b = pixel[2]
      
      # for cold colour, r scales down, b scales up
      # same formula as warm filter, but swapped r and b 
      if b < 64:
        scaled_b = b/64*80
      elif b >= 64 and b < 128:
        scaled_b = ((b-64)/(128-64) * (160-80) + 80)
      else:
        scaled_b = ((b-128)/(255-128) * (255-160) + 160)

      if r < 64:
        scaled_r = r/64*50
      elif r >= 64 and r < 128:
        scaled_r = ((r-64)/(128-64) * (100-50) + 50)
      else:
        scaled_r = ((r-128)/(255-128) * (255-100) + 100)

      # converted scaled r and g to integers because they were floats
      blankimg[row][col][0] = int(scaled_r)
      blankimg[row][col][1] = g # g value stays same
      blankimg[row][col][2] = int(scaled_b)
  return blankimg

# ---- Advanced Function Manipulations ----
def rotateLeft(pixels):
  width = len(pixels[0])
  height = len(pixels)

  # swapped the height and width dimensions for our new image
  blankimg = cmpt120imageProjHelper.getBlackImage(height, width) 

  for row in range(height):
    for col in range(width):
      blankimg[col][row] = pixels[row][width-col-1]
  return blankimg

def rotateRight(pixels):
  width = len(pixels[0])
  height = len(pixels)

  # swapped the height and width dimensions for our new image
  blankimg = cmpt120imageProjHelper.getBlackImage(height, width) 

  for row in range(height):
    for col in range(width):
      blankimg[col][row] = pixels[height-row-1][col]
  return blankimg

def doubleSize(pixels):
  width = len(pixels[0])
  height = len(pixels)
  new_w = width*2
  new_h = height*2

  # making the dimensions of new image 2 times bigger
  blankimg = cmpt120imageProjHelper.getBlackImage(new_w, new_h) 

  for row in range(new_h):
    for col in range(new_w):

      # have to // 2 the row and col of our original image, because
      # we are looping through double the original's dimensions, and
      # our original image itself does not contain double its own
      # dimensions (obviously :D)
      blankimg[row][col] = pixels[row//2][col//2]
  return blankimg

def halfSize(pixels):
  width = len(pixels[0])
  height = len(pixels)

  # opposite of doubleSize function
  new_w = width//2
  new_h = height//2
  blankimg = cmpt120imageProjHelper.getBlackImage(new_w, new_h)
  for row in range(new_h):
    for col in range(new_w):
      blankimg[row][col] = pixels[row*2][col*2]
  return blankimg

def locateFish(pixels):
  width = len(pixels[0])
  height = len(pixels)
  blankimg = cmpt120imageProjHelper.getBlackImage(width, height)
  found_row = [] 
  found_col = []
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]

      h = cmpt120imageProjHelper.rgb_to_hsv(r,g,b)[0] # hue
      s = cmpt120imageProjHelper.rgb_to_hsv(r,g,b)[1] # saturation
      v = cmpt120imageProjHelper.rgb_to_hsv(r,g,b)[2] # value
      
      # these are the estimated h, s, v values I found for yellow online.
      # If a pixel has these values, the location of the row and col 
      # it was found on will be concatenated to found_row and found_col 
      if h > 50 and h < 70:
        if s > 50 and s < 100:
          if v > 70:
            
            # If the row or col number is already in the list, it will not be
            # added. Doing this can get me the length and width of the fish later.
            # This works  because for this specific fish, if you were to draw one 
            # row anywhere across the fish, you can look at each
            # col from top to bottom in that row, and you'll find a yellow pixel, 
            # so, adding up the number of detected yellow pixel columns in a row
            # can give me the width of the fish. 
            # this logic also works vice versa to get the height
            if row not in found_row:
              found_row += [row]
            if col not in found_col:
              found_col += [col]

  # -Fish Dimensions-
  fish_width = len(found_col) 
  fish_height = len(found_row)

  # -Fish's Border Dimensions-
  # top_row gets the smallest row number, which will be the row number 
  # of where the top line border will be located
  # left_col gets the smallest col number, which will be the col number
  # of where the left line border will be located
  top_row = min(found_row)  
  left_col = min(found_col)
  right_col = left_col + fish_width # right line border
  bot_row = top_row + fish_height # bottom line border

  for row in range(height):
    for col in range(width):
      blankimg[row][col] = pixels[row][col] 

      # if the col we are looping through lands within the col of 
      # the fish's border dimensions, and the row is equal to the location of
      # the top or bottom border, a straight green line will be drawn horizontally there
      if col >= left_col and col <= right_col:  
        if row == top_row or row == bot_row:
          blankimg[row][col][1] = 255

      # if the row we are looping through lands within the row of
      # the fish's border dimensions, and the col is equal to the location of
      # the left or right border, a straight green line will be drawn vertically there
      if row >= top_row and row <= bot_row:
        if col == left_col or col == right_col:
          blankimg[row][col][1] = 255
  return blankimg
