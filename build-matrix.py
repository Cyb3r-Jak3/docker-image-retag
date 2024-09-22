import json
import os


def build_matrix() -> dict:
    with open('images.json') as f:
        matrix = json.load(f)
    include = []
    for source in matrix:
        tags = matrix[source]['tags']
        include.append({
            "source": source,
            "tags": tags
        })
    final_matrix = {
        "source": "",
        "tags": [],
        "include": include
    }
    return final_matrix


# Output needed
# source: string
# tags: list of strings


if __name__ == '__main__':
    output = build_matrix()
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ.get('GITHUB_OUTPUT'), 'a') as f:
            print(f'matrix={json.dumps(output)}', file=f)
    else:
        print(json.dumps(output))
