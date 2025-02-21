# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Runtime
# 9422ms, Beats: 5.08%
class FindElements:
    def _change_node(self, value, root: Optional[TreeNode]):
        root.val = value

        if root.left:
            self._change_node(2 * value + 1, root.left)
        
        if root.right:
            self._change_node(2 * value + 2, root.right)

    def __init__(self, root: Optional[TreeNode]):
        self._change_node(0, root)
        self.node_tree = root

        
    def _find_node_value(self, target, node):
        if node.val == target:
            return True

        left_value = None
        if node.left:
            left_value = self._find_node_value(target, node.left)

        right_value = None
        if node.right:
            right_value = self._find_node_value(target, node.right)
        
        if left_value or right_value:
            return True
        return False
    
    def find(self, target: int) -> bool:
        return self._find_node_value(target, self.node_tree)

# Runtime
# 6156ms, Beats: 6.15%
class FindElements:
    def _change_node(self, value, root: Optional[TreeNode]):
        root.val = value

        if root.left:
            self._change_node(2 * value + 1, root.left)
        
        if root.right:
            self._change_node(2 * value + 2, root.right)

    def __init__(self, root: Optional[TreeNode]):
        self._change_node(0, root)
        self.node_tree = root

    
    def find(self, target: int) -> bool:
        stack = []

        stack.append(self.node_tree)

        while stack:
            root = stack.pop()
            if root.val == target:
                return True
            
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return False

# Runtime
# 5ms, Beats: 74.33%
class FindElements:
    def _change_node(self, value, root: Optional[TreeNode]):
        root.val = value
        self.nums.add(value)

        if root.left:
            self._change_node(2 * value + 1, root.left)
        
        if root.right:
            self._change_node(2 * value + 2, root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.nums = set()
        self._change_node(0, root)

    
    def find(self, target: int) -> bool:
        return target in self.nums



# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)