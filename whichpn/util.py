#!/usr/bin/env python3
"""Utility functions."""
from typing import Dict, Optional, List, Tuple
import sys
import io
import csv
import urllib.request
import ssl

SpcDict = Dict[str, int]
CSVRow = Tuple[int, int, int, int, str, str, int]


class CsvExc(RuntimeError):
    ...


def __csv_load(src_path: str) -> str:
    """Load text from file or URL."""
    skip_ssl = ssl.SSLContext()  # FIXME: 'no proto' and ssl.PROTOCOL_TLS depricated
    if src_path.startswith('https://'):
        with urllib.request.urlopen(src_path, context=skip_ssl) as f:
            return f.read().decode('utf-8')
    else:
        with open(src_path, 'rt', newline='', encoding='utf-8') as f:
            return f.read()


def __csv_handle_row(ndc: int, src: List, spc: SpcDict) -> CSVRow:
    """Check and convert CSV row.

    :todo: more checks
    """
    if int(src[0])//100 != ndc:
        raise CsvExc(f"{src[0]} not in NDC.")
    if not src[6]:  # special case:
        if not (inn := spc.get(src[4])):
            raise CsvExc(f"Unknown OpSoS '{src[4]}' without TIN.")
    else:
        inn = int(src[6])
    return int(src[0]), int(src[1]), int(src[2]), int(src[3]), src[4].strip(), src[5].strip(), inn


def csv_handle(ndc: int, csv_path: str, spc: SpcDict) -> Optional[List[CSVRow]]:
    """Load, check/fix and convert CSV."""
    if not (csv_data := __csv_load(csv_path)):
        return
    with io.StringIO(csv_data) as csv_file:
        rdr = csv.reader(csv_file, delimiter=';', quoting=csv.QUOTE_NONE, skipinitialspace=True, strict=True)
        retvalue = []
        for i, row in enumerate(rdr):
            if not i:
                continue  # skip 1st line
            retvalue.append(__csv_handle_row(ndc, row, spc))
        return retvalue


def main():
    """Entry point."""
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <NDC:int=1..9> <csv_source>")
        return 1
    from settings import SPECIAL
    result = csv_handle(int(sys.argv[1]), sys.argv[2], SPECIAL)
    print(f"{len(result)} lines OK.")


if __name__ == '__main__':
    sys.exit(main())
