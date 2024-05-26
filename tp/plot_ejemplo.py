import matplotlib.pyplot as plt

class Node:
    def __init__(self, label):
        self.label = label
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def plot_tree(node, depth=0, pos=(0, 0), parent=None, branch_label=None):
    if node is None:
        return

    # Dibuja el nodo actual
    plt.text(pos[0], pos[1], node.label, bbox=dict(facecolor='lightgray', alpha=0.5), ha='center')
    
    if parent is not None:
        # Dibuja la línea que conecta el nodo actual con su padre
        plt.plot([parent[0], pos[0]], [parent[1], pos[1]], 'k-')
        if branch_label is not None:
            # Etiqueta la rama
            plt.text((parent[0]+pos[0])/2, (parent[1]+pos[1])/2, branch_label, ha='center')

    num_children = len(node.children)
    if num_children > 0:
        # Calcula la separación horizontal entre los nodos hijos
        h_offset = 1.5 ** (5 - depth)
        for i, child in enumerate(node.children):
            # Calcula la posición del nodo hijo
            child_pos = (pos[0] - (num_children - 1) * h_offset / 2 + i * h_offset, pos[1] - 1.5)
            # Dibuja la conexión entre el nodo actual y su hijo
            plot_tree(child, depth + 1, child_pos, pos, f'Child {i+1}')

# Crea un árbol de decisión de ejemplo
root = Node("Root")
child1 = Node("Child1")
child2 = Node("Child2")
child3 = Node("Child3")
grandchild1 = Node("Grandchild1")
grandchild2 = Node("Grandchild2")

root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
child2.add_child(grandchild1)
child2.add_child(grandchild2)

# Dibuja el árbol de decisión
plt.figure(figsize=(8, 8))
plot_tree(root)
plt.axis('off')
plt.show()
