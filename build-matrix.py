import json
import os

DEFAULT_ARCHITECTURES = ["linux/amd64", "linux/arm64", "linux/arm/v7", "linux/arm/v6"]


def build_matrix() -> dict:
    with open('images.json') as f:
        matrix = json.load(f)
    include = []
    for source in matrix:
        for tag in matrix[source]['tags']:
            include.append({
                "source": matrix[source]['source'],
                "tag": tag,
                "name": matrix[source],
                "architectures": matrix[source].get('architectures', DEFAULT_ARCHITECTURES)
            })
    return {"include": include}


# Output needed
# source: string
# tags: list of strings


if __name__ == '__main__':
    output = build_matrix()
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ.get('GITHUB_OUTPUT'), 'a') as f:
            print(f'matrix={output}', file=f)
    else:
        print(output)
