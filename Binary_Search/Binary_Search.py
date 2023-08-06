class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


new = TreeNode("Drink")
hot = TreeNode("hot")
cold = TreeNode("cold")

lette = TreeNode("lette")
cola = TreeNode("cola")

new.left = hot
new.right = cold
hot.left = lette
cold.left = cola


def preTravel(node):
    if not node:  # 到最末端葉子還是會呼叫一次，變成是none
        return
    print(node.data)
    preTravel(node.left)
    preTravel(node.right)


def inOrder(node):
    if not node:
        return
    inOrder(node.left)  # 左邊地回到底
    print(node.data)
    inOrder(node.right)


def postOrder(node):
    if not node:
        return
    inOrder(node.left)  # 走到末端葉子再往下發現沒有東西就回直接return  然後執行下一行
    inOrder(node.right)  # 發現也沒有 所以也return
    print(node.data)  # 最後就執行這一行

preTravel(new)
print("====")
inOrder(new)
print("====")
postOrder(new)
