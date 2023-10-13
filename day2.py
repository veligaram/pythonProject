def unite_linked_lists(cells):
    # Find the head of each individual list
    heads = [i for i in range(1, len(cells) + 1) if cells[i - 1][0] == 0]

    # Merge the lists
    merged_list = []
    for head in heads:
        curr = head
        while curr != 0:
            merged_list.append(curr)
            curr = cells[curr - 1][1]

    # Update the previous and next pointers
    for i in range(len(merged_list)):
        prev = merged_list[i - 1] if i > 0 else 0
        next = merged_list[i + 1] if i < len(merged_list) - 1 else 0
        cells[merged_list[i] - 1] = (prev, next)

    return cells


# Read input
n = int(input())
cells = [tuple(map(int, input().split())) for _ in range(n)]

# Unite the linked lists
united_cells = unite_linked_lists(cells)

# Print the result
for li, ri in united_cells:
    print(li, ri)