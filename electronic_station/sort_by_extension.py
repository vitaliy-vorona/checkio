from typing import List


def checker(file_format):
    if len(file_format) == len(file_format[file_format.rfind(".") :]):
        return ".a"
    if len(file_format[file_format.rfind(".") :]):
        return file_format[file_format.rfind(".") :]


def sort_by_ext(files: List[str]) -> List[str]:
    sorted_files = sorted(files, key=checker)
    if ".config" in sorted_files:
        sorted_files.pop(sorted_files.index(".config"))
        sorted_files.insert(0, ".config")
    elif "config." in sorted_files:
        sorted_files.pop(sorted_files.index("config."))
        sorted_files.insert(0, "config.")

    block_ndx = 0
    print(sorted_files[0])
    print(block_ndx)
    ndx1 = next(obj for obj in sorted_files if obj == "")
    return sorted_files


if __name__ == "__main__":
    # print("Example:")
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
        "1.aa",
        "1.bat",
        "1.cad",
        ".aa.doc",
    ]
    assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
        "1.aa",
        "1.bat",
        "2.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
        "1.aa",
        "1.bat",
        "1.cad",
        "1.aa.doc",
    ]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
        ".bat",
        "1.aa",
        "1.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
        ".aa",
        ".bat",
        "1.bat",
        "1.cad",
    ]
    assert sort_by_ext(
        [
            "no.name.",
            "green.bat",
            ".config",
            "345.bin",
            "format.c",
            "my.doc",
            "1.exe",
            "best.test.exe",
        ]
    ) == [
        ".config",
        "no.name.",
        "green.bat",
        "345.bin",
        "format.c",
        "my.doc",
        "1.exe",
        "best.test.exe",
    ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
