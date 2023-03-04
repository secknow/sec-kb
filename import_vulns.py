from model import *

def open_scan_findings(scan_configuration: dict) -> Scan:
    return Scan(ScanConfiguration(scan_configuration)

def save_scan_finding(scan: Scan, rule: Rule, properties: PropertySet):
    # TODO
    pass

def close_scan_findings(scan: Scan):
    pass

def get_tool(name: str) -> Tool:
    return Tool()
