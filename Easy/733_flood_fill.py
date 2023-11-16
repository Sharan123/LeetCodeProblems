def fill_rec(img, row, column, color, original_color):
    if img[row][column]!=original_color:
        return img
    img[row][column] = color
    if row!=0 and original_color == img[row-1][column]:
        img = fill_rec(img, row-1, column, color, original_color)
    if row!=(len(img)-1) and original_color == img[row+1][column]:
        img = fill_rec(img, row+1, column, color, original_color)
    if column!=0 and original_color == img[row][column-1]:
        img = fill_rec(img, row, column-1, color, original_color)
    if column!=(len(img[0])-1) and original_color == img[row][column+1]:
        img = fill_rec(img, row, column+1, color, original_color)
    return img

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
original_color = image[sr][sc]
if color==original_color:
    print(image)
print(fill_rec(image, sr,sc, color, original_color))