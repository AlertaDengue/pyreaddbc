from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            "pyreaddbc._readdbcmodule",
            sources=[
                "pyreaddbc/_readdbcmodule.c",
                "pyreaddbc/c-src/dbc2dbf.c",
                "pyreaddbc/c-src/blast.c",
            ],
            include_dirs=["pyreaddbc/c-src"],
        ),
    ],
)
