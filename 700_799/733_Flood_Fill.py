class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image

        def dfs(r, c):
            if image[r][c] == original_color:
                image[r][c] = color

                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                        dfs(nr, nc)

        dfs(sr, sc)

        return image
