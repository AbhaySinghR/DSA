from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([(root, root)])
        while q:
            nodeL, nodeR = q.popleft()
            if not nodeL and not nodeR:
                continue
            if not nodeL or not nodeR or nodeL.val != nodeR.val:
                return False
            q.append((nodeL.left, nodeR.right))
            q.append((nodeL.right, nodeR.left))
        return True
