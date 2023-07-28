from setuptools import find_packages, setup

setup(
    name="dagster_dbt_scaffold",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "dagster_dbt_scaffold": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster @ git+https://github.com/dagster-io/dagster.git@release-1.4.3rc0#subdirectory=python_modules/dagster",
        "dagster-cloud",
        "dagster-dbt @ git+https://github.com/dagster-io/dagster.git@release-1.4.3rc0#subdirectory=python_modules/libraries/dagster-dbt",
        "dbt-core>=1.4.0",
        "dbt-duckdb",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)