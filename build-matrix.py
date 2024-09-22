import json
import os

DEFAULT_ARCHITECTURES = ["linux/amd64", "linux/arm64", "linux/arm/v7", "linux/arm/v6"]


def build_matrix() -> dict:
    with open('images.json') as f:
        matrix: dict = json.load(f)
    include = []
    for name, info in matrix.items():
        print(f'Processing {name}')
        print(f'Info: {info}')
        for tag in info['tags']:
            include.append({
                "source": info['source'],
                "tag": tag,
                "name": name,
                "architectures": " ".join(info.get('architectures', DEFAULT_ARCHITECTURES))
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
