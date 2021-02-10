from setuptools import setup

requires = [
    "requests>=2.25.1,<=3"
]


setup(
    name="line_notify",
    version="1.0.0",
    install_requires=requires,
    packages=["line_notify"]
)
