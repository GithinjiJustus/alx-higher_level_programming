#!/usr/bin/python3
"""
12-pascal_triangle
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to row n."""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle


if __name__ == "__main__":
    pass  # You can add test cases or use the provided main function for testing
