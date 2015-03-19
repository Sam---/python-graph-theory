require! 'prelude-ls': {map}

export class Node
    ->
        @connected = []
        @origin = void
        @dist = Infinity

    wipe-dists: ->
        if @dist != Infinity
            @dist = Infinity
            for node in connected
                node.wipe-dists!

    connect-to: (node, path-weight) ->
        @connected.push node: node, weight: path-weight
        node.connected.push node: @, weight: path-weight

    set-origin: ->
        @wipe-dists!
        @build-dist 0 @

    build-dist: (dd, obj) ->
        @origin = obj
        @dist = dd
        needs-build = []
        for {node, weight} in @connected
            if node.dist > @dist + weight
                node.build-dist @dist + weight, obj

    shortest-path-to: (nodes) ->
        @set-origin!
        return map (.dist) nodes
