import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='torch_truncnorm',
    version='0.0.3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='Truncated Normal distribution in PyTorch',
    python_requires='>=3.6',
    install_requires=[
        'torch>=1.5.0',
    ],
    py_modules=['TruncatedNormal'],
    author='Anton Obukhov',
    license='BSD',
    url='https://www.github.com/toshas/torch_truncnorm',
)
