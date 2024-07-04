# pylint: disable=C0115
"""App definition for the src app"""

from ginger.apps import AppConfig
import subprocess


class SrcConfig(AppConfig):
    default_auto_field = "ginger.db.models.BigAutoField"
    name = "src"

    def ready(self):
        try:
            subprocess.run(['db-compose', 'render', '--skip'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running db-compose render: {e}")
