# Source JSON

This folder stores raw language JSON inputs that are not yet packaged as release
ZIP bundles.

## Current inputs

- `jawi/quranjawifinal.json`
- `bangali-urdu/bangaliurduquran.json`
- `maltese/maltesequrandata.json`
- `dv/dv-unknow-simple.json`

## Usage rule

Treat these as source material. Derived app files should be generated elsewhere
so the originals stay untouched.

## Jawi note

The Jawi source JSON has been refreshed from a conservative safe-cleaned baseline
that only normalizes Unicode and spacing. It should still be treated as source
material for further review and packaging.

## DV note

The `dv` source JSON is kept under a short code label until the canonical project
name is confirmed.
