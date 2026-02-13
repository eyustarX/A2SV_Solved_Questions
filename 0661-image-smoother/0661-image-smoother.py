class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        new_img = [[0]*len(img[0]) for _ in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[0])):
                total = 0
                count = 0
                for n in (-1,0,1):
                    for m in (-1,0,1):
                        r = i + n
                        c = j + m

                        if 0 <= c <len(img[0]) and 0 <= r < len(img):
                            total += img[r][c]
                            count += 1
                        
                new_img[i][j] = total // count
            
        return new_img
