from cmaketools import setup

setup(
    name="flacfile",
    version="0.0.1",
    author="Takeshi (Kesh) Ikuma",
    author_email="tikuma@gmail.com",
    description="Read/write FLAC audio files.",
    url="https://github.com/hokiedsp/python-flacfile",
    license="BSD",
    src_dir="src",
    ext_module_hint=r"pybind11_add_module",
    has_package_data=False,
)
