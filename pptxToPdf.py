# Copyright 2023 AE

import subprocess as sp



sp.run(["soffice", "--headless", "convert_to", "pdf" "$1"])


