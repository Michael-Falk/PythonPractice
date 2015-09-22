class BSTNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return "<BST Node, data:" + str(self.data) + ">"

class BST(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def get(self, data):
        return self._get(self.root, data)

    def _get(self, root, data):
        if root is None:
            return None
        if data > root.data:
            return self._get(root.right, data)
        if data == root.data:
            return root.data
        return self._get(root.left, data)

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if root is None:
            self.size += 1
            return BSTNode(data)
        if data > root.data:
            root.right = self._add(root.right, data)
        elif data < root.data:
            root.left = self._add(root.left, data)
        return root

    def remove(self, data):
        store = BSTNode(None)
        self.root = self._remove(self.root, data, store)
        return store.data

    def _remove(self, root, data, store):
        if root is None:
            return None
        if data > root.data:
            root.right = self._remove(root.right, data, store)
        elif data < root.data:
            root.left = self._remove(root.left, data, store)
        else:
            self.size -= 1
            if root.left is not None:
                if root.right is not None:
                    root.left = self._removePredecessor(root.left, store)
                    temp = root.data
                    root.data = store.data
                    store.data = temp
                    return root
                else:
                    store.data = root.data
                    return root.left
            store.data = root.data
            return root.right

    def _removePredecessor(self, root, store):
        if root.right is None:
            return self._remove(root, root.data, store)
        root.right = self.removePredecessor(root.right, store)

    def preorder_traversal(self):
        return [x for x in self._iterpreorder(self.root)]

    def _iterpreorder(self, root):
        yield root.data
        if root.left is not None:
            for x in self._iterpreorder(root.left):
                yield x
        if root.right is not None:
            for x in self._iterpreorder(root.right):
                yield x

    def inorder_traversal(self):
        return [x for x in self._iterinorder(self.root)]

    def _iterinorder(self, root):
        if root.left is not None:
            for x in self._iterinorder(root.left):
                yield x
        yield root.data
        if root.right is not None:
            for x in self._iterinorder(root.right):
                yield x

    def postorder_traversal(self):
        return [x for x in self._iterpostorder(self.root)]

    def _iterpostorder(self, root):
        if root.left is not None:
            for x in self._iterpostorder(root.left):
                yield x
        if root.right is not None:
            for x in self._iterpostorder(root.right):
                yield x
        yield root.data
