# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        length = len(preorder)
        preorder_index = 1
        postorder_index = 0
        stack = [TreeNode(val=preorder[0])]

        while preorder_index < length:
            while stack[-1].val == postorder[postorder_index]:
                postorder_index += 1
                stack.pop()
    
            node = TreeNode(val=preorder[preorder_index])

            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

            preorder_index += 1

        return stack[0]


s = Solution()

print(s.constructFromPrePost(preorder=[1], postorder=[1]))
