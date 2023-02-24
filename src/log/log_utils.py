#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import os

from log.log_meta import LogMeta
from main.version import VERSION
from src.log.log import LOG_FILE_SUFFIX, Log, META_FILE_SUFFIX, CONSOLE_LOG_SUFFIX
from tracks.track import Track
from ui.please_wait import PleaseWait


#
# Public Interface
#

class OpenFileInfo:
    def __init__(self, display_name: str, log_meta: LogMeta, source_meta_files: list[str]):
        self.display_name = display_name
        self.log_meta = log_meta
        self.source_files = source_meta_files


def get_model_info_for_open_model_dialog(track: Track, log_directory: str, please_wait: PleaseWait) -> (list[OpenFileInfo], int):
    _refresh_meta(log_directory, please_wait)
    log_info, excluded_log_count = _get_open_file_model_info(track, log_directory)
    return _sorted_log_info(log_info), excluded_log_count


def get_world_names_of_existing_logs(log_directory: str, please_wait: PleaseWait):
    _refresh_meta(log_directory, please_wait)
    world_names = set()
    for f in os.listdir(log_directory):
        if f.endswith(META_FILE_SUFFIX):
            log = Log(log_directory)
            log.load_meta(f)
            world_names.add(log.get_log_meta().track_name.get())
    return world_names


#
# PRIVATE Implementation Helpers
#

def _refresh_meta(log_directory: str, please_wait: PleaseWait):
    _remove_invalid_meta_files(log_directory)
    logs_without_meta = _get_log_files_without_meta(log_directory)
    _import_logs_without_meta(logs_without_meta, please_wait, log_directory)


def _remove_invalid_meta_files(log_directory: str) -> None:
    all_files = os.listdir(log_directory)
    for f in all_files:
        if f.endswith(META_FILE_SUFFIX):
            if not _is_log_valid(f, all_files, log_directory):
                os.remove(os.path.join(log_directory, f))


def _is_log_valid(meta_file: str, all_files: list, log_directory: str):
    log_file = meta_file[:-len(META_FILE_SUFFIX)]
    if log_file not in all_files:
        return False
    try:
        log = Log(log_directory)
        log.load_meta(meta_file)
        return log.get_log_meta().guru_version.get() == VERSION and log.get_log_meta().matches_os_stats(
            os.stat(os.path.join(log_directory, log_file)))
    except Exception:  # TODO proper exception class for Guru
        return False


def _get_log_files_without_meta(log_directory: str):
    log_files = []

    all_files = os.listdir(log_directory)
    for f in all_files:
        if f.endswith(LOG_FILE_SUFFIX) or f.endswith(CONSOLE_LOG_SUFFIX):
            expected_meta = f + META_FILE_SUFFIX
            if expected_meta not in all_files:
                log_files.append(f)

    return log_files


def _import_logs_without_meta(log_files: list, please_wait: PleaseWait, log_directory: str):
    please_wait.start("Importing")
    total_count = len(log_files)
    for i, f in enumerate(log_files):
        log = Log(log_directory)
        try:
            log.parse(f, please_wait, i / total_count * 100, (i + 1) / total_count * 100)
            log.save()
        except Exception as ex:  # TODO - Trapping specific exceptions not working (Python issue?)
            print("Skipping file <{}> due to processing error <{}>".format(f, ex))
    please_wait.stop()


def _get_open_file_model_info(track: Track, log_directory: str) -> (list[OpenFileInfo], int):
    excluded_log_count = 0
    log_info = []
    used_names = []

    for f in os.listdir(log_directory):
        if f.endswith(META_FILE_SUFFIX):
            log = Log(log_directory)
            log.load_meta(f)
            if track.has_world_name(log.get_log_meta().track_name.get()):
                log_meta = log.get_log_meta()
                display_name = log_meta.model_name.get()
                meta_filenames = [f]

                # Simple fudge to deal with duplicate UI names for now  TODO - Handle worker id etc. intelligently
                if display_name in used_names:
                    i = 1
                    while f"{display_name} ({i})" in used_names:
                        i += 1
                    display_name = f"{display_name} ({i})"
                used_names.append(display_name)
                # End of fudge

                log_info.append(OpenFileInfo(display_name, log_meta, meta_filenames))
            else:
                excluded_log_count += 1

    return log_info, excluded_log_count


def _sorted_log_info(log_info: list[OpenFileInfo]):
    all_names = []
    indexed_logs = {}

    for log in log_info:
        all_names.append(log.display_name)
        indexed_logs[log.display_name] = log

    result = []
    for name in sorted(all_names):
        result.append(indexed_logs[name])

    return result
