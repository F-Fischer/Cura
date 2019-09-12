import configparser
from typing import Tuple, List
import io
from UM.VersionUpgrade import VersionUpgrade


class VersionUpgrade43to44(VersionUpgrade):
    def getCfgVersion(self, serialised: str) -> int:
        parser = configparser.ConfigParser(interpolation = None)
        parser.read_string(serialised)
        format_version = int(parser.get("general", "version"))  # Explicitly give an exception when this fails. That means that the file format is not recognised.
        setting_version = int(parser.get("metadata", "setting_version", fallback = "0"))
        return format_version * 1000000 + setting_version

    ##  Upgrades Preferences to have the new version number.
    #
    #   This renames the renamed settings in the list of visible settings.
    def upgradePreferences(self, serialized: str, filename: str) -> Tuple[List[str], List[str]]:
        parser = configparser.ConfigParser(interpolation = None)
        parser.read_string(serialized)

        # Update version number.
        parser["metadata"]["setting_version"] = "10"

        result = io.StringIO()
        parser.write(result)
        return [filename], [result.getvalue()]

    ##  Upgrades instance containers to have the new version
    #   number.
    #
    #   This renames the renamed settings in the containers.
    def upgradeInstanceContainer(self, serialized: str, filename: str) -> Tuple[List[str], List[str]]:
        parser = configparser.ConfigParser(interpolation=None)
        parser.read_string(serialized)

        # Update version number.
        parser["metadata"]["setting_version"] = "10"

        result = io.StringIO()
        parser.write(result)
        return [filename], [result.getvalue()]

    ##  Upgrades stacks to have the new version number.
    def upgradeStack(self, serialized: str, filename: str) -> Tuple[List[str], List[str]]:
        parser = configparser.ConfigParser(interpolation=None)
        parser.read_string(serialized)

        # Update version number.
        parser["metadata"]["setting_version"] = "10"

        result = io.StringIO()
        parser.write(result)
        return [filename], [result.getvalue()]