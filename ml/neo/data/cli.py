"""Command line for datasets: ``neo-data``.

    neo-data list                         # datasets in the catalogue and what is on disk
    neo-data download ham10000            # dry run: show files and sizes, download nothing
    neo-data download ham10000 --yes      # really download
    neo-data registry ham10000            # extract the images and build the data registry

Downloads are a dry run unless ``--yes`` is given.
"""

from __future__ import annotations

import argparse

from neo import paths
from neo.data import ham10000, registry
from neo.data.download import download_file, free_space, human_size, is_complete
from neo.data.sources import SOURCES, get_source

# Datasets that have a converter to the common registry.
REGISTRY_BUILDERS = {ham10000.KEY: ham10000.build_registry}


def cmd_list(_: argparse.Namespace) -> int:
    print(f"Data folder: {paths.data_dir()}")
    for source in SOURCES.values():
        folder = paths.subdir("raw") / source.key
        print(f"\n{source.key}: {source.title}")
        print(f"  licence {source.license}; DOI {source.doi}; {source.version}")
        for group in source.groups():
            files = source.select([group])
            present = sum(1 for f in files if (folder / f.name).is_file())
            size = human_size(sum(f.size for f in files))
            print(f"  group '{group}': {len(files)} file(s), {size}, {present} on disk")
    return 0


def cmd_download(args: argparse.Namespace) -> int:
    source = get_source(args.dataset)
    groups = args.groups.split(",") if args.groups else None
    files = source.select(groups)
    folder = paths.subdir("raw") / source.key

    print(f"{source.title}")
    print(f"Licence:     {source.license} ({source.license_url})")
    print(f"Source:      {source.landing_page} — {source.version}")
    print(f"Destination: {folder}")
    print("Files:")
    to_fetch = 0
    for remote in files:
        done = is_complete(remote, folder)
        to_fetch += 0 if done else remote.size
        status = "on disk, checksum OK" if done else "to download"
        print(f"  {human_size(remote.size):>10}  {remote.name}  [{status}]")
    print(f"To download: {human_size(to_fetch)}; free disk space: {human_size(free_space(folder))}")
    other = [g for g in source.groups() if g not in (groups or ["core"])]
    if other:
        print(f"Other groups not selected (use --groups): {', '.join(other)}")

    if to_fetch == 0:
        print("Nothing to download.")
        return 0
    if not args.yes:
        print("Dry run: nothing was downloaded. Add --yes to download.")
        return 0
    if to_fetch > free_space(folder):
        print("Not enough free disk space.")
        return 1
    for remote in files:
        download_file(remote, folder)
    print("Done.")
    return 0


def cmd_registry(args: argparse.Namespace) -> int:
    if args.dataset not in REGISTRY_BUILDERS:
        print(f"No registry converter for '{args.dataset}'. Available: {sorted(REGISTRY_BUILDERS)}")
        return 1
    path = REGISTRY_BUILDERS[args.dataset]()
    frame = registry.load(args.dataset)
    print(f"Registry written: {path}")
    print(f"{len(frame)} images, {frame['lesion_id'].nunique()} lesions")
    print(frame["diagnosis"].value_counts().to_string())
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="neo-data", description="Datasets of Neo Helper.")
    commands = parser.add_subparsers(dest="command", required=True)

    commands.add_parser("list", help="Show the catalogue and what is on disk.").set_defaults(
        run=cmd_list
    )

    download = commands.add_parser("download", help="Download a dataset (dry run by default).")
    download.add_argument("dataset", choices=sorted(SOURCES))
    download.add_argument("--groups", help="Comma-separated file groups (default: core).")
    download.add_argument("--yes", action="store_true", help="Really download.")
    download.set_defaults(run=cmd_download)

    build = commands.add_parser("registry", help="Extract images and build the data registry.")
    build.add_argument("dataset", choices=sorted(SOURCES))
    build.set_defaults(run=cmd_registry)

    args = parser.parse_args(argv)
    return args.run(args)


if __name__ == "__main__":
    raise SystemExit(main())
