from blue_sandbox import NAME, VERSION, DESCRIPTION, REPO_NAME
from blueness.pypi import setup

setup(
    filename=__file__,
    repo_name=REPO_NAME,
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=[
        NAME,
        f"{NAME}.cemetery",
        f"{NAME}.cemetery.DALLE",
        f"{NAME}.cemetery.gpt",
        f"{NAME}.cemetery.inference",
        f"{NAME}.help",
        f"{NAME}.microsoft_building_damage_assessment",
        f"{NAME}.palisades",
        f"{NAME}.sagesemseg",
        f"{NAME}.VisuaLyze",
    ],
    include_package_data=True,
    package_data={
        NAME: [
            "config.env",
            "sample.env",
            ".abcli/**/*.sh",
        ],
    },
)
