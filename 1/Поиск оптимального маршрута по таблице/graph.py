class Graph: 
 
 
    def __init__(self, nodes):
        self.adj_list = [ [node, []] for node in nodes ]
        for i in range(len(nodes)):
            nodes[i].index = i
 
 
    def connect_dir(self, node1, node2, weight = 1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        # Отмечает, что нижеуказанное не предотвращает от добавления связи дважды
        self.adj_list[node1][1].append((node2, weight))
 
    def connect(self, node1, node2, weight = 1):
        self.connect_dir(node1, node2, weight)
        self.connect_dir(node2, node1, weight)
 
    
    def connections(self, node):
        node = self.get_index_from_node(node)
        return self.adj_list[node][1]
    
    def get_index_from_node(self, node):
        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError("node must be an integer or a Node object")
        if isinstance(node, int):
            return node
        else:
            return node.index

    def dijkstra(self, src):
        
        src_index = self.get_index_from_node(src)
        # Указывает узлы к DijkstraNodeDecorators
        # Это инициализирует все предварительные расстояния до бесконечности
        dnodes = [ DijkstraNodeDecorator(node_edges[0]) for node_edges in self.adj_list ]
        # Устанавливает предварительное расстояние исходного узла до 0 и его массив перескоков к его узлу
        dnodes[src_index].prov_dist = 0
        dnodes[src_index].hops.append(dnodes[src_index].node)
        # Устанавливает все методы настройки кучи
        is_less_than = lambda a, b: a.prov_dist < b.prov_dist
        get_index = lambda node: node.index()
        update_node = lambda node, data: node.update_data(data)
 
        # Подтверждает работу кучи с DijkstraNodeDecorators с узлами
        heap = MinHeap(dnodes, is_less_than, get_index, update_node)
 
        min_dist_list = []
 
        while heap.size() > 0:
            # Получает узел кучи, что еще не просматривался ('seen')
            # и находится на минимальном расстоянии от исходного узла
            min_decorated_node = heap.pop()
            min_dist = min_decorated_node.prov_dist
            hops = min_decorated_node.hops
            min_dist_list.append([min_dist, hops])
            
            # Получает все следующие перескоки. Это больше не O(n^2) операция
            connections = self.connections(min_decorated_node.node)
            # Для каждой связи обновляет ее путь и полное расстояние от 
            # исходного узла, если общее расстояние меньше, чем текущее расстояние
            # в массиве dist
            for (inode, weight) in connections: 
                node = self.adj_list[inode][0]
                heap_location = heap.order_mapping[inode]
                if(heap_location is not None):
                    tot_dist = weight + min_dist
                    if tot_dist < heap.nodes[heap_location].prov_dist:
                        hops_cpy = list(hops)
                        hops_cpy.append(node)
                        data = {'prov_dist': tot_dist, 'hops': hops_cpy}
                        heap.decrease_key(heap_location, data)
 
        return min_dist_list


class Node:
  
    def __init__(self, data, indexloc = None):
        self.data = data
        self.index = indexloc

        
class BinaryTree:
 
    def __init__(self, nodes = []):
        self.nodes = nodes
 
    def root(self):
        return self.nodes[0]
    
    def iparent(self, i):
        return (i - 1) // 2
    
    def ileft(self, i):
        return 2*i + 1
 
    def iright(self, i):
        return 2*i + 2
 
    def left(self, i):
        return self.node_at_index(self.ileft(i))
    
    def right(self, i):
        return self.node_at_index(self.iright(i))
 
    def parent(self, i):
        return self.node_at_index(self.iparent(i))
 
    def node_at_index(self, i):
        return self.nodes[i]
 
    def size(self):
        return len(self.nodes)


class MinHeap(BinaryTree):
 
    def __init__(self, nodes, is_less_than = lambda a,b: a < b, get_index = None, update_node = lambda node, newval: newval):
        BinaryTree.__init__(self, nodes)
        self.order_mapping = list(range(len(nodes)))
        self.is_less_than, self.get_index, self.update_node = is_less_than, get_index, update_node
        self.min_heapify()
 
    # Изменение в кучу узлов, предполагается, что все поддеревья уже кучи
    def min_heapify_subtree(self, i):
 
        size = self.size()
        ileft = self.ileft(i)
        iright = self.iright(i)
        imin = i
        if( ileft < size and self.is_less_than(self.nodes[ileft], self.nodes[imin])):
            imin = ileft
        if( iright < size and self.is_less_than(self.nodes[iright], self.nodes[imin])):
            imin = iright
        if( imin != i):
            self.nodes[i], self.nodes[imin] = self.nodes[imin], self.nodes[i]
            # Если есть лямбда для получения абсолютного индекса узла
            # обновляет массив order_mapping для указания, где находится индекс
            # в массиве узлов (осмотр для этого индекса будет 0(1))
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[imin])] = imin
                self.order_mapping[self.get_index(self.nodes[i])] = i
            self.min_heapify_subtree(imin)
 
 
    # Превращает в кучу массив, который еще ей не является
    def min_heapify(self):
        for i in range(len(self.nodes), -1, -1):
            self.min_heapify_subtree(i)
 
    def min(self):
        return self.nodes[0]
 
    def pop(self):
        min = self.nodes[0]
        if self.size() > 1:
            self.nodes[0] = self.nodes[-1]
            self.nodes.pop()
            # Обновляет order_mapping, если можно
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[0])] = 0
            self.min_heapify_subtree(0)
        elif self.size() == 1: 
            self.nodes.pop()
        else:
            return None
        # Если self.get_index существует, обновляет self.order_mapping для указания, что
        # узел индекса больше не в куче
        if self.get_index is not None:
            # Устанавливает значение None для self.order_mapping для обозначения непринадлежности к куче 
            self.order_mapping[self.get_index(min)] = None
        return min
 
    # Обновляет значение узла и подстраивает его, если нужно, чтобы сохранить свойства кучи
    def decrease_key(self, i, val):
        self.nodes[i] = self.update_node(self.nodes[i], val)
        iparent = self.iparent(i)
        while( i != 0 and not self.is_less_than(self.nodes[iparent], self.nodes[i])):
            self.nodes[iparent], self.nodes[i] = self.nodes[i], self.nodes[iparent]
            # Если есть лямбда для получения индекса узла 
            # обновляет массив order_mapping для указания, где именно находится индекс
            # в массиве узлов (осмотр этого индекса O(1))
            if self.get_index is not None:
                self.order_mapping[self.get_index(self.nodes[iparent])] = iparent
                self.order_mapping[self.get_index(self.nodes[i])] = i
            i = iparent
            iparent = self.iparent(i) if i > 0 else None
 
    def index_of_node_at(self, i):
        return self.get_index(self.nodes[i])


class DijkstraNodeDecorator:
    
    def __init__(self, node):
        self.node = node
        self.prov_dist = float('inf')
        self.hops = []
 
    def index(self):
        return self.node.index
 
    def data(self):
        return self.node.data
    
    def update_data(self, data):
        self.prov_dist = data['prov_dist']
        self.hops = data['hops']
        return self
