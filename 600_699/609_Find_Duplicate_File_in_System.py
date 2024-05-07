from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_path = defaultdict(list)

        for path in paths:
            directory, *files = path.split()
            for file in files:
                name, content = file[:-1].split("(")
                content_to_path[content].append(f"{directory}/{name}")

        return [paths for paths in content_to_path.values() if len(paths) > 1]
