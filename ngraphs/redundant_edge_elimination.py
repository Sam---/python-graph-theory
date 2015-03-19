def eliminate_redundant_edges(gr):
    for vert in gr.verts:
        gr.path_from(vert)
        for vvert, edge in gr.connected_to(vert):
            if vvert.dist < edge.weight:
                gr.edges.discard(edge)
