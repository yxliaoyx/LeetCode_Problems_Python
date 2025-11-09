class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            log_id, content = log.split(" ", maxsplit=1)
            return (0, content, log_id) if content[0].isalpha() else (1,)

        return sorted(logs, key=get_key)
