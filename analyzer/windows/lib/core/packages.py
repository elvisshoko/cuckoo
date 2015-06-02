# Copyright (C) 2010-2015 Cuckoo Foundation.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os.path

extensions = {
    ".cpl": "cpl",
    ".dll": "dll",
    ".exe": "exe",
    ".pdf": "pdf",
    ".doc": "doc",
    ".docx": "doc",
    ".rtf": "doc",
    ".xls": "xls",
    ".xlsx": "xls",
    ".ppt": "ppt",
    ".pptx": "ppt",
    ".pps": "ppt",
    ".ppsx": "ppt",
    ".pptm": "ppt",
    ".potm": "ppt",
    ".potx": "ppt",
    ".ppsm": "ppt",
    ".htm": "html",
    ".html": "html",
    ".jar": "jar",
    ".zip": "zip",
    ".py": "python",
    ".pyc": "python",
    ".vbs": "vbs",
    ".msi": "msi",
    ".ps1": "ps1",
}

def choose_package(file_type, file_name):
    """Choose analysis package due to file type and file extension.
    @param file_type: file type.
    @param file_name: file name.
    @return: package name or None.
    """
    _, ext = os.path.splitext(file_name)

    if ext in extensions:
        return extensions[ext]

    if not file_type:
        return None

    file_name = file_name.lower()

    if "DLL" in file_type:
        if file_name.endswith(".cpl"):
            return "cpl"
        else:
            return "dll"
    elif "PE32" in file_type or "MS-DOS" in file_type:
        return "exe"
    elif "PDF" in file_type:
        return "pdf"
    elif "Rich Text Format" in file_type or \
            "Microsoft Word" in file_type or \
            "Microsoft Office Word" in file_type:
        return "doc"
    elif "Microsoft Office Excel" in file_type or \
            "Microsoft Excel" in file_type:
        return "xls"
    elif "Microsoft PowerPoint" in file_type:
        return "ppt"
    elif "HTML" in file_type:
        return "html"
    elif "Zip" in file_type:
        return "zip"
    elif "Python script" in file_type:
        return "python"
    else:
        return "generic"
