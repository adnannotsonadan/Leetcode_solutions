class Solution:
    def isSameTree(self, p, q):
        # Base case: If both trees are empty, they are identical.
        if not p and not q:
            return True
        # If one of the trees is empty and the other is not, they are not identical.
        if not p or not q:
            return False
        
        # Compare the values of the current nodes.
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)