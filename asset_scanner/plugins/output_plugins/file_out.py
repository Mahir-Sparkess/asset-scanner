"""
File Output Backend
-------------------

An output backend which outputs the content generated into a text file
in a location of your choosing.

**Plugin name:** ``file_out``

.. list-table::
    :header-rows: 1

    * - Option
      - Value Type
      - Description
    * - ``filepath``
      - ``str``
      - ``REQUIRED`` Path to output file(s), either directory or specific file to write.
      - ``namespace``
      - ``str``
      - Can be used by downstream processors to capture specific outputs.

Example Configuration:
    .. code-block:: yaml

        outputs:
            - name: file_out
              namespace: header
              filepath: location_to_destination_file

"""
__author__ = "Mahir Rahman"
__date__ = "23 Mar 2022"
__copyright__ = "Copyright 2022 United Kingdom Research and Innovation"
__license__ = "BSD - see LICENSE file in top-level package directory"
__contact__ = "kazi.mahir@stfc.ac.uk"

import json
import os

from .base import OutputBackend


class FileoutOutputBackend(OutputBackend):
    """
    Create/Append to files to export data from
    the processor.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.filepath: str = kwargs["filepath"]
        self.filepath = self.filepath.rstrip("/")

    def export(self, data: dict, **kwargs) -> None:

        if kwargs.get("deduplicate", False):
            return

        if os.path.isdir(self.filepath):
            filepath = f"{self.filepath}/file_out.txt"
        else:
            filepath = self.filepath

        with open(f"{filepath}", "a") as file:
            file.write(f"{json.dumps(data)}\n")
